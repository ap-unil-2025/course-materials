# RISKCALC – Command‑Line VaR & ES Calculator (Template Project)

> *Final‑project template for MSc “Elementary Programming in Python” – Spring 2025*

---

## 1 · Why this project?

Financial and insurance risk managers use **Value‑at‑Risk (VaR)** and **Expected
Shortfall (ES)** as daily metrics, yet entry‑level analysts often rely on
spreadsheet macros.  *RISKCALC* delivers a **lightweight, audited CLI** that
reads a CSV of daily profit‑and‑loss (P/L) numbers and outputs VaR & ES under
multiple methods.

Completing this project gives hands‑on experience with:

* statistical quantile estimation, variance–covariance VaR & Cornish‑Fisher
* command‑line UX with **Click** or **Typer**
* packaging, unit‑testing, type‑checking, CI/CD

---

## 2 · Learning objectives

| Domain            | You will be able to…                                                                                      |
| ----------------- | --------------------------------------------------------------------------------------------------------- |
| **Software Eng.** | design a clean CLI, handle file I/O, return JSON/CSV reports                                              |
| **Statistics**    | implement historical VaR, parametric normal VaR, Cornish‑Fisher VaR, bootstrapped CIs, Expected Shortfall |
| **Dev Ops**       | maintain GitHub Actions, fail build on coverage < 90 %, upload wheels to TestPyPI                         |
| **Communication** | write concise usage docs, produce a 3‑page report & live demo                                             |

---

## 3 · Scope & deliverables

### 3.1 Must‑have modules (public API)

| Module         | Core functions / classes                                  |
| -------------- | --------------------------------------------------------- |
| `io.py`        | `load_pl_csv(path)` returns `pd.Series` of returns or P/L |
| `var.py`       | `historical_var`, `parametric_var`, `cornish_fisher_var`  |
| `es.py`        | `expected_shortfall(hist, level)`                         |
| `bootstrap.py` | `bootstrap_ci(func, data, n=1000)` generic helper         |
| `cli.py`       | `riskcalc pl.csv --method cf --level 0.01 --ci`           |

### 3.2 Non‑functional requirements

* Python ≥ 3.10, fully typed
* ≥ 90 % coverage, strict mypy, black & flake8 clean
* Sphinx docs → GitHub Pages
* Wheels to **TestPyPI** on tag push (CI .yml already provided)
* License **MIT**; dependencies limited to NumPy, Pandas, Typer/Click

### 3.3 Deliverables recap

* GitHub repo tag **`v1.0.0`** (Week 10)
* 3–4 page Technical Report (PDF)
* 5‑minute live demo (Week 11)

---

## 4 · Milestones & checkpoints

| Week   | Checkpoint                                      | Acceptance test                                   |
| ------ | ----------------------------------------------- | ------------------------------------------------- |
| **2**  | CLI prints historical VaR for sample CSV        | `riskcalc sample.csv` returns JSON with `var` key |
| **4**  | Add parametric & Cornish‑Fisher VaR             | results match Excel within ±1 %                   |
| **6**  | Implement ES and bootstrap CIs; coverage ≥ 80 % | CI green                                          |
| **8**  | Docs, CI, packaging polish                      | `pip install .` works on CI; wheels on TestPyPI   |
| **10** | **Code‑freeze `v1.0.0`**                        | All §3.2 requirements satisfied                   |
| **11** | Live demo + report                              | Repo, PDF, demo delivered                         |

---

## 5 · Stretch goals (optional extra credit)

* Delta‑normal VaR with user‑supplied covariance matrix
* Add GARCH(1,1) forecasted volatility option
* Parallel bootstrap with `joblib`
* Small Streamlit dashboard (`--web` flag)
* Property‑based tests using **Hypothesis**

---

## 6 · Grading weight inside rubric

| Rubric slice             | Contribution                                             |
| ------------------------ | -------------------------------------------------------- |
| Code quality & packaging | clear CLI, error handling, JSON/CSV export, wheels       |
| Statistical correctness  | VaR & ES formulas, Cornish‑Fisher expansion, CI validity |
| Tests & CI               | coverage, strict typing, green pipeline                  |
| Usability & docs         | helpful `--help`, tutorial in README, Sphinx API         |
| Report & demo            | clarity, reproducible examples, confident answers        |

---

## 7 · External references

* **Jorion, P.** *Value at Risk*, 4th ed. — core formulas
* **Dowd, K.** (2005) *Measuring Market Risk* — Cornish‑Fisher VaR
* Basel Committee (2016) – ES for market‑risk capital

---

> **Rule‑of‑thumb**: keep CLI deterministic, guard edge cases (≤ 250 rows), and log AI‑generated code in `AI_LOG.md`.
