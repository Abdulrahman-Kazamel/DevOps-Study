

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

