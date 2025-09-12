---
layout: page
title: "Individual Project Rulebook"
subtitle: "Your journey to mastery through creative programming"
---

# INDIVIDUAL PROJECT RULEBOOK
Advanced Programming · Fall 2025 · HEC Lausanne

> **Your Final Project = 100% of Your Grade**  
> This is your opportunity to demonstrate mastery through a self-directed project that showcases your programming skills, creativity, and problem-solving abilities.

---

## 🎯 Project Philosophy

The best learning happens when you're building something you care about. This project gives you the freedom to explore your interests while demonstrating the programming skills you've developed. Whether you're passionate about finance, machine learning, web development, or scientific computing, you can craft a project that showcases your unique strengths.

**Core Principles:**
- **Ownership**: This is YOUR project - make it something you're proud of
- **Learning**: Push yourself beyond the course material
- **Impact**: Build something useful, interesting, or innovative
- **Quality**: Write code you'd be happy to show in a job interview

---

## 📚 Project Categories

### 🌟 Choose Your Path

You can propose any project that demonstrates your programming and data analysis skills. Here are focused categories that align with the course content:

#### **📊 Data Analysis & Visualization**
Transform raw data into insights using pandas, NumPy, and matplotlib
- **Financial Data Explorer**: Analyze stock prices, returns, and volatility
- **Economic Dashboard**: Track and visualize economic indicators (GDP, inflation, unemployment)
- **Sports Analytics Tool**: Calculate player/team statistics and performance metrics
- **Weather Pattern Analyzer**: Process historical weather data to find trends
- **Survey Data Processor**: Clean and analyze survey responses with statistical summaries

#### **📈 Business & Finance Tools**
Build practical applications for financial analysis and business decisions
- **Portfolio Tracker**: Monitor investments and calculate returns
- **Budget Analyzer**: Track expenses and generate spending reports
- **Loan Calculator**: Compute payments, amortization schedules, and total interest
- **Risk Assessment Tool**: Calculate Value at Risk (VaR) and other risk metrics
- **Invoice Generator**: Create and manage invoices with data export

#### **🔄 Data Processing Pipelines**
Create tools to collect, clean, and transform data
- **CSV Merger & Cleaner**: Combine multiple files and handle missing data
- **Web Scraper**: Extract data from websites and save to structured formats
- **API Data Collector**: Fetch data from public APIs and store locally
- **Report Generator**: Transform data into formatted PDF/HTML reports
- **Data Validator**: Check data quality and flag inconsistencies

#### **📉 Statistical Analysis Tools**
Implement statistical methods and hypothesis testing
- **A/B Test Calculator**: Determine statistical significance of experiments
- **Regression Analyzer**: Perform linear/multiple regression with diagnostics
- **Time Series Toolkit**: Decompose trends, seasonality, and forecasting
- **Distribution Fitter**: Find best-fitting probability distributions for data
- **Correlation Explorer**: Analyze relationships between variables

#### **🗂️ Database Applications**
Work with structured data storage and retrieval
- **SQLite Data Manager**: CRUD operations with a simple GUI
- **Personal Library System**: Track books, movies, or other collections
- **Inventory Tracker**: Manage stock levels and generate reorder alerts
- **Contact Management System**: Store and search contact information
- **Expense Database**: Track and categorize personal/business expenses

#### **🎮 Simulation & Modeling**
Build models to simulate real-world scenarios
- **Monte Carlo Simulator**: Model uncertainty in financial projections
- **Queue Simulator**: Model wait times and service efficiency
- **Dice Game Simulator**: Analyze probabilities and expected values
- **Population Growth Model**: Simulate demographic changes over time
- **Market Simulator**: Model supply and demand dynamics

### 💡 **Custom Project Proposal**
Have a different idea? Great! As long as it demonstrates:
- Data manipulation with pandas/NumPy
- Visualization with matplotlib/seaborn
- Clean code organization
- Proper testing and documentation

...then propose it! We encourage creative applications of course concepts.

---

## 📦 Deliverables

### What You'll Submit

