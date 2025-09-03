import yaml
import numpy as np
from src.roe.solver import run_case

def test_mass_near_conserved():
    with open("cases/sod_small.yml") as f:
        params = yaml.safe_load(f)
    out = run_case(params)
    dx  = out["dx"]
    m0  = (out["rho0"] * dx).sum()
    m   = (out["rho"]  * dx).sum()
    # allow small numerical error
    assert np.isclose(m, m0, rtol=1e-3, atol=1e-6)
