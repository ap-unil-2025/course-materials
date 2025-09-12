---
layout: default
---

<style>

/* Compact Header for Default Layout */
.weekly-header {
  text-align: center;
  margin-bottom: 1rem;
}

.weekly-header h1 {
  font-size: 2rem;
  color: var(--accent-color);
  margin: 0 0 0.5rem 0;
}

.weekly-header p {
  color: var(--text-secondary);
  margin: 0;
  font-size: 1rem;
}
</style>

<div class="weekly-hub">
  <!-- Compact header for weekly materials -->
  <div class="weekly-header">
    <h1>Weekly Materials</h1>
    <p>DSAP • HEC Lausanne • Fall Semester • Mondays 12:30–16:00 • Internef 263</p>
  </div>
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
        <p>Variables • Control flow • Strings • Git</p>
      </a>

      <a href="{{ '/week/week04' | relative_url }}" class="week-item">
        <div class="week-header">
          <span class="week-num">4</span>
          <span class="week-date">Oct 6</span>
        </div>
        <h4>Python Fundamentals II</h4>
        <p>Functions • Data structures • Recursion</p>
      </a>

      <a href="{{ '/week/week05' | relative_url }}" class="week-item special">
        <div class="week-header">
          <span class="week-num">5</span>
          <span class="week-date">Oct 13</span>
        </div>
        <h4>Special Session: Generative AI</h4>
        <p>LLMs • Autonomous agents (Anna)</p>
      </a>

      <a href="{{ '/week/week06' | relative_url }}" class="week-item">
        <div class="week-header">
          <span class="week-num">6</span>
          <span class="week-date">Oct 20</span>
        </div>
        <h4>Python Fundamentals III</h4>
        <p>OOP • Classes • Inheritance • Testing</p>
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
        <h4>Linear Regression</h4>
        <p>Supervised Learning • Gradient Descent</p>
      </a>

      <a href="{{ '/week/week08' | relative_url }}" class="week-item">
        <div class="week-header">
          <span class="week-num">8</span>
          <span class="week-date">Nov 3</span>
        </div>
        <h4>Classification</h4>
        <p>k-NN • Naive Bayes • Decision Trees</p>
      </a>

      <a href="{{ '/week/week09' | relative_url }}" class="week-item">
        <div class="week-header">
          <span class="week-num">9</span>
          <span class="week-date">Nov 10</span>
        </div>
        <h4>Unsupervised Machine Learning</h4>
        <p>k-Means • GMM • PCA • Clustering</p>
      </a>

      <a href="{{ '/week/week10' | relative_url }}" class="week-item">
        <div class="week-header">
          <span class="week-num">10</span>
          <span class="week-date">Nov 17</span>
        </div>
        <h4>Deep Learning Primer</h4>
        <p>MLPs • Backpropagation • TensorFlow</p>
      </a>
      
    </div>
  </section>

  <section class="course-section">
    <h3 class="section-title">Part III: Advanced Topics</h3>
    <div class="week-grid">

      <a href="{{ '/week/week11' | relative_url }}" class="week-item">
        <div class="week-header">
          <span class="week-num">11</span>
          <span class="week-date">Nov 24</span>
        </div>
        <h4>Best Practices in Data Science</h4>
        <p>Libraries • EDA • Feature Engineering</p>
      </a>

      <a href="{{ '/week/week12' | relative_url }}" class="week-item">
        <div class="week-header">
          <span class="week-num">12</span>
          <span class="week-date">Dec 1</span>
        </div>
        <h4>Introduction to HPC</h4>
        <p>Shared/Distributed Memory • Parallelization</p>
      </a>

      <a href="{{ '/week/week13' | relative_url }}" class="week-item project">
        <div class="week-header">
          <span class="week-num">13</span>
          <span class="week-date">Dec 8</span>
        </div>
        <h4>HPC with Python</h4>
        <p>Numba • JAX • Multi-threading</p>
      </a>

      <a href="{{ '/week/week14' | relative_url }}" class="week-item project">
        <div class="week-header">
          <span class="week-num">14</span>
          <span class="week-date">Dec 15</span>
        </div>
        <h4>Capstone Project Presentations</h4>
        <p>Final presentations • Course wrap-up</p>
      </a>
      
    </div>
  </section>


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
  margin-top: 0;
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

/* Disabled/Coming Soon Week Styling */
.week-item.disabled {
  opacity: 0.5;
  background: #f9fafb;
  border-color: #e5e7eb;
  cursor: not-allowed;
}

.week-item.disabled:hover {
  transform: none;
  border-color: #e5e7eb;
  box-shadow: none;
}

.week-item.disabled .week-header {
  opacity: 0.6;
}

.week-item.disabled h4,
.week-item.disabled p {
  color: #9ca3af;
}

