---
marp: true
paginate: true
backgroundColor: #f5f9ff
header: "Tracking Your Genius (Git & GitHub)"
footer: "Anna Smirnova, June 24, 2025"
# style: |
#   section {
#     font-size: 29px;
#   }
#   h1 {
#     font-size: 40px;
#   }
#   h2 {
#     font-size: 10px;
#   }
#   h3 {
#     font-size: 20px;
#     }

# headerPosition: center
# footerPosition: center
# headerAlign: center
# footerAlign: center
# Part 2: Git & GitHub

---


# Practical Session 2
# Tracking Your Genius: Git & GitHub

**Anna Smirnova**
**October 6, 2025**

---

# First Things First
*   Welcome to the second practical session of the course!
*   In this session, we will cover:
    *   What is version control?
    *   What is Git?
    *   What is GitHub?
    *   Basic Git commands and workflow.
*   How to publish your code on GitHub.
*   How to use Git in VSCode.
*   Your first real assignment!
---

# What is Version Control?

*  **Version Control** is a system that manages changes to files and directories.
*   It is a system that allows you to store the **entire history** of changes in your code files—immensely useful in coding projects.
* It creates a timeline of changes, allowing you to:
    *   Track who made changes and when.
    *   Revert to previous versions of files.
    *   Collaborate with others without overwriting each other's work.
*   Allows collaboration on code and documents, tracking who made what changes and when.
<!-- 
*   **Version Control vs Backup:**
    *   **Version Control**: Stores a history of changes with commit messages, enabling easy rollback or comparison.
    *   **Backup**: A complete copy of data at a point in time, meant for disaster recovery.
    *   Version control is not a backup system but a way to track and manage incremental changes. -->

---

# What is Git?

*   **Git**: A distributed version control system (VCS) for tracking changes in source code during software development.

*   It is a command-line tool, although there are many visual interfaces for it (such as GitHub Desktop, or the VCS extension in VSCode).

*   Git is the most widely used version control tool across the world.
---
# Why Use Git?
*   Helps multiple people collaborate on the same project.
*   Keeps a full history of changes, making it easy to track who changed what and when.
*   Allows you to revert to previous versions of files or the entire project.
*   Makes it easy to experiment with new features without breaking the main project.
*   Enables you to work offline and sync changes later.
*   Enables branching and merging, which allows for experimentation without affecting (and breaking!) the main project.

---

# What Can You Track in Git?


*   Source code files (`.py`, `.ipynb`, etc.).
*   Configuration files (e.g., `.env.example`, `Dockerfile`).
*   Documentation (e.g., `README.md`).
---
# What Can't You Track in Git?
*   Large files (e.g., data files). Any file larger than 100 MB should not be tracked in Git.
*   Binary files (e.g., images, videos) unless they are small and necessary for the project.
*   Temporary files (e.g., `.tmp`, `.log` files).
*   Compiled files (e.g., `.pyc`, `.class` files).
*   System files (e.g., `.DS_Store` on macOS, `Thumbs.db` on Windows).
*   Auto-generated files (e.g., Jupyter Notebook checkpoints in the `.ipynb_checkpoints` folder).
*   **IMPORTANT**: Environment files or virtual environments (the `.venv/` folder).  
*   Private data (e.g., API keys, credentials).
---
# What is a `.gitignore` File?
* In Git, you can use a special text file named `.gitignore` to prevent certain files from being tracked. Adding files or directories to this file tells Git to ignore them. For example, you can add `.venv/` to ignore your virtual environment folder, and then Git will not "see" it at all.
* I have specifically created an extensive .gitignore file for you to use in your projects, which you can find in the `my-research-project` folder. It includes common patterns to ignore temporary files, virtual environments, and other unnecessary files.
---

# Basic Concepts: **Repository**

*   A repository (or "repo") is the place (a folder) where both your project files and the history of changes are stored.
*   Can be **local** (on your computer) or **remote** (on services like GitHub).

---
# Basic Workflow
The basic workflow involves a two-step process to save your changes:

1.  **Stage:** You choose the specific changes you want to save. Think of this as putting files into a box. The command is `git add <file>`.
    * *Staging* adds files to a "staging area" where new changes are not recorded!
2.  **Commit:** You take a permanent snapshot of the staged files and add a descriptive message. This is like sealing the box and labeling it. The command is `git commit -m "your label here"`.
    * *Committing* records changes line-by-line in each committed file, creating a unique **commit hash** that identifies the changes.
---

# First Steps in Git

Run the following in your terminal:

