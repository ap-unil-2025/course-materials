#!/bin/bash

# sync-content.sh - Sync content/ to Jekyll collections for AP 2025 course
# This script copies content from the easy-to-edit content/ structure 
# to the Jekyll collections that build the website

set -e

echo "🔄 Syncing content/ to Jekyll collections..."

# Create directories if they don't exist
mkdir -p docs/_lessons docs/_assignments docs/_projects docs/_slides/practice docs/slides/practice

# Sync lessons from content/weeks/*/lesson.md to docs/_lessons/
echo "📖 Syncing lessons..."
for week_dir in content/weeks/week-*; do
    if [ -d "$week_dir" ]; then
        week_num=$(basename "$week_dir")
        
        # Sync lesson
        if [ -f "$week_dir/lesson.md" ]; then
            # Convert week-XX to weekXX format for Jekyll
            jekyll_name=$(echo "$week_num" | sed 's/week-/week/')
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
echo "   - $(find content/projects -name '*.md' | wc -l) projects synced"  
echo "   - $(find content/assignments -name '*.md' | wc -l) assignments synced"