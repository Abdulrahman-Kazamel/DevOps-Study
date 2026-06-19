

```

[app]
stapp01

[app:vars]
ansible_user=tony
ansible_ssh_pass=Ir0nM@n
ansible_ssh_common_args=-o StrictHostKeyChecking=no
```

ansible all -m setup
![[Pasted image 20260513200451.png]]

## ansible.cfg

```
setting default user.


[defaults]
remote_user = your_default_username

```



![[Pasted image 20260513201728.png]]

