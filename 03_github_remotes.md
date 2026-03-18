# Part 3: Working with GitHub Remotes

**Duration:** ~20 minutes

---

## 3.1 What Is GitHub?

**Git** = the version control tool (runs locally on your computer)  
**GitHub** = a cloud platform for hosting Git repositories and collaborating

```
Your Computer                          GitHub (cloud)
┌──────────────┐     git push      ┌──────────────────┐
│  Local Repo  │  ──────────────►  │   Remote Repo    │
│              │                   │                  │
│  (git init)  │  ◄──────────────  │  (github.com)    │
└──────────────┘     git pull      └──────────────────┘
```

Other platforms: GitLab, Bitbucket, Azure DevOps — same Git commands, different hosts.

---

## 3.2 Creating a Repository on GitHub

### Option A: Create on GitHub first (recommended for new projects)

1. Go to [github.com/new](https://github.com/new)
2. Fill in:
   - **Repository name:** `my-first-repo`
   - **Description:** (optional) "My first GitHub project"
   - **Visibility:** Public or Private
   - **Initialize:** Do NOT check "Add a README" (we already have one locally)
3. Click **Create repository**

GitHub will show you the commands to connect your local repo.

### Option B: Fork an existing repository

1. Go to any repository on GitHub
2. Click the **Fork** button (top right)
3. This creates a copy under your account

---

## 3.3 Connecting Local to Remote

### Add a remote

After creating the repo on GitHub, connect your local repository:

```bash
# Using SSH (recommended)
git remote add origin git@github.com:YOUR_USERNAME/my-first-repo.git

# Using HTTPS
git remote add origin https://github.com/YOUR_USERNAME/my-first-repo.git
```

`origin` is the conventional name for your primary remote.

### Verify the remote

```bash
git remote -v
```

Output:
```
origin  git@github.com:YOUR_USERNAME/my-first-repo.git (fetch)
origin  git@github.com:YOUR_USERNAME/my-first-repo.git (push)
```

---

## 3.4 Pushing Code to GitHub

### First push

```bash
git push -u origin main
```

- `-u` (or `--set-upstream`) links your local `main` branch to `origin/main`
- After this, you can just use `git push`

### Subsequent pushes

```bash
git push
```

### What happens when you push

```
Local commits ────────► GitHub repository
(your machine)          (visible to the world)
```

Refresh your GitHub repository page — your files are now online!

---

## 3.5 Cloning a Repository

To download an existing repository from GitHub:

```bash
# Using SSH
git clone git@github.com:USERNAME/REPOSITORY.git

# Using HTTPS
git clone https://github.com/USERNAME/REPOSITORY.git

# Clone into a specific folder
git clone git@github.com:USERNAME/REPOSITORY.git my-folder-name
```

This creates a local copy with the full commit history and remote already configured.

---

## 3.6 Pulling Changes

When others (or you from another computer) push changes, you need to pull them:

```bash
git pull
```

This does two things:
1. **Fetches** new commits from the remote
2. **Merges** them into your current branch

### Fetch without merging

```bash
git fetch
```

This downloads new commits but doesn't change your working files. Useful to check what's new before merging.

```bash
# See what's new after fetching
git log --oneline origin/main..main    # commits you have that remote doesn't
git log --oneline main..origin/main    # commits remote has that you don't
```

---

## 3.7 The Push/Pull Workflow

```
1. Make changes locally
2. git add .
3. git commit -m "description"
4. git pull          ← get latest changes first (avoid conflicts)
5. git push          ← send your changes to GitHub
```

> **Golden Rule:** Always `pull` before you `push` to minimize merge conflicts.

---

## 3.8 Cloning vs. Forking vs. Creating

| Action | When to use | Command |
|--------|-------------|---------|
| **Create** | Starting a brand new project | `git init` + `git remote add` |
| **Clone** | Working on a repo you have access to | `git clone <url>` |
| **Fork** | Contributing to someone else's project | Fork on GitHub, then `git clone` your fork |

---

## 3.9 Viewing Your Repository on GitHub

Once pushed, explore GitHub's features:
- **Code tab** — browse files and folders
- **Commits** — view the full history
- **README.md** — automatically rendered on the repo homepage
- **Issues** — track bugs and feature requests
- **Settings** — manage collaborators, visibility, etc.

---

## Exercise 3

1. Create a new repository on GitHub (don't initialize with README)
2. Connect your local `my-first-repo` to GitHub using `git remote add`
3. Push your commits with `git push -u origin main`
4. Verify your files appear on GitHub
5. Edit a file on GitHub directly (click the pencil icon), commit it
6. Pull the changes to your local machine with `git pull`

**Bonus:** Clone a public repository (e.g., `https://github.com/octocat/Hello-World`) and explore its history with `git log`.

---

[← Part 2: Git Basics](02_git_basics.md) | [Next: Part 4 — Branching & Merging →](04_branching.md)
