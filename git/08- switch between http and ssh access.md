
```bash
ssh -T git@github.com
Hi Abdulrahman-Kazamel! You've successfully authenticated, but GitHub does not provide shell access.

➜  Appd-remote git:(main) ✗ git push origin main
Username for 'https://github.com':
Password for 'https://github.com':


fatal: Authentication failed for 'https://github.com/Abdulrahman-Kazamel/appdynamics.git/'


➜  Appd-remote git:(main) ✗ git remote -v
origin  https://github.com/Abdulrahman-Kazamel/appdynamics.git (fetch)
origin  https://github.com/Abdulrahman-Kazamel/appdynamics.git (push)


➜  Appd-remote git:(main) ✗ git remote set-url origin git@github.com:Abdulrahman-Kazamel/appdynamics.git


➜  Appd-remote git:(main) ✗ git remote -v
origin  git@github.com:Abdulrahman-Kazamel/appdynamics.git (fetch)
origin  git@github.com:Abdulrahman-Kazamel/appdynamics.git (push)

➜  Appd-remote git:(main) ✗ git push origin main
Everything up-to-date
```