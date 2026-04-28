



```bash
ssh-keygen -t ed25519 -C "myemail@gmail.com"

ssh -T git@github.com
```


#### SSH Agent issue


```
ssh-add -l
# error: no agent

eval "$(ssh-agent -s)"  
ssh-add ~/.ssh/id_rsa

```


