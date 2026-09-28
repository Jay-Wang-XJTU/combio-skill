"""Stress testing an upstream assignment/coordinate process (not calibrated CI)."""
from __future__ import annotations
import numpy as np
from scipy.spatial.distance import cdist


def knn_edges(xy, k: int = 6) -> np.ndarray:
    """Directed kNN, self-excluded. Only use within a physical sample/FOV."""
    xy = np.asarray(xy, dtype=float)
    if xy.ndim != 2 or xy.shape[1] < 2 or np.any(~np.isfinite(xy)) or not 1 <= k < len(xy):
        raise ValueError("Finite coordinates and 1 <= k < n required")
    d = cdist(xy, xy)
    np.fill_diagonal(d, np.inf)
    idx = np.argsort(d, axis=1, kind="stable")[:, :k]
    out = np.zeros((len(xy), len(xy)), bool)
    out[np.arange(len(xy))[:, None], idx] = True
    return out


def edge_jaccard(a, b) -> float:
    a, b = np.asarray(a, bool), np.asarray(b, bool)
    if a.shape != b.shape:
        raise ValueError("Edges must be aligned to the same nodes")
    union = np.count_nonzero(a | b)
    return float(np.count_nonzero(a & b)/union) if union else 1.0


def assignment_mix(x, adjacency, fraction: float) -> np.ndarray:
    """Linear expected-count neighbor contamination, not discrete transcript assignment.

    Each observed row is (1-f)*own + f*mean(neighbors); total counts across cells
    need not be conserved because this is row mixing, not molecule tracking.
    """
    x, a = np.asarray(x, float), np.asarray(adjacency, bool)
    if x.ndim != 2 or a.shape != (len(x), len(x)) or np.any(a.sum(1) == 0):
        raise ValueError("Require counts and aligned graph with nonempty neighborhoods")
    if np.any(~np.isfinite(x)) or np.any(x < 0) or not 0 <= fraction <= 1:
        raise ValueError("Invalid expected counts or mixture fraction")
    return (1-fraction)*x + fraction*(a@x)/a.sum(1, keepdims=True)


def spatial_demo(seed: int = 77, repetitions: int = 40) -> dict:
    rng = np.random.default_rng(seed)
    n = 240
    xy = rng.uniform(size=(n, 2))
    tumor = xy[:, 0] > .5
    # Tumor marker truly absent in non-tumor; asymmetric count levels.
    x = np.c_[np.where(tumor, 120., 0.), np.where(tumor, 1., 12.)]
    adj = knn_edges(xy)
    base = (x + adj@x/6).mean(1)
    interface = (~tumor) & (adj@tumor.astype(int) > 0)
    rows = []
    for fraction, jitter in [(0., 0.), (.05, .005), (.15, .02), (.3, .05)]:
        jac, expr, niche = [], [], []
        for _ in range(repetitions):
            coords = xy + rng.normal(0, jitter, xy.shape)
            new_adj = knn_edges(coords)
            contaminated = assignment_mix(x, new_adj, fraction)
            score = (contaminated + new_adj@contaminated/6).mean(1)
            jac.append(edge_jaccard(adj, new_adj))
            expr.append(float(contaminated[interface, 0].mean()))
            niche.append(float(np.mean(np.abs(score-base))))
        rows.append({"contamination_fraction": fraction, "coordinate_jitter_sd_in_unit_square": jitter,
                     "edge_jaccard_mean": float(np.mean(jac)),
                     "false_tumor_marker_in_interface_non_tumor_mean": float(np.mean(expr)),
                     "niche_score_absolute_drift_mean": float(np.mean(niche))})
    return {"scope": "user-chosen stress scenarios; not posterior samples or calibrated coverage",
            "seed": seed, "repetitions_per_scenario": repetitions, "cells": n,
            "scenarios": rows, "uncertainty_label": "sensitivity range only"}
