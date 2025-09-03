# finitevolume-shocktube
1D finite volume Roe solver for shock-tube problems in compressible flow.

**finitevolume-shocktube** is an open-source Python solver for the 1D compressible Euler equations using the finite volume method with a Roe approximate Riemann solver.
It is developed and maintained under the [RocketiQ](https://github.com/RocketiQ) organization as part of our Track A Open-Source Research Projects, enabling students to learn and contribute to computational fluid dynamics (CFD) in aerospace contexts.

---

## Features
- Roe flux solver for 1D Euler equations (ρ, ρu, ρE).
- Configurable via simple YAML manifests.
- Tested with the classical Sod shock-tube problem.
- Unit tests for positivity and approximate mass conservation.
- Continuous integration (GitHub Actions) runs lint + tests + a reference case.
- Reference outputs (density profile, runtime log) included for validation.

---

## Getting Started

### Clone the repository
```bash
git clone https://github.com/RocketiQ/finitevolume-shocktube.git
```

### Create environment & install dependencies
```bash
python -m venv .venv
. .venv/Scripts/activate    # Windows PowerShell
# or: source .venv/bin/activate  # Linux/Mac

pip install -r env/requirements.txt
```

### Run tests
```bash
python -m pytest -q
```
Expected output:
```
..
2 passed in <time>s
```

### Run the reference Sod case
```bash
python -m scripts.run --manifest cases/sod_small.yml
```

This will produce:
- `outputs/density.png` – final density profile  
- `outputs/run_log.json` – command + wall-time + runtime info

---

## Documentation
- [`docs/METHODS.md`](docs/METHODS.md) – numerical methods, assumptions.  
- [`docs/RESULTS.md`](docs/RESULTS.md) – reference Sod case results.  

---

## Contributing
Contributions are welcome via pull requests.

**Gate 001 (quick readiness check)**
1. Clone the repo and create the environment.
2. Run `python -m pytest -q` (tests must pass).
3. Run `python -m scripts.run --manifest cases/sod_small.yml` and attach `outputs/density.png` in your PR if results change.

PRs must:
- Use the provided [PR template](.github/PULL_REQUEST_TEMPLATE.md).
- Pass CI (lint, tests, reference case).
- Update `docs/RESULTS.md` if results change.

See [`CITATION.cff`](CITATION.cff) for citation info.

---

## License
Distributed under the **Apache 2.0 License**. See [`LICENSE`](LICENSE).

---

## Citation
If you use this code in research or teaching, please cite via GitHub’s **“Cite this repository”** button, which uses the [`CITATION.cff`](CITATION.cff).

