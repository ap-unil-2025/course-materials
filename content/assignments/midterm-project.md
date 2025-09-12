---
layout: assignment
title: "Midterm Project: AI-Powered Personal Finance Tracker"
assignment_number: "Midterm"
due_date: 2025-11-24 23:59:00
points: 150
difficulty: "Advanced"
estimated_time: "20-25 hours (spread over 6 weeks)"
topics:
  - "Python fundamentals"
  - "Object-oriented programming"
  - "Data structures and algorithms"
  - "API integration"
  - "Large Language Models"
  - "Testing and debugging"
  - "Git version control"
  - "Software architecture"
status: "open"
bonus: true
project_type: "incremental"
---

## Overview

Build a comprehensive **AI-Powered Personal Finance Tracker** that demonstrates mastery of all concepts from Weeks 1-6. This project **requires continuous git usage** with specific milestones that cannot be completed in one session - each milestone builds upon the previous and introduces new concepts as they are learned in class.

**This is a BONUS assignment worth 150 points that can significantly boost your grade.**

## Project Vision

Create a sophisticated personal finance application that:
- Tracks income, expenses, and financial goals
- Uses AI to provide intelligent insights and recommendations
- Implements modern software engineering practices
- Demonstrates clean code architecture and comprehensive testing

## Learning Objectives

By completing this project, you will demonstrate:

- **Python Fundamentals**: Variables, control flow, functions, data structures
- **Object-Oriented Design**: Classes, inheritance, encapsulation, polymorphism
- **AI Integration**: LLM integration, prompt engineering, autonomous decision-making
- **Software Engineering**: Testing, debugging, documentation, code organization
- **Version Control**: Git workflow, branching, meaningful commits, collaboration
- **Problem Solving**: Breaking complex problems into manageable components

## 🚨 CRITICAL GIT REQUIREMENTS

This project **CANNOT be completed in one session**. Each milestone has specific requirements:

### Git Workflow Requirements
1. **Create project repository on day of assignment release**
2. **Minimum 3 commits per milestone** with meaningful messages
3. **Feature branches** for each major component
4. **Pull requests** with detailed descriptions for merging features
5. **Tag releases** at each milestone completion
6. **Maintain clean git history** - no massive "final commit" dumps

### Automated Git History Verification
Your submission will be automatically checked for:
- Commit frequency and distribution over time
- Meaningful commit messages following conventional commit format
- Branch usage and merge history
- Code evolution showing incremental development
- **Projects with suspicious git history will receive 0 points**

## Project Milestones & Timeline

### Milestone 1: Foundation & Setup (Week 3) - 25 points
**Due: October 6, 2025**

**Git Requirements**: 
- Repository creation
- Initial project structure commit
- Basic implementation commits (minimum 3)
- Tag: `v0.1.0-foundation`

**Implementation Requirements**:

#### 1.1 Project Setup (10 points)
```
finance-tracker/
├── src/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── transaction.py
│   └── utils/
│       ├── __init__.py
│       └── validators.py
├── tests/
│   ├── __init__.py
│   └── test_transaction.py
├── data/
├── config/
│   └── config.yaml
├── .gitignore
├── requirements.txt
└── README.md
```

#### 1.2 Core Transaction System (15 points)
```python
class Transaction:
    """
    Core transaction class with:
    - Transaction types (income/expense/transfer)
    - Categories and subcategories
    - Date handling and validation
    - Amount validation and currency support
    - Description and tags
    """
    def __init__(self, amount, transaction_type, category, date=None, description=""):
        # Implementation using Week 3 concepts
        pass
    
    def validate_transaction(self):
        """Validate transaction data using control flow"""
        pass
    
    def format_display(self):
        """Format for display using string manipulation"""
        pass
```

**Deliverables**:
- Basic transaction creation and validation
- Input/output handling with error checking
- String manipulation for formatting
- Control flow for business logic
- Unit tests for core functionality

**Git Commits Should Include**:
- `feat: initialize project structure and basic configuration`
- `feat: implement core Transaction class with validation`
- `test: add unit tests for transaction functionality`
- `docs: add project README with setup instructions`

### Milestone 2: Data Management & Advanced Features (Week 4) - 30 points
**Due: October 13, 2025**

**Git Requirements**:
- Feature branch `feature/data-management`
- Minimum 5 commits showing iterative development
- Pull request with detailed description
- Tag: `v0.2.0-data-management`

**Implementation Requirements**:

