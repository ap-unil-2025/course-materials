---
layout: page
title: "Individual Project Rulebook"
subtitle: "Your journey to mastery through data science"
---

# INDIVIDUAL PROJECT RULEBOOK
Advanced Programming · Fall 2025 · HEC Lausanne

> **Your Final Project = 100% of Your Grade**
> Build a machine learning or data analysis project that demonstrates your programming and analytical skills.

---

## 🎯 Project Philosophy

This is your opportunity to apply what you've learned to a real problem. Most projects will focus on **machine learning and data analysis** - comparing models, analyzing datasets, and presenting findings.

**Core Principles:**
- **Working Code First**: If we can't run `python main.py`, we can't grade it
- **Reproducibility**: Same code → same results, every time
- **Clear Documentation**: README explains setup, REPORT explains findings
- **Clean Structure**: Organized code that others can understand

---

## 📊 Project Focus: Machine Learning

Most projects should follow this pattern:

> **Research Question** → **Data** → **Models** → **Evaluation** → **Report**

**Example**: "Which model best predicts customer churn: Random Forest, Logistic Regression, or XGBoost?"

### Recommended Project Types

- **Classification**: Predict categories (spam detection, sentiment analysis, disease diagnosis)
- **Regression**: Predict values (house prices, sales forecasting, stock returns)
- **Clustering**: Find patterns (customer segmentation, anomaly detection)
- **Comparison Studies**: Compare 3+ models on the same task

### Custom Projects

Want to do something different? As long as you can demonstrate:
- Data manipulation with pandas/NumPy
- Some form of analysis or modeling
- Clear methodology and results
- Reproducible code

...then propose it!

---

## 📦 Deliverables

### 1. **Project Proposal** (Due: November 3)
- **Length**: 300-500 words
- **Format**: `PROPOSAL.md` in your repository
- **Content**: What you'll build, what data you'll use, what question you'll answer

### 2. **GitHub Repository** (Due: December 21)

**Required Structure:**
```
your-project/
├── README.md              # Setup and usage instructions
├── PROPOSAL.md            # Your project proposal
├── environment.yml        # Conda dependencies
├── requirements.txt       # Pip dependencies (alternative)
├── main.py               # Entry point - THIS MUST WORK
├── src/                  # Source code modules
│   ├── __init__.py
│   ├── data_loader.py    # Data loading and preprocessing
│   ├── models.py         # Model definitions
│   └── evaluation.py     # Evaluation and visualization
├── data/
│   └── raw/              # Original data (or instructions to download)
├── results/              # Output figures and metrics
└── notebooks/            # Jupyter notebooks (optional, for exploration)
```

**Key Requirements:**
- `python main.py` must run without errors
- All dependencies listed in `environment.yml` or `requirements.txt`
- Data included or clear download instructions
- Use `random_state` for reproducibility

### 3. **Technical Report** (Due: December 21)
- **Length**: ~10 pages (excluding code appendix)
- **Format**: PDF (use provided Markdown or LaTeX template)
- **Structure**:
  1. **Abstract** (200 words): Summary of project
  2. **Introduction**: Research question and motivation
  3. **Literature Review**: Brief context and related work
  4. **Methodology**: Data, preprocessing, models, evaluation metrics
  5. **Results**: Tables, figures, findings
  6. **Discussion**: Interpretation, limitations
  7. **Conclusion**: Summary and future work
  8. **References**: Cited sources

**Download templates from the course website:**
- Markdown template → PDF with pandoc
- LaTeX template → PDF with pdflatex

### 4. **Presentation Video** (Due: December 21, Required)
- **Format**: Recorded video (MP4, YouTube link, or Loom)
- **Duration**: 8-10 minutes
- **Content**:
  - Problem motivation (1-2 min)
  - Technical approach (2-3 min)
  - Demo of your code running (3-4 min)
  - Results and learnings (1-2 min)

**Optional**: Live presentation (TBA) instead of video, with Q&A

---

## 🔧 Technical Requirements

### Must Have

| Component | Requirement |
|-----------|-------------|
| **Language** | Python 3.10+ |
| **Entry Point** | `python main.py` runs successfully |
| **Dependencies** | Listed in `environment.yml` or `requirements.txt` |
| **Reproducibility** | `random_state` set everywhere |
| **Documentation** | README with setup instructions |
| **Report** | ~10 page PDF with methodology and results |

### Nice to Have (But Not Required)

- Unit tests
- CI/CD pipeline
- Docker containerization
- Type hints
- >70% test coverage

**Focus on making your project work well, not on adding features you don't need.**

### Code Quality

- **Formatting**: Use consistent style (black/autopep8 recommended)
- **Naming**: Clear, descriptive variable and function names
- **Structure**: Modular code in `src/` directory
- **Comments**: Explain *why*, not *what*

---

## 📅 Timeline

| Date | Milestone |
|------|-----------|
| **Nov 3** | Project Proposal Due |
| **Nov 10** | Proposal Feedback |
| **Nov 24** | Feature Freeze - stop adding, start polishing |
| **Dec 8** | Documentation Week - finalize README and report |
| **Dec 21** | **Final Submission** |
| **TBA** | Presentations (optional) |

### Development Strategy

1. **Week 1-2**: Set up structure, get data, basic pipeline working
2. **Week 3-4**: Implement models, run experiments
3. **Week 5-6**: Analyze results, create visualizations
4. **Week 7**: Write report, polish documentation

---

## 📊 What We're Looking For

### The #1 Grading Criterion

> **Does `python main.py` work on our machines?**

If we can't run your code, we can't grade it. Test on a fresh environment before submitting!

### Evaluation Focus

- **Working Code**: Runs without errors, produces output
- **Clear Methodology**: We understand what you did and why
- **Meaningful Results**: You actually answered your research question
- **Professional Presentation**: Clean code, clear report, good documentation
- **Reproducibility**: We get the same results when we run it

---

## 🤖 AI Tools Policy

We encourage using AI tools (ChatGPT, Copilot, Claude) as learning aids.

**✅ Good uses:**
- Debugging help
- Learning new libraries
- Code review suggestions
- Documentation writing

**❌ Not acceptable:**
- Submitting code you don't understand
- Having AI write your entire project

**Required**: Create `AI_USAGE.md` documenting how you used AI tools.

---

## ❓ Common Questions

**Q: Can I use a dataset from Kaggle?**
A: Yes! Just cite your source and include download instructions.

**Q: Do I need to write tests?**
A: Not required, but encouraged if you have time.

**Q: What if my model doesn't perform well?**
A: That's fine! Explain why in your discussion section. Negative results are still results.

**Q: Can I work with a partner?**
A: No, all projects are individual work.

**Q: What if I can't finish everything?**
A: Focus on having a working `main.py` and a complete report. A smaller project done well beats an ambitious project that doesn't run.

---

## 🚀 Getting Started

1. **Fork the example project** from the course repository
2. **Replace the Iris example** with your own data and research question
3. **Follow the same structure** - it works!
4. **Test on a fresh environment** before submitting

See the `examples/iris-classification/` folder in the course repository for a complete working example.

---

## 📧 Need Help?

- **Discord**: Quick questions and peer help
- **Office Hours**: In-depth project discussions
- **Email**: Project-specific issues

**We want you to succeed!** Start early, ask questions, and make something you're proud of.

---

*Last updated: November 2025 | Deadline: December 21, 2025*
