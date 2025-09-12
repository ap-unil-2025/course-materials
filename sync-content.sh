#!/bin/bash

# Simple sync script - just copy files, no fancy processing

set -e

echo "🔄 Syncing content/ to Jekyll collections..."

# Create directories
mkdir -p docs/_lessons docs/_assignments docs/_projects docs/_slides/practice docs/slides/practice docs/_weeks

# Sync lessons
echo "📖 Syncing lessons..."
for week_dir in content/weeks/week-*; do
    if [ -d "$week_dir" ]; then
        week_num=$(basename "$week_dir")
        jekyll_name=$(echo "$week_num" | sed 's/week-/week/')
        
        # Copy lesson if exists
        if [ -f "$week_dir/lesson.md" ]; then
            cp "$week_dir/lesson.md" "docs/_lessons/${jekyll_name}-lesson.md"
            echo "  ✅ $week_num/lesson.md → _lessons/${jekyll_name}-lesson.md"
        fi
        
        # Copy slides if exists  
        if [ -f "$week_dir/slides.md" ]; then
            cp "$week_dir/slides.md" "docs/_slides/practice/${week_num}_slides.md"
            echo "  ✅ $week_num/slides.md → _slides/practice/${week_num}_slides.md"
            
            # Build HTML slides with marp
            echo "  🎯 Building $week_num slides..."
            week_num_compact=$(echo "$week_num" | sed 's/week-/week/')
            npx @marp-team/marp-cli "$week_dir/slides.md" \
                --config .marprc.yml \
                --theme content/themes/unil-theme.css \
                --output "docs/slides/practice/${week_num_compact}_slides.html"
        fi
    fi
done

# Sync week definitions - THIS IS THE TRUTH SOURCE, ALWAYS USE THESE
echo "📋 Syncing week pages from week-definitions..."
if [ -d "content/week-definitions" ]; then
    for week_file in content/week-definitions/week*.md; do
        if [ -f "$week_file" ]; then
            filename=$(basename "$week_file")
            cp "$week_file" "docs/_weeks/$filename"
            echo "  ✅ Synced week page: $filename"
        fi
    done
fi

# DISABLED: Auto-generation from lessons - we only use week-definitions now
if false; then  # This whole block is disabled
for week_dir in content/weeks/week-*; do
    if [ -d "$week_dir" ]; then
        week_num=$(basename "$week_dir")
        jekyll_name=$(echo "$week_num" | sed 's/week-/week/')
        week_file="docs/_weeks/${jekyll_name}.md"
        week_num_compact=$(echo "$week_num" | sed 's/week-/week/')
        
        # Extract basic info from lesson if it exists
        if [ -f "$week_dir/lesson.md" ]; then
            # Keep the title exactly as it appears after "title: " (including quotes if present)
            title=$(grep '^title:' "$week_dir/lesson.md" 2>/dev/null | head -1 | sed 's/^title: *//' || echo "\"Week $jekyll_name\"")
            date=$(grep '^date:' "$week_dir/lesson.md" 2>/dev/null | head -1 | sed 's/^date: *//' || echo "2025-09-01")
            # Keep the description exactly as it appears after "summary: " (including quotes if present)
            desc=$(grep '^summary:' "$week_dir/lesson.md" 2>/dev/null | head -1 | sed 's/^summary: *//' || echo "\"Weekly materials\"")
        else
            title="Week: $week_num"
            date="2025-09-01"
            desc="Weekly materials for $jekyll_name"
        fi
        
        # Always create/overwrite week page to keep in sync
        cat > "$week_file" << EOF
---
title: $title
date: $date
description: $desc
lecture_slides: "#"
ta_slides: "/course-materials/slides/practice/${week_num_compact}_slides.html"
lesson: "/course-materials/lessons/${jekyll_name}-lesson.html"
assignment:
  title: "Assignment"
  link: "#"
  description: "Weekly assignment"
examples:
  - title: "Course Materials Repository"
    link: "https://github.com/ap-unil-2025/course-materials"
references:
  - title: "Course Resources"
    link: "https://github.com/ap-unil-2025/course-materials"
    description: "Main course repository with all materials"
---

## Week Overview

This week's materials include lecture content, practice exercises, and assignments designed to build your understanding of the covered topics.

### Getting Started

1. Review the lesson guide for detailed explanations
2. Go through the practice slides for hands-on examples  
3. Complete the weekly assignment
4. Use the course repository for additional examples and resources

### Need Help?

- Check the course discussion forum
- Attend office hours
- Review previous week's materials if needed
EOF
        echo "  ✅ Synced week page: ${week_file}"
    fi
done
fi  # End of disabled block

# Sync projects
echo "🚀 Syncing projects..."
if [ -d "content/projects" ]; then
    for project_file in content/projects/*.md; do
        if [ -f "$project_file" ]; then
            filename=$(basename "$project_file")
            cp "$project_file" "docs/_projects/$filename"
            echo "  ✅ $filename"
        fi
    done
fi

# Sync assignments
echo "📝 Syncing assignments..."
if [ -d "content/assignments" ]; then
    for assignment_file in content/assignments/*.md; do
        if [ -f "$assignment_file" ]; then
            filename=$(basename "$assignment_file")
            cp "$assignment_file" "docs/_assignments/$filename"
            echo "  ✅ $filename"
        fi
    done
fi

echo "✅ Content sync complete!"