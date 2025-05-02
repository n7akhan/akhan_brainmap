
# 🧠 Git + GitHub + Linux Workflow Cheat Sheet

A step-by-step guide to managing my Obsidian knowledge base using Git and GitHub from my Linux machine 💻🐧🧠

---

## 📁 1. Clone Your GitHub Repo (first time only)

```bash
cd ~/Desktop
git clone https://github.com/n7akhan/akhan_brainmap.git
```

✅ This creates a local copy of your GitHub repo on your Linux system.

---

## 📦 2. Add New Notes or Folders

- Inside the cloned folder (`akhan_brainmap`), create or edit Markdown files.
  Example:
  ```bash
  cd akhan_brainmap
  mkdir PYTHON
  touch PYTHON/HelloWorld.md
  ```

---

## 🔍 3. Check What Changed

```bash
git status
```

✅ Shows what files are new or modified.

---

** YOU STAGE, THEN ADD, THEN COMMIT!**

## ➕ 4. Stage Your Changes

To add everything:
```bash
git add .
```

Or to add specific file(s):
```bash
git add PYTHON/HelloWorld.md
```

---

## 📝 5. Commit Changes with a Message

```bash
git commit -m "Add HelloWorld.md to PYTHON folder"
```

✅ Commits the changes with a note for future reference.

---

## 🚀 6. Push to GitHub

```bash
git push origin main
```

✅ Uploads your changes to GitHub!

---

## 🔐 7. Set Up GitHub Authentication

If GitHub asks for your username/password and fails:

> **GitHub no longer supports password login via terminal.**

✅ Instead, use a **Personal Access Token (PAT)**:
1. Go to [GitHub → Settings → Developer Settings → Personal Access Tokens](https://github.com/settings/tokens)
2. Generate a new token with `repo` access.
3. Use:
   - **Username**: `n7akhan`
   - **Password**: *your PAT token*

👉 To save it:
```bash
git config --global credential.helper store
```

---

## 📥 8. Pull New Changes (from GitHub to Linux)

If you made changes on GitHub and want to update your local copy:

```bash
git pull origin main
```

✅ This keeps both sides in sync.

---

## 🧼 Extra: Clean Tips

- `git log` → view commit history
- `git diff` → see file-by-file changes
- `git rm filename` → remove a file from Git and disk
- `git rm --cached filename` → remove a file from Git but keep it locally

---

### 🧠 Summary

| Step | Action           | Command/Tool                            |
|------|------------------|------------------------------------------|
| 1️⃣   | Clone repo        | `git clone <repo-url>`                  |
| 2️⃣   | Add files         | `touch` / `mkdir`                       |
| 3️⃣   | Check status      | `git status`                            |
| 4️⃣   | Stage changes     | `git add .` or `git add <file>`         |
| 5️⃣   | Commit            | `git commit -m "message"`               |
| 6️⃣   | Push to GitHub    | `git push origin main`                  |
| 7️⃣   | Auth (PAT) setup  | Use token in place of GitHub password   |
| 8️⃣   | Pull updates      | `git pull origin main`                  |

---

👨‍💻 Built by Arslan with help from Koji 🤝  
📍 Repo: [akhan_brainmap](https://github.com/n7akhan/akhan_brainmap)
