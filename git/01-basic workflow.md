

```bash
git add .  
git commit -m "almost done with architect"  

## First push (important)   This links: local main ↔ remote origin/main
git push -u origin main

git pull


```
### Pull vs Fetch

```bash
git fetch     # get remote changes only  
git merge     # apply to local  
  
# same as  
git pull      # fetch + merge
```

👉 My understanding:

- fetch → update `origin/main`
- merge → update local `main`


### Important understanding

- `(origin/main)` = remote state at last fetch/clone
- It **does NOT auto update**



### remove some unwanted files

```bash
git pull origin main
git rm "Untitled Diagram.drawio" "Untitled Diagram.drawio.png"
git commit -m "Remove unnecessary diagram files"
git push origin main
```
