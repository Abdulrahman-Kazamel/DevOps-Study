

## 🧩 Scenario Summary

We had a Git repository with two commits:

```
A → initial commitB → add data.txt file (HEAD)
```

The task:

> Revert the latest commit (HEAD) and use commit message: `revert beta`

---

## ❌ Incorrect Approach Used

```
git revert -n 744eee31c56e5d1c9git add .git commit -m "revert beta"
```

### 🔍 What went wrong:

- Targeted **wrong commit** → initial commit instead of HEAD
- Used `-n` (no commit), which:
    - Applies changes without committing
    - Requires manual `git add` + `git commit`
- Result: ❌ Did not meet requirement

---

## ✅ Correct Approach

```
git revert HEAD
```

Then set message:

```
revert beta
```

### 🔍 What this does:

- Reverts **latest commit (HEAD)**
- Automatically creates a new commit
- No need for staging or manual commit

---

## 🧠 Core Concept: What `git revert` Really Does

> **git revert = Undo changes by creating a new commit**

### ✔ Key Behavior:

- Does **NOT delete commits**
- Does **NOT move HEAD backward**
- Creates a new commit that cancels previous changes

---

## 📊 Visual Comparison

### Before:

```
A (initial commit)B (add data.txt) ← HEAD
```

### After `git revert HEAD`:

```
A (initial commit)B (add data.txt)C (revert beta) ← HEAD
```

✔ Commit **B still exists**  
✔ Commit **C undoes B**

---

## 🔁 What You Thought vs Reality

### ❌ Misunderstanding:

> “revert moves me one commit back”

### ✅ Correct Understanding:

> **revert creates a new commit that undoes a previous commit without changing history**

---

## 🆚 `git revert` vs `git reset`

|Feature|`git revert`|`git reset --hard`|
|---|---|---|
|Moves HEAD backward|❌ No|✅ Yes|
|Deletes commits|❌ No|✅ Yes|
|Creates new commit|✅ Yes|❌ No|
|Safe for shared repos|✅ Yes|❌ No|
|Use case|Undo safely|Rewrite history|

---

## ⚙️ Special Option Used

### `-n` (or `--no-commit`)

```
git revert -n <commit>
```

- Applies revert changes
- Does NOT commit automatically
- Requires:
    
    ```
    git add .git commit -m "message"
    ```
    

✔ Useful for combining multiple reverts  
❌ Risky if you target wrong commit (like in your case)

---

## 🎯 Best Practice Rule

- Undo last commit safely:
    
    ```
    git revert HEAD
    ```
    
- Undo specific commit:
    
    ```
    git revert <commit-hash>
    ```
    
- Avoid `reset` if repo is shared

---

## 🧠 Interview Insight

If asked:

> “How do you undo a commit in a shared repository?”

✅ Answer:

> Use `git revert` because it preserves history and safely undoes changes by creating a new commit.

---

## 🚀 Final Takeaway

- `revert` = **safe undo (adds commit)**
- `reset` = **dangerous undo (removes commit)**
- Always double-check the **commit hash**
- Use `HEAD` when you mean “latest commit”