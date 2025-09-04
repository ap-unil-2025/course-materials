---
layout: page
title: "Weekly Materials"
---

# Weekly Materials Hub

All course materials organized by week. Each week page contains lecture slides, TA materials, lesson guides, assignments, examples, and references - everything you need in one place.

---

## Current Week

<div class="current-week-highlight">
  <h3>📅 Week 6: Scientific Computing in Python</h3>
  <p><strong>October 20, 2025</strong></p>
  <p>NumPy arrays, Pandas data manipulation, and Jupyter notebooks for scientific computing</p>
  <a href="{{ '/week/week06' | relative_url }}" class="week-access-btn current">Access This Week's Materials</a>
</div>

---

## All Weeks

### Part I: Python Foundations

<div class="weeks-grid">

<a href="{{ '/week/week00' | relative_url }}" class="week-hub-card">
  <div class="week-number">Week 0-1</div>
  <h4>Course Overview</h4>
  <p class="week-date">September 15, 2025</p>
  <p class="week-desc">Introduction, setup, Unix/Linux basics</p>
  <div class="week-status completed">✓ Materials Available</div>
</a>

<a href="{{ '/week/week02' | relative_url }}" class="week-hub-card no-class">
  <div class="week-number">Week 2</div>
  <h4>No Class</h4>
  <p class="week-date">September 22, 2025</p>
  <p class="week-desc">Swiss Federal Fast (Public Holiday)</p>
  <div class="week-status">📖 Catch-up Guide</div>
</a>

<a href="{{ '/week/week03' | relative_url }}" class="week-hub-card">
  <div class="week-number">Week 3</div>
  <h4>Python Fundamentals I</h4>
  <p class="week-date">September 29, 2025</p>
  <p class="week-desc">Variables, control flow, data structures</p>
  <div class="week-status completed">✓ Materials Available</div>
</a>

<div class="week-hub-card upcoming">
  <div class="week-number">Week 4</div>
  <h4>Python Fundamentals II</h4>
  <p class="week-date">October 6, 2025</p>
  <p class="week-desc">Functions, recursion, OOP basics</p>
  <div class="week-status">📝 Coming Soon</div>
</div>

<a href="{{ '/week/week05' | relative_url }}" class="week-hub-card special">
  <div class="week-number">Week 5</div>
  <h4>Generative AI</h4>
  <p class="week-date">October 13, 2025</p>
  <p class="week-desc">LLMs & autonomous agents (Led by Anna)</p>
  <div class="week-status completed">✓ Materials Available</div>
</a>

<a href="{{ '/week/week06' | relative_url }}" class="week-hub-card current-week">
  <div class="week-number">Week 6</div>
  <h4>Scientific Computing</h4>
  <p class="week-date">October 20, 2025</p>
  <p class="week-desc">NumPy, Pandas, Jupyter notebooks</p>
  <div class="week-status current">📍 Current Week</div>
</a>

</div>

### Part II: Statistical Learning (Coming Soon)

<div class="weeks-grid upcoming-section">

<div class="week-hub-card upcoming">
  <div class="week-number">Week 7</div>
  <h4>Statistical Learning</h4>
  <p class="week-date">October 27, 2025</p>
  <p class="week-desc">ISL Ch. 2, Matplotlib & Seaborn</p>
  <div class="week-status">📝 Coming Soon</div>
</div>

<div class="week-hub-card upcoming">
  <div class="week-number">Week 8</div>
  <h4>Linear Regression</h4>
  <p class="week-date">November 3, 2025</p>
  <p class="week-desc">Simple & multiple regression</p>
  <div class="week-status">📝 Coming Soon</div>
</div>

<div class="week-hub-card upcoming">
  <div class="week-number">Week 9</div>
  <h4>Classification</h4>
  <p class="week-date">November 10, 2025</p>
  <p class="week-desc">Logistic regression, LDA, QDA, kNN</p>
  <div class="week-status">📝 Coming Soon</div>
</div>

</div>

---

## Quick Access

**Need something specific?**

- 📝 **[All Assignments]({{ '/assignments' | relative_url }})** - Homework and project submissions
- 🏆 **[Showcase]({{ '/showcase' | relative_url }})** - Student project gallery  
- 📚 **[Syllabus]({{ '/syllabus' | relative_url }})** - Course overview and policies

---

