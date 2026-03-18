# Part 5: Collaboration — Pull Requests & Code Review

**Duration:** ~25 minutes

---

## 5.1 The Collaboration Workflow

The standard GitHub collaboration model:

```
1. Fork or clone the repository
2. Create a feature branch
3. Make changes and push the branch
4. Open a Pull Request (PR)
5. Team reviews and discusses
6. Merge the PR into main
```

This is how open-source projects, research teams, and companies work together.

---

## 5.2 Pushing a Branch to GitHub

Before opening a Pull Request, push your feature branch:

```bash
# Make sure you're on your feature branch
git switch feature/about-page

# Push the branch to GitHub
git push -u origin feature/about-page
```

Now go to your repository on GitHub — you'll see a banner:

> **"feature/about-page had recent pushes — Compare & pull request"**

---

## 5.3 Creating a Pull Request (PR)

### On GitHub:

1. Click **"Compare & pull request"** (or go to the **Pull Requests** tab → **New pull request**)
2. Fill in:
   - **Title:** A clear summary (e.g., "Add About page")
   - **Description:** What changes were made and why
   - **Reviewers:** Assign team members (if applicable)
   - **Labels:** Categorize (e.g., `enhancement`, `bug`, `documentation`)
3. Click **"Create pull request"**

### Writing a good PR description

```markdown
## What
Added an About page with team information and project description.

## Why
Users need a way to learn about the project and its contributors.

## Changes
- Created `about.md` with project overview
- Added link to About page in `README.md`

## Testing
- Verified markdown renders correctly on GitHub
- Checked all links work

## Screenshots (if applicable)
[Add screenshots here]
```

---

## 5.4 Code Review

### As a Reviewer

1. Go to the PR's **"Files changed"** tab
2. Review the diff line by line
3. Click the `+` icon next to any line to leave a comment
4. Submit your review:
   - **Comment** — general feedback
   - **Approve** — looks good to merge
   - **Request Changes** — needs modifications before merging

### Common review feedback

| Symbol | Meaning |
|--------|---------|
| `nit:` | Nitpick — minor style suggestion, non-blocking |
| `question:` | Asking for clarification |
| `suggestion:` | Proposing an alternative approach |
| `blocker:` | Must be fixed before merging |

### As the PR Author

- Respond to feedback with comments or code changes
- Push new commits to the same branch — the PR updates automatically
- Mark conversations as "Resolved" when addressed

```bash
# Make requested changes
git switch feature/about-page
# ... edit files ...
git commit -am "Address review feedback"
git push
```

---

## 5.5 Merging a Pull Request

Once approved, merge the PR on GitHub:

### Merge options

| Method | Description | When to use |
|--------|-------------|-------------|
| **Create a merge commit** | Preserves full branch history | Default; good for feature branches |
| **Squash and merge** | Combines all PR commits into one | Keeps main history clean |
| **Rebase and merge** | Replays commits on top of main | Linear history, no merge commit |

After merging:
1. Click **"Delete branch"** on GitHub to clean up
2. Locally, update and clean up:

```bash
git switch main
git pull
git branch -d feature/about-page
```

---

## 5.6 Working with Collaborators

### Adding collaborators to your repo

1. Go to **Settings → Collaborators**
2. Click **"Add people"**
3. Enter their GitHub username or email
4. They'll receive an invitation

### Permission levels

| Role | Can do |
|------|--------|
| **Read** | View and clone the repository |
| **Triage** | Manage issues and PRs (no code push) |
| **Write** | Push to branches, merge PRs |
| **Maintain** | Manage repo settings (no destructive actions) |
| **Admin** | Full access including deleting the repo |

---

## 5.7 The Fork & Pull Request Model

For contributing to repositories you **don't own** (e.g., open-source projects):

```
1. Fork the repository          (creates YOUR copy on GitHub)
2. Clone YOUR fork locally      (git clone your-fork-url)
3. Create a feature branch      (git switch -c my-fix)
4. Make changes and push        (git push origin my-fix)
5. Open a PR from your fork     (your-fork → original-repo)
6. Maintainers review & merge
```

### Keeping your fork up to date

```bash
# Add the original repo as "upstream"
git remote add upstream https://github.com/ORIGINAL_OWNER/REPO.git

# Fetch and merge updates
git fetch upstream
git switch main
git merge upstream/main

# Push updates to your fork
git push origin main
```

---

## 5.8 GitHub Issues

Issues are GitHub's built-in task/bug tracking system.

### Creating an issue

1. Go to the **Issues** tab
2. Click **"New issue"**
3. Add title, description, labels, and assignees

### Linking PRs to issues

In your PR description or commit message, use:

```
Fixes #12
Closes #12
Resolves #12
```

This **automatically closes** issue #12 when the PR is merged.

---

## 5.9 Protecting the Main Branch

For team projects, protect `main` from direct pushes:

1. **Settings → Branches → Branch protection rules**
2. Add rule for `main`
3. Enable:
   - ✅ Require a pull request before merging
   - ✅ Require approvals (1 or more)
   - ✅ Require status checks to pass (if you have CI/CD)
   - ✅ Do not allow force pushes

This ensures all changes go through code review.

---

## Exercise 5

### Part A — Solo PR Practice
1. Create a new branch, make changes, and push it to GitHub
2. Go to GitHub and open a Pull Request
3. Review the "Files changed" tab
4. Merge the PR and delete the branch
5. Pull changes to your local `main`

### Part B — Pair Exercise (with a partner)
1. **Person A:** Create a repo and add **Person B** as a collaborator
2. **Person B:** Clone the repo and create a branch with changes
3. **Person B:** Push the branch and open a PR
4. **Person A:** Review the PR, leave comments, and approve
5. **Person A:** Merge the PR
6. Both: Pull the latest `main`

### Part C — Fork Exercise
1. Fork a partner's repository
2. Clone your fork and create a branch with a small change
3. Push and open a PR to the original repository
4. The repo owner reviews and merges

---

[← Part 4: Branching](04_branching.md) | [Next: Part 6 — Advanced Topics →](06_advanced.md)
