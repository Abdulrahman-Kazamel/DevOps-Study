
Generate a complete obsidian note about mid level linux for Devops

Here’s a **complete, well-structured Obsidian note** for **Mid-Level Linux for DevOps**—designed for real-world usage, interviews, and daily work.

---

# 🐧 Mid-Level Linux for DevOps Engineer

## 📌 Overview

This note covers **practical Linux skills** required for a **mid-level DevOps engineer**, focusing on:

- System administration
- Networking
- Process & performance management
- Automation & scripting
- Security & troubleshooting

---

# 🧱 1. File System & Disk Management

## 📂 File System Hierarchy

/       -> root  
/etc    -> config files  
/var    -> logs, variable data  
/home   -> users  
/tmp    -> temporary files  
/opt    -> third-party apps  
/usr    -> binaries & libraries

## 💽 Disk Commands

lsblk              # list disks  
df -h              # disk usage  
du -sh *           # folder sizes  
mount /dev/sdb1 /mnt  
umount /mnt

## 🔧 Partitioning

fdisk /dev/sdb  
mkfs.ext4 /dev/sdb1

## 📌 LVM (Logical Volume Manager)

pvcreate /dev/sdb  
vgcreate my_vg /dev/sdb  
lvcreate -L 5G -n my_lv my_vg  
mkfs.ext4 /dev/my_vg/my_lv

---

# 👤 2. Users & Permissions

## 👥 User Management

useradd devuser  
passwd devuser  
usermod -aG sudo devuser

## 🔐 Permissions

chmod 755 file  
chown user:group file

### Permission Meaning

r = read (4)  
w = write (2)  
x = execute (1)

## 🔥 Special Permissions

chmod +s file   # SUID  
chmod +t dir    # Sticky bit

---

# ⚙️ 3. Process Management

## 📊 Monitoring Processes

ps aux  
top  
htop

## 🧠 Process Control

kill -9 PID  
killall nginx

## ⏱️ Background Jobs

command &  
jobs  
fg %1  
bg %1

---

# 🌐 4. Networking

## 🔍 Network Commands

ip a  
ip route  
ping google.com

## 🔌 Ports & Connections

ss -tuln  
netstat -tulnp  
lsof -i :80

## 🌍 DNS & Curl

nslookup google.com  
dig google.com  
curl http://example.com

---

# 📦 5. Package Management

## 🐧 RHEL/CentOS

yum install nginx  
dnf install git

## 🐧 Ubuntu/Debian

apt update  
apt install nginx

---

# 🔄 6. System Services (systemd)

## 📌 Manage Services

systemctl start nginx  
systemctl stop nginx  
systemctl restart nginx  
systemctl status nginx

## 🚀 Enable at Boot

systemctl enable nginx  
systemctl disable nginx

## 🎯 Change Runlevel

systemctl get-default  
systemctl set-default multi-user.target

---

# 📝 7. Logs & Monitoring

## 📂 Log Locations

/var/log/messages  
/var/log/syslog  
/var/log/nginx/

## 🔍 View Logs

tail -f /var/log/messages  
journalctl -u nginx

---

# 🔐 8. Security & Access

## 🔑 SSH

ssh user@server

## 🔒 Key-Based Auth

ssh-keygen  
ssh-copy-id user@server

## 🔥 Firewall

firewall-cmd --add-port=80/tcp --permanent  
firewall-cmd --reload

## 🛡️ SELinux

getenforce  
setenforce 0

---

# ⏰ 9. Cron Jobs & Scheduling

## 📅 Crontab

crontab -e

## 🧾 Format

* * * * * command  
| | | | |  
| | | | └── day of week  
| | | └──── month  
| | └────── day  
| └──────── hour  
└────────── minute

---

# 🧪 10. Shell Scripting (Bash)

## 🧾 Basic Script

#!/bin/bash  
echo "Hello DevOps"

## 🔁 Loop

for i in {1..5}  
do  
  echo $i  
done

## ❓ Condition

if [ -f file.txt ]; then  
  echo "Exists"  
fi

---

# 📊 11. Performance Monitoring

## 📈 System Metrics

top  
vmstat  
iostat  
free -m

## 🧠 CPU & Memory

uptime  
mpstat

---

# 📦 12. Archives & Compression

tar -cvf file.tar dir/  
tar -xvf file.tar  
  
gzip file  
gunzip file.gz

---

# 🔄 13. Environment Variables

echo $PATH  
export VAR=value

Persist:

~/.bashrc

---

# 🧰 14. DevOps Daily Use Cases

## 🚀 Deployment Debug

- Check service: `systemctl status`
- Check logs: `journalctl`
- Check port: `ss -tuln`

## 🐞 Troubleshooting

- CPU high → `top`
- Memory leak → `free -m`
- Disk full → `df -h`

## 🌐 Network Issue

- `ping`
- `curl`
- `telnet host port`

---

# 🎯 15. Interview Key Topics

- Difference between **soft link vs hard link**
- Process vs thread
- systemd vs init
- LVM vs traditional partition
- TCP vs UDP basics
- How Linux handles permissions
- Debugging high CPU/memory

---

# 🧠 Pro Tips (Real DevOps Level)

- Always check logs first 🔥
- Know how to debug, not just commands
- Automate everything (Bash/Ansible)
- Understand **why**, not just **how**

---

# 📚 Suggested Next Topics

- Docker & Kubernetes (Linux containers)
- Advanced Networking (iptables, routing)
- CI/CD pipelines
- Observability (logs, metrics, tracing)

---

If you want, I can generate the **next level note**:

- 🔥 _Advanced Linux for DevOps (Senior level + real scenarios)_
- 🔧 _Linux Troubleshooting Playbook (production cases like AppDynamics/Riverbed)_