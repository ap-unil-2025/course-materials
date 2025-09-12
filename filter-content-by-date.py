#!/usr/bin/env python3
"""
Filter content based on lecture dates.
Only content with dates <= today will be synced to the docs folder.
"""

import os
import re
import shutil
from datetime import datetime, date
from pathlib import Path
import frontmatter
import json

def parse_week_date(week_def_path):
    """Extract date from week definition file."""
    with open(week_def_path, 'r') as f:
        content = f.read()
        
    # Try to find date in frontmatter
    try:
        post = frontmatter.loads(content)
        if 'date' in post.metadata:
            return datetime.strptime(post.metadata['date'], '%Y-%m-%d').date()
        if 'lecture_date' in post.metadata:
            return datetime.strptime(post.metadata['lecture_date'], '%Y-%m-%d').date()
    except:
        pass
    
    # Try to find date in content (format: October 6, 2025)
    date_pattern = r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2}),\s+(\d{4})'
    match = re.search(date_pattern, content)
    if match:
        month_name, day, year = match.groups()
        month_num = {
            'January': 1, 'February': 2, 'March': 3, 'April': 4,
            'May': 5, 'June': 6, 'July': 7, 'August': 8,
            'September': 9, 'October': 10, 'November': 11, 'December': 12
        }[month_name]
        return date(int(year), month_num, int(day))
    
    return None

def get_lecture_dates():
    """Get all lecture dates from week definitions."""
    dates = {}
    
    # Week 0-1 (combined) - September 16, 2025
    dates['week00'] = date(2025, 9, 16)
    dates['week01'] = date(2025, 9, 16)
    
    # Week 2 is holiday - no content
    dates['week02'] = date(2025, 9, 23)  # Holiday week
    
    # Week 3 - October 6, 2025
    dates['week03'] = date(2025, 10, 6)
    
    # Week 4 - October 13, 2025
    dates['week04'] = date(2025, 10, 13)
    
    # Week 5 - October 20, 2025
    dates['week05'] = date(2025, 10, 20)
    
    # Week 6 - October 27, 2025
    dates['week06'] = date(2025, 10, 27)
    
    # Week 7 - November 3, 2025
    dates['week07'] = date(2025, 11, 3)
    
    # Week 8 - November 10, 2025
    dates['week08'] = date(2025, 11, 10)
    
    # Week 9 - November 17, 2025
    dates['week09'] = date(2025, 11, 17)
    
    # Week 10 - November 24, 2025
    dates['week10'] = date(2025, 11, 24)
    
    # Week 11 - December 1, 2025
    dates['week11'] = date(2025, 12, 1)
    
    # Week 12 - December 8, 2025
    dates['week12'] = date(2025, 12, 8)
    
    # Week 13 - December 15, 2025
    dates['week13'] = date(2025, 12, 15)
    
    # Week 14 - December 22, 2025
    dates['week14'] = date(2025, 12, 22)
    
    return dates

def should_publish_content(week_num, lecture_dates, today=None):
    """Check if content for a given week should be published."""
    if today is None:
        today = date.today()
    
    # Always publish week 0 and 1 (intro content)
    if week_num in ['week00', 'week01', 'week0', 'week1']:
        return True
    
    # Format week number properly
    if week_num.startswith('week'):
        week_key = week_num
    else:
        week_key = f'week{int(week_num):02d}'
    
    if week_key in lecture_dates:
        lecture_date = lecture_dates[week_key]
        return today >= lecture_date
    
    return False

def filter_content(content_dir='content', docs_dir='docs', today=None):
    """Filter and sync content based on dates."""
    if today is None:
        today = date.today()
    
    lecture_dates = get_lecture_dates()
    
    # Track what content is available
    available_content = {
        'weeks': [],
        'assignments': [],
        'practice_sessions': []
    }
    
    print(f"📅 Filtering content for date: {today}")
    print(f"━" * 50)
    
    # Process weeks
    weeks_path = Path(content_dir) / 'weeks'
    if weeks_path.exists():
        for week_dir in sorted(weeks_path.iterdir()):
            if week_dir.is_dir():
                week_name = week_dir.name
                week_num = week_name.replace('week-', 'week')
                
                if should_publish_content(week_num, lecture_dates, today):
                    available_content['weeks'].append(week_name)
                    print(f"✅ Publishing: {week_name}")
                else:
                    print(f"⏳ Holding: {week_name} (not yet available)")
    
    # Process assignments - release one week before the session
    assignments_path = Path(content_dir) / 'assignments'
    if assignments_path.exists():
        for assignment_file in assignments_path.iterdir():
            if assignment_file.suffix == '.md':
                # Check if it's a week-specific assignment
                if 'week' in assignment_file.stem.lower():
                    week_match = re.search(r'week(\d+)', assignment_file.stem.lower())
                    if week_match:
                        week_num = f'week{int(week_match.group(1)):02d}'
                        if week_num in lecture_dates:
                            # Release assignment one week before the lecture
                            assignment_date = lecture_dates[week_num]
                            from datetime import timedelta
                            release_date = assignment_date - timedelta(days=7)
                            
                            if today >= release_date:
                                available_content['assignments'].append(assignment_file.name)
                                print(f"✅ Publishing assignment: {assignment_file.name}")
                            else:
                                print(f"⏳ Holding assignment: {assignment_file.name} (releases {release_date})")
                        else:
                            # No specific week, always publish
                            available_content['assignments'].append(assignment_file.name)
                else:
                    # Non-week specific content (like setup guides)
                    available_content['assignments'].append(assignment_file.name)
    
    # Process practice sessions
    practice_path = Path(content_dir) / 'practice-sessions'
    if practice_path.exists():
        for session_file in practice_path.iterdir():
            if session_file.suffix == '.md':
                week_match = re.search(r'week-?(\d+)', session_file.stem.lower())
                if week_match:
                    week_num = f'week{int(week_match.group(1)):02d}'
                    if should_publish_content(week_num, lecture_dates, today):
                        available_content['practice_sessions'].append(session_file.name)
                        print(f"✅ Publishing practice: {session_file.name}")
                    else:
                        print(f"⏳ Holding practice: {session_file.name}")
    
    # Save manifest of available content
    manifest_path = Path(content_dir) / '.content-manifest.json'
    with open(manifest_path, 'w') as f:
        json.dump({
            'generated': today.isoformat(),
            'available_content': available_content
        }, f, indent=2)
    
    print(f"\n📝 Manifest saved to {manifest_path}")
    print(f"   Available weeks: {len(available_content['weeks'])}")
    print(f"   Available assignments: {len(available_content['assignments'])}")
    print(f"   Available practice sessions: {len(available_content['practice_sessions'])}")
    
    return available_content

def main():
    """Main entry point."""
    import sys
    
    # Allow testing with a specific date
    if len(sys.argv) > 1:
        test_date = datetime.strptime(sys.argv[1], '%Y-%m-%d').date()
        print(f"🧪 Testing with date: {test_date}")
        filter_content(today=test_date)
    else:
        filter_content()

if __name__ == '__main__':
    main()