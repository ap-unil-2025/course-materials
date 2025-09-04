---
layout: page
title: "Weekly Materials"
---

# Weekly Materials

Access lecture slides, lesson guides, and assignments organized by week.

## Quick Navigation
- [Current Week](#current-week)
- [All Materials by Week](#all-weeks)
- [Assignments]({{ '/assignments' | relative_url }})
- [Individual Collections](#collections)

---

## Current Week {#current-week}

### Week 6: Scientific Computing in Python
**October 20, 2025**

**📺 This Week's Slides:** [Week 6 Slides]({{ '/slides/practice/week06_slides.html' | relative_url }})

**📖 Lesson Guide:** [Scientific Computing in Python]({{ '/lessons/week06-lesson' | relative_url }})

**Topics:**
- NumPy arrays and vectorization
- Pandas data cleaning, transformation, grouping
- Jupyter notebooks
- Scientific computing workflow

**📝 Assignment:** [Assignment 2 - Python Fundamentals]({{ '/assignments/assignment-2-python-fundamentals' | relative_url }})

---

## All Materials by Week {#all-weeks}

### Part I: Python Foundations

<div class="week-grid">

<div class="week-card">
<h4>Week 0-1: Course Overview</h4>
<p><strong>September 15, 2025</strong></p>
<p>Introduction, setup, Unix/Linux basics</p>
<div class="week-links">
<a href="{{ '/slides/practice/week00_slides.html' | relative_url }}">📺 Slides</a>
<a href="{{ '/lessons/week00-lesson' | relative_url }}">📖 Lesson</a>
</div>
</div>

<div class="week-card no-class">
<h4>Week 2: No Class</h4>
<p><strong>September 22, 2025</strong></p>
<p>Swiss Federal Fast (Public Holiday)</p>
<div class="week-links">
<a href="{{ '/lessons/week02-lesson' | relative_url }}">📖 Catch-up Guide</a>
</div>
</div>

<div class="week-card">
<h4>Week 3: Python Fundamentals I</h4>
<p><strong>September 29, 2025</strong></p>
<p>Variables, control flow, data structures, Git</p>
<div class="week-links">
<a href="{{ '/slides/practice/week03_slides.html' | relative_url }}">📺 Slides</a>
<a href="{{ '/lessons/week03-lesson' | relative_url }}">📖 Lesson</a>
</div>
</div>

<div class="week-card">
<h4>Week 4: Python Fundamentals II</h4>
<p><strong>October 6, 2025</strong></p>
<p>Functions, recursion, OOP basics</p>
<div class="week-links">
<a href="{{ '/slides/practice/week04_slides.html' | relative_url }}">📺 Slides</a>
<a href="{{ '/lessons/week04-lesson' | relative_url }}">📖 Lesson</a>
</div>
</div>

<div class="week-card special">
<h4>Week 5: Generative AI</h4>
<p><strong>October 13, 2025</strong></p>
<p>LLMs & autonomous agents (Led by Anna)</p>
<div class="week-links">
<a href="{{ '/slides/practice/week05_slides.html' | relative_url }}">📺 Slides</a>
<a href="{{ '/lessons/week05-lesson' | relative_url }}">📖 Lesson</a>
</div>
</div>

<div class="week-card current">
<h4>Week 6: Scientific Computing</h4>
<p><strong>October 20, 2025</strong></p>
<p>NumPy, Pandas, Jupyter notebooks</p>
<div class="week-links">
<a href="{{ '/slides/practice/week06_slides.html' | relative_url }}">📺 Slides</a>
<a href="{{ '/lessons/week06-lesson' | relative_url }}">📖 Lesson</a>
</div>
</div>

</div>

### Part II: Statistical Learning (Coming Soon)

<div class="week-grid upcoming">

<div class="week-card upcoming">
<h4>Week 7: Statistical Learning & Visualization</h4>
<p><strong>October 27, 2025</strong></p>
<p>ISL Ch. 2, Matplotlib & Seaborn</p>
</div>

<div class="week-card upcoming">
<h4>Week 8: Linear Regression</h4>
<p><strong>November 3, 2025</strong></p>
<p>Simple & multiple regression, inference</p>
</div>

<div class="week-card upcoming">
<h4>Week 9: Classification</h4>
<p><strong>November 10, 2025</strong></p>
<p>Logistic regression, LDA, QDA, kNN</p>
</div>

</div>

---

## Individual Collections {#collections}

### 📺 All Slides
Browse all lecture presentations: **[Slides Collection]({{ '/slides' | relative_url }})**

### 📖 All Lessons  
Access detailed lesson guides: **[Lessons Collection]({{ '/lessons' | relative_url }})**

### 📝 All Assignments
Submit homework and track progress: **[Assignments Collection]({{ '/assignments' | relative_url }})**

---

<style>
.week-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.week-card {
  background: var(--surface-color);
  border: 1px solid var(--border-color);
  border-radius: 0.75rem;
  padding: 1.5rem;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.week-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.week-card.current {
  border: 2px solid var(--primary-color);
  background: linear-gradient(135deg, #f0f7ff 0%, var(--surface-color) 100%);
}

.week-card.special {
  border: 2px solid var(--warning-color);
  background: linear-gradient(135deg, #fffbeb 0%, var(--surface-color) 100%);
}

.week-card.no-class {
  background: #f8f9fa;
  border: 1px dashed var(--border-color);
  opacity: 0.8;
}

.week-card.upcoming {
  opacity: 0.7;
  border-style: dashed;
}

.week-links {
  display: flex;
  gap: 0.75rem;
  margin-top: 1rem;
}

.week-links a {
  padding: 0.5rem 1rem;
  background: var(--background-color);
  border: 1px solid var(--border-color);
  border-radius: 0.5rem;
  text-decoration: none;
  font-size: 0.9rem;
  transition: all 0.2s ease;
}

.week-links a:hover {
  background: var(--primary-color);
  color: white;
  text-decoration: none;
}

.week-card h4 {
  margin-top: 0;
  margin-bottom: 0.5rem;
  color: var(--accent-color);
}

.week-card p {
  margin: 0.25rem 0;
  color: var(--text-secondary);
  font-size: 0.9rem;
}

.week-card p:first-of-type {
  font-weight: 600;
  color: var(--text-primary);
}
</style>