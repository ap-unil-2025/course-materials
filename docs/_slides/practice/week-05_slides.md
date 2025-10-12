---
marp: true
theme: tech-conference
paginate: false
size: 16:9
title: "Session 5: Generative AI for Programming"
description: "Large Language Models and Autonomous Agents"
author: "Anna Smirnova"
date: "2025-10-13"
# header: "AP2025 • Advanced Programming"
footer: "Anna Smirnova • DSAP | ADA 2025"
---

<!-- _class: lead -->

# Guest Lecture: Generative AI for Programming ✨

**Large Language Models and Autonomous Agents**

Anna Smirnova | October 13, 2025

---

# Today's Journey

<div style="display: grid; grid-template-columns: 1.2fr 1fr; gap: 2rem; align-items: center;">

<div>

1. **The Landscape** - Three types of AI tools (chatbots, assistants, agents)
2. **The Models** - Understanding standard vs. reasoning AI
3. **Getting Started** - Using GitHub Copilot & how to ask AI
4. **The Reality** - Benefits, limitations, and staying safe
5. **The Future** - AI tools that write code on their own

**Goal:** By the end, you'll know which AI tool to use and how to use it well.

</div>

<div>

![width:400px](cute.png)

</div>

</div>

---
<!-- _class: invert -->

# Part 1: Understanding AI for Coding

---

# What is AI, Really?

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; align-items: center;">

<div>

**Artificial Intelligence** is about making computers do things that normally require human intelligence.

**Three Key Types:**
- 🎯 **Traditional AI** - Rule-based systems (if-then logic, decision trees)
- 🧠 **Machine Learning** - Systems that learn patterns from data
- 🤖 **Deep Learning** - Neural networks that learn hierarchical patterns

</div>

<div>

