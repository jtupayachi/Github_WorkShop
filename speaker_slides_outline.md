# Speaker Slide Outline

> Use this as a guide for creating presentation slides (PowerPoint, Google Slides, etc.)
> Each section maps to one part of the tutorial.

---

## Slide 1 — Title

**Introduction to Git & GitHub**
- Subtitle: A Hands-On Seminar
- Your name, affiliation, date
- Seminar link/QR code for materials

---

## Slide 2 — Agenda

| # | Topic | Time |
|---|-------|------|
| 1 | Setup & Installation | 15 min |
| 2 | Git Basics | 25 min |
| 3 | GitHub Remotes | 20 min |
| 4 | Branching & Merging | 20 min |
| 5 | Collaboration & PRs | 25 min |
| 6 | Advanced Topics | 15 min |

---

## Slide 3 — Why Version Control?

**The Problem:**
- `report_final.docx`, `report_final_v2.docx`, `report_FINAL_really_final.docx`
- "Which version has the latest changes?"
- "Who changed what and when?"
- "I broke something — how do I go back?"

**The Solution: Git**
- Track every change with full history
- Revert to any previous state
- Collaborate without overwriting each other's work

> **Talking point:** Ask audience "Who has had a file naming disaster?" to engage.

---

## Slide 4 — Git vs. GitHub

| Git | GitHub |
|-----|--------|
| Version control tool | Cloud hosting platform |
| Runs locally | Accessible from anywhere |
| Command-line based | Web interface + API |
| Free & open source | Free tier + paid plans |

> Analogy: Git is like a camera (takes snapshots). GitHub is like a photo album in the cloud (stores & shares them).

---

## Slide 5 — Key Concepts (Visual)

```
Working Directory  →  Staging Area  →  Repository
    (edit files)      (git add)       (git commit)
```

- **Working Directory:** Your actual files
- **Staging Area:** "Shopping cart" — choose what to commit
- **Repository:** Permanent history of snapshots

> **Talking point:** Walk through the analogy of saving a video game (commit = save point).

---

## Slide 6 — Live Demo: First Repository

**Show on screen:**
1. `git init`
2. Create a file
3. `git status` (show red = untracked)
4. `git add .`
5. `git status` (show green = staged)
6. `git commit -m "Initial commit"`
7. `git log --oneline`

> Use the files in the `demo/` folder.

---

## Slide 7 — The Git Workflow Diagram

```
  Edit → Add → Commit → Push
   ↑                      │
   └──────── Pull ◄───────┘
```

- This is the daily cycle you'll use
- Pull to get latest, push to share

---

## Slide 8 — Connecting to GitHub

**Steps:**
1. Create repo on GitHub
2. `git remote add origin <url>`
3. `git push -u origin main`

> **Live Demo:** Push the demo project to GitHub and show it in the browser.

---

## Slide 9 — Branching (Visual)

```
         feature
        /       \
main ──●────●────●──● (merge)
```

- Branches = parallel timelines
- Work on features without breaking main
- Merge when ready

> **Talking point:** "Think of branches as drafts. Main is your published version."

---

## Slide 10 — Live Demo: Branching & Merging

1. `git switch -c feature/add-statistics`
2. Add `stats.py`, commit
3. `git push` the branch
4. Open PR on GitHub (show the UI)
5. Merge the PR
6. `git switch main && git pull`

---

## Slide 11 — Merge Conflicts

**When two people edit the same lines:**

```
<<<<<<< HEAD
Hello from Main
=======
Hello from Branch A
>>>>>>> branch-a
```

**Resolution:**
1. Open the file
2. Choose which version to keep
3. Remove conflict markers
4. `git add` + `git commit`

> **Live Demo:** Use `conflict_demo.py` to show a real conflict.

---

## Slide 12 — Pull Requests

**The collaboration workflow:**
1. Create branch
2. Make changes + push
3. Open Pull Request
4. Team reviews code
5. Discuss and improve
6. Merge when approved

> Show a real PR on GitHub: Files Changed tab, comments, approval.

---

## Slide 13 — Code Review Tips

- Be constructive and specific
- Explain the "why" behind suggestions
- Use prefixes: `nit:`, `suggestion:`, `question:`, `blocker:`
- Approve when satisfied, request changes when needed

---

## Slide 14 — Best Practices

1. **Commit often** — small, focused commits
2. **Write clear messages** — imperative mood, explain why
3. **Use branches** — never commit directly to main
4. **Pull before push** — avoid conflicts
5. **Use .gitignore** — keep the repo clean
6. **Never commit secrets** — no passwords or API keys
7. **Review PRs** — learn from each other

---

## Slide 15 — Useful Resources

- **Cheat Sheet** — (hand out printed copies or share link)
- **Git Book:** git-scm.com/book
- **GitHub Skills:** skills.github.com
- **Learn Git Branching:** learngitbranching.js.org
- **This tutorial:** (link to your repo)

---

## Slide 16 — Exercise Time!

**Hands-on activity (choose based on time):**

- **Beginner:** Create a repo, make commits, push to GitHub
- **Intermediate:** Create a branch, open a PR, merge it
- **Advanced:** Fork a partner's repo, contribute via PR

> Set a timer. Walk around and help participants.

---

## Slide 17 — Q&A

**Questions?**

- Contact info
- Link to materials
- QR code to the GitHub repo with this tutorial

---

## Speaker Notes & Tips

### Before the seminar
- [ ] Test your SSH key / GitHub login
- [ ] Create the demo repository on GitHub (empty, no README)
- [ ] Have the demo files ready in `demo/`
- [ ] Test all commands work on the projector laptop
- [ ] Print cheat sheets for participants
- [ ] Prepare a backup plan if WiFi is slow (screenshots of GitHub UI)

### During the seminar
- Go slow during live demos — narrate every command
- Ask the audience to follow along on their laptops
- Pause after each section for questions
- Use `git status` frequently to show what's happening
- If something breaks, use it as a teaching moment!

### Timing guide
- If running short on time: skip Part 6 (Advanced) and do more exercises
- If audience is advanced: spend less time on Parts 1-2, more on Parts 4-5
- Always leave time for hands-on exercises — it's the most valuable part
