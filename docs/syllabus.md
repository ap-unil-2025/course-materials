---
layout: default
---

<style>

/* Compact Header for Default Layout */
.syllabus-header {
  text-align: center;
  margin-bottom: 1rem;
}

.syllabus-header h1 {
  font-size: 2rem;
  color: var(--accent-color);
  margin: 0 0 0.5rem 0;
}

.syllabus-header p {
  color: var(--text-secondary);
  margin: 0;
  font-size: 1rem;
}
</style>

<div class="syllabus">
  <!-- Compact header for syllabus -->
  <div class="syllabus-header">
    <h1>Course Syllabus</h1>
    <p>Learning objectives, schedule, grading policy, and course requirements</p>
  </div>

  <!-- Course Overview Banner -->
  <div class="course-banner">
    <div class="course-content">
      <span class="course-label">2025</span>
      <div class="course-info">
        <h2>Data Science and Advanced Programming</h2>
        <p>DSAP • HEC Lausanne • Mondays 12:30–16:00 • Internef 263</p>
      </div>
    </div>
    <a href="{{ '/weekly-materials' | relative_url }}" class="course-btn">View Materials →</a>
  </div>

  <!-- Link to Professor's Syllabus -->
  <div style="margin: 1.5rem 0; padding: 1rem; background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); border: 1px solid #3b82f6; border-radius: 0.5rem; text-align: center;">
    <p style="margin: 0; font-size: 0.95rem; color: #1e40af;">
      📄 <strong>Note:</strong> View the <a href="{{ '/professor-syllabus' | relative_url }}" style="font-weight: 600; color: #3b82f6;">Professor's Official Syllabus</a> for the most up-to-date course details and schedule
    </p>
  </div>

  <!-- Course Information -->
  <section class="syllabus-section">
    <h3 class="section-title">Course Overview</h3>
    <div class="info-grid">
      
      <div class="info-item">
        <div class="info-header">
          <span class="info-badge">Goal</span>
        </div>
        <h4>Learning Objectives</h4>
        <p>Master Python, statistical learning, and high-performance computing for quantitative analysis in Economics and Finance.</p>
      </div>

      <div class="info-item">
        <div class="info-header">
          <span class="info-badge">Format</span>
        </div>
        <h4>Course Structure</h4>
        <p>Three 45-minute lectures + one 45-minute hands-on session per week with practical applications.</p>
      </div>

      <div class="info-item">
        <div class="info-header">
          <span class="info-badge priority">Platform</span>
        </div>
        <h4>Nuvolos Cloud</h4>
        <p>All materials distributed via cloud platform. <a href="https://app.nuvolos.cloud/enroll/class/RshD654gzU4" target="_blank">Enroll here</a>.</p>
      </div>

      <div class="info-item">
        <div class="info-header">
          <span class="info-badge">Community</span>
        </div>
        <h4>Discord Server</h4>
        <p>Real-time help and peer support. <a href="https://discord.gg/pr4q3QH2" target="_blank">Join Discord</a>.</p>
      </div>

    </div>
  </section>

  <!-- Key Skills Section -->
  <section class="syllabus-section">
    <h3 class="section-title">Skills You'll Master</h3>
    <div class="skills-grid">
      
      <div class="skill-item">
        <div class="skill-icon">🐍</div>
        <h4>Python Programming</h4>
        <p>Clean, efficient code • NumPy & Pandas • Visualization</p>
      </div>

      <div class="skill-item">
        <div class="skill-icon">📊</div>
        <h4>Statistical Learning</h4>
        <p>Bias–variance • Model assessment • ML algorithms</p>
      </div>

      <div class="skill-item">
        <div class="skill-icon">🧠</div>
        <h4>Machine Learning</h4>
        <p>Regression • Classification • Tree methods • Neural networks</p>
      </div>

      <div class="skill-item">
        <div class="skill-icon">⚡</div>
        <h4>High-Performance Computing</h4>
        <p>Code acceleration • Parallel processing • Optimization</p>
      </div>

      <div class="skill-item">
        <div class="skill-icon">🎯</div>
        <h4>Project Management</h4>
        <p>End-to-end projects • Version control • Presentation</p>
      </div>

    </div>
  </section>

  <!-- Course Schedule -->
  <section class="syllabus-section">
    <h3 class="section-title">Course Schedule</h3>
    <p>Detailed weekly materials are available in the <a href="{{ '/weekly-materials' | relative_url }}">Weekly Materials Hub</a>.</p>
    
    <div class="schedule-parts">
      
      <div class="schedule-part">
        <div class="part-header">
          <span class="part-badge">Part I</span>
          <h4>Python Foundations</h4>
          <span class="part-dates">Weeks 1-6</span>
        </div>
        <div class="part-topics">
          <span class="topic">Course Setup</span>
          <span class="topic">Unix/Linux & Git</span>
          <span class="topic">Python Basics</span>
          <span class="topic">Functions & OOP</span>
          <span class="topic">Generative AI</span>
        </div>
      </div>

      <div class="schedule-part">
        <div class="part-header">
          <span class="part-badge">Part II</span>
          <h4>Data Science</h4>
          <span class="part-dates">Weeks 7-10</span>
        </div>
        <div class="part-topics">
          <span class="topic">Linear Regression</span>
          <span class="topic">Classification</span>
          <span class="topic">Unsupervised Learning</span>
          <span class="topic">Deep Learning</span>
        </div>
      </div>

      <div class="schedule-part">
        <div class="part-header">
          <span class="part-badge">Part III</span>
          <h4>Advanced Topics</h4>
          <span class="part-dates">Weeks 11-14</span>
        </div>
        <div class="part-topics">
          <span class="topic">Advanced ML</span>
          <span class="topic">High-Performance Computing</span>
          <span class="topic">Project Presentations</span>
        </div>
      </div>

    </div>
  </section>

  <!-- Assessment & Grading -->
  <section class="syllabus-section">
    <h3 class="section-title">Assessment & Grading</h3>
    <div class="assessment-grid">
      
      <div class="assessment-item primary">
        <div class="assessment-icon">🎯</div>
        <h4>Individual Project</h4>
        <p>Python programming project • 10-page report • GitHub repository • Optional presentation</p>
        <a href="{{ '/INDIVIDUAL_PROJECT_RULES' | relative_url }}" class="project-link">View Project Guidelines →</a>
      </div>

      <div class="assessment-item">
        <div class="assessment-icon">📝</div>
        <h4>No Exams</h4>
        <p>Assessment based entirely on demonstrating understanding through the capstone project</p>
      </div>

      <div class="assessment-item">
        <div class="assessment-icon">⭐</div>
        <h4>Bonus Points</h4>
        <p>Additional opportunities through homework assignments throughout the semester</p>
      </div>

    </div>
  </section>

  <!-- References -->
  <section class="syllabus-section">
    <h3 class="section-title">Course References & Textbooks</h3>
    <div class="references-grid">
      
      <div class="reference-item">
        <div class="reference-type">Statistical Learning</div>
        <h4>An Introduction to Statistical Learning</h4>
        <p>James, Witten, Hastie, Tibshirani (2nd Edition)</p>
        <p><a href="https://www.statlearning.com" target="_blank">statlearning.com</a></p>
      </div>

      <div class="reference-item">
        <div class="reference-type">Machine Learning</div>
        <h4>Probabilistic Machine Learning: An Introduction</h4>
        <p>Kevin P. Murphy • MIT Press</p>
        <p><a href="http://probml.github.io/book1" target="_blank">probml.github.io/book1</a></p>
      </div>

      <div class="reference-item">
        <div class="reference-type">Deep Learning</div>
        <h4>Deep Learning</h4>
        <p>Goodfellow, Bengio, Courville • MIT Press</p>
        <p><a href="http://www.deeplearningbook.org" target="_blank">deeplearningbook.org</a></p>
      </div>

      <div class="reference-item">
        <div class="reference-type">Python Programming</div>
        <h4>Introduction to Computation and Programming Using Python</h4>
        <p>John V. Guttag • MIT Press</p>
        <p>Comprehensive introduction to Python programming</p>
      </div>

      <div class="reference-item">
        <div class="reference-type">Scientific Python</div>
        <h4>A Primer on Scientific Programming with Python</h4>
        <p>Hans Petter Langtangen • Springer</p>
        <p>Focus on scientific computing applications</p>
      </div>

      <div class="reference-item">
        <div class="reference-type">Economics & Finance</div>
        <h4>QuantEcon</h4>
        <p>Lectures on quantitative economics</p>
        <p><a href="https://quantecon.org" target="_blank">quantecon.org</a></p>
      </div>

    </div>
  </section>

