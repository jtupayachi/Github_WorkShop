# Part 1: Setup & Installation

**Duration:** ~15 minutes

---

## 1.1 Installing Git

### macOS

Git comes pre-installed on most Macs. Verify by opening Terminal:

```bash
git --version
```

If not installed, you'll be prompted to install Xcode Command Line Tools. Alternatively:

```bash
# Using Homebrew
brew install git
```

### Windows

Download the installer from [git-scm.com](https://git-scm.com/download/win) and run it with default settings. This installs **Git Bash**, a terminal emulator you'll use for Git commands.

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install git
```

---

## 1.2 Configuring Git

After installation, set up your identity. This information is attached to every commit you make.

```bash
# Set your name
git config --global user.name "Your Name"

# Set your email (use the same email as your GitHub account)
git config --global user.email "your.email@example.com"
```

### Verify your configuration

```bash
git config --list
```

### Set default branch name (recommended)

```bash
git config --global init.defaultBranch main
```

### Set default editor (optional)

```bash
# For VS Code
git config --global core.editor "code --wait"

# For nano
git config --global core.editor "nano"

# For vim
git config --global core.editor "vim"
```

---

## 1.3 Creating a GitHub Account

1. Go to [github.com](https://github.com)
2. Click **Sign Up**
3. Choose a username, enter your email, and create a password
4. Verify your email address

> **Tip for researchers:** You can get free GitHub Pro features with a university email at [education.github.com](https://education.github.com).

---

## 1.4 Setting Up Authentication

GitHub requires authentication when pushing code. The recommended method is **SSH keys** or **Personal Access Tokens**.

### Option A: SSH Key (Recommended)

#### Step 1 — Generate an SSH key

```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
```

Press Enter to accept the default file location. Optionally set a passphrase.

#### Step 2 — Start the SSH agent and add your key

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

#### Step 3 — Copy the public key

```bash
# macOS
pbcopy < ~/.ssh/id_ed25519.pub

# Linux
cat ~/.ssh/id_ed25519.pub
# Then manually copy the output

# Windows (Git Bash)
clip < ~/.ssh/id_ed25519.pub
```

#### Step 4 — Add the key to GitHub

1. Go to [github.com/settings/keys](https://github.com/settings/keys)
2. Click **New SSH key**
3. Give it a title (e.g., "My Laptop")
4. Paste your key and click **Add SSH key**

#### Step 5 — Test the connection

```bash
ssh -T git@github.com
```

You should see: `Hi username! You've successfully authenticated...`

### Option B: Personal Access Token (HTTPS)

1. Go to [github.com/settings/tokens](https://github.com/settings/tokens)
2. Click **Generate new token (classic)**
3. Give it a name, set expiration, and select the `repo` scope
4. Copy the token and use it as your password when pushing

---

## 1.5 Recommended Tools

| Tool | Purpose |
|------|---------|
| **VS Code** | Code editor with built-in Git support |
| **GitHub Desktop** | GUI client for Git (great for beginners) |
| **GitLens** (VS Code extension) | Enhanced Git visualization in VS Code |
| **Terminal / Git Bash** | Command-line interface for Git |

---

## Exercise 1

1. Open your terminal and verify Git is installed: `git --version`
2. Configure your name and email with `git config`
3. Create a GitHub account (if you don't have one)
4. Set up SSH key authentication and test with `ssh -T git@github.com`

---

[Next: Part 2 — Git Basics →](02_git_basics.md)