#### 1. **Project Proposal** (Due: November 3)
- **Length**: 300-500 words
- **Format**: Markdown file (`PROPOSAL.md`) in your repository
- **Content**:
  - Project title and category
  - Problem statement or motivation
  - Planned approach and technologies
  - Expected challenges and how you'll address them
  - Success criteria (how will you know it's working?)
  - Stretch goals (if time permits)

#### 2. **GitHub Repository** 
- **Structure**: Clean, professional organization
  ```
  project-name/
  ├── README.md           # Comprehensive project documentation
  ├── PROPOSAL.md         # Your project proposal
  ├── requirements.txt    # Python dependencies
  ├── setup.py            # Installation script (if applicable)
  ├── src/                # Source code
  │   ├── __init__.py
  │   └── ...
  ├── tests/              # Test suite
  │   └── test_*.py
  ├── data/               # Sample data (if applicable)
  ├── docs/               # Additional documentation
  ├── examples/           # Usage examples
  └── results/            # Output, figures, analysis
  ```
- **Version Control**: 
  - Minimum 20 meaningful commits
  - Clear commit messages
  - Use branches for features (optional but recommended)

#### 3. **Technical Report** (Due: December 15)
- **Length**: Exactly 10 pages (excluding references and appendices)
- **Format**: PDF, single-column, 11pt font, 1-inch margins
- **Structure**:
  1. **Abstract** (200 words): Summary of project and achievements
  2. **Introduction** (1-1.5 pages): Problem motivation and objectives
  3. **Background** (1-1.5 pages): Related work and technical context
  4. **Design & Architecture** (2 pages): System design and key decisions
  5. **Implementation** (2-3 pages): Technical details and challenges
  6. **Evaluation** (1-2 pages): Testing, performance, results
  7. **Discussion** (1 page): Limitations and future work
  8. **Conclusion** (0.5 pages): Summary and key takeaways
  9. **References**: Properly cited sources
  10. **Appendices** (optional): Additional figures, code snippets

#### 4. **Project Presentation** (December 16-20)
- **Format**: Live demo or recorded video
- **Duration**: 8-10 minutes presentation + 5 minutes Q&A
- **Content**:
  - Problem motivation (1-2 min)
  - Technical approach (2-3 min)
  - Live demo (3-4 min)
  - Results and learnings (1-2 min)
  - Future work (1 min)

#### 5. **Code Quality**
- **Documentation**:
  - Comprehensive README with installation and usage
  - Docstrings for all functions/classes
  - Inline comments for complex logic
  - Type hints (strongly recommended)
- **Testing**:
  - Unit tests for core functionality
  - Integration tests for main workflows
  - Test coverage report (aim for >70%)
- **Code Standards**:
  - PEP 8 compliant (use `black` formatter)
  - Meaningful variable/function names
  - Modular design with clear separation of concerns

---

## 🔧 Technical Requirements

### Core Requirements

| Component | Requirement | Why It Matters |
|-----------|-------------|----------------|
| **Language** | Python 3.10+ (others with approval) | Modern features and type hints |
| **Complexity** | Non-trivial algorithms/architecture | Demonstrates problem-solving |
| **Scope** | 1000+ lines of original code | Shows substantial effort |
| **Libraries** | Smart use of external packages | Real-world development skills |
| **Error Handling** | Graceful failure recovery | Production-ready code |
| **Testing** | Comprehensive test suite | Professional practices |
| **Documentation** | Clear and complete | Maintainable code |

### Code Quality Standards

#### **Architecture**
- Modular design with clear separation of concerns
- Well-defined interfaces between components
- Appropriate design patterns where applicable
- Scalable and maintainable structure

#### **Code Style**
- **Formatting**: Use `black` or `autopep8`
- **Linting**: Pass `pylint` or `flake8` checks
- **Type Hints**: Use for function signatures
- **Naming**: Clear, descriptive, consistent

#### **Testing Requirements**
- Unit tests for all core functions
- Integration tests for main workflows
- Edge case and error handling tests
- Performance tests for critical paths
- Aim for >70% code coverage

#### **Documentation Standards**
- **README**: Professional with badges, screenshots, examples
- **Docstrings**: Google or NumPy style for all public APIs
- **Comments**: Explain "why", not "what"
- **Architecture Docs**: High-level design decisions

### Bonus Points (Going Above & Beyond)

#### **Professional Touches**
- CI/CD pipeline with GitHub Actions
- Pre-commit hooks for code quality
- Docker containerization
- Performance profiling and optimization
- Security considerations (input validation, secrets management)

#### **Advanced Features**
- Async/concurrent programming where appropriate
- Caching and optimization strategies
- Plugin architecture or extensibility
- RESTful API with OpenAPI documentation
- Real-time features (WebSockets, streaming)

#### **Engineering Excellence**
- Comprehensive logging system
- Configuration management (YAML/TOML)
- Database migrations (if applicable)
- Monitoring and metrics
- Deployment documentation

---

## 📅 Timeline & Milestones

### Key Dates

| Date | Milestone | Deliverable | Tips |
|------|-----------|-------------|------|
| **Oct 28** | Kickoff | Project guidelines released | Start brainstorming! |
| **Nov 3** | Proposal Due | 300-500 word proposal | Get feedback early |
| **Nov 10** | Proposal Feedback | Instructor comments | Adjust scope if needed |
| **Nov 17** | Progress Check | Optional check-in | Show working prototype |
| **Nov 24** | Feature Freeze | Stop adding features | Focus on polish |
| **Dec 1** | Testing Week | Complete test suite | Fix bugs, optimize |
| **Dec 8** | Documentation | Finalize all docs | Make it professional |
| **Dec 15** | Final Submission | Everything due | Submit early! |
| **Dec 16-20** | Presentations | Present your work | Practice your demo |

### Suggested Development Timeline

#### **Week 1-2: Planning & Setup**
- Research and finalize project idea
- Set up development environment
- Create repository and initial structure
- Write detailed project proposal

#### **Week 3-4: Core Development**
- Implement basic functionality
- Create initial tests
- Regular commits and documentation

#### **Week 5-6: Feature Development**
- Add planned features
- Expand test coverage
- Refactor and optimize

#### **Week 7: Polish & Documentation**
- Complete documentation
- Final testing and bug fixes
- Prepare presentation
- Write technical report

---

## 📊 Evaluation Criteria

Your project will be evaluated based on the grading criteria outlined in the course syllabus. Focus on:

- **Technical Quality**: Clean, working code that demonstrates programming skills
- **Complexity**: Appropriate scope and technical depth
- **Documentation**: Clear README and code documentation
- **Testing**: Comprehensive test coverage
- **Project Management**: Good use of version control and planning

Specific grading rubrics will be provided by your instructor.

---

## 🤖 AI Tools Policy

### Philosophy: AI as a Collaborator, Not a Ghostwriter

We encourage smart use of AI tools (ChatGPT, GitHub Copilot, Claude, etc.) as they're part of modern development. However, this is YOUR project - AI should enhance your work, not replace your thinking.

### ✅ Encouraged Uses

#### **Learning & Understanding**
- Explaining complex concepts
- Debugging assistance
- Code review and improvements
- Learning new libraries or patterns

#### **Productivity Boost**
- Boilerplate code generation
- Documentation writing
- Test case generation
- Refactoring suggestions

#### **Creative Assistance**
- Brainstorming ideas
- Architecture discussions
- Algorithm optimization
- UI/UX suggestions

### 📝 Required Disclosure

Create an `AI_USAGE.md` file documenting:
```markdown
# AI Tool Usage Disclosure

## Tools Used
- GitHub Copilot for autocomplete
- ChatGPT for debugging assistance
- Claude for documentation

## Significant Contributions
1. **Algorithm X Implementation** (src/algorithm.py)
   - AI helped with initial structure
   - I modified for my specific use case
   
2. **Test Suite** (tests/)
   - Generated test cases with AI
   - Manually verified and expanded

## Learning Moments
- Used AI to understand async/await patterns
- Learned about design patterns through AI explanations
```

### ❌ Not Acceptable

- Submitting AI-generated code you don't understand
- Having AI write your entire project
- Copy-pasting without comprehension
- Using AI to circumvent learning

### 💡 Best Practices

1. **Understand Everything**: Be able to explain every line
2. **Add Your Touch**: Improve and customize AI suggestions
3. **Learn From It**: Use AI to learn, not to avoid learning
4. **Stay Honest**: Disclose AI use transparently
5. **Own Your Work**: The project should reflect YOUR abilities

---

## 🎓 Academic Integrity

### The Honor Code

Your project represents your learning journey. We expect:

#### **Originality**
- Your code should be primarily your own work
- Build on others' work with proper attribution
- Create something unique, not a copy

#### **Transparency**
- Cite all sources (Stack Overflow, tutorials, papers)
- Document external code usage
- Acknowledge help received

#### **Understanding**
- Be able to explain every design decision
- Understand all code in your project
- Be ready for code walkthrough during presentation

### Attribution Examples

```python
# Good: Clear attribution
# Algorithm based on: https://arxiv.org/abs/1234.5678
# Modified for parallel processing
def optimized_algorithm(data):
    # My implementation here
    pass

# Bad: No attribution
def optimized_algorithm(data):
    # Complex code with no explanation
    pass
```

### Collaboration Guidelines

#### ✅ **Allowed**
- Discussing ideas and approaches
- Sharing learning resources
- Peer code reviews (with attribution)
- Using open-source libraries

#### ❌ **Not Allowed**
- Copying code from classmates
- Submitting others' work as your own
- Sharing your code before deadline
- Using previous students' projects

### Consequences of Violations

1. **First Offense**: Project rejection, chance to resubmit with penalty
2. **Severe Cases**: Course failure and academic committee review
3. **All Cases**: Reported per university policy

---

## 💪 Support & Resources

### Getting Help

For support with your project:
- Attend office hours (check Moodle for schedule)
- Post questions on the course forum
- Email instructors for specific issues
- Review course materials and examples

### Submission Guidelines

Follow the submission instructions provided on Moodle. Ensure your GitHub repository is accessible and all deliverables are submitted on time.

Late policy and other administrative details are outlined in the course syllabus.

---

## 🚀 Project Ideas & Inspiration

### Project Ideas by Difficulty

#### **Starter Ideas** (Good for building confidence)
- **CSV Data Explorer**: Build a tool to load, clean, and visualize any CSV dataset
- **Stock Price Analyzer**: Download and analyze historical stock data with moving averages
- **Weather Data Dashboard**: Aggregate and visualize local weather patterns
- **Sports Statistics Tracker**: Analyze team/player performance from public datasets

#### **Intermediate Ideas** (Recommended level)
- **Economic Indicator Dashboard**: Combine multiple data sources (GDP, inflation, unemployment)
- **Time Series Forecaster**: Build ARIMA/exponential smoothing models for predictions
- **A/B Testing Framework**: Statistical significance testing for experiments
- **Data Pipeline Builder**: ETL tool for cleaning and transforming messy datasets

#### **Advanced Ideas** (For those seeking a challenge)
- **Real-time Data Streaming Platform**: Build a system for processing live data feeds
- **Monte Carlo Risk Simulator**: Complex financial/business risk modeling
- **Custom Database for Time Series**: Optimized storage and querying for temporal data
- **Distributed Data Processing**: Map-reduce implementation for large datasets

#### **Research-Based Ideas**
- Reproduce econometric studies with new datasets
- Implement statistical algorithms from academic papers
- Compare different forecasting methods on real data
- Apply financial models to cryptocurrency markets

---

## 🎯 Final Advice

### The Secret to a Great Project

1. **Choose Something You Care About**
   - Passion shows in the final product
   - You'll push through challenges better
   - The learning sticks when you're engaged

2. **Start Simple, Then Iterate**
   - Get a basic version working first
   - Add features incrementally
   - Don't try to build everything at once

3. **Focus on One Thing Done Well**
   - Better to excel in one area than be mediocre in many
   - Deep expertise impresses more than surface-level features
   - Quality over quantity always

4. **Tell a Story**
   - Why does your project matter?
   - What problem does it solve?
   - Who would use it and why?

5. **Ship Something You're Proud Of**
   - This goes in your portfolio
   - You might show this in job interviews
   - Make it represent your best work

### Common Pitfalls to Avoid

❌ **Over-scoping**: Better to deliver 100% of a smaller project than 60% of an ambitious one
❌ **Under-documenting**: Great code with poor documentation is hard to appreciate
❌ **Ignoring Tests**: Untested code is unprofessional
❌ **Last-Minute Rush**: Quality suffers under time pressure
❌ **Not Asking for Help**: We're here to support you - use us!

### Remember

> "The best project is one that teaches you something new while solving a real problem. Don't just build something that works - build something that matters to you."

---

## 📧 Questions?

Still have questions? Here's how to get answers:

1. **Check the FAQ** on Moodle
2. **Ask on Discord** for quick clarifications
3. **Email the instructor** for project-specific questions
4. **Come to office hours** for in-depth discussions

**We want you to succeed!** This project is your chance to shine - make the most of it.

---

*Last updated: October 2025 | Version 2.0*