---
marp: true
theme: gradient
backgroundColor: #f5f9ff
title: "Code Like a Scientist: Essential Tools for Research Programming"
author: "Anna Smirnova"
date: "September 15, 2025"
description: "A hands-on tutorial to get you started with essential programming tools for researchers."
paginate: true

header: "Code Like a Scientist: Essential Tools for Research Programming"
footer: "Anna Smirnova, September 15, 2025"
style: |
  section.lead {
    background: #003aff;
    color: white;
  }
  section.lead footer {
    color: white;
  }
  section.lead header {
    color: white;
  }
  section.lead h1, section.lead h2, section.lead h3 {
    color: white;
    border-bottom: none;
  }
  section.lead a {
    color: white;
  }

# headerPosition: center
# footerPosition: center
# headerAlign: center
# footerAlign: center

---

<!-- _class: lead -->
<!-- _backgroundColor: #003aff -->
<!-- _color: white -->
# Practical Session 1 
# Code Like a Scientist: Essential Tools for Research Programming

**Anna Smirnova**
**September 2025**

---

# First Things First
*   **Welcome!** This is a hands-on tutorial to get you started with essential programming tools for researchers.
*   **Goal:** By the end of this session, you will be comfortable using the terminal, managing Python environments, and using VSCode.
*   **Prerequisites:** No prior programming experience is required, but a basic understanding of computers is helpful.
*   **Resources:** All slides and code examples are available in the Nuvolos cloud environment and the class [website](https://ap-unil-2025.github.io/course-materials/).
---
# Please open the following page in your browser!
<p align="center">
    <img src="https://api.qrserver.com/v1/create-qr-code/?size=120x120&data=https://app.nuvolos.cloud/enroll/class/RshD654gzU4" alt="Scan this QR code to enroll" />
    <br>
    <small>Scan this QR code to enroll</small>
</p>

Or [click here to enroll in the course workspace](https://app.nuvolos.cloud/enroll/class/RshD654gzU4).
Log in with your university credentials and launch a new VSCode instance (see demo!). This workspace has all the required tools pre-installed.

> <span style="color: red;"> **Tip:** I highly recommend using Nuvolos for hands-on activities, especially if you are on Windows. But if you prefer to install everything locally, just ask!</span>

---
<p align="center">
    <img src="/Users/asmirnov/Projects/research/AP2025/course-materials/docs/assets/images/nuvolos_logo.svg" alt="Nuvolos Logo" width="360"/>
</p>

<p align="center">
    <b>Nuvolos</b> is a cloud-based platform providing a ready-to-use programming environment based on <b>Linux</b> and VSCode.<br>
    <b>No installation required!</b> Log in with your university credentials and start coding.<br>
    Each student gets their own isolated workspace with all the necessary tools pre-installed.
</p>

---
# Your First Steps in Nuvolos
*   After enrolling, you will see the Nuvolos dashboard.
*   Click on "Launch VSCode" to start a new coding environment.
*   This will open a new browser tab with VSCode running in the cloud.
*   You can also install the [Nuvolos Desktop App](https://nuvolos.cloud/download) for a better experience.
*   Once VSCode is open, you will see a terminal panel at the bottom. If not, open it with `Ctrl + `` (backtick) or via the menu: View > Terminal.
*   You are now ready to start coding!

---
# What is a Terminal, and why do we need it?

*   **Terminal**: A text-based interface to interact with your computer's operating system. But **why use it?**
    *   **Efficiency**: Faster and more flexible than graphical interfaces, especially for repetitive tasks.
    *   **More importantly** — a lot of computers actually don't even come with a graphic interface, like many servers and high-performance computing (HPC) clusters.
*   **The terminal allows you to** do pretty much anything you can do with a graphical user interface (GUI), but often more efficiently.
* A lot of **modern** programming tools and libraries are designed to be used from the terminal!
---

# What is a shell? 

*  A shell is a **program** that **reads and executes** what you write in the terminal.

*   Used to execute commands, navigate the file system, and run scripts.

*   Provides an interface between the user and the system.

*  The two most common shells are:
    *   **Bash** (Bourne Again SHell) — the default on many Linux distributions.
    *   **Zsh** (Z Shell) — the default on macOS and increasingly popular on Linux.

<!-- --- -->

<!-- # A basic terminal

<!-- TODO: This is a placeholder for a screenshot or a live demo of a terminal window. -->
<!-- ![bg right:70% 90%](https://techterms.com/img/xl/terminal_610.png) -->

<!-- --- --> 

<!-- # Using the Terminal on Your Personal Computer: MacOS


*   `Terminal.app` is built-in. Look it up in Spotlight (Cmd + Space) or find it in Applications > Utilities.
*   You can also install applications like `iTerm2`, `Ghostty` or `Warp`.
* Install `brew` (Homebrew) to easily install other tools and packages from the terminal.
* Run 
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
* After that, open a new terminal window and run:
    * `brew install git` to install Git.
    * `brew install python3.12` to install Python.
    * `brew install uv` to install `uv`, our new package manager. -->

<!-- 
---
# Using the Terminal on Your Personal Computer: Windows

*   Use the `Windows Terminal` app (built-in).
* There are a lot of ways to use these commands on Windows, but I recommend using the **Windows Subsystem for Linux (WSL)**, which allows you to run a Linux distribution alongside Windows. 
* This will give you a more consistent experience with the commands we will be using.
* It takes a while to install, so do it before the next session. -->

---

# Using the Terminal in VSCode
> In this course, I will be using the virtual VSCode in the Nuvolos environment for our hands-on activities. But if you wish to install VSCode and Python on your personal computer, feel free to reach out!

*   **Built-in Terminal:**
    *   VSCode has a built-in terminal, accessible with `Ctrl+backtick` (Windows/Linux) or `Cmd+backtick` (macOS).
    *   Supports multiple shell options (e.g., Bash, PowerShell, Zsh).
* Open the terminal in your Nuvolos workspace (bottom panel in VSCode): `Ctrl + `` (backtick) or via the menu: View > Terminal.
---
# What's Going On?
* What you're currently seeing is a terminal window running the `bash` shell.
* The terminal is ready to accept commands. You can type commands and press `Enter` to execute them.
* The prompt (i.e., the text `(base) nuvolos@nuvolos:~$`) indicates your Python environment (if any), your username, the hostname of the machine, and your current directory.
---
# Your first commands in the terminal
*   Type the following command and press Enter:
```bash
echo "Hello, World!"
```
---

# Basic Navigation Commands: `cd`, `ls`

*   `pwd` — **P**rint the full path to the **w**orking **d**irectory you are in.
*   `cd <directory>` — **C**hange **d**irectory.
    *   `cd ..` — Move up one directory level.
    *   `cd ~` — Go to the home directory.
*   `ls` — **L**i**s**t directory contents.
    *   `ls -a` — List **a**ll files, including hidden ones (files that start with a dot).
*   Combine options:
    *   `ls -la` — List all files with detailed information.

The parts of the command written with a dash before them are called **flags**. They modify the behavior of the command. For example, most commands have an `-h` flag for help.

---

# Commands: `mv`, `cp`, `rm`, `touch`, `mkdir`

*   `mv <source> <destination>` — **M**o**v**e or rename files.
*   `cp <source> <destination>` — **C**o**p**y files or directories.
*   `rm <file>` — **R**e**m**ove files. **Caution!** This does not put the files in a “trash bin", it removes them **permanently**.
    *   `rm -r <directory>` — Remove a directory and all files within it recursively.
*   `touch <file>` — Create an empty file or update its timestamp.
*   `mkdir <directory>` — **M**a**k**e a new **dir**ectory.
    *   Use `mkdir -p` to create nested directories.

---

# Using the Wildcard Symbol (`*`)

*   **What is the Wildcard Symbol (`*`)?**
    *   The wildcard symbol `*` matches any number of characters in filenames or directories.
    * That is, it is a **placeholder** for any characters.
    *   Useful for performing operations on multiple files at once.
    

*   **Using Wildcards:**
    *   You can use wildcards to match specific file patterns.
    *   Example: `rm *.jpg` — Removes all files with a `.jpg` extension in the current folder.

---

# Commands: `cat`, `head` and `tail`

*   `cat` — Concatenate and display the content of a file:
    *   `cat <file>` — Displays the entire content of a file.
    * Can also be used to concatenate multiple files: `cat file1 file2 > combined_file`.

* `head` and  `tail` — Display the first/last few lines of a file:
    *   `tail <file>` — Shows the last 10 lines of a file by default.
    *   `tail -n <number> <file>` — Shows the last `<number>` lines of the file.
    *   `tail -f <file>` — Follow a file for real-time updates: continuously displays new lines as they are added to a file (useful for monitoring logs).
---
# Commands: `echo`, `clear`, `man`
*   `echo <text>` — Prints text to the terminal.
    *   Example: `echo "Hello, World!"` prints "Hello, World!" to the terminal.
*   `clear` — Clears the terminal screen.
*   `man <command>` — Displays the manual page for a command.
    *   Provides detailed information about the command, its options, and usage.
    *   Example: `man ls` shows the manual for the `ls` command.
    *   Use `q` to exit the manual page.
---
# Useful Shortcuts for the Terminal

*   `Ctrl + L`:
    *   Clears the terminal screen.
*   `Tab`:
    *   Autocompletes file and directory names.
*   `Ctrl + R`:
    *   Searches through your command history.
*   `Ctrl + C`:
    *   Interrupts or stops the current command.
*   `Ctrl + D`:
    *   Logs out or ends input.
---
# Useful Shortcuts
*   `Ctrl + A`:
    *   Moves the cursor to the beginning of the line.
*   `Ctrl + E`:
    *   Moves the cursor to the end of the line.
*   `Ctrl + U`:
    *   Deletes from the cursor to the start of the line.
*   `Ctrl + K`:
    *   Deletes from the cursor to the end of the line.
---

# Advanced Terminal Features: Scripting, Redirection, Pipes, and More
---
# Bash is a Programming Language
*   Bash is actually a **full-fledged programming language**, just like Python!
*   You can control the behavior of your computer by writing commands in Bash, as we just learned, but...
*   You can also write **scripts** (files with a series of commands) to automate tasks.
* This is commonly used in research to automate data processing, analysis, and other repetitive tasks, as well as in HPC workflows.
---
# Bash is a Programming Language
*   Create a new file named `myscript.sh` and add the following content:
```bash
#!/bin/bash
echo "This is my first script!"
ls -la
```
*   Save the file and make it executable with:
```bash
chmod +x myscript.sh # This command makes the script executable
```
*   Run the script with:
```bash
./myscript.sh # This command executes the script
```
---
# Bash is a Programming Language
*   Bash supports variables, conditionals, loops, and functions.
*   Example of a simple bash script with a loop:
```bash
#!/bin/bash
mkdir my_test_folder
cd my_test_folder
pwd
for i in {1..5}
do
   touch "file_$i.txt"
   echo "Created file_$i.txt"
done
```
*   Save it as `loop.sh`, make it executable, and run it to see the output.
---
# Advanced Bash Features: Passing Arguments
*   You can pass arguments to your bash scripts:
```bash
#!/bin/bash
echo "Hello, $1!"  # $1 is the first argument passed to the script
```
*   Save it as `greet.sh`, make it executable, and run it with:
```bash
./greet.sh Anna  # This will print "Hello, Anna!"
```
*   You can use `$2`, `$3`, etc., for additional arguments.
*   `$0` contains the name of the script itself.
---
# Advanced Bash Features: Conditionals
*   You can use conditionals:
```bash
#!/bin/bash
if [ -d "$1" ]; then
   echo "Directory $1 exists."
else
   echo "Directory $1 does not exist."
fi
```
*   Save it as `check_dir.sh`, make it executable, and run it with a directory name as an argument.
*   You can use `elif` for additional conditions and `&&` and `||` for logical AND and OR operations.

---
# Advanced Commands: Redirection and Output to Files: `>`, `>>`
*   `>` — Redirects the output of a command to a file, overwriting the file if it exists.
    *   Example: `echo "Hello, World!" > hello.txt` — Creates (or overwrites) `hello.txt` with "Hello, World!".
*   `>>` — Appends the output of a command to a file, creating the file if it doesn't exist.
    *   Example: `echo "Another line" >> hello.txt` — Appends "Another line" to `hello.txt`.
*   These operators are useful for saving command output for later use or logging.
---     
# Combining Commands with `&&` and `;`
*   `&&` — Logical AND operator:
    *   Executes the second command only if the first command is successful (returns exit status 0).
    *   Example: `mkdir new_folder && cd new_folder` — Creates a new folder and changes into it only if the folder creation was successful.
*   `;` — Command separator:
    *   Executes the second command regardless of the success or failure of the first command.
    *   Example: `mkdir new_folder; cd new_folder` — Creates a new folder and changes into it, regardless of whether the folder creation was successful or not.

---
# Pipelines with `|`
*   The pipe symbol `|` takes the output of one command and uses it as the input for another command.
*   Example: `ls -l | grep ".txt"` — Lists all files in long format and filters the output to show only `.txt` files.
*   You can chain multiple commands together using pipes.
*   Example: `cat file.txt | grep "error" | sort | uniq` — Finds lines containing "error" in `file.txt`, sorts them, and removes duplicates.
---
# Useful Programs: `curl`, `wget`
*   `curl <url>` — Transfers data from or to a server using various protocols (HTTP, FTP, etc.).
    *   Example: `curl https://example.com` — Fetches the content of the webpage.
*   `wget <url>` — Downloads files from the web.
    *   Example: `wget https://example.com/file.zip` — Downloads `file.zip` from the specified URL.
*   Both programs are useful for downloading datasets, scripts, or other resources directly from the terminal.
*   These programs are installed in your Nuvolos workspace by default.
---
# Useful Programs: `tree`, `find`
*   `tree` — Displays a tree-like structure of directories and files.
    *   Example: `tree` — Shows the directory structure of the current folder.
    *   `tree -L <level>` — Limits the display to a certain depth level.
    * Not available on Nuvolos :(
*   `find <path> -name <pattern>` — Searches for files and directories matching a specific pattern.
    *   Example: `find . -name "*.txt"` — Finds all `.txt` files in the current directory and its subdirectories.
---
# Useful Programs: Search with `grep`
*   `grep <pattern> <file>` — Searches for a specific pattern in a file.
    *   Example: `grep "error" log.txt` — Finds all lines containing "error" in `log.txt`.
*   `grep -i <pattern> <file>` — Case-insensitive search.
*   `grep -r <pattern> <directory>` — Recursively search through all files in a directory.
*   `grep -n <pattern> <file>` — Show line numbers of matching lines.
*   `grep` is a powerful tool for searching through text files and logs.   
<!-- ---
# Useful Programs: `nano`, `vim`, `htop`
*   `nano <file>` — A simple terminal-based text editor.
    *   Easy to use for beginners. Use `Ctrl + X` to exit, `Y` to save changes.
*   `vim <file>` — A powerful terminal-based text editor.
    *   More complex, but very efficient once mastered. Use `:q` to quit, `:w` to save changes.
*   `htop` — An interactive process viewer.
    *   Displays system processes and resource usage in real-time. Use `F10` to exit. -->
<!-- --- -->
<!-- # Advanced Terminal Features: Tab Completion and Command History
*   **Tab Completion:**
    *   Press the `Tab` key while typing a command or filename to auto-complete it.
    *   If multiple options are available, press `Tab` twice to see a list of possible completions.
*   **Command History:**
    *   Use the `Up` and `Down` arrow keys to navigate through your command history.
    *   Press `Ctrl + R` to search through your command history. Start typing a part of a previous command, and it will show matching commands.
*   These features can significantly speed up your workflow in the terminal. -->
---
# Advanced Terminal Programs: `ssh`, `rsync`
* Not needed on Nuvolos, but very useful when working with remote servers or HPC clusters.
*   `ssh` — **S**ecure **SH**ell, used to securely connect to a remote machine over a network.
*   `ssh <user>@<host>` — Securely connect to a remote machine.
    *   Example: `ssh user@192.168.1.1`
*   `rsync` — A fast and versatile file-copying tool.
    *   Can copy files locally or to/from a remote machine.
    *   Example: `rsync -avz file.txt user@192.168.1.1:/remote/directory/`
*   `rsync` is more efficient than `scp` for large files or directories, as it only transfers the differences between source and destination.
---
# Python Environments and Package Management
---
# What is a Python Installation?
 *   The core Python interpreter installed on your system.
        * A Python interpreter is a program that reads and executes Python code, just like the shell we discussed earlier!
*   On most systems, Python is pre-installed or can be installed via package managers (e.g., `apt`, `brew`).
*   On Windows, you generally have to install Python from the Python website.
* On Nuvolos, you don't have to care about this, as Python is already installed in your workspace.
---
# What is a Python (Virtual) Environment?
*   An isolated "space" that includes a specific Python interpreter and its associated packages.
*   Allows you to manage dependencies for different projects without conflicts.
*   As in, it is a **folder** which contains the Python executable file and the files of installed packages.
*   Multiple environments allow different projects to use different package versions without conflicts.
* There are different tools to create and manage Python environments, such as `venv`, `conda`, and `uv`.

---

# Running Python Code in the Terminal

Now we know enough to write and run our first Python script!
*   Create a new file named `hello_world.py` in your project directory.
*   Open it in VSCode and add the following code:
    ```python
    print("Hello, World!")
    ```
*   Save the file.
*  Open your terminal and navigate to the directory where you saved the file.
*   Run the script using the command:
    ```bash
    python hello_world.py
    ```
---


# `venv`

*   `venv` is a built-in Python module for creating virtual environments.
*   Ensures that each project has its own set of dependencies --- that is, **external Python libraries at the specific versions you need.**
*   Prevents version conflicts between projects.
*   Does not break the system installation of Python.
*  Used to be optional, but is currently the **standard** way to manage Python environments.
* Your system Python will actually enforce you to use `venv` for any project that has dependencies!
---
# Creating a Virtual Environment with `venv`
*   To create a new virtual environment, run the following command in your terminal:
```bash
python3 -m venv myenv
```
*   This creates a new directory named `myenv` in your current directory.
*   The `myenv` directory contains a copy of the Python interpreter and a `bin` directory with the `python` and `pip` programs.
*   **Important!** The name `myenv` is just an example. You can name your environment anything you like, but it is a good practice to use a descriptive name that reflects the project it is associated with.
---
# Virtual Environment on Nuvolos: Conda
*   In your Nuvolos workspace, `conda` is the default environment manager.
*   To create a new Conda environment, use the following command:
```bash
conda create --name myenv python=3.13
```
*   This creates a new environment named `myenv` with Python 3.13 installed.
*   To activate the environment, use:
```bash
conda activate myenv
```
*   You can then install packages using `conda install <package>` or `pip install <package>`.
---
# Command: `which`

*   `which <command>` — Shows the full path of the command or executable.

*   Helps identify where an executable is located.

*   **Example: `which python`**
    *   Output: `/opt/conda/bin/python`, tells you the system is using Python from this location.
    *   If you run this after activating a virtual environment, the output will be `.../myenv/bin/python`.

*   Useful for ensuring that you're using the right version of Python in the terminal.

---

# Installing Packages: `pip`

* A **software package** is a collection of files and metadata that provide specific functionality or features, such as libraries or frameworks.
    * They are simply code that someone else wrote, which you can use in your own code.
*   A **package manager** is a tool that automates the process of installing, updating, configuring, and removing software packages.
    *   It helps manage dependencies, ensuring that the correct versions of libraries or software are available for your project.
*   `pip` is the default package manager for Python.
*   Like `python` and `venv`, `pip` is a command you run from your terminal.

---


# Installing Packages: `pip`
> **Caution!** Make sure you are installing packages in the correct **virtual environment** (your prompt should show `(myenv)` when it is activated).
*   `pip install <package>` — Install a package from the Python Package Index (PyPI).
* Try it out! Install the `scikit-learn` package:
```bash
conda activate myenv  # Activate your virtual environment first
pip install scikit-learn
```
* Now you can write:
```python
import sklearn
```
*   to use the `scikit-learn` package in your Python code.
---
# Installing Packages: `pip`
*   `pip install <package>==<version>` — Install a specific version of a package.
    *   Example: `pip install numpy==1.21.0` — Installs version 1.21.0 of the `numpy` package.
*   `pip install -r requirements.txt` — Install all packages listed in a text file (commonly named `requirements.txt`).
        *   A requirements file contains all package versions your project depends on.
        *   This is **crucial** for reproducibility and collaboration!

---
# Installing Packages: `pip`
*   `pip freeze > requirements.txt` — Save the current environment's packages to a file. Will be covered in more detail in the next sessions as it is CRUCIAL for reproducibility.
*   `pip list` — List all installed packages in your current environment.
*   `pip install --upgrade <package>` — Upgrade a package to the latest version
*   `pip uninstall <package>` — Remove a package.

---
# Advanced Package Management: `uv`
*   **`uv`**: A tool for managing Python environments and packages, similar to `pip`, but with a rich set of features and impressive performance.
    *   Provides a more user-friendly interface for managing Python environments and Python versions.
    *   Much faster than `pip` for installing packages.
    * I will cover it in more detail in the next sessions. `uv` includes `venv` and `pip` functionality, so you will not get lost.
    * Install with `pip install uv` in a non-base conda env on Nuvolos.
---
# Summary
*   The terminal is a powerful tool for interacting with your computer and running commands efficiently.
*   Basic commands like `cd`, `ls`, `mv`, `cp`, and `rm` help you navigate and manage files and directories.
*   Python virtual environments (`conda`) are essential for managing project dependencies and avoiding conflicts.
*   `pip` is the default package manager for Python.
*   Using these tools effectively will enhance your productivity and help you manage your coding projects like a pro!
---
# Your Assignment for Next Time 
*   There is no class next week (September 22), but please complete the following tasks before our next session on September 29:
*   Explore the terminal and try out the commands we covered.
*   Study the advanced terminal features in the slides! 
*   Set up a Python virtual environment for your project.
*   Install a few packages using `pip` or `uv`.
*   Prepare any questions you have for our next session!

