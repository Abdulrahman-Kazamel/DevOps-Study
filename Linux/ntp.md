

```bash
yum install ntp ntpdate -y
systemctl start ntpd
systemctl enable ntpd
systemctl status ntpdddd
ntpdate -u -s 0.centos.pool.ntp.org 1.centos.pool.ntp.org 2.centos.pool.ntp.org
systemctl restart ntpd
timedatectl
hwclock -w
```