</div>

<style>
/* Syllabus Page Layout - Using Weekly Hub Patterns */
.syllabus {
  max-width: 1200px;
  margin: 0 auto;
}

/* Course Banner - Similar to Current Week Banner */
.course-banner {
  background: linear-gradient(135deg, #059669 0%, #047857 100%);
  border-radius: 0.75rem;
  padding: 1.25rem 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 2.5rem;
  margin-top: 0;
  box-shadow: 0 4px 15px rgba(5, 150, 105, 0.2);
}

.course-content {
  display: flex;
  align-items: center;
  gap: 1.25rem;
}

.course-label {
  background: rgba(255, 255, 255, 0.2);
  color: white;
  padding: 0.4rem 0.8rem;
  border-radius: 0.375rem;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.05em;
}

.course-info h2 {
  color: white;
  font-size: 1.25rem;
  margin: 0 0 0.25rem 0;
}

.course-info p {
  color: rgba(255, 255, 255, 0.9);
  margin: 0;
  font-size: 0.875rem;
}

.course-btn {
  background: white;
  color: #059669;
  padding: 0.6rem 1.25rem;
  border-radius: 0.5rem;
  text-decoration: none;
  font-weight: 600;
  font-size: 0.9rem;
  transition: all 0.2s ease;
  white-space: nowrap;
}

.course-btn:hover {
  transform: translateX(2px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
  text-decoration: none;
  color: #059669;
}

/* Section Layout */
.syllabus-section {
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

/* Grid Layouts */
.info-grid,
.skills-grid,
.assessment-grid,
.contact-grid,
.references-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1rem;
}

.skills-grid {
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
}

/* Item Styles */
.info-item,
.skill-item,
.assessment-item,
.contact-item {
  background: var(--background-color);
  border: 1px solid var(--border-color);
  border-radius: 0.5rem;
  padding: 1rem;
  transition: all 0.2s ease;
  position: relative;
  overflow: hidden;
}

/* Reference Item Specific Styles */
.reference-item {
  background: var(--background-color);
  border: 1px solid var(--border-color);
  border-radius: 0.625rem;
  padding: 1.25rem;
  transition: all 0.2s ease;
  position: relative;
}

.reference-item:hover {
  border-color: #6b7280;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  background: linear-gradient(135deg, #fafafa 0%, var(--background-color) 100%);
}

.info-item:hover,
.skill-item:hover,
.assessment-item:hover,
.contact-item:hover {
  border-color: var(--primary-color);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.info-item::before,
.skill-item::before,
.assessment-item::before,
.contact-item::before {
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

.info-item:hover::before,
.skill-item:hover::before,
.assessment-item:hover::before,
.contact-item:hover::before {
  transform: scaleY(1);
}

/* Headers and Icons */
.info-header,
.contact-header {
  margin-bottom: 0.5rem;
}

.info-badge,
.contact-role-badge {
  background: var(--primary-color);
  color: white;
  padding: 0.2rem 0.5rem;
  border-radius: 0.25rem;
  font-size: 0.75rem;
  font-weight: 600;
}

.reference-type {
  background: linear-gradient(135deg, #f3f4f6 0%, #e5e7eb 100%);
  color: var(--text-secondary);
  padding: 0.25rem 0.625rem;
  border-radius: 0.375rem;
  font-size: 0.7rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  display: inline-block;
  margin-bottom: 0.5rem;
}

.info-badge.priority {
  background: #10b981;
}

.skill-icon,
.assessment-icon {
  font-size: 1.5rem;
  margin-bottom: 0.75rem;
  display: block;
}

/* Item Content */
.info-item h4,
.skill-item h4,
.assessment-item h4,
.contact-item h4,
.reference-item h4 {
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0 0 0.5rem 0;
  line-height: 1.3;
}

.info-item p,
.skill-item p,
.assessment-item p,
.contact-item p,
.reference-item p {
  font-size: 0.8rem;
  color: var(--text-secondary);
  margin: 0;
  line-height: 1.4;
}

/* Special States */
.assessment-item.primary {
  border-color: #3b82f6;
  background: linear-gradient(135deg, #eff6ff 0%, var(--background-color) 100%);
}

.project-link {
  display: inline-block;
  margin-top: 0.5rem;
  color: #3b82f6;
  font-size: 0.85rem;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.2s ease;
}

.project-link:hover {
  color: #2563eb;
  transform: translateX(2px);
}

/* Schedule Parts */
.schedule-parts {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1rem;
}

.schedule-part {
  background: var(--background-color);
  border: 1px solid var(--border-color);
  border-radius: 0.5rem;
  padding: 1rem;
  transition: all 0.2s ease;
  position: relative;
  overflow: hidden;
}

.schedule-part:hover {
  border-color: var(--primary-color);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.schedule-part::before {
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

.schedule-part:hover::before {
  transform: scaleY(1);
}

.part-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 0.75rem;
}

.part-badge {
  background: var(--primary-color);
  color: white;
  padding: 0.2rem 0.5rem;
  border-radius: 0.25rem;
  font-size: 0.75rem;
  font-weight: 600;
}

.part-header h4 {
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0;
  flex: 1;
  text-align: center;
}

.part-dates {
  color: var(--text-secondary);
  font-size: 0.75rem;
  font-weight: 500;
}

.part-topics {
  display: flex;
  flex-wrap: wrap;
  gap: 0.25rem;
}

.topic {
  background: var(--surface-color);
  color: var(--text-secondary);
  padding: 0.2rem 0.4rem;
  border-radius: 0.25rem;
  font-size: 0.7rem;
  font-weight: 500;
}

/* Mobile Responsive */
@media (max-width: 768px) {
  .course-banner {
    flex-direction: column;
    text-align: center;
    gap: 1rem;
  }
  
  .course-content {
    flex-direction: column;
  }
  
  .info-grid,
  .skills-grid,
  .assessment-grid,
  .contact-grid,
  .references-grid,
  .schedule-parts {
    grid-template-columns: 1fr;
  }
  
  .part-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
  }
  
  .part-header h4 {
    text-align: left;
  }
}
</style>
