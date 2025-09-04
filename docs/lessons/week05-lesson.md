---
layout: lesson
title: "Special Session: Generative AI"
week: 5
date: 2025-10-13
type: "special"
topics:
  - Large Language Models & autonomous agents
  - AI-assisted programming
  - Prompt engineering for code
  - Ethics and best practices
instructor: "Anna Smirnova"
slides: "/slides/practice/week05_slides.html"
summary: "Hands-on session exploring how Large Language Models and autonomous agents can enhance programming productivity and research workflows."
---

# Special Session: Generative AI for Programming and Research

*Led by Anna Smirnova*

This special session explores how Generative AI, particularly Large Language Models (LLMs) and autonomous agents, can revolutionize your programming and research workflow.

## Learning Objectives

By the end of this session, you will:

- Understand the capabilities and limitations of Large Language Models for programming
- Use AI assistants effectively for code generation and debugging
- Apply prompt engineering techniques for better AI interactions
- Implement autonomous agents for research tasks
- Navigate ethical considerations and best practices for AI-assisted work

## Introduction to Large Language Models (LLMs)

### What are LLMs?
- Neural networks trained on vast amounts of text data
- Can generate human-like text, code, and explanations
- Examples: GPT-4, Claude, CodeLlama, GitHub Copilot

### Capabilities for Programmers
- **Code Generation**: Write functions, classes, and entire programs
- **Code Explanation**: Understand complex algorithms and libraries
- **Debugging**: Identify and fix errors in code
- **Documentation**: Generate comments and documentation
- **Refactoring**: Improve code structure and efficiency

## AI-Assisted Programming Tools

### GitHub Copilot
```python
# Type a comment, get AI-generated code
# Function to calculate portfolio variance given weights and covariance matrix

def calculate_portfolio_variance(weights, cov_matrix):
    """
    Calculate portfolio variance given asset weights and covariance matrix.
    
    Args:
        weights (numpy.ndarray): Portfolio weights
        cov_matrix (numpy.ndarray): Asset covariance matrix
    
    Returns:
        float: Portfolio variance
    """
    return np.dot(weights.T, np.dot(cov_matrix, weights))
```

### Claude/ChatGPT for Programming
- Explain complex code concepts
- Generate boilerplate code
- Create test cases
- Review and improve code

### VS Code Extensions
- GitHub Copilot
- Tabnine
- CodeWhisperer
- Codeium

## Prompt Engineering for Code

### Effective Prompting Strategies

1. **Be Specific**
```
❌ "Write a function"
✅ "Write a Python function that calculates the Black-Scholes option price given stock price, strike price, risk-free rate, volatility, and time to expiration"
```

2. **Provide Context**
```
✅ "I'm working on a financial risk management system. Create a class that represents a portfolio of stocks and can calculate Value at Risk using the historical simulation method."
```

3. **Request Examples**
```
✅ "Show me how to use pandas to clean financial time series data, including handling missing values, outliers, and date formatting. Include example data."
```

4. **Ask for Explanations**
```
✅ "Explain this NumPy code line by line and suggest improvements for performance:
[your code here]"
```

## Autonomous Agents for Research

### What are Autonomous Agents?
- AI systems that can perform tasks independently
- Can use tools, make decisions, and execute multi-step workflows
- Examples: AutoGPT, LangChain agents, custom research assistants

### Research Applications
```python
# Example: Autonomous data collection agent
class ResearchAgent:
    def __init__(self, llm, tools):
        self.llm = llm
        self.tools = tools
    
    def research_topic(self, topic):
        # 1. Generate search queries
        queries = self.llm.generate_search_queries(topic)
        
        # 2. Search for papers and data
        results = []
        for query in queries:
            data = self.tools.search_papers(query)
            results.extend(data)
        
        # 3. Analyze and summarize
        summary = self.llm.summarize_research(results)
        return summary
```

### Building Simple Agents
- Use LangChain for agent frameworks
- Integrate with APIs (arXiv, FRED, Yahoo Finance)
- Create custom tools for specific research needs

## Hands-on Activities

### Activity 1: AI Code Generation
1. Use an AI assistant to generate economic calculation functions
2. Compare different prompting strategies
3. Test and refine the generated code

### Activity 2: Code Review with AI
1. Take existing code and ask AI to review it
2. Identify improvement suggestions
3. Implement AI-suggested optimizations

### Activity 3: Research Agent Prototype
1. Design a simple research agent for economic data collection
2. Use AI to help implement the agent
3. Test the agent on a specific research question

## Ethical Considerations and Best Practices

### Academic Integrity
- **Always disclose AI assistance** in academic work
- Understand your institution's AI policies
- Use AI as a tool, not a replacement for learning
- Verify AI-generated content for accuracy

### Code Quality and Reliability
```python
# Always review and test AI-generated code
def ai_generated_function(data):
    # AI-generated code here
    pass

# Add your own tests and validation
def test_ai_function():
    test_data = [1, 2, 3, 4, 5]
    result = ai_generated_function(test_data)
    assert isinstance(result, (int, float)), "Result should be numeric"
    # More tests...
```

### Best Practices

1. **Iterative Refinement**
   - Start with simple prompts
   - Refine based on results
   - Build complexity gradually

2. **Verification is Key**
   - Test all AI-generated code
   - Verify mathematical calculations
   - Check for edge cases

3. **Learning Partnership**
   - Use AI to explain concepts you don't understand
   - Don't just copy-paste; learn from AI-generated code
   - Build your understanding alongside AI assistance

4. **Privacy and Security**
   - Don't share sensitive data with AI tools
   - Be cautious with proprietary code
   - Use local AI models when appropriate

## Tools and Resources

### AI Programming Assistants
- **GitHub Copilot**: Integrated in VS Code
- **Claude**: Web interface and API
- **ChatGPT**: Web interface and API
- **Codeium**: Free alternative to Copilot

### Agent Frameworks
- **LangChain**: Python framework for AI applications
- **AutoGen**: Multi-agent conversation framework
- **CrewAI**: Framework for role-playing AI agents

### Research-Specific Tools
- **Elicit**: AI research assistant for paper discovery
- **Consensus**: AI-powered research platform
- **Connected Papers**: Visual tool for literature review

## Future of AI in Research Programming

### Emerging Trends
- More sophisticated code generation
- Better integration with research workflows
- Domain-specific AI models for economics and finance
- Automated paper writing and review

### Preparing for the Future
- Stay updated with AI tool developments
- Develop critical thinking about AI outputs
- Balance AI assistance with fundamental understanding
- Contribute to ethical AI development in research

## Assessment

This session contributes to:
- Understanding of modern AI tools for research
- Practical skills in AI-assisted programming
- Ethical reasoning about AI use in academic work
- Foundation for using AI in final projects

## Next Steps

Next week we'll apply these AI assistance techniques while diving into scientific computing with NumPy and Pandas, showing how AI can help you learn and use these powerful libraries more effectively.