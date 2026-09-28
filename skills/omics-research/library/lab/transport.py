"""Educational dense log-domain balanced/unbalanced entropic OT.

Independent implementation, not vendored POT. Strictly positive masses and
finite costs only; deliberately reject masked/infinite costs and zero weights.
For large real data use audited sparse/low-rank solvers with the same objective.
"""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np
from scipy.special import logsumexp, xlogy
from scipy.optimize import linprog, minimize


@dataclass
class TransportResult:
    plan: np.ndarray
    iterations: int
    residual: float
    linear_cost: float
    total_objective: float
    total_mass: float
    convention: str


def _inputs(a, b, cost, epsilon):
    a, b, c = np.asarray(a, float), np.asarray(b, float), np.asarray(cost, float)
    if a.ndim != 1 or b.ndim != 1 or not len(a) or not len(b) or c.shape != (len(a), len(b)):
        raise ValueError("Expected vectors a,b and cost with shape (len(a),len(b))")
    if any(np.any(~np.isfinite(q)) for q in [a, b, c]) or np.any(a <= 0) or np.any(b <= 0):
        raise ValueError("Finite costs and strictly positive masses required; trim zero support explicitly")
    if not np.isfinite(epsilon) or epsilon <= 0:
        raise ValueError("epsilon must be positive and finite")
    return a, b, c


def generalized_kl(p, q) -> float:
    p, q = np.asarray(p, float), np.asarray(q, float)
    if p.shape != q.shape or np.any(~np.isfinite(p)) or np.any(~np.isfinite(q)) or np.any(p < 0) or np.any(q <= 0):
        raise ValueError("Require aligned nonnegative p and strictly positive q")
    return float(np.sum(xlogy(p, p/q) - p + q))


def balanced_sinkhorn(a, b, cost, epsilon: float = .1, *, tolerance: float = 1e-9,
                      max_iterations: int = 20000) -> TransportResult:
    a, b, c = _inputs(a, b, cost, epsilon)
    if not np.isclose(a.sum(), b.sum(), rtol=1e-12, atol=1e-12):
        raise ValueError("Balanced OT requires equal mass; do not normalize silently")
    if tolerance <= 0 or max_iterations < 1:
        raise ValueError("Invalid convergence settings")
    ref = np.outer(a, b)
    logk = np.log(ref) - c/epsilon
    u, v = np.zeros_like(a), np.zeros_like(b)
    for it in range(1, max_iterations+1):
        u = np.log(a) - logsumexp(logk+v[None, :], axis=1)
        v = np.log(b) - logsumexp(logk+u[:, None], axis=0)
        logp = u[:, None]+logk+v[None, :]
        p = np.exp(logp)
        residual = max(np.max(np.abs(p.sum(1)-a)), np.max(np.abs(p.sum(0)-b)))
        if residual < tolerance:
            break
    else:
        raise RuntimeError(f"Balanced Sinkhorn not converged: marginal residual={residual:g}")
    linear = float(np.sum(p*c))
    total = linear + epsilon*generalized_kl(p, ref)
    return TransportResult(p, it, float(residual), linear, float(total), float(p.sum()), "KL(plan,a⊗b)")


def uot_objective(plan, a, b, cost, epsilon, rho_a, rho_b, reference: str = "product") -> float:
    p = np.asarray(plan, float)
    a, b, c = _inputs(a, b, cost, epsilon)
    if p.shape != c.shape or min(rho_a, rho_b) <= 0 or not np.isfinite(rho_a+rho_b):
        raise ValueError("Plan shape and positive finite marginal penalties required")
    ref = np.outer(a, b) if reference == "product" else np.ones_like(c) if reference == "ones" else None
    if ref is None:
        raise ValueError("reference must be product or ones")
    return float(np.sum(p*c) + epsilon*generalized_kl(p, ref)
                 + rho_a*generalized_kl(p.sum(1), a) + rho_b*generalized_kl(p.sum(0), b))


