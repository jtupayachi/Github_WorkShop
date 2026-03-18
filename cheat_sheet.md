# Git & GitHub Cheat Sheet

> Quick reference for the most common Git commands.

---

## Setup & Configuration

```bash
git config --global user.name "Your Name"       # Set name
git config --global user.email "you@email.com"   # Set email
git config --global init.defaultBranch main      # Default branch name
git config --list                                # View all settings
```

---

## Creating Repositories

```bash
git init                        # Initialize new repo in current folder
git clone <url>                 # Clone existing repo from GitHub
```

---

## Basic Workflow

```bash
git status                      # Check status of files
git add <file>                  # Stage a specific file
git add .                       # Stage all changes
git commit -m "message"         # Commit staged changes
git commit -am "message"        # Stage + commit tracked files
```

---

## Viewing Changes & History

```bash
git diff                        # Show unstaged changes
git diff --staged               # Show staged changes
git log                         # Full commit history
git log --oneline               # Compact history
git log --oneline --graph --all # Visual branch history
git show <hash>                 # Show details of a commit
```

---

## Branching

```bash
git branch                      # List branches
git branch <name>               # Create branch
git switch <name>               # Switch to branch
git switch -c <name>            # Create + switch
git branch -d <name>            # Delete branch (safe)
git branch -D <name>            # Force delete branch
```

---

## Merging

```bash
git merge <branch>              # Merge branch into current
# If conflicts:
# 1. Edit conflicted files
# 2. git add <file>
# 3. git commit
```

---

## Remote Repositories

```bash
git remote add origin <url>     # Connect to GitHub
git remote -v                   # View remotes
git push -u origin main         # First push (set upstream)
git push                        # Push commits
git pull                        # Pull latest changes
git fetch                       # Download without merging
```

---

## Undoing Things

```bash
git restore <file>              # Discard local changes
git restore --staged <file>     # Unstage a file
git commit --amend              # Modify last commit
git reset --soft HEAD~1         # Undo last commit (keep changes)
git revert <hash>               # Create commit undoing a past commit
```

---

## Stashing

```bash
git stash                       # Save changes temporarily
git stash pop                   # Restore + remove from stash
git stash list                  # List all stashes
git stash apply                 # Restore (keep in stash)
```

---

## Tags

```bash
git tag v1.0.0                  # Lightweight tag
git tag -a v1.0.0 -m "msg"     # Annotated tag
git push origin --tags          # Push all tags
```

---

## .gitignore (common patterns)

```
*.pyc                           # Compiled Python
__pycache__/                    # Python cache
node_modules/                   # Node.js dependencies
.env                            # Environment variables
.DS_Store                       # macOS system file
*.csv                           # CSV data files
.vscode/                        # VS Code settings
```

---

## GitHub Shortcuts

| Shortcut | Action |
|----------|--------|
| `.` on any repo | Open in web editor |
| `t` on any repo | File finder |
| `?` | Show all keyboard shortcuts |
| `Fixes #123` in commit | Auto-close issue #123 |

---

## Workflow Summary

```
git switch -c feature/my-work   # 1. Create branch
# ... make changes ...          # 2. Write code
git add .                       # 3. Stage
git commit -m "description"     # 4. Commit
git push -u origin feature/...  # 5. Push
# Open Pull Request on GitHub   # 6. PR + Review
# Merge on GitHub               # 7. Merge
git switch main && git pull     # 8. Update local
git branch -d feature/my-work   # 9. Clean up
```

---

*Print this page and keep it next to your keyboard!*
