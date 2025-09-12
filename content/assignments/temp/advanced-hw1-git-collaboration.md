---
layout: assignment
title: "Advanced HW1: Git Collaboration & DevOps Challenge"
assignment_number: "HW1"
due_date: 2025-09-22 23:59:00
points: 150
difficulty: "Advanced"
estimated_time: "6-8 hours"
github_classroom_url: "https://classroom.github.com/a/advanced-hw1"
starter_repo: "ap2025-advanced-hw1-starter"
topics:
  - "Advanced Git workflows"
  - "CI/CD pipelines"
  - "Collaborative development"
  - "Code review practices"
bonus: true
status: "open"
---

## Overview

**This is an OPTIONAL grade booster assignment** worth 150 bonus points. You will simulate a real-world development team scenario, managing a multi-contributor project with proper Git workflows, automated testing, and deployment practices.

## The Challenge: "GitFlow Simulator"

You are part of a 3-person development team (simulated by you playing different roles) working on a Python package. You must demonstrate professional Git workflows, handle complex merges, set up CI/CD, and manage releases.

## Learning Objectives

- Master advanced Git operations (cherry-pick, rebase, bisect)
- Implement GitFlow or GitHub Flow workflows
- Set up automated testing with GitHub Actions
- Practice code review and PR management
- Handle complex merge scenarios and hotfixes

## Part 1: Repository Setup & Workflow (30 points)

### Initial Setup
1. Fork the starter repository
2. Set up branch protection rules on `main`
3. Configure required reviews (even if reviewing yourself)
4. Create these branches:
   - `develop` - integration branch
   - `feature/*` - feature branches
   - `hotfix/*` - emergency fixes
   - `release/*` - release preparation

### Required Workflow Documentation
Create `CONTRIBUTING.md` with:
- Branch naming conventions
- Commit message format (use conventional commits)
- PR template
- Code review checklist

## Part 2: Feature Development Simulation (40 points)

Simulate a 3-developer team by using different Git configurations:

```bash
# Developer 1 - Alice
git config user.name "Alice Developer"
git config user.email "alice@team.com"

# Developer 2 - Bob
git config user.name "Bob Engineer"
git config user.email "bob@team.com"

# Developer 3 - Charlie
git config user.name "Charlie Coder"
git config user.email "charlie@team.com"
```

### Required Features to Implement

Each "developer" must create at least one feature:

1. **Alice**: Implement a `Calculator` class with basic operations
2. **Bob**: Add advanced math functions (power, sqrt, factorial)
3. **Charlie**: Create a CLI interface for the calculator

### Collaboration Requirements
- Each feature in its own branch
- Proper PR descriptions with:
  - What changed
  - Why it changed
  - How to test
  - Screenshots/examples
- At least 2 commits per feature
- Simulate code review comments and responses

## Part 3: Conflict Resolution & Advanced Operations (35 points)

### Create and Resolve Conflicts
1. **Intentional Conflict**: Have two "developers" modify the same function differently
2. **Three-way Merge**: Create a scenario requiring a three-way merge
3. **Cherry-pick Operation**: Cherry-pick a specific commit from one branch to another
4. **Interactive Rebase**: Clean up commit history before merging

### Git Bisect Challenge
1. Introduce a "bug" in commit 5 of a 10-commit series
2. Use `git bisect` to find the problematic commit
3. Document the process in `BISECT_LOG.md`

## Part 4: CI/CD Pipeline (25 points)

Create `.github/workflows/ci.yml` with:

```yaml
name: CI Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      # Your implementation here
      # Must include:
      # - Python setup
      # - Dependency installation
      # - Linting (flake8 or ruff)
      # - Testing (pytest)
      # - Coverage report
```

### Requirements
- Tests must pass for PR to be mergeable
- Minimum 80% code coverage
- Linting must pass
- Automatic version bumping on merge to main

## Part 5: Release Management (20 points)

### Create a Release
1. Create release branch from develop
2. Update version numbers
3. Generate CHANGELOG.md (can be manual)
4. Create GitHub release with:
   - Release notes
   - Binary artifacts
   - Tagged version

### Hotfix Scenario
1. After release, discover a "critical bug"
2. Create hotfix branch from main
3. Fix the bug
4. Merge to both main and develop
5. Create patch release

## Bonus Challenges (Extra 30 points)

### Advanced Git Features (10 points each)
1. **Submodules**: Add a submodule and demonstrate proper update workflow
2. **Git Hooks**: Create pre-commit hook for code formatting
3. **Signed Commits**: GPG sign at least 3 commits

## Deliverables

Your repository must contain:
1. **Main codebase** with Calculator implementation
2. **Full test suite** with >80% coverage
3. **CI/CD pipeline** passing all checks
4. **Documentation**:
   - README.md with setup instructions
   - CONTRIBUTING.md with workflow guide
   - CHANGELOG.md with version history
   - BISECT_LOG.md with bisect demonstration
5. **Git history** showing:
   - Multiple branches
   - PRs with reviews
   - Merge commits
   - At least one rebase
   - Cherry-picked commits
   - Tags for releases

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| Repository Setup | 30 | Proper branch structure, protection rules, templates |
| Feature Development | 40 | Three features, proper PRs, simulated collaboration |
| Conflict Resolution | 35 | Successfully handle complex Git scenarios |
| CI/CD Pipeline | 25 | Working automation, tests, coverage |
| Release Management | 20 | Proper release workflow, hotfix handling |
| **Bonus** | 30 | Advanced Git features implementation |
| **Total** | **150** | **(+30 bonus)** |

## Submission

1. Complete all tasks in your forked repository
2. Ensure CI/CD pipeline is green
3. Create final PR to your main branch titled "HW1 Submission"
4. Submit repository URL in GitHub Classroom

## Tips for Success

- **Commit Often**: Small, focused commits are easier to manage
- **Write Good Messages**: Future you will thank present you
- **Use Git Graph**: Visualize your branch structure
- **Test Locally**: Don't rely solely on CI/CD
- **Document Everything**: Over-documentation is better than under

## Resources

- [Git Pro Book](https://git-scm.com/book/en/v2)
- [GitHub Flow Guide](https://githubflow.github.io/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

## Academic Integrity

While this simulates team collaboration, you must complete all parts yourself. You may discuss strategies with classmates but not share code or commits.

---

*This is an optional grade booster assignment. Completing it successfully can add up to 150 points to your course grade (plus 30 bonus for advanced features).*