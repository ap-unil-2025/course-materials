---
marp: true
theme: unil-theme
paginate: true
backgroundColor: #f5f9ff
size: 16:9
title: "Session 5: Generative AI for Programming"
description: "Large Language Models and Autonomous Agents"
author: "Anna Smirnova"
date: "2025-10-13"
header: "Session 5: Generative AI for Programming"
---

<!-- _class: lead -->

# Session 5: Generative AI for Programming

**Large Language Models and Autonomous Agents**

---

# Today's Goals

*   Understand the landscape of **AI in coding**.
*   Learn how **GitHub Copilot** works inside VS Code.
*   Discuss the **benefits and limitations** of AI coding assistants.
*   Look ahead to the future: **Agentic AI Tools**.

---
<!-- _class: invert -->

# Part 1: The AI Coding Revolution

---

# From Spellcheck to Copilot

AI assistance in software development isn't new. We've had:
*   **Linters & Formatters**: Early rule-based AI.
*   **IntelliSense**: Smart, context-aware autocompletion.

What's new is the rise of **Generative AI** powered by Large Language Models (LLMs). These models don't just complete your code based on syntax; they *understand intent* and can *generate novel code* from natural language descriptions.
> Note: I will be covering NLP/LLMs as a guest lecturer in the "Advanced Data Analytics" course on week 8! Stay tuned :)

---
# The Landscape of AI Coding Tools
The AI coding landscape is evolving rapidly. Here are the main categories of tools you'll encounter:
*   **Conversational Assistants (Chatbots)**: These are like having a coding buddy in a chat window.
*   **Code Assistants**: These live inside your editor and help you write code line-by-line.
*   **Agentic Tools**: These are more autonomous and can handle entire workflows or projects.

---
# The Landscape of AI Coding Tools : Conversational Assistants
 * **Conversational Assistants (Chatbots)**: These are maybe the most familiar tools for most of you. 
 * You have a conversation with an AI in a chat window to solve problems, get explanations, or generate code snippets. 
 * Examples are ChatGPT, Claude, Gemini, Deepseek, Grok, Mistral, and many others. 
 * **Copilot Chat** is an *interface* that provides you with access to many of these!
---
# The Landscape of AI Coding Tools : Code Assistants
* These live inside your editor and help you write code line-by-line. They are **tools** that *integrate* the **models** we discussed earlier.
* Examples are **GitHub Copilot** (our focus today!), **Gemini Code Assist**, **Junia** (JetBrains),  They provide:
    *   **Inline Suggestions**: Autocomplete lines or blocks of code, usually completed with a single `Tab`.
    *  **Inline Chat**: Ask questions about your code, get explanations, or generate new code snippets right from the code line.
    *   **Documentation Generation**: Automatically creates docstrings and comments.
---
# The Landscape of AI Coding Tools : Agentic Tools
* **Agentic Tools**: You talk to the AI about your high-level goal, and it works autonomously to achieve it by writing code, debugging, and running tests by itself!
* These tools are still emerging, but in the last year they have achieved impressive results.
* They can handle entire workflows, like building a web scraper, setting up a database, or even deploying a web app.

* The biggest players in this field are Claude Code, Codex (OpenAI), Aider (independent, supports all major model providers and local models), Gemini CLI, and Copilot Agent Mode.

---
# Choosing the Right AI Tool

- **For quick code suggestions and productivity:**  
    Use **Code Assistants** like GitHub Copilot directly in your IDE for real-time help as you write code.

- **For explanations, debugging, or brainstorming:**  
    Try **Conversational Assistants** to ask questions, get code reviews, or generate snippets.

- **For complex, multi-step tasks:**  
    Explore **Agentic Tools** (emerging tech) when you want the AI to handle an entire workflow or project for fast prototyping and scaffolding.

