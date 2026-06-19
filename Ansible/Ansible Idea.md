create machine agent as as service configuration in all appdynamics services


without ansible, configuration drift happens 
ansible based on ssh. 



create sudo user on ansible master and nodes

```bash
sudo useradd -m -s /bin/bash ansadmin
sudo passwd ansadmin
sudo usermod -aG sudo ansadmin
su - ansadmin
ssh-keygen 

##then on each host copy the public keys to the autherized_keys
mkdir ~/.ssh


```

### stopping asking for sudo password
```bash
sudo vim visudo 
#add you user on master node and each node 
ansadmin ALL=(ALL) NOPASSWD: ALL 
```


###default ansible configuration file ansinble.cfg 

```
[defaults]
inventorty = /etc/ansible/hostsFileName
remote_user = ansadmin
host_key_checking = false # do you to contuntui message 
```

![[Pasted image 20260513190954.png]]

```
ansible web -m package -a "name=nginx state=present" --become
```




