#!/bin/bash

# serve-local.sh - Local development server for Advanced Programming course materials
# Usage: ./serve-local.sh [port]

set -e

PORT=${1:-4000}

echo "🚀 Starting local development server for AP 2025 course materials..."

# Check if we're in the right directory
if [ ! -f "docs/_config.yml" ]; then
    echo "❌ Error: docs/_config.yml not found. Please run from project root."
    exit 1
fi

# Check if bundle is installed
if ! command -v bundle &> /dev/null; then
    echo "❌ Error: Bundler not found. Install with: gem install bundler"
    exit 1
fi

# Navigate to docs directory
cd docs

# Install dependencies if Gemfile.lock doesn't exist
if [ ! -f "Gemfile.lock" ]; then
    echo "📦 Installing Ruby dependencies..."
    bundle install
fi

# Start Jekyll server
echo "🌍 Starting Jekyll server on http://localhost:$PORT/course-materials/"
echo "💡 Tips:"
echo "   - Edit files in docs/ to see live changes"
echo "   - Edit slides in docs/_slides/practice/ (rebuild with Marp)"
echo "   - Press Ctrl+C to stop server"
echo ""

# Use the development config and serve with live reload
bundle exec jekyll serve \
    --host 0.0.0.0 \
    --port $PORT \
    --baseurl "/course-materials" \
    --livereload \
    --incremental \
    --watch \
    --open-url