> **Tip:** Start with Copilot for daily coding. Use chatbots for deeper questions. Watch agentic tools as they mature!
---
# Choosing the Right AI Tool
Here's my personal recommendation on AI tools, but remember that the landscape is evolving rapidly:
1. Copilot is the only Tab completion tool you need. The Student subscription also grants you access to the rest of the models in the list in VSCode **for free**.
2. Claude (https://claude.ai; Copilot) is great for code generation and debugging, but has very low limits on the free version.
3. Gemini (https://aistudio.google.com; Copilot) is currently free, and their Gemini 2.5 Pro model is one of the most powerful AI models available.
4. ChatGPT (https://chatgpt.com; Copilot) is great for general-purpose coding questions. Use Plus (20.-/month) to access high quality models.

---

# OpenAI Model Line-up (October 2025) 

- GPT-5: 
- GPT-5 Thinking:
- **GPT-4.1** – models specifically created for coding tasks. Can be accessed in Copilot.
---
<!-- _class: invert -->

# Part 2: Getting Started with GitHub Copilot

---

# What is GitHub Copilot?

GitHub Copilot is an AI "pair programmer" that lives directly inside your editor (like VS Code). 

It covers all three categories of AI tools we've discussed:
1.  **Inline Suggestions**: As you type, it suggests entire lines or blocks of code in grayed-out text. Press `Tab` to accept.
2.  **Copilot Chat**: A full-fledged chatbot panel within VS Code where you can ask questions, generate code, explain snippets, and more.
3. **Copilot Agent Mode**: An experimental feature that allows Copilot to run code, install dependencies, and debug issues autonomously.

---

# Copilot's Superpowers

Copilot uses the context of your **entire project** to provide suggestions. This context includes:

*   The code in your **current file**.
*   The code in **other open files/tabs**.
*   The **filename** itself.
*   Your project's **dependencies** (`pyproject.toml`).
*   Your **comments** and **docstrings**.

**The more context you provide, the better its suggestions will be.**

---

# Using Inline Suggestions

This is Copilot's most basic feature. Just start typing!

*   **Writing a function name**: Type `def calculate_standard_deviation(data: list[float]) -> float:` and pause. Copilot will likely suggest the entire function body.
*   **Writing a comment**: Type `# Function to read a csv file and return a pandas dataframe` and press Enter. Copilot will generate the function for you.
*   **Writing docstrings**: After defining a function, start a docstring with `"""`. Copilot will often write a complete, helpful description of what the function does.

**Key Shortcut:** Press `Tab` to accept a suggestion.

---

# Using Copilot Chat

This is where the real power lies. You can open the Chat panel in VS Code and have a conversation.

**You can ask it to:**

*   **"Explain this selected code"**: Get a plain-English description of a complex function.
*   **"Generate a docstring for this function"**: Automate your documentation.
*   **"Find bugs in this code"**: It will analyze a selection and suggest fixes.
*   **"Write a test for this function using pytest"**: A huge time-saver for writing unit tests.
*   **"How do I...?"**: Ask a general programming question without leaving your editor.

---
# Live Demo: Copilot in Action
Let's see Copilot in action! Please follow along in your VS Code editor.

---

<!-- _class: invert -->

# Part 3: The Art of Prompting

---

# Getting Good Results: Prompt Engineering

Your AI assistant is only as good as the instructions you give it. Vague prompts lead to vague or incorrect code. **Good prompting is a skill.**

### The "CRISPE" Framework for Prompts

*   **C - Context**: Tell it what you're doing. "I'm writing a script using pandas to analyze..."
*   **R - Role**: Assign it a role. "You are an expert Python data scientist."
*   **I - Instruction**: What do you want it to do? "Write a function that..."
*   **S - Specificity**: Provide details. "...takes a DataFrame as input, groups by the 'city' column, and calculates the mean of the 'sales' column."
*   **P - Persona**: Define the output style. "Explain it to me like I'm a beginner."
*   **E - Example**: Show it what you want. "For example, if the input is `...`, the output should be `...`"

---

# Prompting Examples: Good vs. Bad

### Bad Prompt 👎
> "make a function for my data"

This is too vague. What data? What should the function do?

### Good Prompt 👍
> **You are an expert Python data scientist.** I am working with a pandas DataFrame that has columns `['date', 'product_id', 'sales']`.
>
> **Write a Python function** named `summarize_monthly_sales` that:
> 1. Takes this DataFrame as input.
> 2. Converts the 'date' column to datetime objects.
> 3. Groups the data by month.
> 4. Calculates the total sales for each month.
> 5. Returns a new DataFrame with 'month' and 'total_sales' columns.

This prompt is specific, provides context, and gives a clear instruction.

---
<!-- _class: invert -->

# Part 4: Benefits, Limitations, and The Future

---

# The Benefits: Why Use AI?

*   **Increased Productivity**: Write boilerplate code, tests, and documentation in seconds.
*   **Learning Tool**: Ask it to explain complex code or concepts. A "why" button for code.
*   **Reduces "Context Switching"**: Get answers to programming questions without leaving your editor to search online.
*   **Overcomes "Blank Page" Syndrome**: Helps you get started when you're not sure how to begin a new function or script.

---

# The Limitations: Trust but Verify

**AI assistants are not always right!** You are still the programmer in charge.

*   **It can hallucinate**: It might invent functions or libraries that don't exist.
*   **It can introduce subtle bugs**: The code might *look* correct but have a logical flaw.
*   **It can be outdated**: It may not know about the latest version of a library or best practices.
*   **Security risks**: Be very careful about pasting sensitive information (like API keys) into chat prompts.

**Rule #1: You are responsible for the code you commit. Always review and test AI-generated code.**

---
<!-- _class: invert -->

# Part 5: The Future is Agentic

---

# Understanding AI Model Types

Before we dive into agents, let's understand the two types of AI models you'll encounter:

---

# Standard vs. Reasoning Models

<div style="display: flex; gap: 2rem;">
<div style="flex: 1;">

## Standard Models 
**GPT-4, Claude, Gemini**

⚡ **Fast** (instant)
📝 **Writing & coding**
💰 **Cheap** ($10/M tokens)
❌ **Bad at math/logic**

</div>
<div style="flex: 1;">

## Reasoning Models
**o1, o3, Gemini-thinking**

🐌 **Slow** (30+ seconds)
🧠 **Complex problems**
💸 **Expensive** (5x cost)
✅ **Great at algorithms**

</div>
</div>

---

# The Strawberry Test

**Question:** "How many 'r's in strawberry?"

| Standard Model | Reasoning Model |
|---------------|-----------------|
| "2 r's" ❌ | "Let me count: s-t-r-a-w-b-e-r-r-y" |
| | "Positions 3, 8, 9 = **3 r's**" ✅ |

💡 **Why?** Standard models see tokens ["straw"]["berry"], not letters!

---

# Quick Comparison: Binary Tree Problem

**Task:** "Is binary tree balanced?"

**Standard:** ❌ Only checks root
**Reasoning:** ✅ Recursively checks all subtrees

> Reasoning models catch the edge cases!

---

# When to Use Which?

| Use Standard 🚀 | Use Reasoning 🧠 |
|-----------------|------------------|
| Writing docs | Complex algorithms |
| Simple code | Debug subtle bugs |
| Quick answers | Math problems |
| Translations | System design |
| **$10/M tokens** | **$50/M tokens** |

---

# The Hidden Thinking

**You ask:** "What's 15% of 2,847?"
**You see:** "427.05"

**What happened (hidden):**
```
2,847 × 0.15 = 2,847 × 0.1 + 2,847 × 0.05  
= 284.7 + 142.35 = 427.05 ✓
```

💭 o1 hides thinking, Claude/Gemini can show it!

---

# Cost & Performance Comparison (2025)

| Model | Speed | $/1M |
|-------|-------|------|
| GPT-4 | Instant | $10-30 |
| Claude | Instant | $3-15 |
| **o1** | 30 sec | **$60** 💸 |
| **o1-mini** | 10 sec | **$12** |

**👉 Reasoning = 5x cost, 100x slower**

---

# Student Cheat Sheet

**Use Standard 🚀**
- README files
- Test cases  
- Code explanation

**Use Reasoning 🧠**
- Debug recursion
- Optimize algorithms
- Security audits

---

# The Future: Hybrid Approaches

## What's Coming (2025-2026):
- **Automatic routing**: System chooses model based on query complexity
- **Mixed workflows**: Standard for drafting, Reasoning for verification
- **Thinking tokens**: Pay only for visible output, not thinking process
- **Local reasoning**: Smaller reasoning models on your laptop

## Today's Best Practice:
1. Start with standard models (fast & cheap)
2. If output seems wrong → try reasoning model
3. For critical code → always verify with reasoning model
4. For learning → ask reasoning model to "show your thinking"

---

# Try This Now!

**Problem:** "3 apples, eat 1, buy 5, give away half, buy 2x what you gave. Total?"

**Standard:** Often gets 8-9 ❌
**Reasoning:** Step-by-step = 10 ✅

*Let's test it live!*

---

# What Are Agentic AI Tools?

**Traditional AI Assistants** (like Copilot autocomplete):
- Respond to direct commands
- Generate code snippets
- Answer specific questions
- **You drive, AI assists**

**Agentic AI Tools**:
- Work autonomously toward goals
- Can execute code and see results
- Debug and iterate on their own
- Use multiple tools (terminal, file system, web)
- **AI drives, you supervise**

---

# The Agent Loop

```
Goal → Plan → Execute → Check → Fix → Done!
```

**Example:** "Build stock price scraper"
1. 🧐 Plans architecture
2. 📝 Writes code  
3. 🧪 Tests & debugs
4. ✅ Delivers solution

---

# Key Agentic Tools in 2025

## Claude Code (Anthropic)
- **Strengths**: Excellent at complex reasoning, careful with code quality
- **Access**: Built into Claude.ai Pro, VS Code extension
- **Best for**: Full-stack development, refactoring, documentation

## Cursor AI
- **Strengths**: Deep IDE integration, multi-file edits
- **Access**: Standalone IDE based on VS Code
- **Best for**: Rapid prototyping, UI/UX development

## Windsurf (Codeium)
- **Strengths**: Free tier available, fast iterations
- **Access**: VS Code fork with agent capabilities
- **Best for**: Students, open-source projects

---

# Key Agentic Tools (continued)

## Aider (Open Source)
- **Strengths**: Terminal-based, supports all LLMs, git integration
- **Access**: `pip install aider-chat`
- **Best for**: Command-line workflows, automation scripts

## GitHub Copilot Workspace
- **Strengths**: GitHub integration, issue-to-PR workflow
- **Access**: GitHub.com (limited preview)
- **Best for**: Open source maintenance, bug fixes

## Devin (Cognition Labs)
- **Strengths**: Full software engineer capabilities
- **Access**: Limited beta
- **Best for**: Complete project development

---

# Real-World Agentic Example

Let's see how an agent handles a real task:

**Human**: "Create a Python script that fetches cryptocurrency prices from an API and saves them to a CSV file with timestamps"

**Agent's Process**:
1. 🔍 Research available crypto APIs
2. 📝 Write initial script using `requests`
3. 🧪 Test the API connection
4. ❌ Handle API errors gracefully
5. 💾 Implement CSV writing with `pandas`
6. ⏰ Add scheduling functionality
7. 📊 Create visualization bonus feature
8. ✅ Deliver complete, tested solution

---

# Agentic Workflow Demo

```python
# Agent-generated solution (simplified)
import requests
import pandas as pd
from datetime import datetime
import time

def fetch_crypto_prices(symbols=['BTC', 'ETH']):
    """Fetch current prices for given cryptocurrencies."""
    base_url = "https://api.coinbase.com/v2/exchange-rates"
    prices = {}
    
    for symbol in symbols:
        response = requests.get(f"{base_url}?currency={symbol}")
        if response.status_code == 200:
            data = response.json()
            prices[symbol] = float(data['data']['rates']['USD'])
    
    return prices

def save_to_csv(prices, filename='crypto_prices.csv'):
    """Append prices with timestamp to CSV file."""
    df = pd.DataFrame([{
        'timestamp': datetime.now(),
        **prices
    }])
    
    df.to_csv(filename, mode='a', header=not pd.io.common.file_exists(filename), index=False)
    print(f"Saved: {prices}")

# Main execution loop
if __name__ == "__main__":
    while True:
        prices = fetch_crypto_prices()
        save_to_csv(prices)
        time.sleep(300)  # Wait 5 minutes
```

---

# Why Use Agents?

**🚀 10x faster** • Boilerplate in seconds
**🎓 Learn faster** • See best practices live
**🎨 Focus on design** • Not syntax

---

# ⚠️ Agent Limitations

**Problems:** Context limits • Hallucinations • Cost • Security

**Rules:**
✅ Start small
✅ Review everything
✅ Use git
❌ Never share secrets

---

# Quick Start: Aider

```bash
pip install aider-chat
aider --model gpt-4o-mini  # Free tier!
```

**Commands:**
```
/add main.py
make a fibonacci function
/run python main.py
add tests
/commit
```

---

# Advanced Agentic Patterns

## Multi-Agent Collaboration
```
Architect Agent → designs system
    ↓
Developer Agent → implements code
    ↓
Tester Agent → writes and runs tests
    ↓
Reviewer Agent → suggests improvements
```

## Autonomous Debugging
- Agent reads error messages
- Searches documentation
- Modifies code
- Re-runs tests
- Iterates until success

---

# Economics/Finance Agentic Use Cases

## Quantitative Analysis
- "Build a portfolio optimization tool using Modern Portfolio Theory"
- "Create a backtesting framework for trading strategies"
- "Implement a Monte Carlo simulation for option pricing"

## Data Pipeline Automation
- "Set up a daily scraper for Federal Reserve economic data"
- "Create an ETL pipeline for Bloomberg data to PostgreSQL"
- "Build a real-time dashboard for market indicators"

## Research Automation
- "Generate statistical reports from FRED data"
- "Automate literature review summaries"
- "Create reproducible research notebooks"

---

# The Future of Agentic AI (2025-2027)

## Near Term (Now - 2025)
- Better IDE integration
- Improved debugging capabilities
- Lower costs, faster inference
- Multi-modal understanding (screenshots, diagrams)

## Medium Term (2025-2026)
- Agents that maintain entire codebases
- Automatic refactoring and optimization
- Cross-language translations
- Self-healing production systems

## Long Term (2026+)
- AI software teams
- Specification-to-deployment pipelines
- Autonomous DevOps
- AI-first programming languages

---

# Preparing for an Agentic Future

## Skills That Matter More
- **System design** and architecture
- **Problem decomposition**
- **Prompt engineering**
- **Code review** and quality assessment
- **Testing strategies**
- **Domain expertise** (economics, finance)

## Skills That Matter Less
- Memorizing syntax
- Boilerplate code writing
- Manual refactoring
- Basic debugging

---

# Ethical Considerations

## Attribution & Authorship
- Who owns AI-generated code?
- How do we attribute contributions?
- What about licensing?

## Job Market Impact
- Will junior developer roles disappear?
- How will education adapt?
- New roles: AI supervisors, prompt engineers

## Quality & Reliability
- Can we trust critical systems to AI?
- How do we audit AI-generated code?
- What about security vulnerabilities?

---

# Hands-On Exercise

## Try It Yourself (15 minutes)
1. Choose an agentic tool:
   - Claude.ai (free tier)
   - Cursor (free trial)
   - Aider (open source)

2. Give it this task:
   > "Create a Python class for managing a personal budget. It should:
   > - Track income and expenses by category
   > - Calculate monthly summaries
   > - Generate a simple text report
   > - Save/load data from JSON"

3. Observe how it:
   - Plans the implementation
   - Writes code iteratively
   - Tests the solution

---

# Best Practices for Students

## Start Small
- Use agents for homework scaffolding
- Generate test cases for your code
- Get explanations for complex topics

## Learn by Reviewing
- **Don't just copy-paste**
- Understand every line
- Ask "why" decisions were made
- Try alternative approaches

## Build Your Portfolio
- Use agents to accelerate projects
- Focus on unique ideas
- Document your design decisions
- Show human creativity + AI efficiency

---

# Summary: Agentic Programming

## Key Takeaways
✅ Agents work **autonomously** toward goals  
✅ They can **write, test, and debug** code  
✅ Current tools are **powerful but need supervision**  
✅ The future is **collaborative human-AI development**  

## Your Action Items
1. Try at least one agentic tool this week
2. Use it for your next assignment (with attribution!)
3. Focus on learning high-level design
4. Stay curious about new developments

---

# Resources & Further Learning

## Tools to Try
- **Aider**: https://aider.chat
- **Claude Code**: https://claude.ai
- **Cursor**: https://cursor.sh
- **Windsurf**: https://codeium.com/windsurf

## Learning Resources
- **Prompt Engineering Guide**: https://www.promptingguide.ai
- **Agentic Patterns**: https://github.com/aider-dev/aider
- **r/LocalLLaMA**: Community for open-source AI

## Stay Updated
- **AI Tool Reviews**: https://theresanaiforthat.com
- **Weekly AI News**: https://www.therundown.ai

---