#### 2.1 Data Structures & Collections (15 points)
```python
class TransactionManager:
    """
    Manage collections of transactions using:
    - Lists for transaction storage
    - Dictionaries for category mapping
    - Tuples for immutable data
    - Sets for unique value tracking
    """
    def __init__(self):
        self.transactions = []
        self.categories = {}
        self.monthly_totals = {}
    
    def add_transaction(self, transaction):
        """Add transaction with duplicate checking"""
        pass
    
    def filter_transactions(self, **criteria):
        """Filter using advanced list comprehensions"""
        pass
    
    def calculate_statistics(self):
        """Statistical calculations using built-in functions"""
        pass
```

#### 2.2 Advanced Functions & Recursion (15 points)
```python
class BudgetAnalyzer:
    """
    Advanced analysis using functions and recursion
    """
    def analyze_spending_patterns(self, transactions, depth=3):
        """Recursive analysis of spending categories"""
        pass
    
    def calculate_compound_savings(self, principal, rate, years, compound_freq=12):
        """Recursive compound interest calculation"""
        pass
    
    def generate_budget_recommendations(self, transactions):
        """Function composition for complex analysis"""
        pass
```

**Git Commits Should Include**:
- `feat: implement TransactionManager with data structure operations`
- `feat: add filtering and search functionality`
- `feat: create BudgetAnalyzer with recursive algorithms`
- `test: comprehensive tests for data management features`
- `refactor: optimize data structure usage for performance`

### Milestone 3: AI Integration & Intelligent Features (Week 5) - 35 points
**Due: October 20, 2025**

**Git Requirements**:
- Feature branch `feature/ai-integration`
- Minimum 6 commits showing AI feature development
- Pull request demonstrating AI capabilities
- Tag: `v0.3.0-ai-powered`

**Implementation Requirements**:

#### 3.1 LLM Integration for Financial Insights (20 points)
```python
class FinancialAdvisor:
    """
    AI-powered financial advice system
    """
    def __init__(self, llm_client):
        self.llm_client = llm_client
        self.prompt_templates = self._load_prompts()
    
    def analyze_spending_habits(self, transactions):
        """Generate insights from spending patterns"""
        pass
    
    def create_budget_plan(self, income, expenses, goals):
        """AI-generated personalized budget"""
        pass
    
    def predict_future_expenses(self, historical_data):
        """Predictive analysis using AI"""
        pass
```

#### 3.2 Autonomous Financial Agent (15 points)
```python
class FinancialAgent:
    """
    Autonomous agent for financial management
    """
    def __init__(self, user_profile, goals):
        self.profile = user_profile
        self.goals = goals
        self.tools = [BudgetTool(), InvestmentTool(), SavingsTool()]
    
    def plan_financial_strategy(self):
        """Create comprehensive financial plan"""
        pass
    
    def monitor_goals(self):
        """Autonomous goal tracking and adjustments"""
        pass
    
    def generate_actionable_advice(self):
        """Context-aware financial recommendations"""
        pass
```

**Git Commits Should Include**:
- `feat: integrate LLM client for financial analysis`
- `feat: implement prompt templates for financial insights`
- `feat: create autonomous financial planning agent`
- `feat: add predictive expense modeling`
- `test: add tests for AI-powered features`
- `docs: document AI integration and usage examples`

### Milestone 4: Object-Oriented Architecture & Advanced Features (Week 6) - 35 points
**Due: October 27, 2025**

**Git Requirements**:
- Feature branch `feature/oop-architecture`
- Refactoring commits showing evolution to OOP design
- Pull request with architectural documentation
- Tag: `v0.4.0-oop-architecture`

**Implementation Requirements**:

#### 4.1 Advanced OOP Design (20 points)
```python
class FinancialEntity:
    """Base class for all financial entities"""
    def __init__(self, name, created_date=None):
        self._name = name
        self._created_date = created_date or datetime.now()
    
    @property
    def name(self):
        return self._name
    
    @abstractmethod
    def calculate_value(self):
        pass

class Account(FinancialEntity):
    """Bank account with inheritance and encapsulation"""
    def __init__(self, name, account_type, initial_balance=0):
        super().__init__(name)
        self._balance = initial_balance
        self._account_type = account_type
        self._transaction_history = []
    
    def deposit(self, amount, description=""):
        """Polymorphic deposit method"""
        pass
    
    def calculate_value(self):
        """Implementation of abstract method"""
        return self._balance

class Investment(FinancialEntity):
    """Investment class demonstrating inheritance"""
    def __init__(self, name, shares, price_per_share):
        super().__init__(name)
        self.shares = shares
        self.price_per_share = price_per_share
    
    def calculate_value(self):
        return self.shares * self.price_per_share

class Portfolio:
    """Composition and polymorphism demonstration"""
    def __init__(self, name):
        self.name = name
        self.entities = []  # Can contain Accounts, Investments, etc.
    
    def add_entity(self, entity: FinancialEntity):
        self.entities.append(entity)
    
    def calculate_total_value(self):
        """Polymorphism - calls calculate_value on different types"""
        return sum(entity.calculate_value() for entity in self.entities)
```

