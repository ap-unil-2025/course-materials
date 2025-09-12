---
layout: default
---

<style>

/* Compact Header for Default Layout */
.help-header {
  text-align: center;
  margin-bottom: 1rem;
}

.help-header h1 {
  font-size: 2rem;
  color: var(--accent-color);
  margin: 0 0 0.5rem 0;
}

.help-header p {
  color: var(--text-secondary);
  margin: 0;
  font-size: 1rem;
}
</style>

<div class="help-support">
  <!-- Compact header for help & support -->
  <div class="help-header">
    <h1>Help & Support</h1>
    <p>Office hours, TA sessions, Discord community, and learning resources</p>
  </div>

  <!-- Support Banner -->
  <div class="support-banner">
    <div class="support-content">
      <span class="support-label">24/7</span>
      <div class="support-info">
        <h2>DSAP Help & Support</h2>
        <p>Multiple channels • Quick responses • Community driven</p>
      </div>
    </div>
    <a href="https://discord.gg/pr4q3QH2" target="_blank" class="support-btn">Join Discord →</a>
  </div>

  <!-- Office Hours & Contact -->
  <section class="help-section">
    <h3 class="section-title">Office Hours & Direct Contact</h3>
    <div class="contact-grid">
      
      <div class="contact-item priority">
        <div class="contact-header">
          <span class="contact-role">Lead TA</span>
        </div>
        <h4>Anna Smirnova</h4>
        <p><a href="mailto:anna.smirnova@unil.ch">anna.smirnova@unil.ch</a></p>
        <div class="office-hours">
          <div class="hours-item">
            <span class="hours-day">Monday</span>
            <span class="hours-time">15:15–16:00</span>
          </div>
          <div class="hours-item">
            <span class="hours-day">Friday</span>
            <span class="hours-time">On request</span>
          </div>
        </div>
      </div>

      <div class="contact-item">
        <div class="contact-header">
          <span class="contact-role">Professor</span>
        </div>
        <h4>Simon Scheidegger</h4>
        <p><a href="mailto:simon.scheidegger@unil.ch">simon.scheidegger@unil.ch</a></p>
        <p>Available during class time and by appointment</p>
      </div>

      <div class="contact-item">
        <div class="contact-header">
          <span class="contact-role">Platform</span>
        </div>
        <h4>Nuvolos Support</h4>
        <p><a href="mailto:support@nuvolos.cloud">support@nuvolos.cloud</a></p>
        <p>Technical issues with the cloud platform</p>
      </div>

    </div>
  </section>

  <!-- Community Resources -->
  <section class="help-section">
    <h3 class="section-title">Community Resources</h3>
    <div class="resources-grid">
      
      <a href="https://github.com/ap-unil-2025/course-materials/discussions" target="_blank" class="resource-item">
        <div class="resource-icon">💬</div>
        <h4>GitHub Discussions</h4>
        <p>Ask questions • Share solutions • Community help • Course announcements</p>
      </a>

      <a href="#" target="_blank" class="resource-item">
        <div class="resource-icon">🎮</div>
        <h4>Discord Community</h4>
        <p>Real-time chat • Study groups • Quick questions • Peer support</p>
      </a>

      <div class="resource-item">
        <div class="resource-icon">📚</div>
        <h4>Course Materials</h4>
        <p>All slides, code examples, and readings available in <a href="{{ '/weekly-materials' | relative_url }}">Weekly Hub</a></p>
      </div>


    </div>
  </section>

  <!-- Technical Support -->
  <section class="help-section">
    <h3 class="section-title">Technical Support</h3>
    <div class="tech-grid">
      
      <div class="tech-item">
        <div class="tech-header">
          <span class="tech-badge">Platform</span>
        </div>
        <h4>Nuvolos Cloud Issues</h4>
        <p>Login problems • Environment setup • File access • Performance issues</p>
        <div class="tech-actions">
          <a href="mailto:support@nuvolos.cloud" class="tech-link">Email Support</a>
          <a href="https://app.nuvolos.cloud/enroll/class/RshD654gzU4" target="_blank" class="tech-link">Re-enroll</a>
        </div>
      </div>

      <div class="tech-item">
        <div class="tech-header">
          <span class="tech-badge">GitHub</span>
        </div>
        <h4>Repository Access</h4>
        <p>Can't access course materials • GitHub organization issues • Permission problems</p>
        <div class="tech-actions">
          <a href="https://github.com/ap-unil-2025" target="_blank" class="tech-link">GitHub Org</a>
          <a href="mailto:anna.smirnova@unil.ch" class="tech-link">Request Access</a>
        </div>
      </div>

      <div class="tech-item">
        <div class="tech-header">
          <span class="tech-badge">Code</span>
        </div>
        <h4>Programming Help</h4>
        <p>Python syntax • Library issues • Debugging • Best practices</p>
        <div class="tech-actions">
          <a href="https://discord.gg/pr4q3QH2" target="_blank" class="tech-link">Join Discord</a>
          <a href="mailto:anna.smirnova@unil.ch" class="tech-link">Office Hours</a>
        </div>
      </div>

      <div class="tech-item">
        <div class="tech-header">
          <span class="tech-badge">Discord</span>
        </div>
        <h4>Community Chat</h4>
        <p>Real-time help • Peer support • Quick questions • Study groups</p>
        <div class="tech-actions">
          <a href="https://discord.gg/pr4q3QH2" target="_blank" class="tech-link">Join Discord</a>
          <a href="https://github.com/ap-unil-2025/course-materials/discussions" target="_blank" class="tech-link">GitHub Discussions</a>
        </div>
      </div>

    </div>
  </section>

  <!-- Getting Started Guide -->
  <section class="help-section">
    <h3 class="section-title">Quick Start Guide</h3>
    <div class="guide-steps">
      
      <div class="step-item">
        <div class="step-number">1</div>
        <div class="step-content">
          <h4>Enroll in Nuvolos</h4>
          <p>Click the <a href="https://app.nuvolos.cloud/enroll/class/RshD654gzU4" target="_blank">enrollment link</a> and follow setup instructions</p>
        </div>
      </div>

      <div class="step-item">
        <div class="step-number">2</div>
        <div class="step-content">
          <h4>Join GitHub Organization</h4>
          <p>Request access to <a href="https://github.com/ap-unil-2025" target="_blank">ap-unil-2025</a> for course materials</p>
        </div>
      </div>

      <div class="step-item">
        <div class="step-number">3</div>
        <div class="step-content">
          <h4>Join Discord Community</h4>
          <p>Connect with peers and TAs on <a href="https://discord.gg/pr4q3QH2" target="_blank">Discord</a> for real-time help</p>
        </div>
      </div>

      <div class="step-item">
        <div class="step-number">4</div>
        <div class="step-content">
          <h4>Access Weekly Materials</h4>
          <p>Visit the <a href="{{ '/weekly-materials' | relative_url }}">Weekly Hub</a> for lectures, assignments, and practice</p>
        </div>
      </div>

    </div>
  </section>

