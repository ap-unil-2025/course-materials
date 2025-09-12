---
layout: assignment
title: "Advanced HW5: AI Engineering & Code Review Challenge"
assignment_number: "HW5"
due_date: 2025-10-27 23:59:00
points: 150
difficulty: "Advanced"
estimated_time: "6-8 hours"
github_classroom_url: "https://classroom.github.com/a/advanced-hw5"
starter_repo: "ap2025-advanced-hw5-starter"
topics:
  - "AI prompting techniques"
  - "Code generation evaluation"
  - "Debugging AI code"
  - "Prompt engineering"
  - "AI tool comparison"
bonus: true
status: "open"
---

## Overview

**This is an OPTIONAL grade booster assignment** worth 150 bonus points. Master the art of AI-assisted development by creating complex projects with AI, evaluating generated code, fixing AI mistakes, and documenting best practices.

## The Challenge: "AI Development Laboratory"

You will use AI tools (ChatGPT, Claude, GitHub Copilot) to generate code for specific challenges, then critically evaluate, debug, and improve the results. This teaches both effective AI usage and the importance of understanding code.

## Part 1: Prompt Engineering Mastery (30 points)

### The Task Library

You'll receive 5 programming tasks of increasing complexity. For each task, you must:

1. **Write 3 different prompts** (approaches) to solve the problem
2. **Generate solutions** using AI
3. **Compare results** and document differences
4. **Identify the best approach** and explain why

### Task 1: Data Structure Implementation (6 points)
```
Goal: Implement a self-balancing binary search tree

Prompt Approach A: Direct request
"Write a self-balancing BST in Python"

Prompt Approach B: Step-by-step guidance
"I need to implement a self-balancing BST. First, explain the concept,
then show the node structure, then insertion with balancing, then deletion..."

Prompt Approach C: Test-driven development
"Create test cases for a self-balancing BST first, then implement
the class to pass all tests. Include edge cases..."
```

### Task 2: Algorithm Optimization (6 points)
```
Goal: Optimize a naive sorting algorithm for partially sorted data

Your three approaches should explore:
- Performance requirements focus
- Memory constraints focus  
- Real-world use case focus
```

### Task 3: API Design (6 points)
```
Goal: Design a REST API for a library management system

Compare approaches:
- Entity-first design
- Use-case-first design
- OpenAPI specification-first
```

### Task 4: Debugging Challenge (6 points)
```
Goal: Fix a complex recursive function with subtle bugs

Approaches to compare:
- Paste code and ask for fixes
- Describe symptoms and ask for diagnosis
- Request step-by-step debugging process
```

### Task 5: System Architecture (6 points)
```
Goal: Design a scalable chat application architecture

Different prompting strategies:
- Requirements-focused prompt
- Constraints-focused prompt
- Evolutionary design prompt
```

### Deliverable Format

For each task, create a markdown file:
```markdown
# Task X: [Title]

## Approach A: [Strategy Name]
### Prompt Used
```
[Exact prompt text]
```

### AI Response Summary
[Key points from AI response]

### Generated Code
```python
[Code snippet]
```

### Evaluation
- Correctness: [Score/10]
- Completeness: [Score/10]
- Code Quality: [Score/10]
- Performance: [Score/10]

## Approach B: [Strategy Name]
[Same structure]

## Approach C: [Strategy Name]
[Same structure]

## Comparative Analysis
[Which approach worked best and why]

## Lessons Learned
[Key insights about prompting for this type of task]
```

## Part 2: AI Code Debugging Workshop (35 points)

### Intentionally Flawed Code

You'll receive 5 AI-generated code samples with various issues. Your task:

1. **Identify all bugs** (syntax, logic, performance, security)
2. **Categorize issues** by severity and type
3. **Fix the code** properly
4. **Document the debugging process**
5. **Suggest better prompts** to avoid these issues

### Sample 1: The Confident Mistake (7 points)
```python
# AI-generated code for: "Binary search in rotated sorted array"
def search_rotated(arr, target):
    left, right = 0, len(arr)  # Bug: should be len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
            
        # Determine which half is sorted
        if arr[left] <= arr[mid]:  # Bug: doesn't handle duplicates
            if arr[left] <= target < arr[mid]:  # Bug: edge case
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1  # Bug: What if array is empty?
```

### Sample 2: The Overcomplicated Solution (7 points)
AI tends to overcomplicate simple problems. Debug and simplify.

### Sample 3: The Memory Leak (7 points)
Find and fix memory/resource management issues in AI code.

### Sample 4: The Security Vulnerability (7 points)
Identify and patch security issues in AI-generated web code.

### Sample 5: The Performance Disaster (7 points)
Optimize AI code with O(n!) complexity that should be O(n log n).

### Debugging Report Template

```markdown
# Debug Report: [Problem Name]

## Original Code Issues

### Critical Bugs
1. [Line X]: [Description of bug]
   - Impact: [What breaks]
   - Fix: [How to fix]

### Logic Errors
[List logic problems]

### Performance Issues
[List inefficiencies]

### Code Quality Issues
[Style, readability, maintainability problems]

## Fixed Code
```python
[Corrected implementation]
```

## Testing
[Test cases that expose the bugs]

## Root Cause Analysis
Why did the AI make these mistakes?

## Better Prompt
[Improved prompt that would avoid these issues]
```

## Part 3: AI Tool Comparison Study (25 points)

### Multi-Tool Challenge

Take ONE complex programming task and solve it using:
1. ChatGPT (GPT-4)
2. Claude
3. GitHub Copilot
4. One other AI tool (Bard, Bing Chat, etc.)

### The Complex Task
```
Create a mini programming language interpreter that supports:
- Variables (integers and strings)
- Basic arithmetic (+, -, *, /)
- If/else statements
- While loops
- Functions with parameters
- Print statements

Example program in your language:
```
set x = 10
set y = 20
if x < y then
    print "x is smaller"
