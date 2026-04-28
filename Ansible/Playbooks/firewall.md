



```
# make sure installaion through:
ansible-galaxy collection install ansible.posix



- name: Allow HTTPS traffic
  ansible.posix.firewalld:
    service: https
    permanent: true
    immediate: true
    state: enabled




- name: Open port 8081/tcp
  ansible.posix.firewalld:
    port: 8081/tcp
    permanent: true
    state: enabled



- name: Add eth0 to internal zone
  ansible.posix.firewalld:
    zone: internal
    interface: eth0
    permanent: true
    state: enabled




- name: Block specific IP address
  ansible.posix.firewalld:
    rich_rule: 'rule family="ipv4" source address="192.168.1.100" reject'
    permanent: true
    state: enabled





```