---
layout: page
title: "Weekly Materials"
---

<div class="weekly-hub">
  <div class="current-banner">
    <div class="current-content">
      <span class="current-label">NOW</span>
      <div class="current-info">
        <h2>Week 0-1: Course Overview</h2>
        <p>Setup • Unix/Linux • Git</p>
      </div>
    </div>
    <a href="{{ '/week/week00' | relative_url }}" class="current-btn">Open Week 0 →</a>
  </div>

  <section class="course-section">
    <h3 class="section-title">Part I: Python Foundations</h3>
    <div class="week-grid">
      
      <a href="{{ '/week/week00' | relative_url }}" class="week-item current">
        <div class="week-header">
          <span class="week-num">0-1</span>
          <span class="week-date">Sep 15</span>
        </div>
        <h4>Course Overview</h4>
        <p>Setup • Unix/Linux • Git</p>
      </a>

      <a href="{{ '/week/week02' | relative_url }}" class="week-item holiday">
        <div class="week-header">
          <span class="week-num">2</span>
          <span class="week-date">Sep 22</span>
        </div>
        <h4>No Class</h4>
        <p>Swiss Federal Fast</p>
      </a>

      <a href="{{ '/week/week03' | relative_url }}" class="week-item">
        <div class="week-header">
          <span class="week-num">3</span>
          <span class="week-date">Sep 29</span>
        </div>
        <h4>Python Fundamentals I</h4>
        <p>Variables • Control flow • Data</p>
      </a>

      <a href="{{ '/week/week04' | relative_url }}" class="week-item">
        <div class="week-header">
          <span class="week-num">4</span>
          <span class="week-date">Oct 6</span>
        </div>
        <h4>Python Fundamentals II</h4>
        <p>Functions • Recursion • OOP</p>
      </a>

      <a href="{{ '/week/week05' | relative_url }}" class="week-item special">
        <div class="week-header">
          <span class="week-num">5</span>
          <span class="week-date">Oct 13</span>
        </div>
        <h4>Generative AI</h4>
        <p>LLMs • Autonomous agents</p>
      </a>

      <a href="{{ '/week/week06' | relative_url }}" class="week-item">
        <div class="week-header">
          <span class="week-num">6</span>
          <span class="week-date">Oct 20</span>
        </div>
        <h4>Scientific Computing</h4>
        <p>NumPy • Pandas • Jupyter</p>
      </a>
      
    </div>
  </section>

  <section class="course-section">
    <h3 class="section-title">Part II: Statistical Learning</h3>
    <div class="week-grid">
      
      <a href="{{ '/week/week07' | relative_url }}" class="week-item">
        <div class="week-header">
          <span class="week-num">7</span>
          <span class="week-date">Oct 27</span>
        </div>
        <h4>Statistical Learning</h4>
        <p>ISL Ch. 2 • Visualization</p>
      </a>

      <a href="{{ '/week/week08' | relative_url }}" class="week-item">
        <div class="week-header">
          <span class="week-num">8</span>
          <span class="week-date">Nov 3</span>
        </div>
        <h4>Linear Regression</h4>
        <p>Simple • Multiple • Inference</p>
      </a>

      <a href="{{ '/week/week09' | relative_url }}" class="week-item">
        <div class="week-header">
          <span class="week-num">9</span>
          <span class="week-date">Nov 10</span>
        </div>
        <h4>Classification</h4>
        <p>Logistic • LDA • QDA • kNN</p>
      </a>

      <a href="{{ '/week/week10' | relative_url }}" class="week-item">
        <div class="week-header">
          <span class="week-num">10</span>
          <span class="week-date">Nov 17</span>
        </div>
        <h4>Resampling Methods</h4>
        <p>Cross-validation • Bootstrap</p>
      </a>

      <a href="{{ '/week/week11' | relative_url }}" class="week-item">
        <div class="week-header">
          <span class="week-num">11</span>
          <span class="week-date">Nov 24</span>
        </div>
        <h4>Model Selection</h4>
        <p>Subset • Ridge • Lasso</p>
      </a>

      <a href="{{ '/week/week12' | relative_url }}" class="week-item">
        <div class="week-header">
          <span class="week-num">12</span>
          <span class="week-date">Dec 1</span>
        </div>
        <h4>Tree-Based Methods</h4>
        <p>Decision trees • Random forests</p>
      </a>

      <a href="{{ '/week/week13' | relative_url }}" class="week-item">
        <div class="week-header">
          <span class="week-num">13</span>
          <span class="week-date">Dec 8</span>
        </div>
        <h4>Unsupervised Learning</h4>
        <p>PCA • Clustering • K-means</p>
      </a>

      <a href="{{ '/week/week14' | relative_url }}" class="week-item">
        <div class="week-header">
          <span class="week-num">14</span>
          <span class="week-date">Dec 15</span>
        </div>
        <h4>Review & Projects</h4>
        <p>Final presentations • Q&A</p>
      </a>
      
    </div>
  </section>

  <div class="quick-links">
    <a href="{{ '/assignments' | relative_url }}" class="quick-link">📝 Assignments</a>
    <a href="{{ '/showcase' | relative_url }}" class="quick-link">🏆 Showcase</a>
    <a href="{{ '/syllabus' | relative_url }}" class="quick-link">📋 Syllabus</a>
  </div>

