"""Independent implementation of transparent statistical checks.

These utilities do not replace a count-data differential expression package.
References and assumptions: knowledge/02_statistics.md.
"""
from __future__ import annotations
import numpy as np
from scipy import stats


def adjust_pvalues(pvalues, method: str = "BH") -> np.ndarray:
    """BH/BY adjusted p-values, preserving original order. NaN is rejected.

    Supply a prespecified family of valid frequentist p-values, not Bayes factors
    or posterior probabilities. Dependence assumptions are not checked by code.
    """
    p = np.asarray(pvalues, dtype=float)
    if p.ndim != 1 or np.any(~np.isfinite(p)) or np.any((p < 0) | (p > 1)):
        raise ValueError("pvalues must be a finite one-dimensional array in [0,1]")
    if method.upper() not in {"BH", "BY"}:
        raise ValueError("method must be BH or BY")
    m = p.size
    if not m:
        return p.copy()
    order = np.argsort(p, kind="stable")
    correction = np.sum(1.0 / np.arange(1, m + 1)) if method.upper() == "BY" else 1.0
    ranked = p[order] * m * correction / np.arange(1, m + 1)
    adjusted = np.minimum.accumulate(ranked[::-1])[::-1].clip(0, 1)
    out = np.empty_like(p)
    out[order] = adjusted
    return out


def assert_group_disjoint(train_groups, test_groups) -> None:
    a, b = set(train_groups), set(test_groups)
    if not a or not b:
        raise ValueError("Train and test groups must both be nonempty")
    overlap = a & b
    if overlap:
        raise ValueError(f"Independent-unit leakage: {sorted(map(str, overlap))}")


def pseudobulk_counts(counts, groups) -> tuple[np.ndarray, np.ndarray]:
    """Sum *raw integer counts* within supplied donor×celltype groups.

    Empty/absent cell populations are not imputed here. Caller must distinguish
    missing cell populations from genuinely measured zero expression.
    """
    x = np.asarray(counts)
    g = np.asarray(groups)
    if x.ndim != 2 or g.ndim != 1 or len(g) != x.shape[0]:
        raise ValueError("Expected cells×genes counts and one group per cell")
    if not len(g) or np.any(~np.isfinite(x)) or np.any(x < 0) or np.any(x != np.floor(x)):
        raise ValueError("Use nonempty, nonnegative finite raw integer counts")
    if any(v is None or (isinstance(v, (str, np.str_)) and not v.strip())
           or (isinstance(v, (float, np.floating)) and not np.isfinite(v)) for v in g):
        raise ValueError("Missing group identifiers")
    names, inverse = np.unique(g, return_inverse=True)
    out = np.zeros((len(names), x.shape[1]), dtype=np.int64)
    if int(x.max(initial=0)) * max(1, x.shape[0]) > np.iinfo(np.int64).max:
        raise OverflowError("Count sum exceeds int64")
    np.add.at(out, inverse, x.astype(np.int64))
    return names, out


def permutation_pvalue(observed: float, null_statistics, *, two_sided: bool = True,
                       exact_enumeration: bool = False) -> float:
    """Monte Carlo +1 convention; exact enumeration uses an exact fraction.

    Caller supplies statistics from an exchangeability-valid scheme. For exact
    enumeration, include the observed arrangement in the enumerated null.
    """
    null = np.asarray(null_statistics, dtype=float)
    if null.ndim != 1 or not len(null) or not np.isfinite(observed) or np.any(~np.isfinite(null)):
        raise ValueError("Require finite observed value and a nonempty null vector")
    obs = abs(observed) if two_sided else observed
    comp = np.abs(null) if two_sided else null
    b = int(np.count_nonzero(comp >= obs))
    return b / len(null) if exact_enumeration else (b + 1) / (len(null) + 1)


def wilson_interval(successes: int, total: int, confidence: float = .95) -> list[float]:
    if total < 1 or not (0 <= successes <= total) or not (0 < confidence < 1):
        raise ValueError("Invalid binomial interval inputs")
    z = stats.norm.ppf((1 + confidence) / 2)
    phat = successes / total
    den = 1 + z*z / total
    ctr = (phat + z*z/(2*total)) / den
    radius = z * np.sqrt(phat*(1-phat)/total + z*z/(4*total*total)) / den
    return [float(ctr-radius), float(ctr+radius)]


def pseudoreplication_demo(seed: int = 20260928, repetitions: int = 400) -> dict:
    """Null Gaussian random-intercept simulation; NOT RNA count benchmarking."""
    rng = np.random.default_rng(seed)
    nd, nc = 8, 60
    cell_sig, donor_sig = 0, 0
    for _ in range(repetitions):
        intercept = rng.normal(0, 1, (2, nd, 1))
        x = intercept + rng.normal(0, 1, (2, nd, nc))
        cell_sig += stats.ttest_ind(x[0].ravel(), x[1].ravel(), equal_var=False).pvalue < .05
        donor_sig += stats.ttest_ind(x[0].mean(1), x[1].mean(1), equal_var=False).pvalue < .05
    return {"scope": "synthetic Gaussian null; donor mean Welch test, not NB DE",
            "seed": seed, "repetitions": repetitions, "donors_per_arm": nd,
            "cells_per_donor": nc, "nominal_alpha": .05,
            "cell_level_false_positive_rate": cell_sig/repetitions,
            "donor_level_false_positive_rate": donor_sig/repetitions,
            "cell_level_monte_carlo_95CI": wilson_interval(int(cell_sig), repetitions),
            "donor_level_monte_carlo_95CI": wilson_interval(int(donor_sig), repetitions)}


def selection_demo(seed: int = 820, repetitions: int = 6000, family_size: int = 100) -> dict:
    """Independent uniform null p-values illustrate post-selection testing."""
    rng = np.random.default_rng(seed)
    p = rng.uniform(size=(repetitions, family_size))
    selected = p.min(axis=1)
    # Independent holdout p-value for the feature picked in discovery.
    holdout = rng.uniform(size=repetitions)
    family_reject = [np.any(adjust_pvalues(row) <= .05) for row in p]
    return {"scope": "all-null independent Uniform(0,1); FDR equals P(any rejection)",
            "seed": seed, "repetitions": repetitions, "family_size": family_size,
            "postselection_single_test_rejection": float(np.mean(selected <= .05)),
            "full_family_BH_any_rejection": float(np.mean(family_reject)),
            "independent_holdout_rejection": float(np.mean(holdout <= .05))}
