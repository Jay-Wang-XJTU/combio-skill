"""Deterministic unit/numerical tests, distinct from agent behavioral evaluations."""
import numpy as np
import pytest
from scipy.special import ndtr
from scipy.stats import norm
from statsmodels.stats.multitest import multipletests
from lab.statistics import (adjust_pvalues, assert_group_disjoint, pseudobulk_counts,
                            permutation_pvalue, wilson_interval)
from lab.causal import crossfit_aipw
from lab.spatial import knn_edges, assignment_mix, edge_jaccard
from lab.transport import (balanced_sinkhorn, unbalanced_sinkhorn, generalized_kl,
                            exact_balanced_lp, uot_scipy_oracle, sample_pairs)
from lab.flow import affine_path, rk4, affine_truth


@pytest.mark.parametrize("method,official", [("BH", "fdr_bh"), ("BY", "fdr_by")])
@pytest.mark.parametrize("p", [[0., .001, .05, 1.], [.02, .02, .9], [1.], [.6, .003, .02, .0001, .14]])
def test_adjustments_match_statsmodels(method, official, p):
    np.testing.assert_allclose(adjust_pvalues(p, method), multipletests(p, method=official)[1], atol=1e-14)

@pytest.mark.parametrize("p", [[np.nan], [-.01], [1.1], [[.1, .2]]])
def test_invalid_p_rejected(p):
    with pytest.raises(ValueError): adjust_pvalues(p)

def test_empty_p_and_invalid_method():
    assert adjust_pvalues([]).size == 0
    with pytest.raises(ValueError): adjust_pvalues([.1], "unknown")

def test_independent_group_guard():
    assert_group_disjoint(["a", "a"], ["b"])
    with pytest.raises(ValueError): assert_group_disjoint(["a", "b"], ["b"])
    with pytest.raises(ValueError): assert_group_disjoint([], ["b"])

def test_pseudobulk_preserves_count_sum():
    x = np.array([[1, 0], [2, 3], [4, 1]])
    names, out = pseudobulk_counts(x, ["d1:T", "d2:T", "d1:T"])
    assert names.tolist() == ["d1:T", "d2:T"]
    np.testing.assert_array_equal(out, [[5, 1], [2, 3]])
    np.testing.assert_array_equal(x.sum(0), out.sum(0))

@pytest.mark.parametrize("counts", [[[1.1]], [[-1]], [[np.nan]]])
def test_pseudobulk_rejects_invalid_count(counts):
    with pytest.raises(ValueError): pseudobulk_counts(counts, ["d1"])

def test_permutation_nonzero_and_exact():
    assert permutation_pvalue(5, [0, 1, 2], two_sided=False) == .25
    assert permutation_pvalue(5, [0, 1, 2, 5], exact_enumeration=True) == .25
    assert permutation_pvalue(-3, [-4, 0, 4]) == .75

def test_wilson_contains_rate():
    lo, hi = wilson_interval(20, 400)
    assert lo < .05 < hi

def test_posterior_probability_formula_not_a_pvalue():
    # Formula microcheck only: two independent Gaussian posterior draws.
    p = ndtr((1.2-.4)/np.sqrt(.3**2+.5**2))
    ref = 1-norm.cdf(0, loc=.8, scale=np.sqrt(.34))
    assert abs(p-ref) < 1e-14
    assert p > .5

def test_aipw_requires_both_arms():
    with pytest.raises(ValueError): crossfit_aipw(np.arange(10), np.ones(10), np.arange(10))

def test_aipw_randomized_linear_known_effect():
    rng = np.random.default_rng(212)
    x = rng.normal(size=4000); a = rng.binomial(1, .5, 4000)
    y = 3*a+2*x+rng.normal(0, .2, 4000)
    ans = crossfit_aipw(x, a, y)
    assert abs(ans['ate']-3) < .05
    assert ans['fraction_clipped'] == 0

@pytest.mark.parametrize("transform", ["translate", "rotate", "scale"])
def test_knn_geometric_invariance(transform):
    x = np.random.default_rng(12).normal(size=(32, 2))
    y = x+10 if transform == "translate" else x@np.array([[0., -1.], [1., 0.]]) if transform == "rotate" else x*1000
    np.testing.assert_array_equal(knn_edges(x), knn_edges(y))

def test_no_self_and_k_degree():
    a = knn_edges(np.random.default_rng(42).normal(size=(15, 2)), 4)
    assert not np.diag(a).any()
    np.testing.assert_array_equal(a.sum(1), 4)

def test_zero_contamination_identity():
    x = np.ones((10, 3)); a = knn_edges(np.random.default_rng(10).normal(size=(10, 2)))
    np.testing.assert_array_equal(assignment_mix(x, a, 0), x)
    assert edge_jaccard(a, a) == 1

def test_invalid_spatial_shapes():
    with pytest.raises(ValueError): knn_edges([[0, 0]], 1)
    with pytest.raises(ValueError): edge_jaccard(np.ones((2,2)), np.ones((3,3)))
    with pytest.raises(ValueError): assignment_mix(np.ones((2,2)), np.zeros((2,2)), .1)

