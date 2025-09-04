#!/bin/bash

# sync-content.sh - Sync content/ to Jekyll collections for AP 2025 course
# This script copies content from the easy-to-edit content/ structure 
# to the Jekyll collections that build the website

set -e

# Function to create unified week pages
create_week_page() {
    local week_dir="$1"
    local jekyll_name="$2"
    local week_file="docs/_weeks/${jekyll_name}.md"
    
    # Extract metadata from lesson.md if it exists
    local title="Week: $(basename "$week_dir")"
    local date=""
    local description=""
    local topics=""
    
    if [ -f "$week_dir/lesson.md" ]; then
        # Extract title from lesson frontmatter
        title=$(grep '^title:' "$week_dir/lesson.md" | head -1 | sed 's/title: *//' | tr -d '"')
        date=$(grep '^date:' "$week_dir/lesson.md" | head -1 | sed 's/date: *//')
        description=$(grep '^summary:' "$week_dir/lesson.md" | head -1 | sed 's/summary: *//' | tr -d '"')
        
        # Extract topics from lesson frontmatter if they exist
        if grep -q '^topics:' "$week_dir/lesson.md"; then
            topics=$(sed -n '/^topics:/,/^[^[:space:]-]/p' "$week_dir/lesson.md" | grep '^ *-' | sed 's/^ *- */  - /')
        fi
    fi
    
    # Create the unified week page with clean YAML
    cat > "$week_file" << 'FRONTMATTER'
---
title: "TITLE_PLACEHOLDER"
date: DATE_PLACEHOLDER
description: "DESC_PLACEHOLDER"
lecture_slides: "#"
ta_slides: "SLIDES_PLACEHOLDER"
lesson: "LESSON_PLACEHOLDER"
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
FRONTMATTER

    # Replace placeholders with actual values
    sed -i "s|TITLE_PLACEHOLDER|${title:-Week $jekyll_name}|g" "$week_file"
    sed -i "s|DATE_PLACEHOLDER|${date:-$(date +%Y-%m-%d)}|g" "$week_file"
    sed -i "s|DESC_PLACEHOLDER|${description:-Weekly materials for $jekyll_name}|g" "$week_file"
    sed -i "s|SLIDES_PLACEHOLDER|/slides/practice/${week_dir##*/}_slides.html|g" "$week_file"
    sed -i "s|LESSON_PLACEHOLDER|/lessons/${jekyll_name}-lesson|g" "$week_file"
    
    # Add the content section
    cat >> "$week_file" << 'CONTENT'

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
CONTENT

    echo "  ✅ Created unified week page: ${week_file}"
}

echo "🔄 Syncing content/ to Jekyll collections..."

# Create directories if they don't exist
mkdir -p docs/_lessons docs/_assignments docs/_projects docs/_slides/practice docs/slides/practice docs/_weeks

# Sync lessons from content/weeks/*/lesson.md to docs/_lessons/
echo "📖 Syncing lessons and creating unified week pages..."
for week_dir in content/weeks/week-*; do
    if [ -d "$week_dir" ]; then
        week_num=$(basename "$week_dir")
        jekyll_name=$(echo "$week_num" | sed 's/week-/week/')
        
        # Sync lesson
        if [ -f "$week_dir/lesson.md" ]; then
            cp "$week_dir/lesson.md" "docs/_lessons/${jekyll_name}-lesson.md"
            echo "  ✅ $week_num/lesson.md → _lessons/${jekyll_name}-lesson.md"
        fi
        
        # Sync slides (copy to both _slides for source and process with Marp)
        if [ -f "$week_dir/slides.md" ]; then
            # Copy source slides
            cp "$week_dir/slides.md" "docs/_slides/practice/${week_num}_slides.md"
            echo "  ✅ $week_num/slides.md → _slides/practice/${week_num}_slides.md"
            
            # Generate HTML slides if marp is available
            if command -v marp &> /dev/null; then
                echo "  🎯 Building $week_num slides with Marp..."
                marp "$week_dir/slides.md" \
                    --html \
                    --allow-local-files \
                    --output "docs/slides/practice/${week_num}_slides.html"
                echo "  ✅ Generated docs/slides/practice/${week_num}_slides.html"
            else
                echo "  ⚠️  Marp not found - skipping HTML generation for $week_num"
            fi
        fi
        
        # Create unified week page
        echo "  📋 Creating unified week page for $week_num..."
        create_week_page "$week_dir" "$jekyll_name"
    fi
done

# Sync projects
echo "🚀 Syncing projects..."
if [ -d "content/projects" ]; then
    for project_file in content/projects/*.md; do
        if [ -f "$project_file" ]; then
            filename=$(basename "$project_file")
            cp "$project_file" "docs/_projects/$filename"
            echo "  ✅ projects/$filename → _projects/$filename"
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
            echo "  ✅ assignments/$filename → _assignments/$filename"
        fi
    done
fi

echo ""
echo "✅ Content sync complete!"
echo ""
echo "💡 Usage tips:"
echo "   - Edit files in content/ directory (easy structure)"
echo "   - Run ./sync-content.sh to update Jekyll collections"
echo "   - Use ./serve-local.sh to preview changes"
echo "   - Commit and push to deploy via CI"
echo ""

# Show summary
echo "📊 Sync summary:"
echo "   - $(find content/weeks -name 'lesson.md' | wc -l) lessons synced"
echo "   - $(find content/weeks -name 'slides.md' | wc -l) slide sets synced"
echo "   - $(find docs/_weeks -name '*.md' | wc -l) unified week pages created"
echo "   - $(find content/projects -name '*.md' | wc -l) projects synced"  
echo "   - $(find content/assignments -name '*.md' | wc -l) assignments synced"