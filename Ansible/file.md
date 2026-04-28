
# 📘 **Ansible File Creation on Remote Hosts — Full Note**

## 🎯 **Objective**

Use Ansible to:

- Define an inventory of application servers
- Create a file on all servers
- Set permissions
- Assign different ownership per server

---

## 🧱 **1. Inventory Configuration**

📍 Path:

~/playbook/inventory

📄 Content:

[app_servers]  
stapp01 ansible_host=<IP1> ansible_user=tony ansible_password=Ir0nM@n file_owner=tony  
stapp02 ansible_host=<IP2> ansible_user=steve ansible_password=Am3ric@ file_owner=steve  
stapp03 ansible_host=<IP3> ansible_user=banner ansible_password=BigGr33n file_owner=banner

### 🧠 Key Concepts

- **Inventory Group** → `[app_servers]`
- **Host Variables** → defined inline per server
- `file_owner` → custom variable used later in playbook

---

## ⚙️ **2. Playbook Configuration**

📍 Path:

~/playbook/playbook.yml

📄 Content:

---  
- name: Create file on all app servers  
  hosts: app_servers  
  become: yes  
  
  tasks:  
  
    - name: Create blank file with correct permissions and ownership  
      file:  
        path: /usr/src/appdata.txt  
        state: touch  
        mode: '0655'  
        owner: "{{ file_owner }}"  
        group: "{{ file_owner }}"

---

## 🔍 **3. Module Explanation (file module)**

|Parameter|Purpose|
|---|---|
|`path`|Target file path|
|`state: touch`|Create file if not exists|
|`mode`|File permissions|
|`owner`|File owner|
|`group`|File group|

---

## 🔐 **4. Permissions Explained**

0655

Breakdown:

- **0** → octal indicator
- **6 (rw-)** → owner
- **5 (r-x)** → group
- **5 (r-x)** → others

---

## 👤 **5. Dynamic Ownership Logic**

Instead of hardcoding:

owner: tony   ❌

We use:

owner: "{{ file_owner }}"   ✅

✔ This allows:

- stapp01 → tony
- stapp02 → steve
- stapp03 → banner

---

## ⚡ **6. Execution Command**

cd ~/playbook  
ansible-playbook -i inventory playbook.yml

---

## 🚨 **7. Common Mistakes**

### ❌ 1. Missing Privilege Escalation

become: yes

Without it → permission denied on `/usr/src`

---

### ❌ 2. Incorrect Permission Format

mode: 0655   ❌ (may misbehave)  
mode: '0655' ✅

---

### ❌ 3. Hardcoding Owner

Fails requirement of per-server ownership.

---

### ❌ 4. Forgetting Host Variables

Without `file_owner`, playbook breaks.

---

## 🧠 **8. Best Practice Insight**

Instead of inline variables, in real projects you would use:

- `host_vars/`
- `group_vars/`

Example:

host_vars/  
  stapp01.yml  
  stapp02.yml  
  stapp03.yml

---

## 🏁 **Final Outcome**

After execution, all servers will have:

/usr/src/appdata.txt

With:

- ✅ Correct permissions → `0655`
- ✅ Correct owner per server
- ✅ Created automatically if not exists

---

## 💡 **Pro Tip (Exam Trick)**

Whenever you see:

> “different value per host”

👉 Immediately think:  
**Host Variables (`inventory` or `host_vars`)**