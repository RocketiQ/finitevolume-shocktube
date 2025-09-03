import yaml
from src.roe.solver import run_case

def test_smoke_sod_small():
    with open("cases/sod_small.yml") as f:
        params = yaml.safe_load(f)
    out = run_case(params)
    # basic physical sanity
    assert out["rho"].min() > 0.0
    assert out["p"].min()   > 0.0
