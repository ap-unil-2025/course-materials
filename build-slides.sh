#!/bin/bash

# build-slides.sh - Build Marp slides for Advanced Programming course
# Usage: ./build-slides.sh [week] or ./build-slides.sh all

set -e

SLIDES_SOURCE="docs/_slides/practice"
SLIDES_OUTPUT="docs/slides/practice"

# Check if marp is installed
if ! command -v marp &> /dev/null; then
    echo "❌ Error: Marp CLI not found. Install with: npm install -g @marp-team/marp-cli"
    exit 1
fi

# Check if we're in the right directory
if [ ! -d "$SLIDES_SOURCE" ]; then
    echo "❌ Error: $SLIDES_SOURCE directory not found. Please run from project root."
    exit 1
fi

# Create output directory
mkdir -p "$SLIDES_OUTPUT"

# Build function
build_slide() {
    local md_file="$1"
    local base_name=$(basename "$md_file" .md)
    local output_file="$SLIDES_OUTPUT/${base_name}.html"
    
    echo "🎯 Building: $md_file → $output_file"
    marp "$md_file" \
        --html \
        --allow-local-files \
        --theme-set docs/_slides/themes/ \
        --output "$output_file"
}

# Main logic
if [ "$#" -eq 0 ] || [ "$1" = "all" ]; then
    echo "🚀 Building all Marp slides..."
    
    # Build all .md files in practice directory
    for md_file in "$SLIDES_SOURCE"/*.md; do
        if [ -f "$md_file" ]; then
            build_slide "$md_file"
        fi
    done
    
    echo "✅ Built $(ls "$SLIDES_SOURCE"/*.md 2>/dev/null | wc -l) slide sets"
    
elif [ "$1" ]; then
    # Build specific week
    WEEK_NUM="$1"
    MD_FILE="$SLIDES_SOURCE/week${WEEK_NUM}_slides.md"
    
    if [ ! -f "$MD_FILE" ]; then
        echo "❌ Error: Slide file not found: $MD_FILE"
        echo "Available slides:"
        ls "$SLIDES_SOURCE"/*.md 2>/dev/null || echo "  (no slides found)"
        exit 1
    fi
    
    echo "🚀 Building slides for week $WEEK_NUM..."
    build_slide "$MD_FILE"
    echo "✅ Built week $WEEK_NUM slides"
    
else
    echo "Usage: $0 [week_number|all]"
    echo "Examples:"
    echo "  $0 01        # Build week01_slides.md"
    echo "  $0 all       # Build all slides"
    echo "  $0           # Build all slides (default)"
    exit 1
fi

echo ""
echo "💡 Tips:"
echo "   - View slides at http://localhost:4000/course-materials/slides/practice/"
echo "   - Use './serve-local.sh' to start development server"
echo "   - Edit .md files in $SLIDES_SOURCE/"