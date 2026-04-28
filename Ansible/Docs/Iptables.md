

10.244.195.236


```
[app_servers]
stapp01 ansible_user=tony ansible_password=Ir0nM@n ansible_become_pass=Ir0nM@n
stapp02 ansible_user=steve ansible_password=Am3ric@ ansible_become_pass=Am3ric@
stapp03 ansible_user=banner ansible_password=BigGr33n ansible_become_pass=BigGr33n

[lb]
stlb01 ansible_user=loki ansible_password=Mischi3f ansible_become_pass=Mischi3f

[app_servers]
appone ansible_user=root 
apptwo ansible_user=root 
appthree ansible_user=root 

100.100.100.100 db



```



```
---
- name: Configure iptables on app servers
  hosts: app_servers
  become: yes

  vars:
    lbr_ip: 10.244.81.20    

  tasks:

    - name: Install iptables
      yum:
        name: iptables
        state: present

    - name: Start and enable iptables
      service:
        name: iptables
        state: started
        enabled: yes

    - name: Allow port 5000 from LBR
      iptables:
        chain: INPUT
        protocol: tcp
        destination_port: 5000
        source: "{{ lbr_ip }}"
        jump: ACCEPT
        rule_num = 1

    - name: Block port 5000 from others
      iptables:
        chain: INPUT
        protocol: tcp
        destination_port: 5000
        jump: DROP
        rule_num = 2

    - name: Save iptables rules
      shell: iptables-save > /etc/sysconfig/iptables
      
      
      
      
      
      
         "ansible_all_ipv4_addresses": [
        10.244.244.168 stapp01 
         10.244.97.159 stapp02
         10.244.240.128 stapp03
    ]
}
ok: [stapp02] => {
    "ansible_all_ipv4_addresses": [
        "stapp02 10.244.97.159"
    ]
}
ok: [stapp03] => {
    "ansible_all_ipv4_addresses": [
        "stapp03 10.244.240.128"
```



correct version



```root@jump-host ~# cat test.yml 
---
########################################
# 1. Get LB IP dynamically
########################################
- name: Get LB IP
  hosts: stlb01
  gather_facts: yes
  tasks:
    - name: Store LB IP as fact
      set_fact:
        lbr_ip: "{{ ansible_default_ipv4.address }}"


########################################
# 2. Get Apache port from stapp01
########################################
- name: Get Apache Port
  hosts: stapp01
  become: yes
  tasks:
    - name: Read Apache listening port
      shell: "ss -tulpn | awk '/httpd/ {print $5}' | cut -d':' -f2 | head -n1"
      register: apache_port_result
      changed_when: false

    - name: Store Apache port
      set_fact:
        apache_port: "{{ apache_port_result.stdout }}"


########################################
# 3. Configure firewall on all app servers
########################################
- name: Configure iptables
  hosts: app_servers
  become: yes

  vars:
    lbr_ip: "{{ hostvars['stlb01'].lbr_ip }}"
    apache_port: "{{ hostvars['stapp01'].apache_port }}"

  tasks:

    ################################################
    # Install + enable service
    ################################################
    - name: Install iptables
      yum:
        name: iptables
        state: present

    - name: Enable iptables service
      service:
        name: iptables
        state: started
        enabled: yes


    ################################################
    # CRITICAL FIX: remove conflicting old rules
    ################################################
    - name: Flush existing INPUT rules (IMPORTANT FIX)
      iptables:
        chain: INPUT
        flush: yes


    ################################################
    # Apply correct firewall rules
    ################################################
    - name: Allow Apache from LB only
      iptables:
        chain: INPUT
        protocol: tcp
        destination_port: "{{ apache_port }}"
        source: "{{ lbr_ip }}"
        jump: ACCEPT
        state: present
        rule_num: 1
    - name: Block Apache from all others
      iptables:
        chain: INPUT
        protocol: tcp
        destination_port: "{{ apache_port }}"
        source: "0.0.0.0/0"
        jump: DROP
        state: present
        rule_num: 2


    ################################################
    # Persist rules
    ################################################
    - name: Save iptables rules permanently
      shell: iptables-save > /etc/sysconfig/iptables
      changed_when: false
```