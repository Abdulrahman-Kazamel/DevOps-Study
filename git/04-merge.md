

```bash
cd /usr/src/kodekloudrepos/media

git checkout -b datacenter

cp /tmp/index.html .

git add index.html
git commit -m "Added index.html in datacenter branch"

git push origin datacenter   # important step


### git back to origin branch
git checkout master

## merge changes happened on datacenter to my master branch
git merge datacenter

git push origin master


##git log (main and jenkins) branches have the same state 
git log --oneline --decorate
57a6bfa (HEAD -> main, jenkinsUpdates) nothing change on the code, just adding dummy data on the READ ME file




```


git merge (fast forward) works nice when changes on the branches are connected  directly, and the commits 


if there is no conflicts --> git uses 3 ways merging algorithm  strategy called ORT which creates a new commit and add all other last commit in each branch


in conflicts --> when auto merge fails, there is way to fix the file manually on the master , then add, then commit , and it will create new commit sha1 with the merged content 


in automatic solving tools --> kdiff3
```bash
git config --global merge.tool kdiff3
git config --global merge.tool kdiff3.path "pathToBinary"
git config --global merge.tool kdiff3.trustExitCode false

git config --global diff.guitool kdiff3
git config --global difftool.kdiff3.path "pathToBinary"
git config --global difftool.kdiff3.trustExitCode false

git mergetool 
git commit 
```