#### 4.2 Testing & Debugging Framework (15 points)
```python
class FinanceTrackerTester:
    """Comprehensive testing framework"""
    
    def __init__(self):
        self.test_results = []
    
    def run_integration_tests(self):
        """Test complete workflows"""
        pass
    
    def run_performance_tests(self):
        """Test with large datasets"""
        pass
    
    def generate_test_report(self):
        """Comprehensive test reporting"""
        pass
```

**Git Commits Should Include**:
- `refactor: convert to object-oriented architecture`
- `feat: implement inheritance hierarchy for financial entities`
- `feat: add portfolio management with composition`
- `feat: implement comprehensive testing framework`
- `fix: resolve performance issues in data processing`
- `docs: add architectural documentation and UML diagrams`

### Milestone 5: Integration & Polish (Weeks 7-8) - 25 points
**Due: November 10, 2025**

**Git Requirements**:
- Feature branch `feature/integration-polish`
- UI/UX improvement commits
- Performance optimization commits
- Tag: `v1.0.0-release-candidate`

**Implementation Requirements**:

#### 5.1 User Interface & Experience (15 points)
```python
class FinanceTrackerCLI:
    """
    Command-line interface with:
    - Interactive menu system
    - Data visualization (ASCII charts)
    - Export/import functionality
    - Configuration management
    """
    def __init__(self):
        self.tracker = PersonalFinanceTracker()
        self.commands = self._setup_commands()
    
    def run_interactive_mode(self):
        """Main application loop"""
        pass
    
    def display_dashboard(self):
        """ASCII dashboard with key metrics"""
        pass
```

#### 5.2 Data Persistence & Configuration (10 points)
```python
class DataManager:
    """
    Handle data persistence with:
    - JSON/CSV export/import
    - Configuration file management
    - Data backup and recovery
    - Migration tools
    """
    def save_data(self, tracker, filename):
        pass
    
    def load_data(self, filename):
        pass
    
    def create_backup(self, tracker):
        pass
```

### Final Milestone: Documentation & Deployment (Week 9) - 10 points
**Due: November 24, 2025**

**Git Requirements**:
- Final integration on main branch
- Comprehensive documentation commits
- Tag: `v1.0.0-final`

## Comprehensive Feature Requirements

Your final application must include:

### Core Features (Required)
1. **Transaction Management**: Add, edit, delete, categorize transactions
2. **Account Management**: Multiple accounts, transfers, balance tracking
3. **Budget Planning**: Create and monitor budgets with AI assistance
4. **Goal Tracking**: Set and track financial goals
5. **Reporting**: Generate detailed financial reports
6. **Data Export**: CSV/JSON export for external analysis

### Advanced Features (Required for Full Points)
1. **AI Insights**: Spending pattern analysis and recommendations
2. **Autonomous Monitoring**: Automated goal tracking and alerts
3. **Predictive Modeling**: Future expense and income predictions
4. **Investment Tracking**: Portfolio management and performance analysis
5. **Interactive Visualizations**: Charts and graphs (ASCII-based)

### Technical Requirements
1. **Clean Architecture**: Separation of concerns, SOLID principles
2. **Comprehensive Testing**: Unit tests, integration tests, >80% coverage
3. **Error Handling**: Graceful error handling throughout
4. **Documentation**: Clear docstrings, README, architectural docs
5. **Performance**: Handle datasets with 1000+ transactions efficiently

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| **Milestone Completion** | 60 | All milestones completed on time with required features |
| **Git Usage & History** | 25 | Proper git workflow, meaningful commits, clean history |
| **Code Architecture** | 20 | Clean OOP design, SOLID principles, maintainable code |
| **AI Integration** | 15 | Effective LLM usage, intelligent recommendations |
| **Testing & Quality** | 15 | Comprehensive tests, error handling, code quality |
| **Documentation** | 10 | Clear documentation, setup instructions, examples |
| **Innovation & Polish** | 5 | Creative features, user experience, technical excellence |
| **Total** | **150** | |

### Git History Evaluation
- **Commit Frequency**: Regular commits throughout development period
- **Commit Quality**: Meaningful messages following conventional commit format
- **Branch Usage**: Feature branches with proper merging
- **Code Evolution**: Clear progression showing incremental development
- **Collaboration Simulation**: Pull requests with detailed descriptions

