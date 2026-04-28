
```bash
ssh-keygen -t ed25519 -C "myemail@gmail.com"
#test connectivity with github after ssh pub key copy on github ssh configration
ssh -T git@github.com

#=======
ssh-add -l
Could not open a connection to your authentication agent.

eval "$(ssh-agent -s)"
Agent pid 7165


ssh-add /home/kazamel/.ssh/id_rsa
Identity added: /home/kazamel/.ssh/id_rsa (kazamel@Kazamel)

ssh-add -l
3072 SHA256:YzugGipcwnwaZzsuBxP/mtE5Oxci7HkEdtMBP6+iyuk kazamel@Kazamel (RSA)

git clone git@github.com:Abdulrahman-Kazamel/golang-multi-tier.git


```
