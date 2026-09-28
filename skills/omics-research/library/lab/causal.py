"""Synthetic causal checks. Identification is an assumption, not a fit metric."""
from __future__ import annotations
import numpy as np
from scipy.special import expit
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.model_selection import StratifiedKFold


def crossfit_aipw(x, a, y, folds: int = 5, seed: int = 314, clip: float = .01) -> dict:
    """ATE with cross-fitted logistic/linear nuisance models on independent rows.

    For cell/niche rows, first reformulate around independent experimental units
    or use group cross-fitting and cluster-aware inference. No causal guarantee
    from this function. Clipping may introduce bias; fraction is reported.
    """
    x, a, y = np.asarray(x, float), np.asarray(a), np.asarray(y, float)
    if x.ndim == 1:
        x = x[:, None]
    if x.ndim != 2 or a.ndim != 1 or y.ndim != 1 or len(x) != len(y) or len(a) != len(y):
        raise ValueError("Shape mismatch")
    if np.any(~np.isfinite(x)) or np.any(~np.isfinite(y)) or not set(np.unique(a)) == {0, 1}:
        raise ValueError("Finite x/y and both binary treatment arms required")
    if not 0 < clip < .5 or folds < 2 or min(np.bincount(a.astype(int))) < folds:
        raise ValueError("Invalid clipping/folds or insufficient independent units per arm")
    e, m0, m1 = [np.zeros(len(y)) for _ in range(3)]
    for train, test in StratifiedKFold(folds, shuffle=True, random_state=seed).split(x, a):
        ps = LogisticRegression(C=1e5, max_iter=500).fit(x[train], a[train])
        e[test] = ps.predict_proba(x[test])[:, 1]
        for arm, m in [(0, m0), (1, m1)]:
            subset = train[a[train] == arm]
            m[test] = LinearRegression().fit(x[subset], y[subset]).predict(x[test])
    ec = np.clip(e, clip, 1-clip)
    influence = m1-m0 + a*(y-m1)/ec - (1-a)*(y-m0)/(1-ec)
    weights = a/ec + (1-a)/(1-ec)
    return {"ate": float(influence.mean()),
            "iid_standard_error": float(influence.std(ddof=1)/np.sqrt(len(y))),
            "propensity_min_max": [float(e.min()), float(e.max())],
            "fraction_clipped": float(np.mean(e != ec)),
            "weight_effective_sample_size": float(weights.sum()**2/(weights@weights)),
            "assumption": "independent rows; consistency, positivity, measured exchangeability; nuisance regularity"}


def causal_demo(seed: int = 9001, n: int = 10000) -> dict:
    rng = np.random.default_rng(seed)
    x = rng.normal(size=n)
    a = rng.binomial(1, expit(.9*x))
    y = 2*a + 1.8*x + rng.normal(size=n)
    naive = y[a == 1].mean() - y[a == 0].mean()
    estimated = crossfit_aipw(x, a, y)
    # A and U independent, collider C receives both; true A->Y effect is zero.
    ar = rng.binomial(1, .5, n)
    u = rng.normal(size=n)
    collider = ar + u + .3*rng.normal(size=n)
    outcome = u + rng.normal(size=n)
    coef_unadj = LinearRegression().fit(ar[:, None], outcome).coef_[0]
    coef_coll = LinearRegression().fit(np.c_[ar, collider], outcome).coef_[0]
    return {"scope": "synthetic measured-confounder and collider counterexamples, not patient evidence",
            "seed": seed, "independent_units": n, "known_ATE": 2.,
            "unadjusted_difference": float(naive), "crossfit_AIPW": estimated,
            "collider_example_true_effect": 0., "collider_unadjusted_coefficient": float(coef_unadj),
            "collider_adjusted_coefficient": float(coef_coll)}
