```
---
 - name: check http server is up on all appservers and nginx up on lb
   hosts: app_servers
   become: yes
   tasks:
    - name: http installed
      ansible.builtin.yum:
        name: httpd
        state: present

    - name: http is up
      ansible.builtin.service:
        name: httpd
        state: started


```



```
---
- hosts: all
  become: yes
  become_user: root
  tasks:
    - name: Install httpd package    
      yum: 
        name: httpd 
        state: installed
    
    - name: Start service httpd
      service:
        name: httpd
        state: started
```