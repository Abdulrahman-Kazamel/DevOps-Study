

docker network create --driver=bridge  --subnet=100.100.100.0/24 --ip-range=100.100.100.0/24 --gateway=100.100.100.254  my-advanced-network


```bash
   1  exit
    2  halt
    3  docker network create --subnet=192.168.100.0/24 --driver=bridge --gateway=192.168.100.1 web-net 
    4  docker run -d -it -p 80:80 --network web-net --ip 192.168.100.10 --cpus="1" --memory="512m" --name=nginx  nginx
    5  docker ps
    6  curl 192.168.100.10:80
    7  docker run -d -it -p 8080:80 --network web-net --ip 192.168.100.20 --cpus="1" --memory="512m" --name=apache httpd
    8  curl 192.168.100.20:8080
    9  curl 192.168.100.20:80
   10  docker ps
   11  curl http://192.168.100.20:8080
   12  ip a
   13  curl 127.0.0.1:80
   14  curl 127.0.0.1:8080
   15  docker ps
   16  curl 127.0.0.1:80
   17  curl 127.0.0.1:8080
   18  docker ps
   19  curl 127.0.0.1:8080
   20  curl 127.0.0.1:80
   21  history 
```