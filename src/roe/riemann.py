import numpy as np

def Riemann(left_state, right_state, gamma: float) -> np.ndarray:
    """
    Roe flux for 1D Euler using primitive states [rho, u, p] on each side.
    Returns flux vector [rho*u, rho*u**2 + p, u*(ke+ue+p)].
    """
    rho_l, u_l, p_l = left_state
    rho_r, u_r, p_r = right_state

    ke_l = 0.5 * rho_l * u_l**2
    ue_l = p_l / (gamma - 1.0)
    h_l  = (ke_l + ue_l + p_l) / rho_l

    ke_r = 0.5 * rho_r * u_r**2
    ue_r = p_r / (gamma - 1.0)
    h_r  = (ke_r + ue_r + p_r) / rho_r

    # Roe-averaged state
    sr_l, sr_r = np.sqrt(rho_l), np.sqrt(rho_r)
    denom = sr_l + sr_r
    u_t  = (sr_l * u_l + sr_r * u_r) / denom
    h_t  = (sr_l * h_l + sr_r * h_r) / denom
    a_t  = np.sqrt((gamma - 1.0) * (h_t - 0.5 * u_t**2))

    lam1, lam2, lam3 = u_t - a_t, u_t, u_t + a_t
    evalues = np.array([lam1, lam2, lam3])

    r1 = np.array([1.0, u_t - a_t, h_t - a_t * u_t])
    r2 = np.array([1.0, u_t,       0.5 * u_t**2])
    r3 = np.array([1.0, u_t + a_t, h_t + a_t * u_t])
    evec = np.array([r1, r2, r3])

    rho_rl = sr_l * sr_r
    dv1 = 0.5 / (a_t**2) * ((p_r - p_l) - rho_rl * a_t * (u_r - u_l))
    dv2 = (rho_r - rho_l) - (p_r - p_l) / (a_t**2)
    dv3 = 0.5 / (a_t**2) * ((p_r - p_l) + rho_rl * a_t * (u_r - u_l))
    ws  = np.array([dv1, dv2, dv3])

    # Physical fluxes
    F_l = np.array([rho_l * u_l, rho_l * u_l**2 + p_l, u_l * (ke_l + ue_l + p_l)])
    F_r = np.array([rho_r * u_r, rho_r * u_r**2 + p_r, u_r * (ke_r + ue_r + p_r)])

    # Roe flux
    flux_diff = np.zeros(3)
    for i in range(3):
        flux_diff += ws[i] * abs(evalues[i]) * evec[i]
    return 0.5 * (F_l + F_r) - 0.5 * flux_diff

