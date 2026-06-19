# Git Repository Restructure & Rebase Troubleshooting Guide

## Overview

This documentation explains a real-world Git troubleshooting scenario involving:

- Accidentally initializing Git in the wrong parent directory
    
- Nested repositories and folder structure problems
    
- Cleaning repository boundaries
    
- Reinitializing a proper Git repository
    
- Connecting to GitHub remote
    
- Handling diverged branches
    
- Resolving Git rebase conflicts
    
- Understanding add/add merge conflicts
    
- Cleaning large files from Git tracking
    
- Best practices for DevOps project repositories
    

---

# Initial Problem

The repository started showing unexpected files and folders from the parent directory.

Example:

```bash
modified:   ../.github/workflows/pipeline.yaml
deleted:    ../app.js

Untracked files:
        ../1st_project/
        ../ansible/
        ../k8_labs/
```

## Why This Happened

The `../` prefix means Git believed the actual repository root existed one level above the current folder.

This usually happens when:

- `git init` was executed in the wrong directory
    
- A parent directory accidentally became a Git repository
    
- Multiple projects existed inside one giant repository unintentionally
    

---

# Original Directory Structure

```text
projects/
├── 1st_project/
├── ansible/
├── k8_labs/
├── flask-automated-app/
├── mastry/
└── .git/
```

Problem:

The `.git` directory existed at the `projects/` level.

Therefore Git tracked ALL subprojects together.

---

# Why This Is Bad

For DevOps and engineering portfolios, unrelated projects should usually be isolated.

Bad Example:

```text
DevOps/.git
```

Tracking:

- Kubernetes labs
    
- Docker projects
    
- Bash scripts
    
- Jenkins data
    
- Ansible labs
    
- Random experiments
    

in one repository.

---

# Recommended Structure

Each project should have its own Git repository.

Correct Structure:

```text
projects/
├── ansible/.git
├── k8_labs/.git
├── flask-automated-app/.git
├── mastry/.git
└── random_labs/.git
```

Benefits:

- Cleaner Git history
    
- Easier CI/CD integration
    
- Better GitHub portfolio organization
    
- Independent branching
    
- Easier collaboration
    
- Cleaner pull requests
    
- Better DevOps workflow
    

---

# Step 1 — Remove Wrong Parent Repository

Move to parent directory:

```bash
cd ..
```

Verify contents:

```bash
ls -la
```

Remove accidental parent Git repository:

```bash
sudo rm -r .git
```

## Explanation

This deletes Git metadata only.

It DOES NOT delete:

- project files
    
- folders
    
- source code
    

It only removes repository tracking from the parent folder.

---

# Step 2 — Initialize Correct Repository

Navigate to actual project:

```bash
cd mastry
```

Initialize Git:

```bash
git init
```

Git created:

```text
mastry/.git/
```

Now only the `mastry` project is tracked.

---

# Step 3 — Rename Branch

Git initialized with:

```text
master
```

Rename to modern standard:

```bash
git branch -m main
```

---

# Step 4 — Connect GitHub Remote

Add remote repository:

```bash
git remote add origin git@github.com:Abdulrahman-Kazamel/devops_mastry.git
```

## Explanation

- `origin` → alias for remote repository
    
- SSH URL used instead of HTTPS
    
- Enables push/pull operations
    

---

# Step 5 — Initial Commit

Stage files:

```bash
git add .
```

Commit:

```bash
git commit -m "initial clean commit"
```

---

# Step 6 — Push Rejected

Attempt:

```bash
git push -u origin main
```

Result:

```text
! [rejected] main -> main (fetch first)
```

---

# Why Push Was Rejected

GitHub remote already contained commits.

Examples:

- README.md
    
- License
    
- Existing project history
    
- GitHub initialization commit
    

Local history and remote history were different.

Git refused to overwrite remote history automatically.

---

# Step 7 — Configure Upstream Branch

Git requested tracking setup:

```bash
git branch --set-upstream-to=origin/main main
```

## What This Means

Now local branch:

```text
main
```

tracks:

```text
origin/main
```

Benefits:

Now these work automatically:

```bash
git pull
git push
```

without specifying remote and branch every time.

---

# Step 8 — Pull With Rebase

Command:

```bash
git pull --rebase
```

---

# Why Rebase Instead of Merge

## Merge

Creates extra merge commits.

History:

```text
A---B---C
     \   \
      D---M
```

## Rebase

Replays commits on top of remote history.

Cleaner history:

```text
A---B---C---D
```

Preferred for:

- cleaner Git history
    
- professional workflows
    
- feature branch management
    

---

# Step 9 — Massive Merge Conflicts

Git produced:

```text
CONFLICT (add/add)
```

Example:

```text
both added: react-docker/package.json
```

---

# What "add/add" Conflict Means

Both repositories independently created the same file.

Git could not decide:

- keep local version?
    
- keep remote version?
    
- merge content?
    

---

# Rebase State

Git entered:

```text
interactive rebase in progress
```

This means:

- rebase paused
    
