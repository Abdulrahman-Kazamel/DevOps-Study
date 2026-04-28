
# 🚀 Ansible Interview Guide (Top 20 Questions & Answers)

---

## 🧠 1. What is Ansible?

**Answer:**  
Ansible is an open-source automation tool used for:

- Configuration management
    
- Application deployment
    
- Task automation
    

✔ Agentless (uses SSH)  
✔ Written in Python  
✔ Uses YAML (easy to read)

---

## 🧠 2. Why use Ansible?

**Answer:**

- No agents required
    
- Easy syntax (YAML)
    
- Fast setup
    
- Idempotent operations
    
- Works over SSH
    

---

## 🧠 3. What is an Inventory in Ansible?

**Answer:**  
Inventory is a file that defines:

- Target hosts
    
- Groups of servers
    
- Connection variables
    

Example:

```ini
[web]
server1
server2
```

---

## 🧠 4. What are Ansible Modules?

**Answer:**  
Modules are small programs used to perform tasks.

Examples:

- `ping` → test connectivity
    
- `yum` → install packages
    
- `service` → manage services
    
- `copy` → copy files
    

---

## 🧠 5. What is a Playbook?

**Answer:**  
A Playbook is a YAML file that defines automation tasks.

Example:

```yaml
- hosts: all
  tasks:
    - name: Install nginx
      yum:
        name: nginx
        state: present
```

---

## 🧠 6. What is Idempotency?

**Answer:**  
Idempotency means:  
👉 Running the same task multiple times gives the same result

Example:

- Installing a package → installs only once
    

---

## 🧠 7. Difference between Ad-hoc commands and Playbooks?

|Ad-hoc|Playbook|
|---|---|
|One-time task|Reusable|
|CLI based|YAML file|
|Quick execution|Structured automation|

---

## 🧠 8. What is `become` in Ansible?

**Answer:**  
Used for privilege escalation (sudo)

Example:

```yaml
become: yes
```

CLI:

```bash
ansible all -b -a "whoami"
```

---

## 🧠 9. What is the difference between `command` and `shell` module?

|command|shell|
|---|---|
|No shell features|Supports shell|
|Safer|More flexible|
|No pipes/redirection|Supports pipes|

---

## 🧠 10. What is a Role in Ansible?

**Answer:**  
Role is a structured way to organize playbooks.

Structure:

```
roles/
  web/
    tasks/
    handlers/
    templates/
    files/
```

---

## 🧠 11. What are Variables in Ansible?

**Answer:**  
Used to store values dynamically.

Example:

```yaml
vars:
  package_name: nginx
```

---

## 🧠 12. What are Facts?

**Answer:**  
Facts are system information collected by Ansible.

Example:

- IP address
    
- OS version
    
- CPU info
    

Command:

```bash
ansible all -m setup
```

---

## 🧠 13. What is Ansible Handler?

**Answer:**  
Handler runs only when notified.

Example:

```yaml
- name: restart nginx
  service:
    name: nginx
    state: restarted
```

---

## 🧠 14. What is `notify` in Ansible?

**Answer:**  
Triggers a handler when a task changes.

Example:

```yaml
notify: restart nginx
```

---

## 🧠 15. What is Ansible Vault?

**Answer:**  
Used to encrypt sensitive data (passwords, keys).

Command:

```bash
ansible-vault encrypt file.yml
```

---

## 🧠 16. What is a Template in Ansible?

**Answer:**  
Templates use Jinja2 for dynamic files.

Example:

```jinja
server_name {{ hostname }}
```

---

## 🧠 17. What is the difference between `copy` and `template`?

|copy|template|
|---|---|
|Static file|Dynamic file|
|No variables|Supports variables|

---

## 🧠 18. How does Ansible connect to remote servers?

**Answer:**

- Uses SSH
    
- Requires Python on remote host
    
- No agent installation needed
    

---

## 🧠 19. What is `ansible.cfg`?

**Answer:**  
Configuration file for Ansible.

Controls:

- Inventory path
    
- Default user
    
- Timeout
    
- SSH settings
    

---

## 🧠 20. What is the difference between `hosts` and `groups`?

**Answer:**

- **Host** → single machine
    
- **Group** → collection of hosts
    

Example:

```ini
[web]
server1
server2
```

---

## 🔥 Bonus Tips (Very Important)

### ✔ Always use modules instead of shell/command when possible

### ✔ Use roles for large projects

### ✔ Keep playbooks idempotent

### ✔ Avoid hardcoding passwords → use Vault

---

## 🎯 Strong Interview Closing Answer

> “I use Ansible for automating configuration and deployments in an agentless way. I prefer playbooks with roles for scalability, ensure idempotency, and use privilege escalation securely with become.”

---