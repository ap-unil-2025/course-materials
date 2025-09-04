# Content Directory - Easy Editing Structure

This directory contains all course materials in an easy-to-edit structure. **Edit files here, not in the `docs/` folder!**

## 📁 Directory Structure

```
content/
├── weeks/              # Weekly course materials
│   ├── week-00/
│   │   ├── lesson.md   # Lesson content (markdown)
│   │   └── slides.md   # Marp slides (markdown)
│   ├── week-01/
│   │   ├── lesson.md
│   │   └── slides.md
│   └── ...
├── projects/           # Project descriptions
│   ├── simclt.md
│   ├── econgames.md
│   └── ...
└── assignments/        # Course assignments
    ├── assignment-1-git-basics.md
    └── ...
```

## ✏️ How to Edit Content

### 1. Edit Files in `content/`
- **Lessons**: Edit `content/weeks/week-XX/lesson.md`
- **Slides**: Edit `content/weeks/week-XX/slides.md` (Marp format)
- **Projects**: Edit `content/projects/project-name.md`
- **Assignments**: Edit `content/assignments/assignment-name.md`

### 2. Sync to Jekyll
After editing, run the sync script to update the website:
```bash
./sync-content.sh
```

### 3. Preview Changes
Start local development server:
```bash
./serve-local.sh
```

### 4. Deploy
Commit and push to trigger automatic deployment:
```bash
git add content/
git commit -m "Update course materials"
git push
```

## 🔄 How It Works

1. **You edit** files in `content/` (easy structure)
2. **Sync script** copies content to Jekyll collections in `docs/`
3. **CI pipeline** builds slides and website
4. **Website** is automatically deployed

## 📝 File Formats

### Lessons (`lesson.md`)
Standard markdown with Jekyll front matter:
```yaml
---
title: "Week 1: Essential Tools"
date: 2025-01-27
---

# Your lesson content here...
```

### Slides (`slides.md`)
Marp-formatted slides:
```yaml
---
marp: true
theme: default
---

# Slide Title

Your slide content...

---

# Next Slide

More content...
```

### Projects & Assignments
Standard Jekyll markdown with front matter.

## 🚀 Benefits

- **Clean organization**: All materials organized by week
- **Easy editing**: Simple file structure, no Jekyll complexity
- **Automatic sync**: Script handles copying to Jekyll
- **Version control**: All source content tracked in git
- **CI/CD ready**: Push changes and site rebuilds automatically

## 💡 Tips

- Always edit in `content/`, never directly in `docs/`
- Run `./sync-content.sh` after making changes
- Use `./serve-local.sh` to preview locally
- The sync script also builds slides with Marp if installed
- Check the GitHub Actions for build status after pushing