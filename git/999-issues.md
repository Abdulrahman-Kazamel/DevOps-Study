

### Pager Issue (terminal shows `(END)`)

Problem:

```
 (END)
```

👉 Reason:

- Git uses pager (less)

### Solutions:

```bash
git --no-pager branch -a

#Disable globally (not always recommended)

git config --global core.pager cat
```


-----------------------------------------------------
#### error: src refspec main does not match any

Cause:  no commits yet

```bash
	git add .
	git commit -m "initial commit"
	git push -u origin main
```

---
#### fatal: current branch has no upstream

```bash
git push --set-upstream origin main
```
---
#### non-fast-forward (rejected push)

Cause: - remote has changes you don’t have

```bash
git pull origin main --rebase  
git push
```
---
#### Authentication asking for username/password Even after SSH success:

```bash
ssh -T git@github.com
```

Cause: - repo is using HTTPS not SSH

```bash
git remote -v
git remote set-url origin git@github.com:Abdulrahman-Kazamel/appdynamics.git
```

---
#### Embedded Repo Problem

Warning: adding embedded git repository
Cause: repo inside repo

```bash
git rm --cached Monitoring/Appd-remote -f
```

------------
#### SSH Agent issue


```bash
ssh-add -l
# error: no agent
# Could not open a connection to your authentication agent.


eval "$(ssh-agent -s)"  
ssh-add ~/.ssh/id_rsa


