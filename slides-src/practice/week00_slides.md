---
marp: true
theme: rose-pine-dawn
paginate: true
size: 16:9
header: "Advanced Programming @ UNIL 2025"
footer: "Anna Smirnova, September 2025"

---


# Session 0: Welcome to Advanced Programming @ UNIL 2025!
## Anna Smirnova, TA
## [Course Website](https://ap-unil-2025.github.io/ap-unil-2025-meta/)
---

# Welcome! I'm Anna

A little about me:
*   My PhD research area is Economics, but I have a degree in Computer Science, and I've worked in software development for several years.
*   Now, I use programming for... everything in my work!
*   My goal for my part of the Advanced Programming course is to give you the practical, real-world tools that I wish I had known when I started.

**This is not a typical computer science course. This is about making your research life easier.**

---
# Part 1: Why Are We Here?

---
# A Real-World Example
*   Me and Professor Scheidegger have vastly different working styles and workflows.
* He works on Ubuntu Linux with Kate, and I use a combination of Mac and Arch Linux laptops with an array of esoteric editors.
*   He prefers to write code in an elegant, minimalist way, while I like to think in terms of modular, reusable components and pipelines with OOP.
* But we collaborate on research projects, as he is my PhD supervisor.
* How do we make this work?
* We use modern programming tools and practices to bridge the gap between our different styles.

---

# The Goal of This Tutorial Series

To equip you with a foundational toolkit for writing **reproducible, maintainable, and collaborative code** for your research.

We will focus on the **"how"** and **"why"** of modern programming workflows.

### This course is for you if you've ever:
*   Had ever named a file `final_code_v3_real_final_I_swear.py` ...
    * ...then zipped it up and emailed it to a colleague
*   Spent hours trying to get a colleague's script to run on your machine.
*   Felt overwhelmed by your own messy code a few months after writing it.
*   Wanted to feel more confident and professional in your coding skills.

---

# Our Journey Over the Next Few Weeks

1.  **The Terminal & Environments**: Your command center.
2.  **Git & GitHub**: A time machine for your code.
3.  **Modern Project Management**: Building clean, organized projects.
4.  **Debugging & Type Hints**: Finding and preventing bugs.
5.  **Object-Oriented Programming**: A new way to structure code.
6.  **AI Coding Partners**: Leveraging tools like GitHub Copilot.

---
## Practical Course Logistics: Materials
*   **Course Website**: 
*   **GitHub**: We will use GitHub for assignments and collaboration. Make sure you have an account set up.
* **Editor**: Make sure you have installed VS Code and the Python extension.
---
# Practical Course Logistics: Grading
*   **Assignments**: There will be weekly assignments that will be graded on a pass/fail basis with GitHub Classroom.
    *   **Due Dates**: Assignments will be due one week after they are assigned.
    *   **Late Submissions**: Late submissions will not be accepted unless you have a valid reason.
*   **Participation**: Active participation in class and on GitHub will be considered in your final grade.
*   **Final Project**: A significant portion of your grade will come from a final project where you will apply what you've learned to a real-world problem.
    * 25% assigments and participation
    * 75% final project
---
# Final Project
*   I will provide a list of several **team project ideas** that you can choose from and register your team with me. 
*   You can **also propose your own project idea**, but it must be approved by me.
*   The project will be due at the end of the semester, and you will present your project to the class, as well as submit a report.
*   The project should demonstrate your ability to apply the concepts and tools learned in this course to a real-world problem.
*   Look for more details on the course website. We will discuss this more in the coming weeks.

---
# Administrative Details
*   **Office Hours**: I will hold weekly office hours on Friday for questions and help with assignments. I will not be covering full solutions during these hours, or live debugging your code, but I will help you understand the concepts and guide you in the right direction.
*   **Communication**: Please use the course GitHub Discussions for questions and discussions. I will monitor it regularly.
> **Note:** I will not be answering questions via email. Please use GitHub Discussions for all course-related questions.
> **Note:** **I will not be using Moodle** for this course, except for announcements. All course materials will be on the course website and GitHub.
---

# Part 2: Let's Get to Know Each Other

**(This part is interactive!)**

---

# Who's in the Room?

Let's do a quick poll. Please raise your hand!

What is your major?
*   Finance
*   Economics
*   Acturial Science
*   Management
*   Other

---

# Gauging Our Collective Skill Level

This helps me tailor the course. Be honest --- there are no wrong answers! **Which statement best describes you?**

*   **A) The Absolute Beginner**: "I have never written a line of code, or I've only copied/pasted things."
*   **B) The Scripter**: "I can write scripts in a language like Python or R to get a specific task done. I'm comfortable with variables, loops, and functions."
*   **C) The Tool-User**: "I'm comfortable with scripting, and I've used tools like Git before, but maybe not consistently or confidently."
*   **D) The Confident Coder**: "I feel pretty good about my skills. I know about things like classes and environments, but I'm here to learn best practices and new tools."


<!-- # Part 3: A Quick, Live Coding Puzzle

**(No pressure! This is just to warm up our brains.)**

---

# The Puzzle: "Character Frequency Counter"

**The Goal:** Write a simple Python function that takes a string of text and returns a dictionary counting the frequency of each character.

**Example:**
*   **Input:** `"hello world"`
*   **Expected Output:** `{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}`

---

# Let's Solve It Together (Live)

How would we approach this? Let's brainstorm.

1.  What do we need to start with? (A function definition).
2.  How can we store the counts? (A dictionary seems right).
3.  How do we go through the input string? (A `for` loop).
4.  Inside the loop, what's the logic?
    *   If we've seen this character before...
    *   If this is a new character...

*(Here, you would live-code a solution, engaging the audience for suggestions. Start with a simple, slightly inefficient version, and then perhaps show a more "Pythonic" one if the audience is advanced).*

---

### A Possible Solution

```python
def count_characters(text: str) -> dict[str, int]:
    # Create an empty dictionary to store our counts
    frequency = {}

    # Loop through each character in the input text
    for char in text:
        # If we have already seen this character, increment its count
        if char in frequency:
            frequency[char] += 1
        # Otherwise, this is the first time we've seen it, so add it
        else:
            frequency[char] = 1

    return frequency

# Let's test it!
result = count_characters("hello world")
print(result)
``` -->
