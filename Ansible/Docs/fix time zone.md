# 📘 Ansible Lab Note — Fix Timezone + SSH Host Key Issue

---

# 🎯 Scenario Overview

In a **Stratos Datacenter (Nautilus project)**:

- Multiple application servers:
    - `stapp01` (tony)
    - `stapp02` (steve)
    - `stapp03` (banner)

### 🚨 Problem

Timezone settings are inconsistent across servers.

### ✅ Requirement

Set all servers to:

Asia/Krasnoyarsk

---

# 🧩 Part 1 — Ansible Solution (Core Task)

## 📁 Inventory File

[app_servers]  
stapp01 ansible_user=tony ansible_password=Ir0nM@n  
stapp02 ansible_user=steve ansible_password=Am3ric@  
stapp03 ansible_user=banner ansible_password=BigGr33n  
  
[app_servers:vars]  
ansible_connection=ssh  
ansible_become=true  
ansible_become_method=sudo

---

## ⚙️ Playbook

---  
- name: Set timezone on all application servers  
  hosts: app_servers  
  become: yes  
  
  tasks:  
    - name: Set timezone to Asia/Krasnoyarsk  
      timezone:  
        name: Asia/Krasnoyarsk

---

## ▶️ Execution

ansible-playbook -i inventory.ini set_timezone.yml

---

## 🔍 Verification

ansible app_servers -i inventory.ini -a "timedatectl"

Expected output:

Time zone: Asia/Krasnoyarsk

---

# 💥 Part 2 — Error You Faced

## ❌ Error Message

Using a SSH password instead of a key is not possible because Host Key checking is enabled

---

# 🧠 Root Cause (VERY IMPORTANT)

### 🔐 What is happening internally?

When Ansible connects:

1. Uses **SSH**
2. Uses **password (sshpass)** instead of SSH key
3. SSH tries to verify server identity using:
    
    ~/.ssh/known_hosts
    
4. Server fingerprint is **not موجود**
5. SSH refuses connection (security protection 🚨)

---

# 🔎 Key Concept — Host Key Checking

### 📌 Definition

A security mechanism in SSH to prevent:

- Man-in-the-middle attacks
- Fake servers

### 📁 File Used

~/.ssh/known_hosts

---

# 🛠️ Part 3 — Fixes (3 Approaches)

---

## 🟢 Option 1 — Quick Fix (Best for Exams / Labs)

export ANSIBLE_HOST_KEY_CHECKING=False  
ansible-playbook -i inventory.ini set_timezone.yml

### ✅ Why use it?

- Fast
- Works instantly
- Expected in lab environments

---

## 🟡 Option 2 — Permanent Disable

nano ~/.ansible.cfg

Add:

[defaults]  
host_key_checking = False

---

## 🔵 Option 3 — Secure Fix (Production Best Practice)

ssh-keyscan stapp01 >> ~/.ssh/known_hosts  
ssh-keyscan stapp02 >> ~/.ssh/known_hosts  
ssh-keyscan stapp03 >> ~/.ssh/known_hosts

Then run playbook again.

---

# ⚡ Part 4 — Alternative Solution (If Module Fails)

If `timezone` module not available:

- name: Set timezone manually  
  command: timedatectl set-timezone Asia/Krasnoyarsk

---

# 🚀 Part 5 — Ad-hoc Command (Fast Way)

ansible app_servers -i inventory.ini -b -m timezone -a "name=Asia/Krasnoyarsk"

---

# 🧠 Part 6 — Interview Knowledge

## 🔥 Important Points

### 1. Why use Ansible module instead of command?

- Idempotent (runs safely multiple times)
- Cleaner & standardized

---

### 2. What is sshpass limitation?

- Cannot handle host key checking
- Needs known_hosts OR disabled checking

---

### 3. Best Practice in Real Life

- Use SSH keys (NOT passwords)
- Maintain known_hosts
- Avoid disabling security

---

### 4. Real-world Scenario Answer

If asked:

> “Playbook failed due to SSH issue, what do you do?”

Answer:

1. Check error message
2. Identify host key issue
3. Either:
    - Disable checking (temporary)
    - Add hosts to known_hosts (preferred)

---

# 🧩 Part 7 — Real DevOps Flow (Mental Model)

Ansible → SSH → Authentication → Host Verification → Execute Task

Failure here:

Host Verification ❌

---

# 📌 Part 8 — Key Commands Summary

# Disable checking (temporary)  
export ANSIBLE_HOST_KEY_CHECKING=False  
  
# Run playbook  
ansible-playbook -i inventory.ini set_timezone.yml  
  
# Verify timezone  
ansible app_servers -a "timedatectl"  
  
# Add hosts manually  
ssh-keyscan stapp01 >> ~/.ssh/known_hosts

---

# 🎯 Final Takeaways

- ✅ Always read error messages carefully
- ✅ SSH issues are very common in Ansible
- ✅ Know **3 fixes** (quick / permanent / secure)
- ✅ Prefer modules over raw commands
- ✅ Understand SSH flow (very important for interviews)

---

If you want next step, I can build you:

✅ **Top 20 Ansible troubleshooting scenarios (real interview level)**  
✅ OR **full Ansible roadmap (from zero → advanced DevOps level)**