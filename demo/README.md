# Live Demo Scripts

This folder contains files used for the **live coding demonstration** during the seminar.

---

## Demo Flow (for the speaker)

### Demo 1: First Repository (~5 min)

```bash
# Create and navigate to demo folder
mkdir demo-project && cd demo-project

# Initialize repo
git init

# Create files
cat README.md          # Show pre-made README
cat analysis.py        # Show pre-made script

# First commit
git status
git add .
git status
git commit -m "Initial commit: add README and analysis script"
git log --oneline
```

### Demo 2: Making Changes (~3 min)

```bash
# Edit the analysis script (add the plot function)
# Show the diff
git diff

# Commit the change
git add analysis.py
git commit -m "Add data visualization function"
git log --oneline
```

### Demo 3: Pushing to GitHub (~3 min)

```bash
# (Create repo on GitHub beforehand — show the audience)
git remote add origin git@github.com:YOUR_USERNAME/demo-project.git
git push -u origin main

# Show the repo on GitHub in the browser
```

### Demo 4: Branching & PR (~5 min)

```bash
# Create a feature branch
git switch -c feature/add-statistics

# Add the stats module
cat stats.py

git add stats.py
git commit -m "Add statistical analysis module"
git push -u origin feature/add-statistics

# Go to GitHub → open a Pull Request → walk through the UI
# Merge the PR on GitHub
# Pull locally
git switch main
git pull
git log --oneline --graph --all
```

### Demo 5: Merge Conflict (~5 min)

```bash
# Show conflict_demo.py — two people editing the same line
# Create two branches, show the conflict, resolve it live
```

---

## Files in this folder

| File | Purpose |
|------|---------|
| `README.md` | This file |
| `sample_README.md` | Sample README for the demo project |
| `analysis.py` | Python script used in demo |
| `stats.py` | Module added during branching demo |
| `conflict_demo.py` | File used to demonstrate merge conflicts |
