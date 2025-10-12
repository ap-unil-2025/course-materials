# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a course materials website for Advanced Programming 2025 (AP-UNIL-2025), built with Jekyll and deployed via GitHub Pages at https://ap-unil-2025.github.io/course-materials/

## Content Architecture

**Critical**: Always edit content in `content/`, never directly in `docs/`. The repository uses a dual-directory architecture:

- **`content/`** - Source of truth for all course materials (edit here)
- **`docs/`** - Jekyll site (auto-generated, do not edit directly)

### Content Structure

```
content/
├── weeks/              # Weekly materials (lessons + slides)
│   ├── week-00/
│   │   ├── lesson.md   # Lesson content (markdown)
│   │   └── slides.md   # Marp presentation (markdown)
├── week-definitions/   # Week pages (TRUTH SOURCE for week metadata)
├── assignments/        # Course assignments
├── projects/          # Project descriptions
└── themes/            # Marp theme CSS
```

### Week Numbering

The repository uses a `week-XX` naming convention (e.g., week-00, week-01) which does NOT directly correspond to syllabus weeks. See `COURSE_MAPPING.md` for the alignment between syllabus weeks and website weeks.

## Common Commands

### Development Workflow

```bash
# Sync content from content/ to docs/ Jekyll collections
./sync-content.sh              # Full sync with Marp slide building
./sync-content.sh --fast       # Skip slide building (CI mode)
./sync-content.sh --slides     # Only rebuild slides

# Sync assignments specifically
./sync-assignments.sh

# Start local development server
./serve-local.sh               # Defaults to port 4000
./serve-local.sh 8080          # Custom port

# Access site at: http://localhost:4000/course-materials/
```

### Slide Building

Slides use Marp (Markdown Presentation Ecosystem) with a custom UNIL theme:

```bash
# Manual slide build for a specific week
npx @marp-team/marp-cli content/weeks/week-XX/slides.md \
  --config .marprc.yml \
  --theme content/themes/unil-theme.css \
  --html \
  --output docs/slides/practice/weekXX_slides.html
```

Template: `content/slide-template.md`

## Jekyll Collections

The site uses Jekyll collections defined in `docs/_config.yml`:

- `_weeks` - Week landing pages (sourced from `content/week-definitions/`)
- `_lessons` - Lesson content (synced from `content/weeks/week-XX/lesson.md`)
- `_slides` - Slide markdown (synced from `content/weeks/week-XX/slides.md`)
- `_assignments` - Assignment files (synced from `content/assignments/`)
- `_projects` - Project briefs (synced from `content/projects/`)

## Deployment

The site auto-deploys via GitHub Actions on push to `master`:

1. Workflow: `.github/workflows/build-content.yml`
2. Steps: Update submodules → Install Marp → Sync content → Build Jekyll → Deploy to Pages
3. Triggers on changes to `content/**`, `docs/**`, or workflow files

## Key Files

- `COURSE_MAPPING.md` - Alignment between syllabus weeks and website weeks
- `content/README.md` - Detailed editing guide for content directory
- `.marprc.yml` - Marp configuration (theme, HTML options)
- `docs/_config.yml` - Jekyll configuration

## Week Definitions

Week pages are ALWAYS sourced from `content/week-definitions/weekXX.md`. These files contain:
- Front matter with metadata (title, date, description)
- Links to lecture slides, TA slides, lessons, assignments
- Examples and references

Do NOT auto-generate week pages from lesson files. The `sync-content.sh` script has a disabled block for this legacy behavior.

## Python Solutions

Python solution files exist in some week directories (e.g., `content/weeks/week-03/contact_manager_v1_solutions.py`). These are instructor reference materials and should not be synced to the public-facing docs.
