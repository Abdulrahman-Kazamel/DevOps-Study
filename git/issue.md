

why in my terminal i get the output like this * main remotes/origin/Abdulrahman-Kazamel-patch-1 remotes/origin/Abdulrahman-Kazamel-patch-2 remotes/origin/Abdulrahman-Kazamel-patch-3 remotes/origin/HEAD -> origin/main remotes/origin/errors remotes/origin/main
(END) 
not just get back to the terminal


```bash
git --no-pager branch -a
#Disable globally (not always recommended)
git config --global core.pager cat

```


```bash
git pull origin main
git rm "Untitled Diagram.drawio" "Untitled Diagram.drawio.png"
git commit -m "Remove unnecessary diagram files"
git push origin main
```