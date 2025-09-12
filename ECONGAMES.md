# ECONGAMES – Monte‑Carlo Game‑Theory Toolkit (Template Project)

> *Final‑project template for MSc “Elementary Programming in Python” – Spring 2025*

---

## 1 · Why this project?

Many economic and actuarial problems can be framed as **strategic interactions**—from
price wars to underwriting cycles.  The research community has mature theory but
lacks **hands‑on, reproducible simulation tools** for teaching and exploration.
*ECONGAMES* fills that gap: students will ship a **pip‑installable package & CLI**
that simulates repeated 2‑player normal‑form games (e.g., Prisoner’s Dilemma,
Cournot duopoly) under configurable strategies, then produces statistical
comparisons of pay‑offs.

By completing this project you will practise:

* object‑oriented modelling (Game, Strategy, Simulator classes)
* discrete‑event simulation & randomisation with **NumPy**
* statistical comparison of strategy performance (means, variance, t‑tests)
* packaging, testing, CI/CD and documentation discipline

---

## 2 · Learning objectives

| Domain            | You will be able to…                                                                                             |
| ----------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Software Eng.** | apply the Strategy pattern, expose a Typer CLI, package wheels to TestPyPI                                       |
| **Statistics**    | estimate mean/variance of pay‑offs, run paired *t*‑tests or non‑parametric comparisons, reason about convergence |
| **Dev Ops**       | maintain GitHub Actions pipelines, coverage ≥ 90 %, docs on Pages                                                |
| **Communication** | write concise API docs, explain simulation design in a PDF and live demo                                         |

---

## 3 · Scope & deliverables

### 3.1 Must‑have modules (public API)

| Module          | Public classes / functions                                          |
| --------------- | ------------------------------------------------------------------- |
| `game.py`       | `NormalFormGame` with `.payoff()` and factory `prisoners_dilemma()` |
| `strategies.py` | `Strategy` ABC + `RandomStrategy`, `TitForTat`, `GrimTrigger`       |
| `simulator.py`  | `MonteCarloSimulator.run()` + `.summary()` (mean, var)              |
| `cli.py`        | `econgames play --strategy1 tft --strategy2 grim --rounds 500`      |

### 3.2 Non‑functional requirements

* Python ≥ 3.10, fully type‑annotated (`mypy --strict` clean)
* black + flake8 clean; coverage ≥ 90 %
* CI pipeline identical to SIMCLT (tests, lint, type, wheels to TestPyPI)
* Sphinx API docs → GitHub Pages
* License **MIT**; dependencies permissive

### 3.3 Deliverables recap

* GitHub repo tag **`v1.0.0`** (Week 10), green CI
* 3–4 page Technical Report (architecture, stats, validation, labour split)
* 5‑minute live demo (Week 11)

---

## 4 · Milestones & checkpoints

| Week   | Checkpoint                                              | Acceptance test                                              |
| ------ | ------------------------------------------------------- | ------------------------------------------------------------ |
| **2**  | Smoke: CLI prints stats for Random vs. Random           | `econgames play` returns JSON with keys `p1_mean`, `p2_mean` |
| **4**  | Add deterministic strategies & paired *t*‑test utility  | Mean pay‑offs reproduce Axelrod textbook within ±1 %         |
| **6**  | CLI flag `--repeats` to replicate sims; coverage ≥ 80 % | Coverage gate passes in CI                                   |
| **8**  | Docs, CI, packaging polish                              | `pip install .` works on CI; wheels on TestPyPI              |
| **10** | **Code‑freeze `v1.0.0`**                                | All §3.2 requirements satisfied                              |
| **11** | Live demo + report                                      | Repo, PDF, demo delivered                                    |

---

## 5 · Stretch goals (optional extra credit)

* Add a YAML config loader so users can simulate arbitrary normal‑form games without editing code.
* Implement **evolutionary dynamics** (e.g., replicator) to study strategy populations.
* Parallel simulation with `joblib` or `multiprocessing`.
* Simple web dashboard via **Streamlit** (optional flag `--web`).
* Property‑based tests with **Hypothesis**.


---

## 6 · Grading weight inside rubric

| Rubric slice                    | How ECONGAMES maps                                    |
| ------------------------------- | ----------------------------------------------------- |
| Code quality & packaging (35 %) | OOP design, clean API, wheels, semantic versioning    |
| Statistical correctness (25 %)  | Pay‑off calculations, t‑tests implemented & validated |
| Tests & CI (20 %)               | Coverage, strict typing, green pipeline               |
| Usability & docs (10 %)         | Helpful CLI, clear docs, YAML config (if added)       |
| Report & demo (10 %)            | PDF clarity, live execution, confident answers        |

---

## 7 · External resources

* **Axelrod, R.** *The Evolution of Cooperation* (1984) — baseline pay‑offs.
* **Nowak, M.** (2006) *Evolutionary Dynamics* — stretch‑goal reference.
* Python library **`axelrod`** (MIT) — can be used for validation tests (cite if copied).

---

> **Rule‑of‑thumb**: push small, keep CI green, and log every AI‑generated snippet in `AI_LOG.md`.
