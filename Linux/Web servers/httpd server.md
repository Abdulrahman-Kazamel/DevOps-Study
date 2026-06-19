



```bash
#!/bin/bash
yes | sudo apt update && yes | sudo apt install apache2
sudo chown -R $USER:$USER /var/www/html
echo "</h1>Server Details</h1>
<p><strong>Hostname:</strong> $(hostname) </p>
<p><strong>IP Address:</strong> $(hostname -I | cut -d" " -f1)</p> " | sudo tee /var/www/html/index.html
sudo systemctl restart apache2
### or 


sudo chown -R $USER:$USER /var/www/html
echo "</h1>Server Details</h1>
<p><strong>Hostname:</strong> $(hostname) </p>
<p><strong>IP Address:</strong> $(hostname -I | cut -d" " -f1)</p> " > /var/www/html/index.html


```

# 🧠 Apache Not Reachable on Port 8084 – Troubleshooting Runbook

## 📌 Scenario

Monitoring system reported:

> Apache service on `stapp01` is not reachable on port `8084` from jump host.

---

## 🎯 Objective

- Restore connectivity to Apache on port `8084`
- Ensure access from jump host:

curl http://stapp01:8084

- ❗ Do NOT compromise security (no disabling firewall/SELinux)

---

## 🔍 Step 1: Verify Apache Service

### Check if Apache is running

systemctl status httpd

### Check listening ports

netstat -tulpn | grep 8084

### ✅ Observed

tcp6 :::8084 LISTEN httpd

### 🧠 Insight

- Apache is running
- But listening only on **IPv6**

---

## 🔧 Step 2: Fix Apache Binding (IPv4 Issue)

### Problem

- Jump host uses IPv4
- Apache bound only to IPv6 → not reachable

### Fix

Edit config:

vi /etc/httpd/conf/httpd.conf

Update:

Listen 8084

To:

Listen 0.0.0.0:8084

### Restart Apache

systemctl restart httpd

---

## 🔍 Step 3: Verify Fix

netstat -tulpn | grep 8084

### ✅ Expected

tcp 0.0.0.0:8084 LISTEN httpd

---

## 🧪 Step 4: Local Testing

curl http://localhost:8084

### ✅ Result

- Working → Apache OK

---

## ❌ Step 5: Remote Test Failure

From jump host:

curl http://stapp01:8084

### ❌ Error

No route to host

---

## 🧠 Root Cause Analysis

### Key Observations

|Component|Status|
|---|---|
|Apache|✅ Running|
|Port Binding|✅ Correct|
|SELinux|❌ Disabled|
|firewalld|❌ Not installed|
|UFW|❌ Not installed|

👉 Remaining suspect: **iptables**

---

## 🔥 Step 6: Investigate iptables

### Check rules

iptables -L -n

### 🧠 Insight

- Traffic likely **blocked or rejected**
- Causes:
    - DROP rule
    - REJECT rule

---

## 🔓 Step 7: Fix iptables (Secure Way)

### Allow only required port

iptables -I INPUT -p tcp --dport 8084 -j ACCEPT

### 💾 Save rules

iptables-save > /etc/sysconfig/iptables

---

## 🔍 Step 8: Verify Rule

iptables -L -n | grep 8084

---

## 🌐 Step 9: Final Test

From jump host:

curl http://stapp01:8084

### ✅ Expected Result

- Apache page loads successfully

---

## 🚫 Security Considerations

### ❌ Avoid

systemctl stop firewalld  
ufw disable  
iptables -F  
setenforce 0

### ✅ Followed Principle

> **Least Privilege Access**

- Only opened port `8084`
- No global security changes

---

## 🧠 Key Concepts Learned

### 1. Difference Between Errors

|Error Message|Meaning|
|---|---|
|Connection refused|Service not running|
|No route to host|Network/firewall block|
|Timeout|Packet dropped silently|

---

### 2. IPv4 vs IPv6 Binding

|Binding Type|Meaning|
|---|---|
|`:::8084`|IPv6 only|
|`0.0.0.0:8084`|IPv4 (all interfaces)|

---

### 3. Firewall Layers in Linux

|Tool|Role|
|---|---|
|firewalld|High-level firewall manager|
|UFW|Simplified firewall|
|iptables|Low-level packet filtering (root cause here)|

---

## 🎯 Final Interview Answer

> Apache was running but initially bound only to IPv6, which prevented IPv4 access. After fixing the binding, the service was reachable locally but not remotely. Since no firewall service was active, the issue was traced to iptables rules blocking the port. I securely allowed TCP port 8084 using iptables without disabling any security controls, restoring connectivity from the jump host.

---

## 🔥 Pro Troubleshooting Flow (Golden Path)

1. Check service → ✅
2. Check port binding → ⚠️
3. Fix binding → ✅
4. Test locally → ✅
5. Test remotely → ❌
6. Check firewall layers:
    - firewalld ❌
    - UFW ❌
    - iptables ✅
7. Fix rule → ✅

---

## 🚀 Real-World Insight (APM / NPM)

This exact scenario is common in:

- AppDynamics troubleshooting
- Riverbed packet analysis
- Production outages

👉 Always think in layers:

1. Application
2. OS
3. Network
4. Security