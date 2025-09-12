---
layout: assignment
title: "Week 5: Building with LLMs & Autonomous Agents"
assignment_number: 5
due_date: 2025-10-20 23:59:00
points: 100
difficulty: "Intermediate"
estimated_time: "5-6 hours"
topics:
  - "Large Language Models"
  - "Prompt Engineering"
  - "Autonomous Agents"
  - "API Integration"
status: "open"
---

## Overview

Learn to integrate Large Language Models (LLMs) into Python applications and build autonomous agents. This hands-on assignment explores practical applications of generative AI in software development.

## Learning Objectives

By completing this assignment, you will:

- Understand LLM capabilities and limitations
- Master prompt engineering techniques
- Build autonomous agents with decision-making capabilities
- Integrate AI APIs into Python applications
- Implement safety and validation mechanisms

## Prerequisites

- OpenAI API key (free tier sufficient) or local LLM setup
- Basic understanding of APIs and JSON
- Python async programming basics (helpful but not required)

## Part 1: LLM Integration Basics (25 points)

Create `llm_basics.py` implementing:

### 1.1 API Wrapper Class (10 points)

```python
class LLMClient:
    """
    Wrapper for LLM API with:
    - Configurable model selection
    - Retry logic for failed requests
    - Token counting and cost estimation
    - Response caching
    """
    def __init__(self, api_key, model="gpt-3.5-turbo"):
        # Your implementation here
    
    async def generate(self, prompt, **kwargs):
        """Generate text from prompt"""
        # Your implementation here
    
    def estimate_cost(self, prompt, response):
        """Estimate API cost for request"""
        # Your implementation here
```

### 1.2 Prompt Templates (8 points)

```python
class PromptTemplate:
    """
    Create reusable prompt templates with:
    - Variable substitution
    - Input validation
    - Output parsing
    """
    def __init__(self, template, variables, output_parser=None):
        # Your implementation here
    
    def format(self, **kwargs):
        """Format template with variables"""
        # Your implementation here
```

### 1.3 Response Validation (7 points)

```python
def validate_json_response(response, schema):
    """Validate LLM JSON output against schema"""
    # Your implementation here

def extract_code_blocks(response, language="python"):
    """Extract and validate code from LLM response"""
    # Your implementation here
```

## Part 2: Prompt Engineering Workshop (25 points)

Create `prompt_engineering.py` with specialized prompts:

### 2.1 Code Generation (10 points)

```python
class CodeGenerator:
    """
    Generate Python code from natural language:
    - Function generation from description
    - Test case generation
    - Code documentation
    - Bug fixing suggestions
    """
    def generate_function(self, description, test_cases=None):
        """Generate function from description"""
        # Your implementation here
    
    def generate_tests(self, function_code):
        """Generate unit tests for function"""
        # Your implementation here
```

### 2.2 Data Analysis Assistant (8 points)

```python
class DataAnalyst:
    """
    LLM-powered data analysis:
    - Generate analysis plans
    - Suggest visualizations
    - Interpret results
    - Write summary reports
    """
    def analyze_dataset(self, data_description):
        """Generate analysis plan"""
        # Your implementation here
```

### 2.3 Chain-of-Thought Reasoning (7 points)

```python
def solve_with_reasoning(problem, steps=None):
    """
    Implement chain-of-thought prompting:
    - Break down complex problems
    - Show step-by-step reasoning
    - Validate each step
    """
    # Your implementation here
```

## Part 3: Autonomous Agent System (35 points)

Create `autonomous_agent.py` implementing:

### 3.1 Base Agent Architecture (15 points)

```python
class AutonomousAgent:
    """
    Build an agent that can:
    - Plan tasks
    - Execute actions
    - Use tools
    - Learn from feedback
    """
    def __init__(self, name, goal, tools=None):
        self.name = name
        self.goal = goal
        self.tools = tools or []
        self.memory = []
        self.plan = []
    
    def plan_task(self, task_description):
        """Generate execution plan"""
        # Your implementation here
    
    def execute_step(self, step):
        """Execute single step of plan"""
        # Your implementation here
    
    def reflect(self, result):
        """Learn from execution results"""
        # Your implementation here
```

### 3.2 Tool Integration (10 points)

```python
class Tool:
    """Base class for agent tools"""
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def execute(self, *args, **kwargs):
        raise NotImplementedError

class CalculatorTool(Tool):
    """Calculator tool for math operations"""
    # Your implementation here

class WebSearchTool(Tool):
    """Web search tool (can be simulated)"""
    # Your implementation here

class FileTool(Tool):
    """File read/write operations"""
    # Your implementation here
```

### 3.3 Multi-Agent Collaboration (10 points)

```python
class AgentOrchestrator:
    """
    Coordinate multiple agents:
    - Task delegation
    - Communication between agents
    - Conflict resolution
    - Result aggregation
    """
    def __init__(self, agents):
        self.agents = agents
    
    def delegate_task(self, task, criteria=None):
        """Assign task to best-suited agent"""
        # Your implementation here
    
    def facilitate_discussion(self, topic, participants):
        """Enable agent communication"""
        # Your implementation here
```

## Part 4: Practical Application (15 points)

Build a **Code Review Assistant** that:

### 4.1 Core Features (10 points)
- Analyzes Python code for issues
- Suggests improvements
- Generates documentation
- Provides complexity analysis
- Offers refactoring suggestions

### 4.2 Interactive Mode (5 points)
- Chat interface for questions about code
- Iterative improvement suggestions
- Learning from user feedback

Create `code_review_assistant.py`:

```python
class CodeReviewAssistant:
    """
    AI-powered code review system
    """
    def review_code(self, code, language="python"):
        """Comprehensive code review"""
        # Your implementation here
    
    def suggest_refactoring(self, code):
        """Suggest code improvements"""
        # Your implementation here
    
    def generate_docs(self, code):
        """Generate documentation"""
        # Your implementation here
    
    def interactive_review(self):
        """Interactive review session"""
        # Your implementation here
```

## Bonus Challenges (+20 points)

### RAG Implementation (+10 points)
Implement Retrieval-Augmented Generation:
```python
class RAGSystem:
    """
    Build a RAG system with:
    - Document embedding
    - Similarity search
    - Context injection
    """
    # Your implementation here
```

### Safety Mechanisms (+10 points)
Implement safety features:
```python
class SafetyFilter:
    """
    - Content moderation
    - Prompt injection detection
    - Output validation
    - Rate limiting
    """
    # Your implementation here
```

## Submission Requirements

```
week5-assignment/
├── llm_basics.py
├── prompt_engineering.py
├── autonomous_agent.py
├── code_review_assistant.py
├── config/
│   └── prompts.yaml  # Store your prompts
├── examples/
│   ├── agent_demo.py
│   └── review_demo.py
├── tests/
│   └── test_agents.py
├── requirements.txt
└── README.md
```

## Important Notes

### API Usage
- Use environment variables for API keys
- Implement rate limiting to avoid excessive costs
- Cache responses where appropriate
- Provide fallback for API failures

### Evaluation Criteria
- Code quality and organization
- Prompt effectiveness
- Agent autonomy and decision-making
- Error handling and edge cases
- Documentation and examples

## Resources

- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [LangChain Documentation](https://python.langchain.com/)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [Building Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/)

## Getting Help

- Office hours: Mondays 15:15-16:00 with Anna Smirnova
- Discord channel: #week5-llm-agents
- Example notebooks provided in course repository

---

*Due: {{ page.due_date | date: "%B %d, %Y at %I:%M %p" }} • Points: {{ page.points }} • Difficulty: {{ page.difficulty }}*