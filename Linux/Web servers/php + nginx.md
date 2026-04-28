


```
sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm




sudo dnf install https://rpms.remirepo.net/enterprise/remi-release-9.rpm



sudo dnf module reset php
sudo dnf module enable php:remi-8.2 -y


sudo dnf install php php-fpm php-cli php-common php-gd php-mysqlnd php-xml php-mbstring php-opcache -y




vi nginx.conf && nginx.conf.default


root /var/www/html;  
index index.php index.html;



location ~ \.php$ {  
	include fastcgi_params;  
	fastcgi_pass unix:/var/run/php-fpm/default.sock;  
	fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;  
}




#change unix socket name 
ls -l /var/run/php-fpm/
vi /etc/php-fpm.d/www.conf

listen = /var/run/php-fpm/default.sock
listen.owner = nginx  
listen.group = nginx  
listen.mode = 0660

systemctl restart php-fpm



vi /etc/nginx/conf.d/php-fpm.conf
server unix:/var/run/php-fpm/default.sock;



grep -R "www.sock" /etc/nginx/

```


