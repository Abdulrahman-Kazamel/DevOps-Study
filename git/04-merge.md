

```bash
cd /usr/src/kodekloudrepos/media

git checkout -b datacenter

cp /tmp/index.html .

git add index.html
git commit -m "Added index.html in datacenter branch"

git push origin datacenter   # important step

git checkout master

git merge datacenter

git push origin master
```



## Key Concepts (your style preserved)

- origin/main = last known remote state
- fetch updates origin/main only
- merge applies changes to local
- pull = fetch + merge
- SSH vs HTTPS mismatch = auth issue
- no commit = no branch = push fails
- upstream = link between local and remote
