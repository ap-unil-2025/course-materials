# SIMCLT – Chain‑Ladder Reserving Simulator (Template Project)

> *Final‑project template for MSc “Advanced Programming” – Spring 2025*

---

## 1 · Why this project?

The **Mack Chain‑Ladder** technique is the workhorse for actuaries who must estimate
the unpaid claim liability on portfolios of property‑casualty insurance business.
Yet many practitioners rely on opaque spreadsheets.  *SIMCLT* aims to provide a
**transparent, open‑source Python package and CLI** that reproduces textbook
Chain‑Ladder results, including stochastic variation, in a way that is
installable from PyPI and fully unit‑tested.

By completing this project you will practise:

* packaging & dependency management (`pyproject.toml`, wheels, TestPyPI)
* numerical programming with **NumPy/Pandas**
  (triangle reshaping, cumulative sums, link ratios)
* statistical implementation of Mack variance & residual bootstrap
* automated testing / CI / coverage discipline (≥ 90 %)
* clean CLI design with **Typer** and type‑hinted public APIs

---

## 2 · Learning objectives

| Category          | You will be able to…                                                                      |
| ----------------- | ----------------------------------------------------------------------------------------- |
| **Software Eng.** | structure a `src/` package, expose entry‑points, ship wheels, enforce semantic versioning |
| **Statistics**    | derive & code Mack σ² formulae, implement a bootstrap to obtain reserve distributions     |
| **Dev Ops**       | configure GitHub Actions for tests → wheel build → TestPyPI upload                        |
| **Communication** | document APIs in Sphinx, write a short technical report, deliver a 5‑min demo             |

---

## 3 · Scope & deliverables

### 3.1 Must‑have modules (public API)

| Module         | Key public classes / functions                                           |
| -------------- | ------------------------------------------------------------------------ |
| `triangle.py`  | `Triangle.from_csv()`, `.as_numpy()`, `.to_csv()`                        |
| `mack.py`      | `MackChainLadder.reserve()`, `.reserve_variance()`                       |
| `bootstrap.py` | `BootstrapChainLadder.simulate()`, `.quantile(q)`                        |
| `cli.py`       | `simclt mack <csv>` & `simclt bootstrap <csv> --nsim 10000 --quant 0.95` |

### 3.2 Non‑functional requirements

* Python ≥ 3.10, type‑annotated (`mypy --strict` clean)
* black‑formatted, flake8‑clean
* ≥ 90 % pytest coverage (`--cov-fail-under=90` in CI)
* Sphinx docs auto‑deploy via GitHub Pages
* Wheels built & uploaded to **TestPyPI** on every tag push (`v0.x.y`, `v1.0.0`)
* License: **MIT**; all dependencies permissive (MIT/BSD/Apache‑2.0)

### 3.3 Deliverables recap

* GitHub repo **tag `v1.0.0`** (Week 10) with green CI
* 3–4 page Technical Report (PDF) covering architecture, maths, validation, labour split
* 5‑minute demo in Week 11 practical session

---

## 4 · Milestones & checkpoints

| Week   | Checkpoint                             | Acceptance test                                        |
| ------ | -------------------------------------- | ------------------------------------------------------ |
| **2**  | Triangle loader + smoke test           | `simclt mack sample.csv` prints a numeric reserve      |
| **4**  | Deterministic reserve **and variance** | Values match CAS textbook within ±1 %                  |
| **6**  | Bootstrap simulator                    | 10 000 sims converge ±5 % and coverage ≥ 80 %          |
| **8**  | Docs + CI + packaging polish           | `pip install .` works on CI runner; wheels on TestPyPI |
| **10** | **Code‑freeze `v1.0.0`**               | All repo requirements in §3.2 satisfied                |
| **11** | Live demo + report                     | Repo, PDF, demo delivered                              |

---

## 5 · Stretch goals (optional + extra credit)

* Plugin entry‑points for alternative reserving methods (Bornhuetter‑Ferguson, GLM)
* Cython or Numba speed‑up of the bootstrap loop
* Parallel simulations via `joblib.Parallel`
* Property‑based tests using **Hypothesis**
<!-- All very funny suggestions, I'll think about them * Add a `--verbose` flag to the CLI to print intermediate results
* Implement a `--plot` flag to visualize the reserve distribution
* Add a `--validate` flag to check the input triangle for consistency
* Add a `--save` flag to save the reserve distribution to a file
* Add a `--compare` flag to compare two reserve distributions
* Add a `--report` flag to generate a report of the reserve distribution
* Add a `--config` flag to load configuration from a file
* Add a `--version` flag to print the package version
* Add a `--help` flag to print the CLI help message
* Add a `--license` flag to print the package license
* Add a `--changelog` flag to print the package changelog
* Add a `--contributors` flag to print the package contributors
* Add a `--citation` flag to print the package citation
* Add a `--benchmark` flag to run performance benchmarks
* Add a `--profile` flag to profile the code execution
* Add a `--debug` flag to enable debug logging
* Add a `--test` flag to run the test suite
* Add a `--lint` flag to run the linter
* Add a `--format` flag to format the code
* Add a `--typecheck` flag to type-check the code
* Add a `--docs` flag to build the documentation
* Add a `--ci` flag to run the CI pipeline
* Add a `--release` flag to create a new release
* Add a `--deploy` flag to deploy the package to PyPI -->

---

## 7 · External resources

* **Mack, T.** (1993). “Distribution‑free Calculation of the Standard Error of
  Chain‑Ladder Reserve Estimates.” *ASTIN Bulletin* 23(2).
* **England & Verrall** (1999). “Analytic and Bootstrap Estimates of Prediction
  Errors in Claims Reserving.”
* R package **`ChainLadder`** – inspection reference for test cases.

---

> **Thumb‑rule for success:** keep CI green, commit small, test every formula, and
> document any AI‑generated snippet in `AI_LOG.md`.