<style>
/* Current Week Highlight */
.current-week-highlight {
  background: linear-gradient(135deg, var(--primary-color) 0%, #0031d9 100%);
  color: white;
  padding: 2rem;
  border-radius: 1rem;
  text-align: center;
  margin: 2rem 0 3rem 0;
}

.current-week-highlight h3 {
  margin: 0 0 0.5rem 0;
  font-size: 1.5rem;
  color: white;
}

.current-week-highlight p {
  margin: 0.5rem 0;
  opacity: 0.9;
  font-size: 1rem;
}

.current-week-highlight p:last-of-type {
  margin-bottom: 1.5rem;
  font-size: 1.1rem;
}

.week-access-btn {
  display: inline-block;
  background: white;
  color: var(--primary-color);
  padding: 0.75rem 2rem;
  border-radius: 0.5rem;
  text-decoration: none;
  font-weight: 600;
  font-size: 1rem;
  transition: all 0.2s ease;
}

.week-access-btn:hover {
  background: rgba(255, 255, 255, 0.95);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  text-decoration: none;
  color: var(--primary-color);
}

/* Weeks Grid */
.weeks-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.upcoming-section {
  opacity: 0.8;
}

/* Week Hub Cards */
.week-hub-card {
  background: var(--background-color);
  border: 1px solid var(--border-color);
  border-radius: 0.75rem;
  padding: 1.5rem 1.5rem 3.5rem 1.5rem;
  text-decoration: none;
  color: inherit;
  transition: all 0.2s ease;
  cursor: pointer;
  display: block;
  position: relative;
  min-height: 160px;
}

.week-hub-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
  text-decoration: none;
  color: inherit;
}

.week-hub-card.current-week {
  border: 2px solid var(--primary-color);
  background: linear-gradient(135deg, #f0f7ff 0%, var(--background-color) 100%);
}

.week-hub-card.special {
  border: 2px solid var(--warning-color);
  background: linear-gradient(135deg, #fffbeb 0%, var(--background-color) 100%);
}

.week-hub-card.no-class {
  background: linear-gradient(135deg, #f8f9fa 0%, var(--background-color) 100%);
  border: 1px dashed var(--border-color);
}

.week-hub-card.upcoming {
  opacity: 0.7;
  border-style: dashed;
  cursor: default;
  pointer-events: none;
}

.week-number {
  display: inline-block;
  background: var(--primary-color);
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.8rem;
  font-weight: 600;
  margin-bottom: 1rem;
}

.week-hub-card.current-week .week-number {
  background: var(--primary-color);
}

.week-hub-card.special .week-number {
  background: var(--warning-color);
}

.week-hub-card.no-class .week-number {
  background: var(--secondary-color);
}

.week-hub-card.upcoming .week-number {
  background: var(--text-muted);
}

.week-hub-card h4 {
  margin: 0 0 0.5rem 0;
  font-size: 1.25rem;
  color: var(--accent-color);
}

.week-date {
  font-weight: 600;
  color: var(--text-primary);
  margin: 0.25rem 0;
  font-size: 0.9rem;
}

.week-desc {
  color: var(--text-secondary);
  margin: 0.5rem 0 1rem 0;
  font-size: 0.9rem;
  line-height: 1.4;
}

.week-status {
  position: absolute;
  bottom: 1rem;
  left: 1.5rem;
  right: 1.5rem;
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  font-size: 0.8rem;
  font-weight: 500;
  text-align: center;
}

.week-status.completed {
  background: #f0fdf4;
  color: var(--success-color);
  border: 1px solid #bbf7d0;
}

.week-status.current {
  background: #eff6ff;
  color: var(--primary-color);
  border: 1px solid #bfdbfe;
}

.week-status:not(.completed):not(.current) {
  background: var(--surface-color);
  color: var(--text-muted);
  border: 1px solid var(--border-color);
}

/* Mobile Responsiveness */
@media (max-width: 768px) {
  .current-week-highlight {
    padding: 1.5rem;
  }
  
  .current-week-highlight h3 {
    font-size: 1.25rem;
  }
  
  .weeks-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
  
  .week-hub-card {
    padding: 1.25rem 1.25rem 3rem 1.25rem;
    min-height: 140px;
  }
  
  .week-status {
    left: 1.25rem;
    right: 1.25rem;
  }
}
</style>