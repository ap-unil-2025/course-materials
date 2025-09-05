---
layout: page
title: Course Curriculum
permalink: /curriculum/
---

<style>
.curriculum-document {
  max-width: 900px;
  margin: 0 auto;
  padding: 2rem;
}

.curriculum-week {
  margin-bottom: 3rem;
  border-bottom: 1px solid #e0e0e0;
  padding-bottom: 2rem;
}

.curriculum-week:last-child {
  border-bottom: none;
}

.week-header {
  background: #f5f5f5;
  padding: 1rem;
  border-left: 4px solid #6366f1;
  margin-bottom: 1.5rem;
}

.week-header h2 {
  margin: 0;
  color: #333;
}

.week-meta {
  display: flex;
  gap: 2rem;
  margin-top: 0.5rem;
  font-size: 0.9rem;
  color: #666;
}

.section-title {
  font-weight: bold;
  color: #444;
  margin-top: 1.5rem;
  margin-bottom: 0.5rem;
  font-size: 1.1rem;
}

.topics-list {
  list-style-type: disc;
  margin-left: 1.5rem;
  margin-bottom: 1rem;
}

.materials-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin-top: 1rem;
}

.material-link {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 4px;
  text-decoration: none;
  color: #333;
  transition: all 0.2s;
}

.material-link:hover {
  background: #6366f1;
  color: white;
  border-color: #6366f1;
}

@media print {
  .material-link {
    background: none;
    border: none;
    padding: 0;
    color: #333;
    text-decoration: underline;
  }
  
  .week-header {
    break-inside: avoid;
  }
  
  .curriculum-week {
    break-inside: avoid-page;
  }
}
</style>

<div class="curriculum-document">

# Advanced Programming 2025 - Complete Curriculum

This document contains the complete curriculum for the Advanced Programming course at UNIL, Spring 2025. Each week covers specific topics with associated lectures, practice sessions, and assignments.

---

{% for week in site.weeks %}
<div class="curriculum-week">
  <div class="week-header">
    <h2>{{ week.title }}</h2>
    <div class="week-meta">
      <span>📅 {{ week.date | date: "%B %d, %Y" }}</span>
      <span>📚 Week {{ week.url | split: '/' | last | replace: 'week', '' }}</span>
    </div>
  </div>

  {% if week.description %}
  <div class="section-title">Overview</div>
  <p>{{ week.description }}</p>
  {% endif %}

  {% assign week_num = week.url | split: '/' | last %}
  {% assign lesson = site.lessons | where_exp: "l", "l.url contains week_num" | first %}
  
  {% if lesson %}
    {% if lesson.topics %}
    <div class="section-title">Topics Covered</div>
    <ul class="topics-list">
      {% for topic in lesson.topics %}
      <li>{{ topic }}</li>
      {% endfor %}
    </ul>
    {% endif %}
    
    {% if lesson.objectives %}
    <div class="section-title">Learning Objectives</div>
    <ul class="topics-list">
      {% for objective in lesson.objectives %}
      <li>{{ objective }}</li>
      {% endfor %}
    </ul>
    {% endif %}
  {% endif %}

  <div class="section-title">Course Materials</div>
  <div class="materials-grid">
    {% if week.lesson %}
    <a href="{{ week.lesson }}" class="material-link">
      📖 Lesson Guide
    </a>
    {% endif %}
    
    {% if week.ta_slides %}
    <a href="{{ week.ta_slides }}" class="material-link">
      🎯 Practice Slides
    </a>
    {% endif %}
    
    {% if week.lecture_slides and week.lecture_slides != "#" %}
    <a href="{{ week.lecture_slides }}" class="material-link">
      📊 Lecture Slides
    </a>
    {% endif %}
    
    {% if week.assignment and week.assignment.link != "#" %}
    <a href="{{ week.assignment.link }}" class="material-link">
      ✏️ Assignment
    </a>
    {% endif %}
  </div>

  {% if week.references %}
  <div class="section-title">Additional Resources</div>
  <ul class="topics-list">
    {% for ref in week.references %}
    <li><a href="{{ ref.link }}">{{ ref.title }}</a>{% if ref.description %} - {{ ref.description }}{% endif %}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>
{% endfor %}

---

## Final Projects

The course culminates in a final project where students can choose from several predefined projects or propose their own topic. Projects should demonstrate the programming skills and best practices learned throughout the course.

### Available Projects
{% for project in site.projects %}
- **[{{ project.title }}]({{ project.url }})**: {{ project.description }}
{% endfor %}

---

## Course Resources

- **Course Repository**: [github.com/ap-unil-2025/course-materials](https://github.com/ap-unil-2025/course-materials)
- **Discussion Forum**: Available through Moodle
- **Office Hours**: Tuesdays 14:00-16:00, Thursdays 10:00-12:00

---

## Assessment

- Weekly Assignments: 40%
- Midterm Project: 25%  
- Final Project: 35%

All assignments must be submitted through GitHub Classroom by the specified deadlines.

</div>

<script>
// Add print button
document.addEventListener('DOMContentLoaded', function() {
  const header = document.querySelector('.curriculum-document h1');
  const printBtn = document.createElement('button');
  printBtn.innerHTML = '🖨️ Print / Save as PDF';
  printBtn.style.cssText = 'float: right; padding: 0.5rem 1rem; background: #6366f1; color: white; border: none; border-radius: 4px; cursor: pointer;';
  printBtn.onclick = function() { window.print(); };
  header.parentNode.insertBefore(printBtn, header);
});
</script>