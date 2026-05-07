
---

## 🔥 Most Asked Questions

### 1. Difference between fetch & pull?

👉 Answer:
- `git fetch` → downloads changes (no merge)  
- `git pull` → fetch + merge  

---

### 2. What is origin?

👉 Default remote pointing to your repo

---

### 3. What is upstream?

👉 Original repo (especially in fork workflow)

---

### 4. What is non-fast-forward?

👉 Your branch is behind remote → must pull first

---

### 5. Why `src refspec main does not match`?

👉 No commits exist yet

---

### 6. Why Git asks for password even with SSH?

👉 Remote is HTTPS not SSH

---

### 7. Difference between merge & rebase?

👉 Merge:
- keeps history

👉 Rebase:
- linear history (cleaner)

---

### 8. What is bare repo?

👉 Repo without working directory (used as server)

---

# 🎯 3) Real Interview Debug Scenarios

---

## 🧪 Scenario 1

```bash
git push -u origin main
error: src refspec main does not match any