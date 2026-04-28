# 🧠 Ansible Task: Set GUI as Default Runlevel (No Reboot)

## 📌 Task Overview

We have 3 application servers:

- stapp01 (user: tony)
    
- stapp02 (user: steve)
    
- stapp03 (user: banner)
    

🎯 Goal:  
Set all servers to boot into **GUI mode (graphical.target)** using Ansible  
🚫 Without rebooting the servers

---

## 🏗️ What is Ansible?

**Ansible** is a configuration management tool used to:

- Automate server tasks
    
- Run commands on multiple machines at once
    
- Avoid manual SSH into each server
    

👉 It works using:

- SSH (no agent required)
    
- Inventory file (list of servers)
    

---

## ⚙️ Step 1: Install Ansible

```bash
yum install -y ansible
```

✔ Installs Ansible on the control node (jump-host)

---

## 📂 Step 2: Inventory File

Path:

```bash
/etc/ansible/hosts
```

Content:

```ini
[app_servers]
stapp01 ansible_user=tony ansible_password=Ir0nM@n ansible_become_pass=Ir0nM@n
stapp02 ansible_user=steve ansible_password=Am3ric@ ansible_become_pass=Am3ric@
stapp03 ansible_user=banner ansible_password=BigGr33n ansible_become_pass=BigGr33n
```

### 🔍 Explanation:

|Parameter|Meaning|
|---|---|
|`app_servers`|Group name (used in commands)|
|`stapp01`|Hostname|
|`ansible_user`|SSH username|
|`ansible_password`|SSH password|
|`ansible_become_pass`|sudo password|

💡 Why we added passwords here?  
→ So Ansible doesn’t ask interactively

---

## 🔌 Step 3: Test Connection

```bash
ansible app_servers -m ping
```

✔ Expected output:

```
pong
```

### 🔍 Explanation:

- `-m ping` → Ansible module to test connectivity
    
- Confirms SSH + Python working
    

---

## 🧑‍💻 Step 4: Execute the Task

```bash
ansible app_servers -b -m command -a "systemctl set-default graphical.target"
```

---

## 🔍 Breakdown of Command

|Part|Meaning|
|---|---|
|`ansible`|CLI tool|
|`app_servers`|Target group|
|`-b`|Become (sudo)|
|`-m command`|Use command module|
|`-a`|Arguments to command|
|`"systemctl set-default graphical.target"`|Actual Linux command|

---

## ⚙️ What is `graphical.target`?

In Linux (systemd):

|Old Runlevel|New Target|
|---|---|
|Runlevel 3|multi-user.target (CLI)|
|Runlevel 5|graphical.target (GUI)|

👉 We are switching from:

```
multi-user.target ❌
```

to:

```
graphical.target ✅
```

---

## 🚫 Why No Reboot?

Command:

```bash
systemctl set-default graphical.target
```

✔ Only changes **future boot behavior**  
❌ Does NOT affect current running state

---

## ✅ Step 5: Verify

```bash
ansible app_servers -a "systemctl get-default"
```

✔ Expected:

```
graphical.target
```

---

## ❗ Common Errors & Fixes

### 1. ❌ Missing sudo password

```
Missing sudo password
```

✔ Fix:

- Add `ansible_become_pass` in inventory
    

---

### 2. ❌ Permission denied / timeout

✔ Cause:

- Not using `-b` (sudo)
    

✔ Fix:

```bash
-b
```

---

### 3. ❌ Incorrect sudo password

✔ Fix:

- Ensure password matches SSH user
    

---

## 🧠 Key Concepts (Important for Interviews)

### 🔹 Ansible Modules

- `ping` → test connectivity
    
- `command` → run Linux commands
    
- `shell` → run shell commands
    

---

### 🔹 Become (Privilege Escalation)

```bash
-b
```

→ Run command as root

---

### 🔹 Inventory

Defines:

- Servers
    
- Users
    
- Credentials
    

---

## 🚀 Pro Tip (Senior Level)

Instead of using command module:

```yaml
- name: Set default target
  hosts: app_servers
  become: yes
  tasks:
    - name: Set GUI
      command: systemctl set-default graphical.target
```

Run:

```bash
ansible-playbook playbook.yml
```

---

## 🏁 Final Result

✔ All servers now boot into GUI  
✔ No reboot performed  
✔ Task completed using Ansible automation

---

## 💬 Summary

- Installed Ansible
    
- Configured inventory with credentials
    
- Used `-b` for sudo access
    
- Executed systemctl command remotely
    
- Verified changes successfully
    

---
