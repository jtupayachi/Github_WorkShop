# Part 2: Git Basics — Your First Repository

**Duration:** ~25 minutes

---

## 2.1 What Is Git?

Git is a **distributed version control system** that tracks changes to files over time. Think of it as an **unlimited undo history** for your entire project.

### Key Concepts

```
Working Directory  →  Staging Area  →  Repository (History)
    (your files)      (git add)         (git commit)
```

| Concept | Description |
|---------|-------------|
| **Repository (repo)** | A project folder tracked by Git |
| **Commit** | A snapshot of your project at a point in time |
| **Staging Area** | A preparation zone where you choose what goes into the next commit |
| **Working Directory** | The actual files on your computer |

---

## 2.2 Creating Your First Repository

### Initialize a new repository

```bash
# Create a project folder
mkdir my-first-repo
cd my-first-repo

# Initialize Git tracking
git init
```

You should see: `Initialized empty Git repository in .../my-first-repo/.git/`

### Check the status

```bash
git status
```

This is the command you'll use **most often**. It tells you what's changed, what's staged, and what's untracked.

---

## 2.3 The Git Workflow: Add → Commit

### Step 1 — Create a file

```bash
echo "# My First Project" > README.md
echo "This is my first Git repository!" >> README.md
```

### Step 2 — Check status

```bash
git status
```

Output will show `README.md` as an **untracked file** (in red).

### Step 3 — Stage the file

```bash
git add README.md
```

### Step 4 — Check status again

```bash
git status
```

Now `README.md` appears as a **new file** ready to be committed (in green).

### Step 5 — Commit the file

```bash
git commit -m "Initial commit: add README"
```

The `-m` flag lets you write the commit message inline.

---

## 2.4 Making More Changes

### Edit the file

```bash
echo "" >> README.md
echo "## About" >> README.md
echo "Learning Git step by step." >> README.md
```

### See what changed

```bash
# Show which files changed
git status

# Show the exact changes (diff)
git diff
```

The `git diff` output shows:
- Lines starting with `+` were **added**
- Lines starting with `-` were **removed**

### Stage and commit

```bash
git add README.md
git commit -m "Add About section to README"
```

> **Shortcut:** You can stage and commit tracked files in one step:
> ```bash
> git commit -am "Your message here"
> ```
> (This only works for files Git is already tracking, not new files.)

---

## 2.5 Viewing History

### See the commit log

```bash
git log
```

### Compact one-line view

```bash
git log --oneline
```

### Graphical view (useful later with branches)

```bash
git log --oneline --graph --all
```

### See changes in a specific commit

```bash
git show <commit-hash>
```

(Use the first 7 characters of the hash from `git log --oneline`.)

---

## 2.6 Staging Multiple Files

```bash
# Create multiple files
echo "print('Hello, Git!')" > hello.py
echo "body { margin: 0; }" > style.css
echo "node_modules/" > .gitignore

# Stage everything at once
git add .

# Or stage specific files
git add hello.py style.css

# Check what's staged
git status

# Commit
git commit -m "Add hello script, stylesheet, and gitignore"
```

---

## 2.7 Undoing Things

### Unstage a file (keep changes)

```bash
git restore --staged <filename>
```

### Discard changes in working directory

```bash
git restore <filename>
```

> **Warning:** This permanently discards your local changes!

### Amend the last commit message

```bash
git commit --amend -m "New corrected message"
```

### Amend the last commit (add forgotten files)

```bash
git add forgotten_file.txt
git commit --amend --no-edit
```

---

## 2.8 The .gitignore File

The `.gitignore` file tells Git which files to **ignore** (not track).

### Common .gitignore patterns

```
# Compiled files
*.pyc
__pycache__/

# OS files
.DS_Store
Thumbs.db

# IDE files
.vscode/
.idea/

# Dependencies
node_modules/
venv/

# Secrets
.env
*.key

# Data files (too large for Git)
*.csv
data/
```

> **Tip:** Use [gitignore.io](https://gitignore.io) to generate `.gitignore` files for your tech stack.

---

## 2.9 Understanding the Three States

```
┌──────────────┐    git add    ┌──────────────┐   git commit   ┌──────────────┐
│              │  ──────────►  │              │  ────────────►  │              │
│   Working    │               │   Staging    │                 │  Repository  │
│  Directory   │  ◄──────────  │    Area      │                 │   (History)  │
│              │  git restore  │              │                 │              │
└──────────────┘               └──────────────┘                 └──────────────┘
```

| State | Description | Command to move forward |
|-------|-------------|------------------------|
| **Modified** | Changed but not staged | `git add` |
| **Staged** | Marked for next commit | `git commit` |
| **Committed** | Safely stored in history | — |

---

## Exercise 2

1. Create a new folder and initialize a Git repository
2. Create at least 3 files (e.g., `README.md`, `hello.py`, `.gitignore`)
3. Make an initial commit with all files
4. Edit one of the files and use `git diff` to see changes
5. Make a second commit
6. View your commit history with `git log --oneline`

**Bonus:** Try using `git restore --staged` to unstage a file before committing.

---

[← Part 1: Setup](01_setup.md) | [Next: Part 3 — GitHub Remotes →](03_github_remotes.md)