### Bonus Opportunities (+25 points)
- **Web Interface**: Simple web UI using Flask/FastAPI (+10 points)
- **Advanced Visualizations**: Interactive charts with libraries (+5 points)
- **Machine Learning**: Custom ML models for predictions (+10 points)
- **API Integration**: Real financial data from APIs (+5 points)
- **Mobile Export**: Data formatted for mobile apps (+5 points)

## Submission Requirements

### Final Submission Structure
```
finance-tracker/
├── src/
│   ├── core/                    # Core business logic
│   ├── ai/                      # AI integration modules
│   ├── ui/                      # User interface
│   ├── data/                    # Data management
│   └── utils/                   # Utility functions
├── tests/                       # Comprehensive test suite
├── docs/                        # Project documentation
├── data/                        # Sample data and schemas
├── config/                      # Configuration files
├── scripts/                     # Setup and utility scripts
├── requirements.txt             # Python dependencies
├── README.md                    # Project overview and setup
├── ARCHITECTURE.md              # System architecture documentation
├── API_DOCUMENTATION.md         # API and usage documentation
└── DEVELOPMENT.md               # Development setup and guidelines
```

### Documentation Requirements
1. **README.md**: Project overview, setup instructions, usage examples
2. **ARCHITECTURE.md**: System design, class diagrams, data flow
3. **API_DOCUMENTATION.md**: Function/class documentation with examples
4. **Inline Documentation**: Comprehensive docstrings and comments

## Development Guidelines

### Code Quality Standards
- Follow PEP 8 style guidelines
- Use type hints for function signatures
- Implement comprehensive error handling
- Write self-documenting code with meaningful names
- Maintain consistent coding patterns

### Testing Requirements
- Unit tests for all core functionality
- Integration tests for complete workflows
- Edge case testing for error conditions
- Performance tests with large datasets
- Automated test runners with coverage reporting

### Git Best Practices
- Conventional commit messages (`feat:`, `fix:`, `docs:`, `test:`)
- Feature branches for all development
- Pull requests with detailed descriptions
- Regular rebasing to maintain clean history
- Meaningful tags at each milestone

## Academic Integrity & Collaboration

### Allowed Resources
- Course materials and lectures
- Official Python documentation
- Stack Overflow for specific technical questions
- Open-source libraries and frameworks
- LLM assistance for code generation and debugging

### Prohibited Actions
- Copying complete solutions from other students
- Using pre-built finance tracking applications as base
- Submitting work with fabricated git history
- Sharing your complete solution with other students

### Collaboration Guidelines
- You may discuss design approaches with classmates
- Code review and feedback sessions are encouraged
- Help others debug specific issues without sharing solutions
- Acknowledge any assistance received in your documentation

## Resources & Support

### Technical Resources
- [Python Official Documentation](https://docs.python.org/3/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [Git Best Practices](https://www.atlassian.com/git/tutorials)
- [Testing with pytest](https://docs.pytest.org/)
- [Object-Oriented Design Principles](https://python-patterns.guide/)

### Course Support
- **Office Hours**: Wednesdays 14:15-15:00
- **TA Sessions**: Fridays during practice sessions
- **Discord Channel**: #midterm-project
- **Code Review Sessions**: Bi-weekly during office hours

### Sample Code and Examples
- Basic project structure template available in course repository
- Example AI integration patterns
- Testing framework examples
- Git workflow demonstration repository

## Evaluation Timeline

| Date | Evaluation Point | Feedback Type |
|------|-----------------|---------------|
| Oct 6 | Milestone 1 Check | Automated + Brief feedback |
| Oct 13 | Milestone 2 Check | Code review + Suggestions |
| Oct 20 | Milestone 3 Check | AI integration review |
| Oct 27 | Milestone 4 Check | Architecture assessment |
| Nov 10 | Pre-final Review | Comprehensive feedback session |
| Nov 24 | Final Submission | Complete project evaluation |

## Success Tips

### Time Management
- Start immediately - don't wait for "perfect" understanding
- Dedicate 3-4 hours per week consistently
- Use milestones to maintain steady progress
- Ask for help early when stuck

### Technical Approach
- Begin with simple implementations and refactor
- Write tests as you develop, not afterward
- Commit frequently with meaningful messages
- Document your design decisions

### Learning Focus
- This project reinforces every concept from the course
- Use it as an opportunity to solidify understanding
- Don't just implement - understand why each piece works
- Connect course concepts to real-world applications

---

**This project represents the culmination of your learning in the first half of the Applied Programming course. It's designed to be challenging but achievable with consistent effort and proper time management. The skills you develop here will serve as a foundation for the remainder of the course and your future programming endeavors.**

*Due: {{ page.due_date | date: "%B %d, %Y at %I:%M %p" }} • Points: {{ page.points }} (BONUS) • Difficulty: {{ page.difficulty }}*