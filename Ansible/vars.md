

---
- name : Install and start Apache
  hosts: all
  become: yes
  vars:
    package_name: apache2
  tasks:
    - name: Install Apache
      apt:
        name: "{{package_name}}"
        state: present

    - name: Start Apache
      service:
        name: apache2
        state: started
        enabled: yes

```

```bash
ansible-playbook myplaybook.yaml -e "package=nginx"
```



![[Pasted image 20260513192216.png]]