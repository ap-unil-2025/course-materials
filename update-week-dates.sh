#!/bin/bash

# Update all week dates to match the actual course schedule

echo "📅 Updating week dates..."

# Week 0-1 are combined on September 16
sed -i '' 's/^date: 2025-09-15$/date: 2025-09-16/' content/week-definitions/week00.md
sed -i '' 's/^date: 2025-09-01$/date: 2025-09-16/' content/week-definitions/week01.md

# Week 2 is September 23 (holiday week)
sed -i '' 's/^date: 2025-09-22$/date: 2025-09-23/' content/week-definitions/week02.md

# Week 3 is October 6 (already correct)

# Week 4 is October 13 (already correct)

# Week 5 is October 20 (already correct)

# Week 6 is October 27
sed -i '' 's/^date: 2025-10-20$/date: 2025-10-27/' content/week-definitions/week06.md

# Week 7 is November 3
sed -i '' 's/^date: 2025-10-27$/date: 2025-11-03/' content/week-definitions/week07.md

# Weeks 8-14 are already correct

echo "✅ Dates updated!"
echo ""
echo "Current dates:"
grep "^date:" content/week-definitions/week*.md | sort