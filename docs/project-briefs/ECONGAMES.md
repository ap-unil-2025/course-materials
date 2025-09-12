# 🎮 ECONGAMES: Monte-Carlo Game Theory Toolkit
## Complete Project Specification & Student Guide

> **Template Repository**: [github.com/ap-unil-2025/econgames-template](https://github.com/ap-unil-2025/econgames-template)  
> **Difficulty**: Advanced (⭐⭐⭐⭐⭐)  
> **Type**: INDIVIDUAL PROJECT  
> **Duration**: 10 weeks  

---

## 📋 Table of Contents
1. [Project Vision](#project-vision)
2. [Learning Objectives](#learning-objectives)
3. [Technical Requirements](#technical-requirements)
4. [Deliverables & Milestones](#deliverables--milestones)
5. [Getting Started Guide](#getting-started-guide)
6. [Implementation Roadmap](#implementation-roadmap)
7. [Grading Criteria](#grading-criteria)
8. [Resources & Support](#resources--support)

---

## 🎯 Project Vision

### Why This Project?
Many economic and actuarial problems can be framed as **strategic interactions** — from price wars to insurance underwriting cycles. While the research community has mature game theory, it lacks **hands-on, reproducible simulation tools** for teaching and exploration.

### What You'll Build
You will create **ECONGAMES**: a professional-grade, pip-installable Python package with CLI that:
- Simulates repeated 2-player normal-form games (Prisoner's Dilemma, Cournot duopoly, etc.)
- Implements various strategies (Tit-for-Tat, Grim Trigger, Random, and your own)
- Produces statistical comparisons of payoffs
- Provides insights into strategic behavior and equilibria

### Real-World Applications
- **Economics**: Market competition, pricing strategies
- **Insurance**: Competitive underwriting cycles
- **Finance**: Trading strategies, market making
- **Policy**: Environmental cooperation, regulatory compliance
- **Business**: Supply chain negotiations, vendor relationships

---

## 🎓 Learning Objectives

By completing this project, you will master:

### Software Engineering
- ✅ **Design Patterns**: Strategy pattern, Factory pattern, ABC (Abstract Base Classes)
- ✅ **Type Safety**: Strict MyPy type checking, type hints everywhere
- ✅ **Testing**: Property-based testing with Hypothesis, 90% coverage requirement
- ✅ **CI/CD**: GitHub Actions, automated testing, deployment to TestPyPI
- ✅ **Documentation**: Sphinx API docs, Google-style docstrings, GitHub Pages

### Domain Knowledge
- ✅ **Game Theory**: Nash equilibria, dominant strategies, Pareto efficiency
- ✅ **Simulation**: Monte Carlo methods, discrete-event simulation
- ✅ **Statistics**: Hypothesis testing, confidence intervals, convergence analysis
- ✅ **Economics**: Strategic interactions, repeated games, cooperation vs. competition

### Professional Skills
- ✅ **Independent Work**: Self-directed learning, time management, problem-solving
- ✅ **Communication**: Technical writing, presentations, API design
- ✅ **Project Management**: Personal milestones, issue tracking, sprint planning

---

## 🔧 Technical Requirements

### Core Modules (Must Have)

#### 1. `game.py` - Game Definitions
```python
class NormalFormGame:
    """Represents a 2-player normal-form game."""
    
    def payoff(self, action_p1: str, action_p2: str) -> Tuple[float, float]:
        """Return payoffs for given actions."""
        
    @classmethod
    def prisoners_dilemma(cls) -> "NormalFormGame":
        """Factory method for Prisoner's Dilemma."""
        
    @classmethod
    def stag_hunt(cls) -> "NormalFormGame":
        """Factory method for Stag Hunt game."""
```

#### 2. `strategies.py` - Strategy Implementations
```python
class Strategy(ABC):
    """Abstract base class for strategies."""
    
    @abstractmethod
    def first_move(self) -> str:
        """Return the first move."""
        
    @abstractmethod
    def next_move(self, my_history: List[str], opp_history: List[str]) -> str:
        """Return next move based on history."""

# Required implementations:
# - RandomStrategy
# - TitForTat
# - GrimTrigger
# - AlwaysCooperate
# - AlwaysDefect
# - Pavlov (Win-Stay, Lose-Shift)
```

#### 3. `simulator.py` - Simulation Engine
```python
class MonteCarloSimulator:
    """Run repeated game simulations."""
    
    def run(self) -> SimulationResult:
        """Execute simulation."""
        
    def summary(self) -> pd.DataFrame:
        """Return statistical summary."""
        
    def compare_strategies(self, n_repeats: int = 100) -> ComparisonResult:
        """Compare strategies with statistical tests."""
```

#### 4. `cli.py` - Command-Line Interface
```bash
# Basic simulation
econgames play --strategy1 tft --strategy2 grim --rounds 500

# Multiple repetitions with statistics
econgames tournament --repeats 100 --rounds 1000 --output results.csv

# List available strategies and games
econgames list-strategies
econgames list-games

# Run comprehensive tournament
econgames championship --all-strategies --export-plots
```

### Non-Functional Requirements

#### Code Quality
- ✅ Python 3.10+ with full type annotations
- ✅ MyPy strict mode (`mypy --strict` must pass)
- ✅ Ruff linting with comprehensive rules
- ✅ Black formatting (line length: 100)
- ✅ 90% test coverage minimum

#### Development Practices
- ✅ Pre-commit hooks installed and passing
- ✅ Semantic versioning (v1.0.0 at submission)
- ✅ Comprehensive docstrings (Google style)
- ✅ No security vulnerabilities (Bandit scan)

#### CI/CD Pipeline
- ✅ Tests on Python 3.10, 3.11, 3.12
- ✅ Cross-platform (Linux, macOS, Windows)
- ✅ Automated deployment to TestPyPI
- ✅ Documentation on GitHub Pages

---

## 📦 Deliverables & Milestones

### Week-by-Week Roadmap

| Week | Milestone | Acceptance Criteria | Points |
|------|-----------|-------------------|---------|
| **2** | 🟢 Basic Scaffold | CLI runs, Random vs Random works | 10 |
| **3** | 🟡 Core Strategies | TitForTat, GrimTrigger implemented | 15 |
| **4** | 🟡 Statistical Tests | T-tests, mean/variance calculations | 15 |
| **5** | 🟡 Advanced Strategies | Pavlov, custom strategies | 10 |
| **6** | 🟠 Tournament Mode | `--repeats` flag, batch simulations | 15 |
| **7** | 🟠 Visualization | Plots, convergence graphs | 10 |
| **8** | 🔴 Documentation | Sphinx docs, API reference | 10 |
| **9** | 🔴 Polish & Testing | 90% coverage, performance | 10 |
| **10** | 🚀 **SUBMISSION** | Tag v1.0.0, all tests green | 5 |

### Final Deliverables

1. **GitHub Repository**
   - Tagged release `v1.0.0`
   - Green CI badge
   - Complete README
   - CONTRIBUTING.md guide

2. **Technical Report** (3-4 pages)
   - Architecture overview
   - Statistical methodology
   - Validation results
   - Development challenges & solutions

3. **Live Demo** (5 minutes)
   - Run tournament
   - Show statistical analysis
   - Explain design decisions
   - Answer questions

4. **TestPyPI Package**
   - Installable via pip
   - Working CLI
   - Published documentation

---

## 🚀 Getting Started Guide

### Step 1: Create Your Repository
```bash
# 1. Go to template repository
# https://github.com/ap-unil-2025/econgames-template

# 2. Click "Use this template" → "Create a new repository"

# 3. Clone YOUR new repository
git clone https://github.com/YOUR-USERNAME/econgames-YOURNAME.git
cd econgames-YOURNAME
```

### Step 2: Set Up Development Environment
```bash
# Install uv package manager
pip install uv

# Create virtual environment and install dependencies
make install-dev

# Verify everything works
make check
```

### Step 3: Run Initial Tests
```bash
# Run the basic CLI
econgames play

# Run all tests
make test

# Check type hints
make type-check
```

### Step 4: Start Development
```bash
# Create feature branch
git checkout -b feature/add-pavlov-strategy

# Make changes, test continuously
make test-watch

# Before committing
make fix  # Auto-fix formatting
make check  # Run all checks
```

---

## 🗺️ Implementation Roadmap

### Phase 1: Foundation (Weeks 1-3)
- [ ] Set up development environment
- [ ] Implement basic game structure
- [ ] Create Random, TitForTat, GrimTrigger strategies
- [ ] Basic CLI with JSON output
- [ ] Achieve 50% test coverage

### Phase 2: Core Features (Weeks 4-6)
- [ ] Add statistical analysis (t-tests, confidence intervals)
- [ ] Implement tournament mode with repeats
- [ ] Add more strategies (Pavlov, AlwaysCooperate, AlwaysDefect)
- [ ] Create custom game matrices
- [ ] Achieve 75% test coverage

### Phase 3: Advanced Features (Weeks 7-8)
- [ ] Add visualization (matplotlib/seaborn)
- [ ] Implement evolutionary dynamics (optional)
- [ ] Add YAML configuration support
- [ ] Performance optimization
- [ ] Achieve 90% test coverage

### Phase 4: Polish (Weeks 9-10)
- [ ] Complete documentation
- [ ] Add property-based tests
- [ ] Performance benchmarking
- [ ] Prepare presentation
- [ ] Final testing and release

---

## 📊 Grading Criteria

### Grade Breakdown (100 points)

| Component | Weight | Details |
|-----------|--------|---------|
| **Code Quality** | 35% | Clean architecture, type safety, best practices |
| **Functionality** | 25% | All features work correctly, edge cases handled |
| **Testing** | 20% | 90% coverage, property tests, CI green |
| **Documentation** | 10% | Clear docs, helpful README, API reference |
| **Presentation** | 10% | Clear demo, good answers, well-prepared |

### Excellence Indicators (A+ Grade)
- ✨ Innovative strategies or analysis methods
- ✨ Beautiful visualizations
- ✨ Performance optimizations (parallel processing)
- ✨ Web interface (Streamlit/Gradio)
- ✨ Published to real PyPI (not just TestPyPI)
- ✨ Evolutionary dynamics implementation

### Common Pitfalls (Grade Deductions)
- ❌ Type checking errors (-5 points per error)
- ❌ Coverage below 90% (-1 point per percentage)
- ❌ Missing docstrings (-2 points per public function)
- ❌ Failing CI (-10 points)
- ❌ No semantic versioning (-5 points)

---

## 📚 Resources & Support

### Essential Reading
- 📖 **Axelrod, R.** (1984) *The Evolution of Cooperation* - Classic reference
- 📖 **Nowak, M.** (2006) *Evolutionary Dynamics* - Advanced concepts
- 📖 [Game Theory .net](http://gametheory.net/) - Interactive tutorials

### Python Libraries for Reference
- 🔧 [Axelrod](https://github.com/Axelrod-Python/Axelrod) - Inspiration (cite if used!)
- 🔧 [Nashpy](https://github.com/drvinceknight/Nashpy) - Nash equilibrium computation
- 🔧 [Mesa](https://github.com/projectmesa/mesa) - Agent-based modeling

### Getting Help
- 💬 **Office Hours**: Tuesdays 14:00-16:00, Room 234
- 💬 **Discord**: #econgames-project channel
- 💬 **GitHub Issues**: Use project template issues
- 💬 **Email**: instructor@university.edu

### Development Tools
- 🛠️ [MyPy Playground](https://mypy-play.net/) - Test type hints
- 🛠️ [Regex101](https://regex101.com/) - Test regex patterns
- 🛠️ [Hypothesis](https://hypothesis.readthedocs.io/) - Property testing docs
- 🛠️ [Sphinx](https://www.sphinx-doc.org/) - Documentation generator

---

## 🎯 Success Tips

### From Previous Years' Top Students

1. **Start Early**: Week 1 setup saves Week 10 panic
2. **Test Continuously**: Write tests before code (TDD)
3. **Commit Often**: Small, focused commits with good messages
4. **Document as You Go**: Don't leave docs for the end
5. **Use the Template**: It has everything configured already
6. **Ask Questions**: Office hours are underutilized
7. **Break Down Problems**: Tackle complex algorithms step by step
8. **Profile Performance**: Find bottlenecks early
9. **Visualize Results**: Graphs make reports compelling
10. **Practice Demo**: Rehearse your presentation

### Common Questions

**Q: Can we use external libraries like Axelrod?**  
A: You can use them for validation/testing, but must cite them. Core implementation should be your own.

**Q: What if our strategies don't converge?**  
A: That's a valid result! Document it and explain why.

**Q: How many strategies should we implement?**  
A: Minimum 6 (including required ones), but more is better for analysis.

**Q: Can we work on other game types?**  
A: Yes! After implementing PD, add Stag Hunt, Chicken, or Battle of Sexes.

**Q: What about 3+ player games?**  
A: Stretch goal! But ensure 2-player works perfectly first.

---

## 🚨 Important Reminders

- **Academic Integrity**: All code must be original or properly cited
- **AI Usage**: Log all AI assistance in `AI_LOG.md`
- **Deadlines**: No extensions except for documented emergencies
- **Questions**: Don't hesitate to ask for help when stuck
- **Version Control**: Push to GitHub daily, don't lose work!

---

> **Ready to build something amazing?** 🚀  
> Your ECONGAMES toolkit could become the reference implementation for game theory education!

---

*Last updated: 2025-01-12 | Questions? → instructor@university.edu*