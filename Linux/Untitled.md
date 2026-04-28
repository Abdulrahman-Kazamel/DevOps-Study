

 cat /scripts/beta_backup.sh 
#!/bin/bash
zip xfusioncorp_beta.zip /var/www/html/beta
#tar -czvf  xfusioncorp_beta.zip /var/www/html/beta
mv xfusioncorp_beta.zip /backup/
scp /backup/xfusioncorp_beta.zip natasha@ststor01:/backup




grep -o "Text" /root/nautilus.xml | wc -l
66
[root@jump-host ~]# grep -o "Torpedo" /root/nautilus.xml | wc -l
0
[root@jump-host ~]# sed -i 's/Text/Torpedo/g' /root/nautilus.xml 
[root@jump-host ~]# grep -o "Torpedo" /root/nautilus.xml | wc -l
66
[root@jump-host ~]# grep -o "Text" /root/nautilus.xml | wc -l
0
[root@jump-host ~]# 