else
    print "y is smaller"
end

function add(a, b)
    return a + b
end

set result = add(x, y)
print result
```
```

### Comparison Criteria

Create a detailed comparison table:

| Criteria | ChatGPT | Claude | Copilot | [Other] |
|----------|---------|---------|---------|---------|
| Initial Understanding | | | | |
| Code Completeness | | | | |
| Code Correctness | | | | |
| Error Handling | | | | |
| Code Organization | | | | |
| Documentation | | | | |
| Performance | | | | |
| Creativity/Approach | | | | |
| Iterations Needed | | | | |
| Overall Score (/100) | | | | |

### Deep Dive Analysis

Write a 500-word analysis covering:
- Which tool understood requirements best?
- Which produced most maintainable code?
- Which required least human intervention?
- Which explained their approach best?
- Surprising findings
- Recommendations for different use cases

## Part 4: Prompt Pattern Catalog (30 points)

### Create a Prompt Engineering Guide

Based on your experiments, create a comprehensive guide with 10 prompt patterns:

### Pattern Template
```markdown
## Pattern Name: [Descriptive Name]

### Intent
[What this pattern helps achieve]

### Context
[When to use this pattern]

### Structure
```
[Prompt template with placeholders]
```

### Example
```
[Concrete example using the pattern]
```

### AI Response Quality
[Expected improvement in response]

### Anti-patterns
[Common mistakes to avoid]

### Related Patterns
[Other patterns that work well with this]
```

### Required Patterns to Document

1. **The Socratic Method**: Make AI teach by asking questions
2. **The Rubber Duck**: Use AI as debugging partner
3. **The Code Reviewer**: Get comprehensive code reviews
4. **The Test Generator**: Create exhaustive test suites
5. **The Refactoring Assistant**: Improve existing code
6. **The Documentation Writer**: Generate clear documentation
7. **The Error Message Decoder**: Understand cryptic errors
8. **The Performance Optimizer**: Find bottlenecks
9. **The Security Auditor**: Identify vulnerabilities
10. **The Learning Path**: Create personalized tutorials

## Part 5: The Meta Challenge (20 points)

### Build an AI Prompt Optimizer

Create a Python program that:
1. Takes a basic prompt as input
2. Enhances it using learned patterns
3. Generates multiple variations
4. (Bonus) Tests them against an AI API

```python
def optimize_prompt(basic_prompt, task_type='general'):
    """
    Enhance a basic prompt using best practices
    
    Args:
        basic_prompt: Original user prompt
        task_type: 'debug', 'create', 'explain', 'review', etc.
    
    Returns:
        Dictionary with:
        - enhanced_prompt: Improved version
        - variations: List of alternative approaches
        - tips: Suggestions for further improvement
    """
    # Your implementation here
    pass
```

### Features to Implement

1. **Context Injector**: Add relevant context automatically
2. **Constraint Specifier**: Add useful constraints
3. **Example Provider**: Include relevant examples
4. **Output Formatter**: Specify desired output format
5. **Edge Case Handler**: Add edge case considerations

## Part 6: Reflection Essay (10 points)

Write a 750-word reflective essay on:

**"The Promise and Peril of AI-Assisted Programming"**

Address:
- What AI does well vs. poorly
- Why understanding code remains crucial
- How to use AI responsibly
- The future of programming education
- Ethical considerations

## Deliverables

Submit a repository containing:

```
ai-engineering-challenge/
├── part1-prompting/
│   ├── task1-data-structure.md
│   ├── task2-algorithm.md
│   ├── task3-api-design.md
│   ├── task4-debugging.md
│   └── task5-architecture.md
├── part2-debugging/
│   ├── debug1-binary-search.md
│   ├── debug2-overcomplicated.md
│   ├── debug3-memory-leak.md
│   ├── debug4-security.md
│   └── debug5-performance.md
├── part3-comparison/
│   ├── interpreter-chatgpt.py
│   ├── interpreter-claude.py
│   ├── interpreter-copilot.py
│   ├── interpreter-other.py
│   └── comparison-analysis.md
├── part4-patterns/
│   └── prompt-pattern-catalog.md
├── part5-optimizer/
│   ├── prompt_optimizer.py
│   └── test_optimizer.py
├── part6-reflection/
│   └── reflection-essay.md
└── README.md
```

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| Prompt Engineering | 30 | Quality of prompts, analysis depth |
| Debugging Workshop | 35 | Bug identification, fixes, analysis |
| Tool Comparison | 25 | Thoroughness, fairness, insights |
| Pattern Catalog | 30 | Usefulness, clarity, examples |
| Meta Challenge | 20 | Code quality, creativity |
| Reflection Essay | 10 | Thoughtfulness, writing quality |
| **Total** | **150** |

## Important Notes

### On Using AI for This Assignment

Yes, you MUST use AI for this assignment - that's the point! However:
- Document EVERYTHING (prompts, responses, iterations)
- Your analysis and debugging must be YOUR work
- The reflection essay must be YOUR thoughts

### On Academic Integrity

- All prompts and interactions must be your own
- Share insights, not solutions
- Credit any patterns learned from others

## Tips for Success

- **Be Scientific**: Treat this as research, document everything
- **Be Critical**: AI makes mistakes - find them
- **Be Creative**: Try unusual prompting strategies
- **Be Reflective**: Think about what you're learning
- **Be Honest**: Document what doesn't work too

## Resources

- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [ChatGPT Best Practices](https://platform.openai.com/docs/guides/best-practices)
- [Claude Prompting](https://www.anthropic.com/index/prompting-claude)

---

*This optional grade booster teaches critical AI literacy skills essential for modern software development.*