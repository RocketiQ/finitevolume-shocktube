import numpy as np
from .riemann import Riemann

def run_case(params: dict) -> dict:
    """
    Runs a 1D shock-tube using Roe flux.
    params: nx, cfl, t_end, gamma, (optional x_ini, x_fin)
    Returns dict with arrays/metadata for tests/plots.
    """
    nx     = int(params.get("nx", 100))
    CFL    = float(params.get("cfl", 0.5))
    t_end  = float(params.get("t_end", 0.20))
    gamma  = float(params.get("gamma", 1.4))
    x_ini  = float(params.get("x_ini", 0.0))
    x_fin  = float(params.get("x_fin", 1.0))

    dx = (x_fin - x_ini) / nx
    x  = np.linspace(x_ini + 0.5 * dx, x_fin - 0.5 * dx, nx)

    # Sod IC
    mid  = nx // 2
    rho0 = np.empty(nx); u0 = np.zeros(nx); p0 = np.empty(nx)
    rho0[:mid] = 1.0;   rho0[mid:] = 0.125
    p0[:mid]   = 1.0;   p0[mid:]   = 0.1

    E0 = p0 / ((gamma - 1.0) * rho0) + 0.5 * u0**2
    q  = np.vstack([rho0, rho0 * u0, rho0 * E0])

    t, it = 0.0, 0
    while t < t_end:
        rho = q[0]
        u   = q[1] / np.maximum(rho, 1e-14)
        e   = q[2] / np.maximum(rho, 1e-14)
        p   = (gamma - 1.0) * rho * (e - 0.5 * u**2)
        a   = np.sqrt(np.maximum(gamma * p / np.maximum(rho, 1e-14), 1e-14))

        if p.min() <= 0:
            print("Warning: non-physical pressure encountered.")

        dt = CFL * dx / np.max(np.abs(u) + a)
        if t + dt > t_end:
            dt = t_end - t

        F = np.zeros((3, nx - 1))
        for i in range(nx - 1):
            left  = np.array([rho[i],     u[i],     p[i]])
            right = np.array([rho[i + 1], u[i + 1], p[i + 1]])
            F[:, i] = Riemann(left, right, gamma)

        q0 = q.copy()
        for i in range(1, nx - 1):
            q[:, i] = q0[:, i] - (dt / dx) * (F[:, i] - F[:, i - 1])
        q[:, 0]  = q0[:, 0]
        q[:, -1] = q0[:, -1]

        t  += dt
        it += 1

    rho = q[0]
    u   = q[1] / np.maximum(rho, 1e-14)
    e   = q[2] / np.maximum(rho, 1e-14)
    p   = (gamma - 1.0) * rho * (e - 0.5 * u**2)

    return {"x": x, "dx": dx, "rho0": rho0, "rho": rho, "u": u, "p": p, "t": t, "it": it}

