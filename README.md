
# MSc Programming Projects 2025 — **Global Hub**

**This repository is the *single source of truth* for every practical-session and final-project requirement.
Your project repository, technical report, and 5-minute demo are the *graded deliverables* for this course — none are optional.**


<!-- 🚨 SHOUTY RED LINK FOR GITHUB & LMS 🚨 -->
<p align="center"><strong><font color="#D91E18">⚠️  MUST READ → <a href="docs/rules.md"><font color="#D91E18">FINAL PROJECT RULES</font></a> ⚠️</font></strong></p>

---

## 📋 What’s in here?

| Folder / file | What you’ll find |
|---------------|------------------|
| `docs/` | • Project briefs, rules, timeline<br>• Practical-session curriculum |
| `README.md` (this file) | Quick links, how-to-start guide |
| GitHub Pages site | Nicely rendered version of everything at **https://<ORG>.github.io/<META-REPO>/** |

---

## 🔖 Project Catalogue (choose one)

| ID | Focus | Template repo | Brief |
|----|-------|---------------|-------|
| **SIMCLT** | Chain-Ladder reserving simulator | (coming soon) | `docs/projects/SIMCLT.md` |
| **ECONGAMES** | Monte-Carlo game-theory toolkit | (coming soon) | `docs/projects/ECONGAMES.md` |
| **RISKCALC** | CLI VaR & ES calculator | (coming soon) | `docs/projects/RISKCALC.md` |
| **PYMORT** | Longevity-bond pricing engine | (coming soon) | `docs/projects/PYMORT.md` |
| **QSIM** | Discrete-event queue simulator | (coming soon) | `docs/projects/QSIM.md` |

### Alternative: *Solo “Free-Topic” Project*
Prefer to work alone? You may propose an **individual project on any software-engineering topic** (does *not* have to relate to economics or statistics) **provided it is *not* a data-science build** (i.e. no dataset-plus-model focus).
The solo project must still satisfy **all mandatory requirements**: repository structure, tests ≥ 90 % coverage, CI, documentation, technical report, and in-class demo.
Submit a one-paragraph proposal via LMS by **Week 2 Friday 23:59** for approval.

---

## 🚀 How to get started

1. **Form a team (3–4 students)** and pick a template — or decide on a solo free-topic project.
2. Click **“Use this template”** in the chosen repo to create your private fork.
3. Clone it locally and bootstrap:

  ```bash
   git clone https://github.com/your-org/your-project.git
   cd your-project
   python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
   pip install -e .[dev]
   pytest -q                # smoke tests green
```

4. Register your repository URL (or solo proposal) in the Moodle *Projects → Registration* section by Week 2 deadline.

---

## 📚 Global Rules & Deliverables (abridged)

*Full details in* `docs/PROJECT_RULES.md`. **Highlights:**

| Must-do                 | Notes                                                                                                                                                                   |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Repository layout**   | Keep provided `src/`, `tests/`, `pyproject.toml`. *No Jupyter notebooks.*                                                                                               |
| **Coding standards**    | Python ≥ 3.10, `black`, `flake8`, `mypy --strict`, NumPy-style docstrings.                                                                                              |
| **Tests & CI**          | GitHub Actions must stay green; test coverage ≥ 80 % by Week 6, ≥ 90 % final.                                                                                           |
| **Documentation**       | `README.md` quick-start + Sphinx API docs on GitHub Pages.                                                                                                              |
| **AI tooling**          | Allowed; maintain **`AI_LOG.md`** citing prompts versus kept code.                                                                                                      |
| **Graded deliverables** | 1️⃣ Tagged release `v1.0.0` in GitHub (repo) — **mandatory**<br>2️⃣ 4-6 page technical report (PDF) — **mandatory**<br>3️⃣ 15-minute live demo (TBA) — **mandatory** |

Grading split: **35 % code quality, 25 % statistical correctness, 20 % tests & CI, 10 % usability, 10 % report/demo**.

---

## 🗓️ Timeline
<!-- 
| Week  | Fri 23:59 deadline                        | Milestone                       |
| ----- | ----------------------------------------- | ------------------------------- |
| **2** | Team/solo registration & repo initialised | Scaffold runs, smoke tests pass |
| **4** | Deterministic maths implemented           | Values validated, CI green      |
| **6** | Stochastic/advanced engine finished       | Coverage ≥ 80 %                 |
| **8** | **Code freeze + tag `v1.0.0`**            | Docs, CI, packaging polished    |
| **9** | In-class demos                            | Report PDF uploaded to LMS      | -->
TBA

*(All dates 2025, Europe/Zurich timezone. Full calendar in `docs/timeline.md`.)*

---

## 🛠️ Practical-Session Curriculum

Every hands-on lab is spelled out in [`docs/practical_sessions.md`](docs/practical_sessions.md)
(or browse the prettier version at the GitHub Pages site).

---

## 🔗 Course Resources

* **Live sessions!** Prepare your questions for the weekly live Q&A sessions and put them in the document:
  - [Q&A document](https://docs.google.com/document/d/1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7a8b9c/edit?usp=sharing)
* **Lecture slides** — [PDF]
* **Lecture repo** — live-coding examples
* **Sample data & config files** live inside each template under `sample_data/`

> 👉 **Prefer HTML?** Browse all docs at **https\://<ORG>.github.io/<META-REPO>/**

---

## FAQ

<details>
<summary>Can we switch projects after Week 2?</summary>

> No. After registration, TA allocations & rubrics are fixed.

</details>

<details>
<summary>What counts as “data science” (forbidden in solo projects)?</summary>

> Any project whose *primary* goal is to ingest a dataset, fit/compare machine-learning or statistical models,
> and output metrics/plots. If in doubt, ask the TA before submitting your solo proposal.

</details>

---

## License

Documentation in this meta-repo is **CC-BY 4.0**.
Each template project ships with its own MIT license; keep MIT (or compatible) when you fork.

---

> **Good luck & happy coding!**
> Questions? Open an issue in this repo.

--- Anna