</div>

<style>
/* Help & Support Page Layout - Using Weekly Hub Patterns */
.help-support {
  max-width: 1200px;
  margin: 0 auto;
}

/* Support Banner */
.support-banner {
  background: linear-gradient(135deg, #7c3aed 0%, #5b21b6 100%);
  border-radius: 0.75rem;
  padding: 1.25rem 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 2.5rem;
  margin-top: 0;
  box-shadow: 0 4px 15px rgba(124, 58, 237, 0.2);
}

.support-content {
  display: flex;
  align-items: center;
  gap: 1.25rem;
}

.support-label {
  background: rgba(255, 255, 255, 0.2);
  color: white;
  padding: 0.4rem 0.8rem;
  border-radius: 0.375rem;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.05em;
}

.support-info h2 {
  color: white;
  font-size: 1.25rem;
  margin: 0 0 0.25rem 0;
}

.support-info p {
  color: rgba(255, 255, 255, 0.9);
  margin: 0;
  font-size: 0.875rem;
}

.support-btn {
  background: white;
  color: #7c3aed;
  padding: 0.6rem 1.25rem;
  border-radius: 0.5rem;
  text-decoration: none;
  font-weight: 600;
  font-size: 0.9rem;
  transition: all 0.2s ease;
  white-space: nowrap;
}

.support-btn:hover {
  transform: translateX(2px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
  text-decoration: none;
  color: #7c3aed;
}

/* Section Layout */
.help-section {
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
.contact-grid,
.resources-grid,
.tech-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1rem;
}

/* Contact Items */
.contact-item {
  background: var(--background-color);
  border: 1px solid var(--border-color);
  border-radius: 0.5rem;
  padding: 1rem;
  transition: all 0.2s ease;
  position: relative;
  overflow: hidden;
}

.contact-item:hover {
  border-color: var(--primary-color);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

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

.contact-item:hover::before {
  transform: scaleY(1);
}

.contact-item.priority {
  border-color: #10b981;
  background: linear-gradient(135deg, #f0fdf4 0%, var(--background-color) 100%);
}

.contact-header {
  margin-bottom: 0.5rem;
}

.contact-role {
  background: var(--primary-color);
  color: white;
  padding: 0.2rem 0.5rem;
  border-radius: 0.25rem;
  font-size: 0.75rem;
  font-weight: 600;
}

.office-hours {
  margin-top: 0.75rem;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.hours-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: var(--surface-color);
  padding: 0.25rem 0.5rem;
  border-radius: 0.25rem;
  font-size: 0.8rem;
}

.hours-day {
  font-weight: 500;
  color: var(--text-primary);
}

.hours-time {
  color: var(--text-secondary);
}

/* Resource Items */
.resource-item {
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

.resource-item:hover {
  border-color: var(--primary-color);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  text-decoration: none;
  color: inherit;
}

.resource-item::before {
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

.resource-item:hover::before {
  transform: scaleY(1);
}


.resource-icon {
  font-size: 1.5rem;
  margin-bottom: 0.75rem;
  display: block;
}

/* Tech Support Items */
.tech-item {
  background: var(--background-color);
  border: 1px solid var(--border-color);
  border-radius: 0.5rem;
  padding: 1rem;
  transition: all 0.2s ease;
  position: relative;
  overflow: hidden;
}

.tech-item:hover {
  border-color: var(--primary-color);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.tech-item::before {
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

.tech-item:hover::before {
  transform: scaleY(1);
}

.tech-header {
  margin-bottom: 0.5rem;
}

.tech-badge {
  background: var(--primary-color);
  color: white;
  padding: 0.2rem 0.5rem;
  border-radius: 0.25rem;
  font-size: 0.75rem;
  font-weight: 600;
}

.tech-actions {
  margin-top: 0.75rem;
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.tech-link {
  background: var(--surface-color);
  color: var(--text-secondary);
  padding: 0.25rem 0.5rem;
  border-radius: 0.25rem;
  text-decoration: none;
  font-size: 0.8rem;
  font-weight: 500;
  transition: all 0.2s ease;
}

.tech-link:hover {
  background: var(--primary-color);
  color: white;
  text-decoration: none;
}

/* Quick Start Guide */
.guide-steps {
  display: grid;
  gap: 1rem;
}

.step-item {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  background: var(--background-color);
  border: 1px solid var(--border-color);
  border-radius: 0.5rem;
  padding: 1rem;
  transition: all 0.2s ease;
  position: relative;
  overflow: hidden;
}

.step-item:hover {
  border-color: var(--primary-color);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.step-item::before {
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

.step-item:hover::before {
  transform: scaleY(1);
}

.step-number {
  background: var(--primary-color);
  color: white;
  width: 2rem;
  height: 2rem;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 0.9rem;
  flex-shrink: 0;
}

.step-content {
  flex: 1;
}

/* Common Content Styles */
.contact-item h4,
.resource-item h4,
.tech-item h4,
.step-content h4 {
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0 0 0.5rem 0;
  line-height: 1.3;
}

.contact-item p,
.resource-item p,
.tech-item p,
.step-content p {
  font-size: 0.8rem;
  color: var(--text-secondary);
  margin: 0;
  line-height: 1.4;
}

/* Mobile Responsive */
@media (max-width: 768px) {
  .support-banner {
    flex-direction: column;
    text-align: center;
    gap: 1rem;
  }
  
  .support-content {
    flex-direction: column;
  }
  
  .contact-grid,
  .resources-grid,
  .tech-grid {
    grid-template-columns: 1fr;
  }
  
  .step-item {
    flex-direction: column;
    text-align: center;
  }
  
  .step-number {
    align-self: center;
  }
}
</style>