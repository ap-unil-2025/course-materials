#!/bin/bash

# Sync assignments from content folder to docs folder
echo "Syncing assignments from content/ to docs/_assignments/"

# Create docs/_assignments directory if it doesn't exist
mkdir -p docs/_assignments

# Remove old assignments from docs
rm -f docs/_assignments/*.md

# Copy all assignment markdown files from content to docs
cp content/assignments/*.md docs/_assignments/

# Don't copy the github-classroom-templates folder
# Those stay in content/ for instructor use only

echo "✅ Assignments synced successfully!"
echo ""
echo "Files synced:"
ls -la docs/_assignments/*.md | awk '{print "  - " $NF}'

echo ""
echo "GitHub Classroom templates remain in:"
echo "  content/assignments/github-classroom-templates/"