- waiting for conflict resolution
    
- repository temporarily in detached state
    

---

# Step 10 — Resolve Conflicts

Command used:

```bash
git add .
```

Then:

```bash
git rebase --continue
```

## What Happened Internally

By staging files, Git assumed:

```text
current working tree = resolved version
```

Then rebase continued successfully.

---

# Successful Rebase

Git output:

```text
Successfully rebased and updated refs/heads/main.
```

Meaning:

- local commits replayed successfully
    
- remote history integrated
    
- repository history became linear
    

---

# Step 11 — Successful Push

Command:

```bash
git push origin main
```

Push succeeded.

---

# Large File Warning

GitHub warned:

```text
kube-demo/kubectl.exe is 58 MB
```

---

# Why Large Files Are Bad In Git

Git is optimized for:

- source code
    
- text changes
    
- diff tracking
    

Git performs poorly with:

- binaries
    
- executables
    
- media files
    
- archives
    

Problems caused:

- larger repository size
    
- slower clones
    
- slower pushes/pulls
    
- history bloat
    
- GitHub limits
    

---

# Recommended Cleanup

## Create .gitignore

```bash
touch .gitignore
```

Suggested content:

```gitignore
node_modules/
dist/
build/
*.log
*.exe
.env
```

---

# Remove File From Tracking

```bash
git rm --cached kube-demo/kubectl.exe
```

## Important

`--cached` means:

- remove from Git tracking
    
- keep file locally
    

---

# Commit Cleanup

```bash
git add .
git commit -m "cleanup large binaries and add gitignore"
```

Push changes:

```bash
git push origin main
```

---

# Final Clean Structure

```text
devops/
├── ansible/
├── flask-automated-app/
├── k8_labs/
├── random_labs/
└── mastry/
    ├── .git/
    ├── hello-docker/
    ├── kube-demo/
    ├── react-docker/
    └── vite-project/
```

---

# Real-World Git Concepts Learned

## 1. Git Repository Root

Check actual repository root:

```bash
git rev-parse --show-toplevel
```

Critical for debugging nested repo problems.

---

## 2. Upstream Tracking

Command:

```bash
git branch --set-upstream-to=origin/main main
```

Links local and remote branches.

---

## 3. Rebase Workflow

Used for:

- linear history
    
- professional Git workflow
    
- cleaner commit graph
    

---

## 4. Conflict Resolution

Key commands:

```bash
git status
git add .
git rebase --continue
```

---

## 5. Detached HEAD During Rebase

Temporary Git state during replay process.

Normal during rebase operations.

---

## 6. Git Ignore Best Practices

Never track:

- node_modules
    
- executables
    
- secrets
    
- build artifacts
    
- logs
    

---

# Recommended DevOps Repository Strategy

## Option 1 — Monorepo

One repository for all projects.

Good for:

- tightly coupled systems
    
- shared pipelines
    
- shared deployment workflows
    

Bad for unrelated labs.

---

## Option 2 — Multi-Repo (Recommended)

Separate repositories.

Better for:

- portfolio projects
    
- independent CI/CD
    
- microservices
    
- isolated experiments
    
- cleaner GitHub profile
    

---

# Useful Git Commands Reference

## Check repository status

```bash
git status
```

---

## Show remote repositories

```bash
git remote -v
```

---

## Show current branch

```bash
git branch
```

---

## Show repository root

```bash
git rev-parse --show-toplevel
```

---

## Abort rebase

```bash
git rebase --abort
```

---

## Continue rebase

```bash
git rebase --continue
```

---

## Skip problematic commit

```bash
git rebase --skip
```

---

## Force push

```bash
git push --force
```

Use carefully.

---

# Key Lessons Learned

1. Always verify repository root before initializing Git.
    
2. Keep unrelated projects in separate repositories.
    
3. Learn rebase because it is heavily used professionally.
    
4. Understand merge conflicts instead of fearing them.
    
5. Use `.gitignore` from the beginning.
    
6. Avoid committing large binaries.
    
7. SSH remotes are cleaner for development environments.
    
8. Git conflict resolution is a normal engineering workflow.
    

---

# Final Outcome

Successfully achieved:

- Clean repository architecture
    
- Proper GitHub integration
    
- Correct upstream tracking
    
- Successful rebase workflow
    
- Conflict resolution
    
- Clean project isolation
    
- Better DevOps portfolio organization
    

---

# Suggested Next Improvements

## Add README files

Each project should contain:

- architecture overview
    
- setup steps
    
- Docker usage
    
- Kubernetes deployment steps
    
- screenshots
    
- CI/CD explanation
    

---

## Add GitHub Actions

Potential CI pipeline:

```text
Push → Build → Test → Docker Build → Security Scan → Deploy
```

---

## Add Branch Strategy

Recommended:

```text
main
develop
feature/*
hotfix/*
```

---

## Add Conventional Commits

Examples:

```text
feat: add kubernetes deployment
fix: resolve docker networking issue
refactor: clean react container build
```

---

# End of Documentation