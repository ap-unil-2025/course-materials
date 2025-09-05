# Week Definitions

This folder contains the ACTUAL week page definitions that will be copied to `docs/_weeks/`.

## Structure

Each week file should have these fields ONLY:

```yaml
---
title: "Week Title"
date: 2025-09-15
description: "Brief description"
topics:
  - Topic 1
  - Topic 2
lecture_slides: "#" or "/path/to/slides"
ta_slides: "/path/to/ta/slides" 
lesson: "/path/to/lesson"
assignment:
  title: "Assignment Name"
  link: "/path/to/assignment"
  description: "Assignment description"
examples:
  - title: "Example 1"
    link: "https://github.com/..."
references:
  - title: "Reference 1"
    link: "https://..."
    description: "Description"
---

Any additional content goes here (optional).
```

## Important Notes

- DO NOT include `layout:` - it's automatically set
- DO NOT include `week_number:` - not supported
- DO NOT include `ta_slides_2:` or `lesson_2:` - not supported
- For multiple slides/lessons, put links in the content section below the frontmatter

## Week Mapping

- week00.md = Week 1 in syllabus (Sep 15) - Course Overview  
- week01.md = Week 2 in syllabus (Sep 22) - Holiday
- week02.md = Week 3 in syllabus (Sep 29) - Python I + Git
- week03.md = Week 4 in syllabus (Oct 6) - Python II
- etc.