```bash
git config --global user.email "YOUR_EMAIL_HERE@unil.ch"
git config --global user.name "Your Name"
```

*   Sets the global email and username for all your repositories.
*   This is the name and email that show up when you will **commit** your changes.
*   This is the first required step to use Git.
*   As Git is fundamentally multi-user, you cannot track changes anonymously.

---

# Basic Git Workflow

*   `git init` — Run in a folder to make it into a repository.

*   `git status` — Shows the status of your files (e.g., changes, untracked files).

*   `git add <file>` — Adds a file to the staging area.

*   `git restore --staged <file>` — Remove a file from the staging area.

*   `git commit -m "message"` — Commits staged changes with a message. Your changes are now recorded under a unique **commit hash**.

*   `git log` — See commit history, with hashes, authors, and commit times.


---

# What is GitHub?

*   **GitHub**: a web-based platform for hosting Git repositories.
*   It hosts Git repositories in the cloud, allowing you to easily share you code with others, access it from anywhere, and collaborate on it remotely.
*   It makes the whole history of changes public as well.
*   To get a copy of a repo: `git clone <repository link>`.
*   To publish your own code, you will need to:
    1.  Make an account (please!)
    2.  Make an **access token** (used as a password).
    3.  Make a **remote** repository on the website.
---

# Publishing and Updating a Git Repository


*   A **remote repository** is a version of your project hosted on an online service, such as GitHub.
*   You can link a local repository to a remote using the command: `git remote add origin <URL>`.
*   `origin` is a nickname for your remote URL.

---
# Basic Git Commands for Remote Repositories
*   **Push:**
    *   `git push origin <branch>` — Sends your local commits to the remote repository.
    *   Once changes are pushed, they become available to everyone with access.

*   **Pull:**
    *   `git pull origin <branch>` — Fetches the latest changes from the remote repository and merges them into your current branch.
    *   Essential for collaboration or when working on multiple machines.
---
# Using Git in VSCode

*   VSCode provides a user-friendly interface to Git and GitHub through its Source Control panel.

*  Please look at the live demo :)

---

# Your First (Real) Assignment