![width:400px](https://www.researchgate.net/publication/378394229/figure/fig1/AS:11431281225168931@1708621228583/LLMs-within-the-AI-taxonomy-LLMs-exist-as-a-subset-of-deep-learning-models-which-are-a.tif)

</div>

</div>

---

# The Evolution of AI
```
Traditional AI → Machine Learning → Neural Networks → LLMs
(1960s-1980s)   (1990s-2010s)     (2010s)          (2020s)
```

- **1960s-1980s**: Early AI used programmed rules - scientists wrote if-then logic by hand. Computers could play chess but couldn't learn.
- **1990s-2010s**: Machine learning emerged - AI learned patterns from data instead of following fixed rules. Email spam filters, recommendation systems.
- **2010s**: Deep learning breakthrough - neural networks with many layers could recognize images, understand speech. AI beat humans at Go.
- **2020s**: Large language models arrived - AI trained on billions of words can now understand context, write code, and have conversations.

---

# What's a Neural Network?

<div style="display: grid; grid-template-columns: 1.5fr 1fr; gap: 2rem; align-items: center;">

<div>

Think of it like a **brain-inspired learning machine**.

- Network of connected "neurons" (nodes with mathematical functions)
- Each connection has a "weight" (how strong the influence is)
- During training: adjusts weights to recognize patterns
- Has millions to billions of parameters (weights)

**Simple Example - Recognizing a Cat:**
```
Input (cat photo)
  → Layer 1 (finds edges)
  → Layer 2 (finds shapes)
  → Layer 3 (finds cat features)
  → Output ("It's a cat!")
```

</div>

<div>

![width:350px](https://upload.wikimedia.org/wikipedia/commons/4/46/Colored_neural_network.svg)

</div>

</div>

---

# What are Large Language Models (LLMs)?

LLMs predict the **next most likely word** based on the words that came before.

```
Input: "The capital of France is"
       → AI looks at patterns
       → Predicts: "Paris" (highest probability)
```

**How it works:** The AI has seen millions of sentences like this during training, so it "knows" Paris usually comes after "capital of France is."

**Key Insight:** More layers = can learn more complex patterns (like grammar, facts, even coding!)

---


# How LLMs Learned to Code

**Training Recipe (simplified):**
1. **Feed it code**: Millions of GitHub projects, Stack Overflow answers, programming documentation
2. **Teach patterns**: "Given this code, what usually comes next?"
3. **Get feedback**: Humans rate which code suggestions are good vs. bad
4. **Result**: AI that can write good code

**Example in action:**

You type: `def sort_list_by_date(`

The AI thinks: "I've seen thousands of similar functions... usually they take a list parameter and return a sorted list"

AI suggests: complete function code that makes sense!

---

# Why Now? Why 2025?

**Q:** AI has been around for decades. Why is AI coding suddenly *everywhere*?

**A:** Three breakthroughs finally came together:

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 2rem; align-items: center;">

<div>

**1. Size & Data** *(2020-2023)*
- Models became massive
- Billions of examples
- Better patterns
- Read entire internet

</div>

<div>

**2. Usability** *(2022-2023)*
- Talk naturally
- Learn good vs bad
- ChatGPT works
- Helpful AI

</div>

<div>

**3. Real Tools** *(2024-2025)*
- AI *does things*
- Run code, edit files
- Fast & real-time
- Read projects

</div>

</div>

> **Result:** AI became good enough to handle real programming tasks—not just answer questions.

---
# Three Types of AI Tools for Coding
There are three main types of AI tools you can use for programming:
1. 💬 **Conversational Assistants (Chatbots)** - You ask questions, get answers
2. 💻 **Code Assistants (In-Editor)** - AI lives inside your code
3. 🤖 **Agentic Tools (Autonomous)** - AI works on your code independently toward a goal

---

# 💬 Type 1: Conversational Assistants (Chatbots)

**What they are:** Chat interfaces where you ask questions and get answers -- most familiar type to everyone

**What you use them for:**
- "Explain this error message"
- "How do I parse JSON in Python?"
- "How do I run linear regression in R?"

**💡 Student tip:** GitHub Copilot Chat gives you access to multiple models (GPT, Claude, Gemini) right in VS Code—best of both worlds!

---

# 💻 Type 2: Code Assistants (In-Editor)
![width:700px center](https://code.visualstudio.com/assets/docs/copilot/inline-suggestions/js-suggest.png)

**What they are:** AI living inside your code editor

**What they do:**
- **Inline autocomplete:** Type code, see ghost suggestions, press Tab
- **Chat panel:** Ask questions without leaving your editor
- **Context-aware:** Uses your open files, project structure, dependencies

---

# 🤖 Type 3: Agentic Tools (Autonomous)

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; align-items: center;">

<div>

**What they are:** AI that works autonomously toward a goal

**What they do:**
- You: gives them a goal
- AI: plans, writes, tests, debugs, iterates

**The difference:** 
- Edit multiple files at once
- Run terminal commands
- Iterate on their own mistakes
- Work for minutes/hours autonomously

</div>

<div>

![width:600px](https://github.com/anthropics/claude-code/raw/main/demo.gif)

</div>

</div>

---

# Quick Comparison: Which Type When?

| Task | Chatbot 💬 | Code Assistant 💻 | Agent 🤖 |
|------|-----------|-----------------|---------|
| "Explain recursion" | ✅ Perfect | ⚠️ OK | ❌ Overkill |
| "Autocomplete this function" | ❌ Tedious | ✅ Perfect | ❌ Overkill |
| "Update 10 files" | ❌ Very tedious | ⚠️ Slow | ✅ Perfect |
| "Fix this error" | ✅ Good | ✅ Good | ✅ Better |
| "Learn a new concept" | ✅ Best | ⚠️ OK | ❌ Wrong tool |
| "Build a prototype quickly" | ❌ Too slow | ⚠️ Slow | ✅ Lovable! |
---
<!-- _class: invert -->

# Part 2: Understanding AI Models

---

# Quick Vocab: Understanding AI Terms

Before we go further, let's learn some common words you'll hear:

- **LLM** = Large Language Model (the AI that understands and writes text)
- **Prompt** = What you ask or tell the AI
- **Token** = Small piece of text the AI reads (roughly ¾ of a word)
- **Context window** = How much text the AI can remember at once
- **Fine-tuning** = Teaching the AI to be better at specific tasks
- **Hallucination** = When AI makes up fake information
- **API** = A way for programs to talk to AI services

*You'll hear these words a lot in AI discussions!*

---

# Two Types of AI Models

Before we dive into using AI tools, let's understand what's "under the hood":

---

# Standard vs. Reasoning Models

<div style="display: flex; gap: 2rem;">
<div style="flex: 1;">

## Standard Models 🏃‍♂️
**GPT-5, Claude Sonnet, Gemini**

⚡ **Fast** (instant responses)
📝 **Writing & coding**
💰 **Cheaper** ($3-30/M tokens)
❌ **Not great at math/logic**
🎯 **Use for**: docs, simple code, chat

</div>
<div style="flex: 1;">

## Reasoning Models 🧠
**GPT-5-Thinking, Claude (Extended Thinking), Gemini 2.5 Pro**

🐌 **Slow** (30+ seconds of "thinking")
🧠 **Complex problems**
💸 **More expensive** (5-10x cost)
✅ **Better at algorithms**
🎯 **Use for**: finding problems, math, security

</div>
</div>

---

# The Strawberry Test 🍓

This went viral in 2024 and broke everyone's brain:

**Question:** "How many 'r's in strawberry?"

| Standard Model | Reasoning Model |
|---------------|-----------------|
| "2 r's" ❌ | "Let me count: s-t-r-a-w-b-e-r-r-y" |
| (confidently wrong) | "Positions 3, 8, 9 = **3 r's**" ✅ |

💡 **Why?** Standard models see tokens like ["straw"]["berry"], not individual letters! They're predicting text, not actually counting.

*This is why you can't trust AI for math without thinking it through yourself.*

---

# Quick Comparison: Planning a Trip

**Task:** "Plan a 3-day trip to Paris on a $500 budget"

**Standard Model:** ❌ Suggests expensive hotels, forgets to check if flights fit the budget

**Reasoning Model:** ✅ Thinks step-by-step:
- First calculates flight cost ($300)
- Then finds hotel within remaining budget ($150 for 3 nights)
- Leaves $50 for food and activities

> Reasoning models think through the whole problem!

---
# How Reasoning Models Think (The Hidden Process)

**You ask:** "What's 15% of 2,847?"

**Standard Model (GPT-5):** "427.05" ✅ (instant, but doesn't show work)

**Reasoning Model (GPT-5-Thinking):**
```
<thinking>
Need to calculate 15% of 2,847
15% = 0.15
Breaking down: 2,847 × 0.15
= 2,847 × 0.1 + 2,847 × 0.05
= 284.7 + 142.35
= 427.05
</thinking>
The answer is 427.05
```

💡 **Key difference:** Reasoning models show their "chain of thought" - they think through the problem step-by-step before answering. This improves their accuracy!

---

# Closed-Source Models (October 2025)

| Platform | Free Tier | Pro Subscription | Best For |
|----------|-----------|------------------|----------|
| **ChatGPT** | GPT-5 limited | $20/mo (GPT-5-Thinking + high limits) | General use |
| **Claude** | Sonnet 4.5 limited | $20/mo (5x limit + extended thinking) | Writing & code |
| **Gemini** | 2.5 Flash unlimited | $20/mo (2.5 Pro + 2M context) | Google workspace |
| **Le Chat** | Mistral limited | €5.99/mo students! | European, multilingual |
| **Grok** | Grok 3 free! | $40/mo Premium+ (Grok 4 + Code Fast) | X integration + coding |
| **Cursor** | 2000 completions | $20/mo (500 fast requests/mo) | IDE coding |

---

# Open-Source Models (October 2025)

| Model | Size | Where to Use | Best For |
|-------|------|--------------|----------|
| **DeepSeek R1** | 671B | https://chat.deepseek.com/ | Reasoning! |
| **Qwen 3 Max** | Huge MoE | https://chat.qwen.ai/ | Beats DeepSeek V3 on benchmarks |
| **Mistral Medium 3** | ?? | https://chat.mistral.ai/ (Le Chat) | French! |
| **GLM-4.5** | 355B | https://glm45.org/ | Reasoning + coding + agents |
| **Qwen 3 Coder** | 7-32B | https://chat.qwen.ai/ | Code-specific tasks |

---

# When to Pay More for Reasoning Models

<div class="grid-2">
<div>

## Use Reasoning Models 🧠

- Your code has a hard-to-find problem
- You're working on math or statistics problems
- You need to make sure code is secure
- You're doing something complicated with many steps
- You need to think through different ways to solve something

</div>
<div>

## Use Standard Models 🚀

- Writing simple programs
- Adding comments or documentation
- Asking quick questions like "What does this error mean?"
- Doing something you've done before
- Making basic changes to code

</div>
</div>

**Pro tip**: Use English when prompting! AI models perform best in English because they were trained on more English text than other languages.

---

# OpenAI Model Line-up (August 2025)

**GPT-5** (Released August 7, 2025)
- OpenAI's "unified" model combining reasoning + speed
- 94.6% on AIME math problems, 74.9% on coding benchmarks
- **Free for all ChatGPT users!** (Plus/Pro get higher limits)

**GPT-5 Pro**
- Unlimited access for ChatGPT Pro subscribers ($200/month)
- Best for complex coding, research, and deep thinking tasks

---

# Anthropic Model Line-up (2025)

**Claude Sonnet 4.5** (Released September 2025)
- Default model for Claude Code
- Excellent at coding, can handle complex multi-file changes
- Think of it as: GPT-5's thoughtful older sibling 🧘

**Claude Opus 4.1**
- Heavyweight reasoning model, slower but more thorough
- Best for critical code, security checks, complex algorithms

---

# Google Gemini Line-up (2025)

**Gemini 2.5 Pro**
- Google's flagship model, competitive with GPT-5 and Claude
- Excellent at coding, **huge 2M token context window** (can read entire codebases!)
- **Currently FREE** at aistudio.google.com
- Best for: Students on a budget who need power

**Why students love Gemini:** It's free, it's good, and the context window is massive. Perfect for "paste my entire project and ask questions."

---

# My Personal AI Tool Stack (Anna's Edition)

Here's what I actually use (but this changes quickly!):

1. **GitHub Copilot**: The only Tab-completion tool you need. Student subscription = **FREE** access to GPT-5, Claude, Gemini in VS Code!
2. **Claude** (https://claude.ai): Great for generating code and finding bugs. Free tier available.
3. **Claude Code** (CLI): My choice for big projects with multiple files. Requires Claude Pro/Max subscription.

---
<!-- _class: invert -->

# Part 3: Getting Started with AI

---

# GitHub Copilot - Your First AI Tool

---

# What is GitHub Copilot?

GitHub Copilot is your AI "pair programmer" that lives inside VS Code. Think of it as a helpful friend who always remembers the code syntax.

**Good news:** Copilot gives you access to multiple AI models (GPT-5, Claude, Gemini) all in one place!

**It has three main features:**
1.  **Inline Suggestions**: Type code, see gray suggestion text appear. Press `Tab` to accept. Very helpful!
2.  **Copilot Chat**: A chatbot panel in VS Code. Ask questions, generate code, debug errors, get explanations.
3. **Copilot Agent Mode** (NEW in 2025): The AI can run code, install packages, and fix bugs on its own until your tests pass!

---

# Copilot's Superpowers

Copilot uses the context of your **entire project** to provide suggestions. This context includes:

-   The code in your **current file**.
-   The code in **other open files/tabs**.
-   The **filename** itself.
-   Your project's **dependencies** (`pyproject.toml`).
-   Your **comments** and **docstrings**.

**The more context you provide, the better its suggestions will be.**

---

# Using Inline Suggestions

This is Copilot's most basic feature. Just start typing!

*   **Writing a function name**: Type `def calculate_standard_deviation(data):` and pause. Copilot will likely suggest the entire function body.
*   **Writing a comment**: Type `# Function to read an excel file and calculate std` and press Enter. Copilot will generate the function for you.
*   **Writing docstrings**: After defining a function, start a docstring with `"""`. Copilot will often write a complete, helpful description of what the function does.

**Key Shortcut:** Press `Tab` to accept a suggestion; Press `Ctrl/Cmd+I` to open Inline Chat.

---

# Using Copilot Chat

This is where the real power lies. You can open the Chat panel in VS Code and have a conversation.

**You can ask it to:**

*   **"Explain this selected code"**: Get a plain-English description of what the code does.
*   **"Generate a docstring for this function"**: Write documentation automatically.
*   **"Find problems in this code"**: It will look at your code and suggest fixes.
*   **"Write a test for this function using pytest"**: Saves time writing tests.
*   **"How do I...?"**: Ask a general programming question without leaving your editor.
**Key Shortcut:** Select code and press `Ctrl/Cmd+I` to open Inline Chat with context.
Or open the full Chat panel from the sidebar.

---

# Getting Good Results: How to Ask AI

**Reality check:** AI is a language model, not a mind reader. How you ask matters.

1. 🥉 Basic Level (will get you *something*)
`"make a calculator"`

2. 🥈 Better Level (will get you something *decent*)
`"Write a Python calculator with add, subtract, multiply, divide functions"`

3. 🥇 Best Level (will get you something *good*)
`"Write a Python calculator class with methods for add/subtract/multiply/divide. Handle division by zero. Include documentation and type hints. Use pytest for tests."`

**The pattern:** Be specific → Add details → Include what makes code good

---

# Simple Rules for Asking AI
<div class="grid-2">
<div>

### ✅ DO: Give examples of what you want
Vague:  "write a function to sort books"
Clear:  "write a function that sorts books by year, like this:
         Input: [{'title': 'Python Basics', 'year': 2020}]
         Output: sorted by year"

### ✅ DO: Mention what could go wrong
Basic:  "read a file"
Better: "read a file, but show an error message if the file
         doesn't exist"

</div>
<div>

### ❌ DON'T: Write long paragraphs (keep it short!)
### ❌ DON'T: Assume AI knows what you're thinking
### ❌ DON'T: Ask multiple questions at once (seriously!)
### ❌ DON'T: Say "you're a senior expert"

</div>

---

# Three Simple Strategies

## 1. Show, Don't Just Tell
Instead of saying "my code is broken," show the code:
```
"This code gives the wrong answer:
[paste your code]
I expected: 42
But I got: 43
Can you fix it?"
```
**Why this helps:** AI can see exactly what's wrong.

---

## 2. Start Simple, Then Add More
```
First:  "Write a function to read a Excel file"
Then:   "Now add code to skip empty lines"
Then:   "Now add code to handle files with missing data"
```
**Why this helps:** You build up slowly, AI remembers each step.

---

## 3. Tell AI Your Limits
```
"Write a function to calculate averages.
I can only use basic Python (no special libraries). Keep it simple, or explain each step."
```
**Why this helps:** AI won't give you overly complicated code.

---

# Real-World Example: From Vague to Clear

### 😩 Too Vague
*"help me with my code it doesn't work"*

### 🤔 Getting Better
*"My Python program crashes when I try to read a big file. How do I fix it?"*

### 💎 Clear and Helpful
*"My Python program crashes with 'MemoryError' when I open files bigger than 100MB:*
```python
def read_csv(path):
     with open(path) as f:
         return f.read().splitlines()
```
*How can I read the file one line at a time instead of all at once?"*

---
<!-- _class: invert -->

# Part 4: The Reality Check

---

# The Benefits: Why Use AI?

*   **Work Faster**: Write code much quicker than typing everything yourself
*   **Learn as You Go**: Ask AI to explain complex code or concepts - like having a tutor available 24/7
*   **Stay Focused**: Get answers without leaving your code editor to search Google
*   **Get Unstuck**: AI helps you start when you're staring at a blank screen unsure how to begin

---

# The Limitations: Check Everything

**AI assistants are not always right!** You are still the programmer in charge. Seriously.

*   **It makes things up**: Will confidently invent libraries, functions, or entire APIs that don't exist. "Just use `pandas.magic_sort()`!" (no such thing)
*   **Hidden problems**: Code looks good, but might have small errors or miss special cases
*   **Security risks**: It'll happily paste your API key into code examples if you're not careful

**Rule #1: You are responsible for the code you commit.** Always review, test, and understand AI-generated code. Your name goes on it, not the AI's.

---
<!-- _class: invert -->

# Part 5: The Future is Agentic

---

# What Are AI Agents?

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">

<div>

## Regular AI Tools 💬
*(like Copilot)*

- You tell them exactly what to do
- They give you one answer
- You copy and paste the code
- **You're in control**

</div>

<div>

## AI Agents 🤖
*(autonomous)*

- You give them a goal
- They figure out the steps
- They can try multiple things until it works
- **They work more independently**

</div>

</div>

**What makes agents special:**
- 🔄 **They iterate**: If the first try doesn't work, they try again differently
- 🧠 **They plan**: Break your goal into smaller steps automatically
- 🛠️ **They use tools**: Can run code, search files, install packages, read documentation
- 🔍 **They debug themselves**: When they see an error, they try to fix it without you asking

---

# How Agents Work

```
You give a goal → Agent makes a plan → Agent writes code →
Agent tests it → Agent fixes problems → Done!
```

**Example:** "Make a program that gets stock prices"
1. 🧐 Agent figures out what to do
2. 📝 Agent writes the code
3. 🧪 Agent runs it and checks for errors
4. 🔧 Agent fixes any problems
5. ✅ Gives you working code

---

# Three Types of AI Agents

There are three ways to use AI agents:

## 🌐 Website Agents
- Use them in your web browser
- No need to install anything
- **Examples**: Lovable, Claude.ai, Bolt.new
- **Best for**: Quick experiments, trying things out

## 💻 Editor Agents
- Work inside VS Code (your coding program)
- Can see all your project files
- **Examples**: Cursor, Copilot Agent Mode
- **Best for**: Working on real projects

## ⌨️ Terminal Agents
- Run from the command line
- More control and flexibility
- **Examples**: Claude Code, Codex, Aider
- **Best for**: When you get more comfortable with coding

---

# 🌐 Website Agents - Example

## Claude.ai + Artifacts 🎨
- **What it does**: You chat with it and it creates working programs you can see immediately
- **Cool feature**: **Artifacts** - creates games, websites, charts that you can use right away
- **Cost**: Free version available, Pro is $20/month
- **Best for**: Quick demos, learning, making simple apps
- **Why it's cool**: Type "make me a Tetris game" → playable game appears instantly!

---

# 💻 Editor Agents - Examples

<div class="grid-2">
<div>

## GitHub Copilot Agent Mode
- **What it does**: Works inside VS Code to complete bigger tasks
- **Cool feature**: Connects with GitHub where your code is stored
- **Cost**: Free for students!
- **Best for**: If you already use Copilot

</div>
<div>

## Cursor
- **What it does**: Like VS Code but with AI built-in
- **Cool feature**: Can change multiple files at once
- **Cost**: $20/month, free trial available
- **Best for**: Building real projects
- **Why people like it**: Familiar but more powerful

</div>
</div>

---

# ⌨️ Terminal Agents - Examples

These run from the command line (the terminal window):

**Claude Code**
- **What it does**: AI agent that runs in your terminal
- **Cool feature**: Can edit files, search the web, run commands
- **Cost**: Part of Claude Pro subscription
- **Why it's different**: Works with any text editor you like
- **Bonus**: Also has a VS Code extension!

Many others: **Codex**, **Aider**, **OpenCode** (try with Grok for free!). All of them are fairly similar in concept.

---

# Which Type Should You Use?

| Your Situation | Best Choice | Why? |
|----------|---------------|------|
| "I want to try AI quickly" | 🌐 **Website** (Claude.ai) | Nothing to install, just visit a website |
| "I'm learning to code" | 💻 **Editor** (Copilot) | Free for students, helps you learn |
| "I'm working on a project" | 💻 **Editor** (Cursor) | Works with your files |
| "I'm a professional" | ⌨️ **CLI tools** | Powerful and flexible |
| "I want to try everything" | Try all three! | See what you like best |

**Tip for beginners:** Start with website tools (easy!), then try editor tools once you're comfortable. Terminal tools are for later.

---

# ⚠️ Important Warnings About Agents

**The Problems:**
- **Can't remember everything**: Forgets things if your project is too big
- **Makes stuff up**: Will invent fake functions or libraries
- **Costs money**: Can be expensive if you use it a lot
- **Can be dangerous**: If it has access to your files, it could delete things

**The Safety Rules:**
✅ Start with small tasks (don't give it your entire project on day 1)
✅ Always check what it did (don't trust it blindly)
✅ Save your work first (use git so you can undo mistakes)
❌ Never share passwords or secret keys with AI

*Think of agents like a helpful but overeager assistant: they try hard but need supervision.*

---
# Agents for Students?

## **The Paradox:**
- AI agents can solve most beginner programming tasks in one shot
- BUT: You need to learn programming basics first to use agents effectively

## **My advice:**
- Learn the fundamentals yourself first
- Once you understand the basics, agents become powerful tools
- Don't skip the learning phase - you'll regret it later!

---

# How You Might Use Agents (Economics/Finance)

## Analyzing Data
- "Make a program to analyze different investment portfolios"
- "Create a tool to test trading strategies with historical data"
- "Build a calculator for option prices"

## Getting Data Automatically
- "Write a program that downloads Federal Reserve data every day"
- "Make a tool to collect stock market data and save it"
- "Build a dashboard that shows economic indicators"

---

# What Skills Matter Now?

## Skills That Are MORE Important Now
- **Planning**: Knowing what you want to build
- **Problem decomposition**: Breaking big problems into smaller steps
- **Communication**: Explaining clearly what you need (to AI and humans)
- **Code review**: Checking that code actually works
- **Domain knowledge**: Understanding your field (economics, finance)

## Skills That Are LESS Important Now
- Memorizing exact code syntax
- Writing repetitive boilerplate code
- Doing manual, repetitive tasks
- Finding small typos and formatting issues

---

# Questions to Think About

### Who Owns AI-Written Code?
- If AI writes your code, who owns it? (Legal grey area!)
- GitHub trained AI on public code - is that fair to original authors?
- If AI writes most of your project, is it really "your" work?

### What About Jobs?
- **Will AI replace programmers?** Jobs will change, not disappear
- More focus on: planning, AI collaboration, quality control

### Can We Trust AI Code?
- Should critical systems (banks, hospitals) use AI-written code?
- How do we verify code we didn't write ourselves?
- AI can accidentally introduce security vulnerabilities

---

# Summary: What You Learned Today

## Key Takeaways
✅ **Three types of AI tools**: Chatbots (for questions), Code Assistants (in your editor), Agents (autonomous workers)
✅ **Two types of models**: Standard (fast) vs. Reasoning (slow but smarter)
✅ **How to ask AI well**: Be specific, give examples, mention edge cases
✅ **AI limitations**: Makes mistakes, invents things, needs supervision
✅ **Your new skills**: Learn to plan, communicate clearly, and review code critically


---

# Resources & Tools to Try
- **Claude Artifacts**: https://claude.ai (free tier, instant demos)
- **Lovable**: https://lovable.dev (full-stack MVPs)
- **Bolt.new**: https://bolt.new (StackBlitz instant deploy)
- **Cursor**: https://cursor.sh (free trial, then $20/month)
- **GitHub Copilot**: Free for students! Get it via GitHub Education Pack
- **Claude VSCode Extension**: Part of Claude Pro/Max subscription
- **Aider**: https://aider.chat (open source, supports any LLM)
- **OpenAI Codex CLI**: `npm install -g @openai/codex`
- **OpenCode**: https://opencode.ai (Go-based TUI)

---

# Learning Resources
- **Anthropic Prompt Library**: https://docs.anthropic.com/prompts
- **OpenAI Prompt Guide**: https://platform.openai.com/docs/guides/prompt-engineering
- **PromptingGuide.ai**: https://www.promptingguide.ai (comprehensive)
- **Awesome ChatGPT Prompts**: https://github.com/f/awesome-chatgpt-prompts

---

# Stay Updated (This Space Moves FAST)

## 📰 News & Communities
- **r/ClaudeAI**: https://reddit.com/r/ClaudeAI
- **r/LocalLLaMA**: Open-source AI community
- **Hacker News - AI section**: https://news.ycombinator.com/newest?q=AI
- **There's An AI For That**: https://theresanaiforthat.com (search AI tools)
- **Future Tools**: https://futuretools.io (Matt Wolfe's curated list)
- **AI Tool Tracker**: Track new releases on Product Hunt
- **GitHub Student Developer Pack**: Free Copilot + more!
- **Google AI Studio**: Free Gemini access
- **Anthropic Research**: https://anthropic.com/research (understand how Claude works)

---

<!-- _class: lead -->

# Thank You! Questions?

**Next: Live Building Session**

We'll learn how to use Copilot for your projects and I'll show you how to use Claude Artifacts to build something interactive!

**Your Assignment:**
Build a small project using AI tools and document how you used them. Share in Discord!


