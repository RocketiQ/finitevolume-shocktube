import os, json, time, argparse, yaml
import matplotlib.pyplot as plt
from src.roe.solver import run_case

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True, help="Path to YAML case file")
    args = ap.parse_args()

    with open(args.manifest) as f:
        params = yaml.safe_load(f)

    t0 = time.time()
    out = run_case(params)
    wall = time.time() - t0

    os.makedirs("outputs", exist_ok=True)

    plt.figure()
    plt.plot(out["x"], out["rho"])
    plt.title(f"Density (t={out['t']:.3f})")
    plt.xlabel("x"); plt.ylabel("rho")
    plt.tight_layout()
    plt.savefig("outputs/density.png", dpi=150)
    plt.close()

    log = {
        "cmd": f"python -m scripts.run --manifest {args.manifest}",
        "wall_time_s": wall,
        "nx": len(out["x"]),
        "t_final": out["t"],
    }
    with open("outputs/run_log.json", "w") as f:
        json.dump(log, f, indent=2)

if __name__ == "__main__":
    main()