def unbalanced_sinkhorn(a, b, cost, epsilon: float = .1, rho_a: float = 1., rho_b: float = 1.,
                        *, reference: str = "product", tolerance: float = 1e-9,
                        max_iterations: int = 20000) -> TransportResult:
    a, b, c = _inputs(a, b, cost, epsilon)
    if min(rho_a, rho_b) <= 0 or not np.isfinite(rho_a+rho_b):
        raise ValueError("Positive finite rho required; use balanced solver for hard marginals")
    if tolerance <= 0 or max_iterations < 1:
        raise ValueError("Invalid convergence settings")
    if reference not in {"product", "ones"}:
        raise ValueError("reference must be product or ones")
    logref = np.log(np.outer(a, b)) if reference == "product" else np.zeros_like(c)
    logk = logref-c/epsilon
    u, v = np.zeros_like(a), np.zeros_like(b)
    tau_a, tau_b = rho_a/(rho_a+epsilon), rho_b/(rho_b+epsilon)
    for it in range(1, max_iterations+1):
        u = tau_a*(np.log(a) - logsumexp(logk+v[None, :], axis=1))
        v = tau_b*(np.log(b) - logsumexp(logk+u[:, None], axis=0))
        logp = logk+u[:, None]+v[None, :]
        logr = logsumexp(logp, axis=1)
        logs = logsumexp(logp, axis=0)
        # First-order residual, not distance to hard marginals (which are relaxed).
        gradient = c + epsilon*(logp-logref) + rho_a*(logr-np.log(a))[:, None] + rho_b*(logs-np.log(b))[None, :]
        residual = float(np.max(np.abs(gradient)))
        if residual < tolerance:
            break
    else:
        raise RuntimeError(f"UOT not converged: first-order residual={residual:g}")
    p = np.exp(logp)
    if np.any(~np.isfinite(p)) or p.sum() <= 0:
        raise FloatingPointError("Plan overflow/underflow; rescale cost and regularization")
    return TransportResult(p, it, residual, float(np.sum(p*c)),
                           uot_objective(p, a, b, c, epsilon, rho_a, rho_b, reference),
                           float(p.sum()), "KL(plan,a⊗b)" if reference == "product" else "KL(plan,ones)")


def exact_balanced_lp(a, b, cost) -> np.ndarray:
    a, b, c = _inputs(a, b, cost, 1.)
    if not np.isclose(a.sum(), b.sum(), atol=1e-12, rtol=1e-12):
        raise ValueError("Unequal mass")
    n, m = c.shape
    ae = np.r_[np.kron(np.eye(n), np.ones((1, m))), np.kron(np.ones((1, n)), np.eye(m))]
    ans = linprog(c.ravel(), A_eq=ae, b_eq=np.r_[a, b], bounds=(0, None), method="highs")
    if not ans.success:
        raise RuntimeError(ans.message)
    return ans.x.reshape(n, m)


def uot_scipy_oracle(a, b, cost, epsilon, rho_a, rho_b, reference="product") -> dict:
    """Small dense independent L-BFGS-B oracle in positive plan coordinates."""
    a, b, c = _inputs(a, b, cost, epsilon)
    ref = np.outer(a, b) if reference == "product" else np.ones_like(c)
    def fg(vec):
        p = vec.reshape(c.shape)
        f = uot_objective(p, a, b, c, epsilon, rho_a, rho_b, reference)
        g = c+epsilon*np.log(p/ref)+rho_a*np.log(p.sum(1)/a)[:, None]+rho_b*np.log(p.sum(0)/b)[None, :]
        return f, g.ravel()
    ans = minimize(fg, np.outer(a, b).ravel(), jac=True, method="L-BFGS-B",
                   bounds=[(1e-14, None)]*c.size,
                   options={"ftol": 1e-14, "gtol": 1e-9, "maxiter": 10000})
    if not ans.success:
        raise RuntimeError(ans.message)
    return {"plan": ans.x.reshape(c.shape), "objective": float(ans.fun), "iterations": int(ans.nit)}


def sample_pairs(plan, n: int, rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    """Sample from plan/total_mass. This DISCARDs total-mass information for FM."""
    p = np.asarray(plan, float)
    if p.ndim != 2 or np.any(~np.isfinite(p)) or np.any(p < 0) or p.sum() <= 0 or n < 1:
        raise ValueError("Require nonzero nonnegative plan and positive sample size")
    flat = rng.choice(p.size, n, p=(p/p.sum()).ravel())
    return np.unravel_index(flat, p.shape)


def transport_demo() -> dict:
    a, b = np.array([.4, .6]), np.array([.5, .5])
    c = np.array([[0., 1.], [1., 0.]])
    bal = balanced_sinkhorn(a, b, c, .06)
    lp = exact_balanced_lp(a, b, c)
    ua, ub = np.array([.3, .7]), np.array([.2, .4, .3])
    uc = np.array([[.1, .7, 1.2], [.8, .3, .2]])
    comparisons = []
    for ref in ["product", "ones"]:
        u = unbalanced_sinkhorn(ua, ub, uc, .3, .7, 1.1, reference=ref)
        oracle = uot_scipy_oracle(ua, ub, uc, .3, .7, 1.1, ref)
        comparisons.append({"reference": ref, "iterations": u.iterations,
                            "first_order_residual": u.residual, "mass": u.total_mass,
                            "linear_cost": u.linear_cost, "total_objective": u.total_objective,
                            "oracle_max_plan_abs_error": float(np.max(np.abs(u.plan-oracle['plan']))),
                            "oracle_objective_abs_error": abs(u.total_objective-oracle["objective"])})
    return {"scope": "independent dense implementation vs SciPy optimization; POT runtime not used",
            "balanced_marginal_residual": bal.residual, "balanced_linear_cost": bal.linear_cost,
            "unregularized_LP_cost": float(np.sum(lp*c)), "unbalanced": comparisons}
