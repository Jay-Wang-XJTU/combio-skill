"""Own conditional flow-matching laboratory in PyTorch; no upstream code copied."""
from __future__ import annotations
import numpy as np


def affine_path(x0, x1, t):
    """Linear endpoint path and target velocity; t is scalar or (batch,1)."""
    x0, x1, t = np.asarray(x0, float), np.asarray(x1, float), np.asarray(t, float)
    if x0.shape != x1.shape or x0.ndim != 2 or np.any(~np.isfinite(x0)) or np.any(~np.isfinite(x1)):
        raise ValueError("Endpoints must be equal-shape finite batch×features")
    if np.any(~np.isfinite(t)) or np.any((t < 0) | (t > 1)) or not (t.ndim == 0 or t.shape == (len(x0), 1)):
        raise ValueError("t must be scalar or (batch,1) in [0,1]")
    return (1-t)*x0+t*x1, x1-x0


def rk4(velocity, x0, steps: int = 100):
    """NumPy RK4 on [0,1], retaining sample shape."""
    if steps < 1:
        raise ValueError("steps must be positive")
    x = np.asarray(x0, float).copy()
    if np.any(~np.isfinite(x)):
        raise ValueError("Nonfinite initial values")
    h = 1./steps
    for i in range(steps):
        t = i*h
        k1 = np.asarray(velocity(t, x), float)
        k2 = np.asarray(velocity(t+h/2, x+h*k1/2), float)
        k3 = np.asarray(velocity(t+h/2, x+h*k2/2), float)
        k4 = np.asarray(velocity(t+h, x+h*k3), float)
        if any(k.shape != x.shape or np.any(~np.isfinite(k)) for k in [k1, k2, k3, k4]):
            raise ValueError("Velocity must return finite values with unchanged shape")
        x += h*(k1+2*k2+2*k3+k4)/6
    return x


def affine_truth(t, x):
    # x1 = 1.5*x0+2. Conditional velocity expressed in current coordinates.
    return (.5*np.asarray(x)+2)/(1+.5*t)


def flow_demo(seed: int = 31415, training_steps: int = 1500) -> dict:
    import torch
    from torch import nn
    torch.set_num_threads(1)
    torch.manual_seed(seed)
    torch.use_deterministic_algorithms(True)
    model = nn.Sequential(nn.Linear(2, 64), nn.SiLU(), nn.Linear(64, 64), nn.SiLU(), nn.Linear(64, 1))
    optimizer = torch.optim.Adam(model.parameters(), lr=.002)
    # Validation sample is fixed and independent of subsequently sampled training pairs.
    xv = torch.randn(2048, 1); tv = torch.rand(2048, 1)
    targetv = .5*xv+2
    inputv = torch.cat([(1+.5*tv)*xv+2*tv, tv], dim=1)
    with torch.no_grad():
        initial = float(((model(inputv)-targetv)**2).mean())
    for _ in range(training_steps):
        x0 = torch.randn(256, 1)
        t = torch.rand(256, 1)
        x1 = 1.5*x0+2
        xt = (1-t)*x0+t*x1
        loss = ((model(torch.cat([xt, t], dim=1))-(x1-x0))**2).mean()
        optimizer.zero_grad(set_to_none=True); loss.backward(); optimizer.step()
    with torch.no_grad():
        final = float(((model(inputv)-targetv)**2).mean())
    def velocity(t, x):
        z = torch.as_tensor(x, dtype=torch.float32)
        tt = torch.full_like(z, t)
        with torch.no_grad():
            return model(torch.cat([z, tt], dim=1)).numpy().astype(float)
    rng = np.random.default_rng(seed+1)
    x0 = rng.normal(size=(2048, 1))
    target = 1.5*x0+2
    y40, y80 = rk4(velocity, x0, 40), rk4(velocity, x0, 80)
    return {"scope": "own 1D affine Gaussian CFM, not CellFlow or published biological replication",
            "seed": seed, "device": "CPU", "steps": training_steps,
            "initial_heldout_velocity_MSE": initial, "final_heldout_velocity_MSE": final,
            "paired_endpoint_RMSE": float(np.sqrt(np.mean((y80-target)**2))),
            "empirical_1D_endpoint_W2": float(np.sqrt(np.mean((np.sort(y80[:,0])-np.sort(target[:,0]))**2))),
            "endpoint_mean": float(y80.mean()), "endpoint_sd": float(y80.std()),
            "RK4_40_vs_80_max_abs_difference": float(np.max(np.abs(y40-y80))),
            "ground_truth": "known affine coupling x1=1.5*x0+2; normalized time, not biological units"}