def test_balanced_marginals_and_exact_limit():
    a, b = [.4, .6], [.5, .5]; c = np.array([[0., 1.], [1., 0.]])
    out = balanced_sinkhorn(a, b, c, .06)
    np.testing.assert_allclose(out.plan.sum(1), a, atol=2e-9)
    np.testing.assert_allclose(out.plan.sum(0), b, atol=2e-9)
    lp = exact_balanced_lp(a, b, c)
    assert abs(out.linear_cost-(lp*c).sum()) < 1e-7

def test_balanced_cost_constant_invariance():
    a, b = [.3, .7], [.6, .4]; c = np.array([[0., .7], [.8, .1]])
    p = balanced_sinkhorn(a, b, c, .2).plan
    q = balanced_sinkhorn(a, b, c+3, .2).plan
    np.testing.assert_allclose(p, q, atol=1e-9)

def test_balance_does_not_silently_normalize():
    with pytest.raises(ValueError): balanced_sinkhorn([1.], [2.], [[0.]])

def test_uot_one_point_analytic():
    # derivative: C + e*log(g/c) + r1*log(g/a)+r2*log(g/b)=0
    a,b,eps,r1,r2,cost = 2.,3.,.2,.8,1.2,.4
    exact = np.exp((eps*np.log(a*b)+r1*np.log(a)+r2*np.log(b)-cost)/(eps+r1+r2))
    out = unbalanced_sinkhorn([a], [b], [[cost]], eps, r1, r2)
    assert abs(out.plan[0,0]-exact) < 1e-8

@pytest.mark.parametrize("reference", ["product", "ones"])
def test_uot_against_independent_optimizer(reference):
    a,b = [.3, .7], [.2, .4, .3]
    c = [[.1,.7,1.2],[.8,.3,.2]]
    u = unbalanced_sinkhorn(a,b,c,.3,.7,1.1,reference=reference)
    o = uot_scipy_oracle(a,b,c,.3,.7,1.1,reference)
    np.testing.assert_allclose(u.plan,o['plan'],atol=2e-7)
    assert abs(u.total_objective-o['objective']) < 1e-8

def test_uot_reference_changes_plan():
    args = ([.5,.5],[.5,.5],[[0.,1.],[1.,0.]],1.,1.,1.)
    p = unbalanced_sinkhorn(*args,reference='product')
    q = unbalanced_sinkhorn(*args,reference='ones')
    assert abs(p.total_mass-q.total_mass) > .05

def test_uot_cost_shift_changes_mass():
    p = unbalanced_sinkhorn([1.], [1.], [[0.]])
    q = unbalanced_sinkhorn([1.], [1.], [[2.]])
    assert q.total_mass < p.total_mass

def test_uot_scaling_all_penalties_preserves_plan():
    c = np.array([[.2,.7],[.9,.1]])
    p = unbalanced_sinkhorn([.4,.6],[.5,.5],c,.2,.7,.9).plan
    q = unbalanced_sinkhorn([.4,.6],[.5,.5],c*10,2.,7.,9.).plan
    np.testing.assert_allclose(p,q,atol=2e-8)

@pytest.mark.parametrize("solver", [balanced_sinkhorn, unbalanced_sinkhorn])
def test_solver_rejects_zero_weights_and_nonconvergence(solver):
    with pytest.raises(ValueError): solver([0.,1.],[.5,.5],np.zeros((2,2)))
    with pytest.raises(RuntimeError): solver([.2,.8],[.6,.4],[[.1,1.],[.4,.2]],max_iterations=1,tolerance=1e-15)

def test_generalized_kl_nonnegative_and_zero():
    assert abs(generalized_kl([0.,1.],[1.,1.])-1) < 1e-14
    assert generalized_kl([.2,.8],[.2,.8]) == 0

def test_pair_sampling_respects_plan_and_mass_normalization():
    p = np.array([[0.,.3],[.7,0.]])
    i,j = sample_pairs(p,10000,np.random.default_rng(1))
    assert np.all(i != j)
    assert abs(np.mean(i==0)-.3) < .03
    k,l = sample_pairs(5*p,10000,np.random.default_rng(1))
    np.testing.assert_array_equal(i,k);np.testing.assert_array_equal(j,l)

@pytest.mark.parametrize("t", [0., .3, 1.])
def test_affine_path_endpoints_and_velocity(t):
    a = np.array([[1.,2.],[3.,4.]]);b = a*2+1
    z,v = affine_path(a,b,t)
    np.testing.assert_allclose(z,(1-t)*a+t*b)
    np.testing.assert_allclose(v,b-a)

def test_affine_time_derivative():
    a = np.array([[1.],[4.]]);b = np.array([[4.],[2.]])
    z1,v = affine_path(a,b,.4+1e-5);z0,_ = affine_path(a,b,.4-1e-5)
    np.testing.assert_allclose((z1-z0)/2e-5,v,atol=1e-9)

def test_affine_bad_time_shape():
    with pytest.raises(ValueError): affine_path(np.ones((4,2)),np.ones((4,2)),np.ones(4))

def test_rk4_affine_endpoint():
    x = np.linspace(-3,3,20)[:,None]
    np.testing.assert_allclose(rk4(affine_truth,x,40),1.5*x+2,atol=1e-10)

def test_rk4_constant_field():
    x = np.ones((3,2))
    np.testing.assert_allclose(rk4(lambda t,x: np.ones_like(x)*2,x,10),3)

def test_rk4_rejects_nonfinite():
    with pytest.raises(ValueError): rk4(lambda t,x: x*np.nan,[[1.]],10)
