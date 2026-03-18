# Part 4: Branching & Merging

**Duration:** ~20 minutes

---

## 4.1 What Are Branches?

Branches let you work on different features or experiments **without affecting the main codebase**.

```
          feature-branch
         /                \
main ───●───●───●──────────●───●───  (merge)
              ↑
        branching point
```

Think of branches as **parallel timelines** for your project. You can:
- Develop a new feature without breaking the main code
- Experiment freely and throw away changes if they don't work
- Have multiple people working on different things simultaneously

---

## 4.2 Creating and Switching Branches

### See current branch

```bash
git branch
```

The branch with `*` is your current branch.

### Create a new branch

```bash
git branch feature-login
```

### Switch to the branch

```bash
git checkout feature-login

# OR (modern alternative, recommended)
git switch feature-login
```

### Create AND switch in one step

```bash
git checkout -b feature-login

# OR
git switch -c feature-login
```

---

## 4.3 Working on a Branch

```bash
# 1. Create and switch to a new branch
git switch -c feature-login

# 2. Make changes
echo "def login(user, password):" > auth.py
echo "    return True" >> auth.py

# 3. Stage and commit
git add auth.py
git commit -m "Add login function"

# 4. Make more changes
echo "def logout(user):" >> auth.py
echo "    return True" >> auth.py
git commit -am "Add logout function"
```

### View branch history

```bash
git log --oneline --graph --all
```

Output:
```
* b234567 (HEAD -> feature-login) Add logout function
* a123456 Add login function
* 9876543 (main) Initial commit: add README
```

---

## 4.4 Merging Branches

When your feature is complete, merge it back into `main`.

### Step 1 — Switch to the target branch

```bash
git switch main
```

### Step 2 — Merge the feature branch

```bash
git merge feature-login
```

### Step 3 — Delete the branch (optional, cleanup)

```bash
git branch -d feature-login
```

### Types of merges

| Type | When it happens | Result |
|------|----------------|--------|
| **Fast-forward** | No new commits on `main` since branching | Linear history, no merge commit |
| **Three-way merge** | Both branches have new commits | Creates a merge commit |

---

## 4.5 Handling Merge Conflicts

Merge conflicts happen when **two branches modify the same lines** in the same file.

### Example scenario

```bash
# On main
echo "Hello World" > greeting.txt
git add greeting.txt
git commit -m "Add greeting"

# Create branch and edit
git switch -c branch-a
echo "Hello from Branch A" > greeting.txt
git commit -am "Update greeting in branch-a"

# Go back to main and make a different edit
git switch main
echo "Hello from Main" > greeting.txt
git commit -am "Update greeting in main"

# Try to merge — CONFLICT!
git merge branch-a
```

### What a conflict looks like

```
<<<<<<< HEAD
Hello from Main
=======
Hello from Branch A
>>>>>>> branch-a
```

### Resolving the conflict

1. **Open the file** in your editor
2. **Choose** which version to keep (or combine both)
3. **Remove** the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
4. **Save** the file
5. **Stage and commit**:

```bash
git add greeting.txt
git commit -m "Resolve merge conflict in greeting.txt"
```

> **Tip:** VS Code has a built-in merge conflict editor that makes this much easier — it shows "Accept Current", "Accept Incoming", and "Accept Both" buttons.

---

## 4.6 Branch Naming Conventions

Good branch names describe the work being done:

```
feature/user-authentication
bugfix/fix-login-redirect
hotfix/security-patch
docs/update-readme
experiment/new-algorithm
```

Common prefixes:
| Prefix | Purpose |
|--------|---------|
| `feature/` | New functionality |
| `bugfix/` | Bug fixes |
| `hotfix/` | Urgent production fixes |
| `docs/` | Documentation changes |
| `refactor/` | Code restructuring |
| `test/` | Adding or modifying tests |

---

## 4.7 Visualizing Branches

### Command line

```bash
git log --oneline --graph --all --decorate
```

### Alias for convenience

```bash
git config --global alias.lg "log --oneline --graph --all --decorate"

# Now just use:
git lg
```

### GUI tools

- **VS Code** — Source Control panel + GitLens extension
- **GitHub Desktop** — History view
- **gitk** — Built-in graphical viewer (`gitk --all`)

---

## 4.8 Common Branch Workflow (Git Flow Lite)

```
main ────────────────●──────────●──────────● (stable, production-ready)
                    / \        / \        /
feature-a ────────●   ●      /   \      /
                             /     \    /
feature-b ──────────────────●       ●──●
```

1. Start from `main`
2. Create a `feature/` branch for each task
3. Work and commit on your feature branch
4. Merge back to `main` when the feature is done
5. Delete the feature branch

---

## Exercise 4

1. From `main`, create a new branch called `feature/about-page`
2. On that branch, create an `about.md` file and make 2 commits
3. Switch back to `main` and create a different file (e.g., `contact.md`), commit it
4. Merge `feature/about-page` into `main`
5. View the merge with `git log --oneline --graph --all`

**Bonus (Conflict Practice):**
1. Create two branches from `main` that both edit the same line in `README.md`
2. Merge the first branch into `main` (no conflict)
3. Merge the second branch into `main` (conflict!) and resolve it

---

[← Part 3: GitHub Remotes](03_github_remotes.md) | [Next: Part 5 — Collaboration →](05_collaboration.md)
