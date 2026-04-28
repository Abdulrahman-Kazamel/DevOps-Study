

```bash
cd /usr/src/kodekloudrepos/media

# Create branch
git checkout -b datacenter

# Copy file
cp /tmp/index.html .

# Add & commit
git add index.html
git commit -m "Added index.html in datacenter branch"

# Push datacenter branch (YOU MISSED THIS)
git push origin datacenter

# Switch back to master
git checkout master

# Merge
git merge datacenter

# Push master
git push origin master
```