.coming-soon-overlay {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: rgba(255, 255, 255, 0.95);
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  font-weight: 600;
  color: #6b7280;
  font-size: 0.875rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
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

<script>
// Immediate greying out for future weeks
(function() {
  // Test date: September 11, 2025
  const testDate = new Date('2025-09-11T00:00:00');
  const weekDates = {
      'week00': '2025-09-15',
      'week01': '2025-09-15', // Week 0-1 combined
      'week02': '2025-09-22',
      'week03': '2025-09-29',
      'week04': '2025-10-06',
      'week05': '2025-10-13',
      'week06': '2025-10-20',
      'week07': '2025-10-27',
      'week08': '2025-11-03',
      'week09': '2025-11-10',
      'week10': '2025-11-17',
      'week11': '2025-11-24',
      'week12': '2025-12-01',
      'week13': '2025-12-08',
      'week14': '2025-12-15'
  };

  // Check if week content should be available based on date
  function isWeekAvailable(weekId, weekDate) {
    // Always allow Week 0-1 (course introduction)
    if (weekId === 'week00' || weekId === 'week01') {
      return true;
    }
    
    const week = new Date(weekDate + 'T00:00:00');
    return testDate >= week;
  }

  // Extract week ID from href attribute
  function extractWeekId(href) {
    if (!href) return null;
    
    const weekMatch = href.match(/week(\d+)/);
    if (weekMatch) {
      const weekNum = weekMatch[1].padStart(2, '0');
      return 'week' + weekNum;
    }
    return null;
  }

  // Apply disabled styling to future weeks
  function applyWeekAvailability() {
    console.log('Applying week availability checks...');
    
    // Wait a bit more to ensure elements are ready
    const weekItems = document.querySelectorAll('.week-item');
    
    if (weekItems.length === 0) {
      console.warn('No week items found, retrying...');
      return false; // Indicate retry needed
    }
    
    console.log('Found', weekItems.length, 'week items');
    
    let processedCount = 0;
    
    weekItems.forEach(item => {
      // Skip holiday weeks - they have special styling already
      if (item.classList.contains('holiday')) {
        console.log('Skipping holiday week');
        return;
      }
      
      // Don't modify current week styling
      if (item.classList.contains('current')) {
        console.log('Skipping current week');
        return;
      }
      
      const href = item.getAttribute('href');
      const weekId = extractWeekId(href);
      
      if (!weekId) {
        console.warn('Could not extract week ID from href:', href);
        return;
      }
      
      const weekDate = weekDates[weekId];
      if (!weekDate) {
        console.warn('No date configured for week:', weekId);
        return;
      }
      
      console.log('Checking', weekId, 'with date', weekDate);
      
      if (!isWeekAvailable(weekId, weekDate)) {
        console.log('Disabling', weekId);
        
        // Remove any existing disabled state first
        item.classList.remove('disabled');
        const existingOverlay = item.querySelector('.coming-soon-overlay');
        if (existingOverlay) {
          existingOverlay.remove();
        }
        
        // Apply disabled state
        item.classList.add('disabled');
        item.style.pointerEvents = 'none';
        
        // Add coming soon overlay
        const overlay = document.createElement('div');
        overlay.className = 'coming-soon-overlay';
        overlay.textContent = 'Coming Soon';
        item.appendChild(overlay);
        
        processedCount++;
      } else {
        console.log('Week', weekId, 'is available');
        // Ensure it's not disabled if it should be available
        item.classList.remove('disabled');
        item.style.pointerEvents = '';
        const existingOverlay = item.querySelector('.coming-soon-overlay');
        if (existingOverlay) {
          existingOverlay.remove();
        }
      }
    });
    
    console.log('Processed', processedCount, 'weeks as unavailable');
    return true; // Indicate success
  }

  // Robust initialization with multiple fallbacks
  function initialize() {
    console.log('Initializing week availability system...');
    
    // Try to apply immediately
    if (applyWeekAvailability()) {
      return; // Success on first try
    }
    
    // Fallback 1: Wait for DOM
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', function() {
        console.log('DOM ready, applying week availability...');
        if (!applyWeekAvailability()) {
          // Fallback 2: Short delay after DOM
          setTimeout(function() {
            console.log('Delayed attempt after DOM ready...');
            applyWeekAvailability();
          }, 100);
        }
      });
    }
    
    // Fallback 3: Wait for full page load
    window.addEventListener('load', function() {
      console.log('Page loaded, ensuring week availability is applied...');
      applyWeekAvailability();
    });
    
    // Fallback 4: Delayed execution for slow-loading content
    setTimeout(function() {
      console.log('Final delayed check...');
      applyWeekAvailability();
    }, 500);
  }

  // Handle both initial load and AJAX navigation
  if (document.readyState === 'complete') {
    // Page already loaded
    initialize();
  } else {
    // Page still loading
    initialize();
  }
  
  // Re-run when content is loaded via AJAX (for the navigation system)
  document.addEventListener('DOMContentLoaded', function() {
    // Watch for content changes (for AJAX navigation)
    const observer = new MutationObserver(function(mutations) {
      let shouldRecheck = false;
      mutations.forEach(function(mutation) {
        if (mutation.type === 'childList' && mutation.addedNodes.length > 0) {
          // Check if week items were added
          for (let node of mutation.addedNodes) {
            if (node.nodeType === 1 && (node.classList.contains('week-item') || node.querySelector('.week-item'))) {
              shouldRecheck = true;
              break;
            }
          }
        }
      });
      
      if (shouldRecheck) {
        console.log('Content changed, reapplying week availability...');
        setTimeout(applyWeekAvailability, 100);
      }
    });
    
    // Start observing
    observer.observe(document.body, {
      childList: true,
      subtree: true
    });
  });
  
})();
</script>