#!/bin/bash

# Fast sync script for CI - skips Marp slide building

set -e

echo "🔄 Fast syncing content/ to Jekyll collections (no slide building)..."

# Create directories
mkdir -p docs/_lessons docs/_assignments docs/_projects docs/_slides/practice docs/_weeks

# Sync lessons
echo "📖 Syncing lessons..."
for week_dir in content/weeks/week-*; do
    if [ -d "$week_dir" ]; then
        week_num=$(basename "$week_dir")
        jekyll_name=$(echo "$week_num" | sed 's/week-/week/')
        
        # Copy lesson if exists
        if [ -f "$week_dir/lesson.md" ]; then
            cp "$week_dir/lesson.md" "docs/_lessons/${jekyll_name}-lesson.md"
        fi
        
        # Copy slides markdown (but don't build HTML)
        if [ -f "$week_dir/slides.md" ]; then
            cp "$week_dir/slides.md" "docs/_slides/practice/${week_num}_slides.md"
        fi
    fi
done

# Sync week definitions
echo "📋 Syncing week pages..."
if [ -d "content/week-definitions" ]; then
    for week_file in content/week-definitions/week*.md; do
        if [ -f "$week_file" ]; then
            cp "$week_file" "docs/_weeks/"
        fi
    done
fi

# Sync assignments
echo "📝 Syncing assignments..."
if [ -d "content/assignments" ]; then
    for file in content/assignments/*.md; do
        if [ -f "$file" ]; then
            filename=$(basename "$file")
            cp "$file" "docs/_assignments/$filename"
        fi
    done
fi

# Sync projects
echo "🎯 Syncing projects..."
if [ -d "content/projects" ]; then
    for file in content/projects/*.md; do
        if [ -f "$file" ]; then
            cp "$file" "docs/_projects/"
        fi
    done
fi

echo "✅ Fast sync complete!"