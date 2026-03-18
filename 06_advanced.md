# Part 6: Advanced Topics & Best Practices

**Duration:** ~15 minutes

---

## 6.1 Writing Good Commit Messages

### The Convention

```
<type>: <short summary in imperative mood>

<optional body — explain WHAT and WHY, not HOW>

<optional footer — reference issues, breaking changes>
```

### Examples

```
feat: add user authentication module

Implemented JWT-based authentication with login/logout
endpoints. Password hashing uses bcrypt.

Closes #42
```

```
fix: resolve crash on empty dataset input

The model training script crashed when receiving an empty
CSV file. Added input validation with descriptive error.

Fixes #87
```

### Common types

| Type | Purpose |
|------|---------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `style` | Formatting, no logic change |
| `refactor` | Code restructuring |
| `test` | Adding/modifying tests |
| `chore` | Build process, dependencies |

### Rules of thumb

- Use **imperative mood**: "Add feature" not "Added feature"
- Keep the first line under **50 characters**
- Wrap body at **72 characters**
- Reference issue numbers when applicable

---

## 6.2 Git Stash — Save Work Temporarily

When you need to switch branches but aren't ready to commit:

```bash
# Save current changes to the stash
git stash

# List stashed changes
git stash list

# Apply the most recent stash (keeps it in the list)
git stash apply

# Apply and remove from the stash list
git stash pop

# Apply a specific stash
git stash apply stash@{2}

# Drop a stash
git stash drop stash@{0}
```

### Named stashes

```bash
git stash push -m "Work in progress: login form"
```

---

## 6.3 Git Tags — Marking Releases

Tags are permanent bookmarks for important commits (like releases).

```bash
# Create a lightweight tag
git tag v1.0.0

# Create an annotated tag (recommended)
git tag -a v1.0.0 -m "Release version 1.0.0"

# List tags
git tag

# Push tags to GitHub
git push origin v1.0.0
git push origin --tags   # push all tags

# View tag details
git show v1.0.0
```

On GitHub, tags automatically appear under **Releases**.

---

## 6.4 GitHub Actions — Automated Workflows (Overview)

GitHub Actions lets you automate tasks like testing, building, and deploying.

### Example: Run tests on every push

Create `.github/workflows/test.yml`:

```yaml
name: Run Tests

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: python -m pytest
```

### Common use cases

- Run tests automatically on every PR
- Build and deploy documentation
- Lint and format code
- Publish packages

---

## 6.5 GitHub Pages — Free Website Hosting

Host a static website directly from your repository:

1. Go to **Settings → Pages**
2. Source: **Deploy from a branch**
3. Branch: `main`, folder: `/ (root)` or `/docs`
4. Your site will be at `https://USERNAME.github.io/REPO-NAME`

Great for:
- Project documentation
- Personal portfolios
- Research project pages

---

## 6.6 Large File Storage (Git LFS)

Git is not designed for large binary files (datasets, models, images). Use **Git LFS**:

```bash
# Install Git LFS
brew install git-lfs   # macOS
git lfs install

# Track large file types
git lfs track "*.csv"
git lfs track "*.h5"
git lfs track "*.pkl"

# The tracking rules are stored in .gitattributes
git add .gitattributes
git commit -m "Configure Git LFS for large files"

# Then use git normally — LFS handles the rest
git add large_dataset.csv
git commit -m "Add training dataset"
git push
```

---

## 6.7 Useful Git Aliases

Add these to your `~/.gitconfig` or set them with `git config`:

```bash
git config --global alias.st "status"
git config --global alias.co "checkout"
git config --global alias.br "branch"
git config --global alias.ci "commit"
git config --global alias.lg "log --oneline --graph --all --decorate"
git config --global alias.last "log -1 HEAD"
git config --global alias.unstage "restore --staged"
```

Now you can use:
```bash
git st          # instead of git status
git co main     # instead of git checkout main
git lg          # pretty log graph
git last        # see last commit
```

---

## 6.8 Common Mistakes and How to Fix Them

### "I committed to the wrong branch!"

```bash
# Undo last commit but keep changes
git reset --soft HEAD~1

# Switch to the correct branch
git switch correct-branch

# Re-commit
git commit -am "Your message"
```

### "I need to undo a pushed commit!"

```bash
# Create a new commit that reverses the changes
git revert <commit-hash>
git push
```

> **Never** use `git reset` or `git push --force` on shared branches.

### "I accidentally deleted a file!"

```bash
# Restore from the last commit
git restore deleted_file.txt

# Restore from a specific commit
git checkout <commit-hash> -- deleted_file.txt
```

### "My repo has secrets I need to remove!"

```bash
# Remove a file from Git tracking (keeps local copy)
git rm --cached secrets.env
echo "secrets.env" >> .gitignore
git commit -am "Remove secrets from tracking"
```

> For files already in history, you'll need tools like `git filter-branch` or [BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/).

---

## 6.9 Best Practices Summary

| Practice | Why |
|----------|-----|
| **Commit often** | Small commits are easier to understand and revert |
| **Write clear commit messages** | Future you will thank present you |
| **Use branches** | Keep `main` stable; experiment on branches |
| **Pull before push** | Minimize merge conflicts |
| **Use .gitignore** | Don't track generated or secret files |
| **Review PRs carefully** | Catch bugs and share knowledge |
| **Tag releases** | Mark important milestones |
| **Never commit secrets** | API keys, passwords, tokens — keep them out |
| **Use SSH keys** | More secure and convenient than passwords |
| **Back up with remotes** | Push regularly to GitHub |

---

## 6.10 Where to Go Next

- **Git Documentation:** [git-scm.com/doc](https://git-scm.com/doc)
- **GitHub Skills:** [skills.github.com](https://skills.github.com) — interactive courses
- **Pro Git Book (free):** [git-scm.com/book](https://git-scm.com/book/en/v2)
- **Oh My Git!** — [ohmygit.org](https://ohmygit.org) — a game to learn Git
- **Learn Git Branching:** [learngitbranching.js.org](https://learngitbranching.js.org) — interactive visualization
- **GitHub Docs:** [docs.github.com](https://docs.github.com)

---

[← Part 5: Collaboration](05_collaboration.md) | [Cheat Sheet →](cheat_sheet.md)
