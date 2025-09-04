---
marp: true
theme: gradient
paginate: true
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
*   Master **best practices for prompting** to get the best results.
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

# OpenAI Model Line-up (June 25 2025) 

- **GPT-4o (“omni”)** – multimodal (works with images and audio)  flagship; became ChatGPT’s default model on Apr 30 2025. Default model for Plus subscribers, can help with some tasks, but more a of generalist than a specialist.
- **GPT-4o mini** – lightweight model (≈8 B params) that’s ≈60 % cheaper than GPT-3.5 Turbo yet tops other small LLMs, announced Jul 18 2024. This is the default free version of ChatGPT, and (in my opinion) not very high-quality.
- **GPT-4.1 / 4.1 mini / 4.1 nano** – models specifically created for coding tasks, up to 1 M-token context and faster/cheaper than 4o. Default model for Copilot, and now available in ChatGPT for Plus subscribers.
---
# OpenAI model lineup: Reasoning → **o-series**  
> **Reasoning models** are models which "think" (generate intermediate steps) before answering a question, and are therefore more accurate than the previous models. They are also more expensive to run, so they are not available in the free version of ChatGPT.
- **o3** – frontier long-form reasoning model launched Apr 16 2025.
- **o3-pro** – premium variant with extended “think time,” rolled out Jun 10 2025 to Pro users (200.-/month)  
- **o4-mini**/**o4-mini-high** – cost-efficient sibling; matches o3 accuracy with lower latency/cost. 
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

# The Future is Agentic

**Example Goal:**
> "Build a web scraper to get the titles and prices of all books from example.com/books, and save the results to a CSV file named `books.csv`."

See agentic AI in action in the live demo :)