</div>

<style>
.weekly-hub {
  max-width: 1200px;
  margin: 0 auto;
}

/* Current Week Banner */
.current-banner {
  background: linear-gradient(135deg, #3b82f6 0%, #1e40af 100%);
  border-radius: 0.75rem;
  padding: 1.25rem 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 2.5rem;
  margin-top: 1rem;
  box-shadow: 0 4px 15px rgba(59, 130, 246, 0.2);
}

.current-content {
  display: flex;
  align-items: center;
  gap: 1.25rem;
}

.current-label {
  background: rgba(255, 255, 255, 0.2);
  color: white;
  padding: 0.4rem 0.8rem;
  border-radius: 0.375rem;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.05em;
}

.current-info h2 {
  color: white;
  font-size: 1.25rem;
  margin: 0 0 0.25rem 0;
}

.current-info p {
  color: rgba(255, 255, 255, 0.9);
  margin: 0;
  font-size: 0.875rem;
}

.current-btn {
  background: white;
  color: #3b82f6;
  padding: 0.6rem 1.25rem;
  border-radius: 0.5rem;
  text-decoration: none;
  font-weight: 600;
  font-size: 0.9rem;
  transition: all 0.2s ease;
  white-space: nowrap;
}

.current-btn:hover {
  transform: translateX(2px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
  text-decoration: none;
  color: #3b82f6;
}

/* Course Sections */
.course-section {
  margin-bottom: 2.5rem;
}

.section-title {
  color: var(--text-secondary);
  font-size: 0.875rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin: 0 0 1rem 0;
  padding-bottom: 0.5rem;
  border-bottom: 1px solid var(--border-color);
}

/* Week Grid */
.week-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 1rem;
}

/* Week Items */
.week-item {
  background: var(--background-color);
  border: 1px solid var(--border-color);
  border-radius: 0.5rem;
  padding: 1rem;
  text-decoration: none;
  color: inherit;
  transition: all 0.2s ease;
  display: block;
  position: relative;
  overflow: hidden;
}

.week-item:hover {
  border-color: var(--primary-color);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  text-decoration: none;
  color: inherit;
}

.week-item::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 3px;
  height: 100%;
  background: var(--primary-color);
  transform: scaleY(0);
  transition: transform 0.2s ease;
}

.week-item:hover::before {
  transform: scaleY(1);
}

/* Week Header */
.week-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.75rem;
}

.week-num {
  background: var(--primary-color);
  color: white;
  padding: 0.2rem 0.5rem;
  border-radius: 0.25rem;
  font-size: 0.75rem;
  font-weight: 600;
}

.week-date {
  color: var(--text-secondary);
  font-size: 0.75rem;
  font-weight: 500;
}

.week-item h4 {
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0 0 0.5rem 0;
  line-height: 1.3;
}

.week-item p {
  font-size: 0.8rem;
  color: var(--text-secondary);
  margin: 0;
  line-height: 1.4;
}

/* Special Week Styles */
.week-item.holiday {
  background: #f9fafb;
  opacity: 0.7;
}

.week-item.holiday .week-num {
  background: #6b7280;
}

.week-item.special .week-num {
  background: #f59e0b;
}

.week-item.current {
  border-color: #3b82f6;
  background: linear-gradient(135deg, #eff6ff 0%, var(--background-color) 100%);
}

.week-item.current .week-num {
  background: #3b82f6;
}

/* Quick Links */
.quick-links {
  display: flex;
  justify-content: center;
  gap: 2rem;
  margin-top: 3rem;
  padding-top: 2rem;
  border-top: 1px solid var(--border-color);
}

.quick-link {
  color: var(--text-secondary);
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 500;
  transition: color 0.2s ease;
}

.quick-link:hover {
  color: var(--primary-color);
  text-decoration: none;
}

/* Mobile Responsive */
@media (max-width: 768px) {
  .hub-header h1 {
    font-size: 1.5rem;
  }
  
  .current-banner {
    flex-direction: column;
    text-align: center;
    gap: 1rem;
  }
  
  .current-content {
    flex-direction: column;
  }
  
  .week-grid {
    grid-template-columns: 1fr;
  }
  
  .quick-links {
    flex-direction: column;
    align-items: center;
    gap: 1rem;
  }
}
</style>