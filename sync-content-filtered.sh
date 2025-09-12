#!/bin/bash

# Date-aware sync script - only publishes content after lecture dates

set -e

echo "🔄 Updating submodules..."
git submodule update --init --recursive
git config --global pull.rebase false
git submodule foreach 'git pull origin main || git pull origin master || true'

# Run the date filter to generate manifest
echo "📅 Filtering content by date..."
python3 filter-content-by-date.py

# Read the manifest to know what to sync
if [ ! -f "content/.content-manifest.json" ]; then
    echo "❌ No content manifest found. Running regular sync."
    ./sync-content.sh
    exit 0
fi

echo "🔄 Syncing filtered content to Jekyll collections..."

# Create directories
mkdir -p docs/_lessons docs/_assignments docs/_projects docs/_slides/practice docs/slides/practice docs/_weeks

# Parse manifest using Python (more reliable than bash JSON parsing)
AVAILABLE_WEEKS=$(python3 -c "
import json
with open('content/.content-manifest.json') as f:
    data = json.load(f)
    for week in data['available_content']['weeks']:
        print(week)
")

AVAILABLE_ASSIGNMENTS=$(python3 -c "
import json
with open('content/.content-manifest.json') as f:
    data = json.load(f)
    for assignment in data['available_content']['assignments']:
        print(assignment)
")

# Sync lessons - only available weeks
echo "📖 Syncing available lessons..."
for week_name in $AVAILABLE_WEEKS; do
    week_dir="content/weeks/$week_name"
    if [ -d "$week_dir" ]; then
        jekyll_name=$(echo "$week_name" | sed 's/week-/week/')
        
        # Copy lesson if exists
        if [ -f "$week_dir/lesson.md" ]; then
            cp "$week_dir/lesson.md" "docs/_lessons/${jekyll_name}-lesson.md"
            echo "  ✅ $week_name/lesson.md → _lessons/${jekyll_name}-lesson.md"
        fi
        
        # Copy slides if exists  
        if [ -f "$week_dir/slides.md" ]; then
            cp "$week_dir/slides.md" "docs/_slides/practice/${week_name}_slides.md"
            echo "  ✅ $week_name/slides.md → _slides/practice/${week_name}_slides.md"
            
            # Build HTML slides with marp
            echo "  🎯 Building $week_name slides..."
            week_num_compact=$(echo "$week_name" | sed 's/week-/week/')
            npx @marp-team/marp-cli "$week_dir/slides.md" \
                --config .marprc.yml \
                --theme content/themes/unil-theme.css \
                --output "docs/slides/practice/${week_num_compact}_slides.html"
        fi
        
        # Also copy new slides if they exist
        if [ -f "$week_dir/slides_new.md" ]; then
            cp "$week_dir/slides_new.md" "docs/_slides/practice/${week_name}_slides_new.md"
            echo "  ✅ $week_name/slides_new.md → _slides/practice/${week_name}_slides_new.md"
            
            # Build HTML for new slides
            npx @marp-team/marp-cli "$week_dir/slides_new.md" \
                --config .marprc.yml \
                --theme content/themes/unil-theme.css \
                --output "docs/slides/practice/${week_num_compact}_slides_new.html"
        fi
    fi
done

# Sync week definitions - only for available weeks
echo "📋 Syncing available week pages..."
for week_name in $AVAILABLE_WEEKS; do
    week_num=$(echo "$week_name" | sed 's/week-0*//')
    week_file="content/week-definitions/week$(printf "%02d" $week_num).md"
    
    if [ -f "$week_file" ]; then
        filename=$(basename "$week_file")
        cp "$week_file" "docs/_weeks/$filename"
        echo "  ✅ Synced week page: $filename"
    fi
done

# Sync assignments - only available ones
echo "📝 Syncing available assignments..."
for assignment_name in $AVAILABLE_ASSIGNMENTS; do
    assignment_file="content/assignments/$assignment_name"
    if [ -f "$assignment_file" ]; then
        cp "$assignment_file" "docs/_assignments/$assignment_name"
        echo "  ✅ $assignment_name"
    fi
done

# Projects are always available (no date restriction)
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

# Create a "coming soon" page for future content
echo "📝 Creating coming soon notice..."
cat > docs/_includes/coming-soon.html << 'EOF'
<div class="alert alert-info" style="margin: 20px 0; padding: 15px; background: #e3f2fd; border-left: 4px solid #2196F3;">
  <strong>🔒 Future Content</strong><br>
  Content for upcoming weeks will be released after each lecture date. Check back soon!
</div>
EOF

# Update the homepage to show available vs upcoming content
python3 -c "
import json
from datetime import datetime

with open('content/.content-manifest.json') as f:
    data = json.load(f)
    
print('📊 Content Status:')
print(f'  Available weeks: {len(data[\"available_content\"][\"weeks\"])}')
print(f'  Available assignments: {len(data[\"available_content\"][\"assignments\"])}')
print(f'  Generated: {data[\"generated\"]}')
"

echo "✅ Filtered content sync complete!"