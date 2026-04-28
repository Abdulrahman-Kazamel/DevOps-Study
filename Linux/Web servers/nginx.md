


```note

server {

    listen 443 ssl;
    server_name _;

    ssl_certificate     /etc/nginx/ssl/certs/nautilus.crt;
    ssl_certificate_key /etc/nginx/ssl/certs/nautilus.key;

}
```


```bash
chmod 600 /etc/pki/nginx/private/nautilus.key
chmod 644 /etc/pki/nginx/nautilus.crt
chown nginx:nginx /etc/pki/nginx/nautilus.crt
chown nginx:nginx /etc/pki/nginx/private/nautilus.key
```


```

# Settings for a TLS enabled server.
 server {
  listen 443 ssl http2;
   listen [::]:443 ssl http2; 
   server_name _;
    root /usr/share/nginx/html; 
  ssl_certificate /etc/pki/nginx/nautilus.crt;  
ssl_certificate_key /etc/pki/nginx/private/nautilus.key;
      ssl_session_cache shared:SSL:1m; 
       ssl_session_timeout 10m; 
        ssl_ciphers PROFILE=SYSTEM; 
         ssl_prefer_server_ciphers on;
          # # # Load configuration files for the default server block.
            include /etc/nginx/default.d/*.conf;
              error_page 404 /404.html; 
               location = /40x.html { # } 
               
 error_page 500 502 503 504 /50x.html;
  location = /50x.html { # } } 
  
  }
```


```bash
nginx -t
systemctl restart nginx
```


## as load balancer 



```
cat /etc/nginx/nginx.conf
# For more information on configuration, see:
#   * Official English Documentation: http://nginx.org/en/docs/
#   * Official Russian Documentation: http://nginx.org/ru/docs/

user nginx;
worker_processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

# Load dynamic modules. See /usr/share/doc/nginx/README.dynamic.
include /usr/share/nginx/modules/*.conf;

events {
    worker_connections 1024;
}

http {
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile            on;
    tcp_nopush          on;
    tcp_nodelay         on;
    keepalive_timeout   65;
    types_hash_max_size 4096;

    include             /etc/nginx/mime.types;
    default_type        application/octet-stream;

    # Load modular configuration files from the /etc/nginx/conf.d directory.
    # See http://nginx.org/en/docs/ngx_core_module.html#include
    # for more information.
    include /etc/nginx/conf.d/*.conf;

    upstream myapp1 {
        server stapp01:6000;
        server stapp02:6000;
        server stapp03:6000;
    }






    server {
        listen       80;
        listen       [::]:80;
        server_name  _;
        root         /usr/share/nginx/html;

        location / {
            proxy_pass http://myapp1;
            }


        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        error_page 404 /404.html;
        location = /404.html {
        }

        error_page 500 502 503 504 /50x.html;
        location = /50x.html {
        }
    }

# Settings for a TLS enabled server.
#
#    server {
#        listen       443 ssl http2;
#        listen       [::]:443 ssl http2;
#        server_name  _;
#        root         /usr/share/nginx/html;
#
#        ssl_certificate "/etc/pki/nginx/server.crt";
#        ssl_certificate_key "/etc/pki/nginx/private/server.key";
#        ssl_session_cache shared:SSL:1m;
#        ssl_session_timeout  10m;
#        ssl_ciphers PROFILE=SYSTEM;
#        ssl_prefer_server_ciphers on;
#
#        # Load configuration files for the default server block.
#        include /etc/nginx/default.d/*.conf;
#
#        error_page 404 /404.html;
#            location = /40x.html {
#        }
#
#        error_page 500 502 503 504 /50x.html;
#            location = /50x.html {
#        }
#    }

}

[loki@stlb01 ~]$ 


```


#### Default load balancing configuration

The simplest configuration for load balancing with nginx may look like the following:

```
 http {
     upstream myapp1 {
        server srv1.example.com;
         server srv2.example.com;
        server srv3.example.com;
    }

     server {
         listen 80;

         location / {
            proxy_pass http://myapp1;
        }
     }
}
```


![[Pasted image 20260419164404.png]]



![[Pasted image 20260419164513.png]]



![[Pasted image 20260419164630.png]]



```
sudo chown -R nginx:nginx /var/www/html


```

### multiple domains on same server
![[Pasted image 20260419165102.png]]



```
mkdir -p /var/www/example /var/www/test
sudo chown -R nginx:nginx /var/www/


```



enable caching 


![[Pasted image 20260419165510.png]]



redirect



![[Pasted image 20260419165910.png]]