Go to the link below and accept the invite to the classroom. The assignment is to clone your first GitHub repository, edit a file, commit it and push it to GitHub:
[GitHub Classroom Assignment](https://classroom.github.com/a/your-assignment-link)
 
Try to complete the assignment by the end of the session. If you have any questions, please ask!

---
# Homework

TBA

---
<!-- _class: invert -->
# Advanced Git and GitHub: Take-Home Review

**Not optional, please do this!**

---
# Advanced Practices: Undoing Commits?

*   You can undo commits, however, you should first think about what you're committing!

*   **Bad practice (don't do this!):**
    ```bash
    git add .
    git commit -m "some updates"
    ```

*   Commit only those files that constitute a meaningful change, and write a message describing the change.

*  **Good practice:**
    ```bash
    git add <specific-file>
    git commit -m "Add feature X to improve Y"
    ```
---
# Advanced Practices: Undoing Commits
*   If you made a mistake in your last commit, you can undo it with:
    *   `git reset HEAD~1` — This will unstage the last commit but keep the changes in your working directory.
    *   `git reset --hard HEAD~1` — This will remove the last commit and discard all changes (use with caution!).
        * `HEAD` refers to the latest commit in your current branch.
        * The `~1` means "one commit before HEAD" (the last commit). You can change this number.
---
# Advanced Practices: Undoing Commits
*   If you want to undo a commit that has already been pushed, you can use:
    *   `git revert <commit-hash>` — This creates a new commit that undoes the changes made in the specified commit.
    *   This is safer than `git reset` because it preserves the commit history.
*   **Important:** Always be careful when undoing commits, especially if they have been pushed to a shared repository. Communicate with your team before making changes that affect the shared history.

---

# Advanced Practices: Using `git diff` to Compare Changes

*   `git diff` shows the differences between two versions of a file or set of files.
*   Useful for reviewing changes before staging or committing.
*   `git diff` — Shows changes in the working directory compared to the last commit.
*   `git diff <file>` — Displays changes in a specific file.
*   `git diff --staged` — Shows differences between the staged files and the latest commit.
*   `git diff <commit1> <commit2>` — Compare two specific commits.
*   `git diff --name-only` — Show only the names of files that have changed.

---
# Advanced Practices: Branching and Merging
 Branches in Git are like parallel universes for your code 🌌
*   **What is a Branch?**
    *   A branch is a separate line of development in your project.
    *   It allows you to work on new features or fixes without affecting the main codebase (usually called `main` or `master`).
*   **Why Use Branches?**
    *   To isolate changes until they are ready to be merged into the main codebase.
    *   To experiment with new ideas without risking the stability of the main project.
---
# **Basic Branch Commands**

*   `git branch` — Lists all branches in your repository.
*   `git branch <branch-name>` — Creates a new branch.
*   `git checkout <branch-name>` — Switches to the specified branch.
*   `git checkout -b <branch-name>` — Creates and switches to a new branch in one command.
*   `git merge <branch-name>` — Merges changes from the specified branch into the current branch.
*   `git branch -d <branch-name>`
    — Deletes the specified branch (only if it has been merged).

---

# Advanced Git Usage: Branches and Merge Conflicts

*   When you are done creating a new feature in a branch, you might want to transfer it to your main codebase. This is achieved by **merging**.

*   **Merging Branches:**
    *   `git merge <branch>` — Merges changes from one branch into another.
    *   If changes conflict, Git will flag the conflict in the files, and you will need to resolve them manually.

*   **Handling Merge Conflicts:**
    *   Conflicts occur when two branches modify the same part of a file.
    *   Manually edit the conflicting parts and commit the resolution.

---
# Advanced Git Usage: Feature Branches
*   **Feature Branches**: A common practice is to create a new branch for each feature or bug fix. This keeps the main branch clean and stable, and once the feature is complete, it can be merged back into the main branch.
*   **Workflow:**
    1.  Create a new branch: `git checkout -b feature/new-feature`.
    2.  Work on the feature, committing changes as you go.
    3.  When done, switch back to the main branch: `git checkout main`.
    4.  Merge the feature branch: `git merge feature/new-feature`.
    5.  Delete the feature branch: `git branch -d feature/new-feature`.
---
# Advanced Git Usage: Branches and Best Practices

*   Keep branches focused on a single feature or fix.
*   Regularly merge changes from the main branch into your feature branch to avoid large conflicts.
*   Use descriptive branch names (e.g., `feature/add-login`, `bugfix/fix-typo`).
---
# Advanced GitHub Usage: Pull Requests
*   **Pull Requests (PRs)**: A way to propose changes to a repository without directly modifying the main codebase.
*   They allow the owner of the repository to review changes before merging them into the main branch.
*   **Creating a Pull Request:**
    1.  Push your branch to GitHub: `git push origin <branch-name>`.
    2.  Go to the repository on GitHub.
    3.  Click on "Pull Requests" and then "New Pull Request".
    4.  Select the branch you want to merge and the target branch (usually `main`).
    5.  Add a title and description, then click "Create Pull Request".
---
# Advanced GitHub Usage: Issues and Project Management
*   **Issues**: GitHub provides a way to track bugs, feature requests, and other tasks through issues.
*   You can create an issue by clicking on the "Issues" tab in your repository and then "New Issue".
*   **Labels**: You can categorize issues using labels (e.g, `bug`, `enhancement`, `question`).
*   **Milestones**: You can group issues into milestones to track progress on larger features or releases.
*   **Project Boards**: GitHub also offers project boards to organize issues and pull requests in a Kanban-style board.
---
# Advanced GitHub Usage: GitHub Actions
*   **GitHub Actions**: A powerful feature that allows you to automate workflows directly in your GitHub repository.
*   You can set up actions to run tests, build your project, deploy code, or perform other tasks automatically when certain events occur (e.g., when a pull request is opened or code is pushed).
*  We will be using GitHub Actions in the final projects to automate testing and deployment, so stay tuned!

---
# Advanced GitHub Usage: Forking 
*   **Forking**: A fork is a personal copy of someone else's repository. You can make changes to your fork without affecting the original repository.
*   To fork a repository, click the "Fork" button on the top right of the repository page on GitHub.
*   After forking, you can clone your forked repository to your local machine, make changes, and push them back to your fork.
*   If you want to contribute your changes back to the original repository, you can create a pull request from your fork to the original repository.
*   This is a common practice in open-source projects, allowing you to contribute without needing direct write access to the original repository.
---
# Resources for Learning More
*   **Official Documentation:**
    *   [Git Documentation](https://git-scm.com/doc)
    *   [GitHub Documentation](https://docs.github.com/en)
    *   [Python Documentation](https://docs.python.org/3/)
    *   [VSCode Documentation](https://code.visualstudio.com/docs)

# Your Assignment
*   Review the key concepts covered in this session.
*   Complete the GitHub Classroom assignment if you haven't already.
*   Practice using Git commands in your terminal.
*   Explore GitHub features like issues, pull requests, and project boards.
*   If you have any questions or need help, feel free to reach out during office hours or via email.