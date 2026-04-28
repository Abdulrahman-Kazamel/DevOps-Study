

```
yum install mariadb-server mariadb-backup mariadb-common
 systemctl start mariadb
 systemctl enable mariadb
systemctl status mariadb

 mysql_secure_installation
 
 mysql -u root -p
 
 
 
 
 SELECT User FROM mysql.user;


CREATE DATABASE kodekloud_db9;


CREATE USER 'kodekloud_roy'@'localhost' IDENTIFIED BY 'dCV3szSGNA';


DROP USER bob; 
DROP USER 'kodekloud_roy'@'localhost';





##giving full permision


GRANT SELECT, INSERT, UPDATE ON kodekloud_db9.* TO 'kodekloud_roy'@'localhost';
GRANT ALL PRIVILEGES ON kodekloud_db9.* TO 'kodekloud_roy'@'localhost';





FLUSH PRIVILEGES;
SHOW GRANTS FOR 'kodekloud_roy'@'localhost';
```


