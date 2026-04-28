https://github.com/ahmedsami76/AraBigData 

video at 4:30 is very very important (docker file , docker structure file)

-c means command cmd 
-h hostname itself
docker image rm $(docker image ls -q)   => -q returns image id == ---->this command will remove the return of $().


docker run -e "ACCEPT_EULA=Y" -e "SA_P@ssw0rd" -e "MSSQL_PID=Express" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2019-latest 


-p 80:80   host:container =====<           


--add-host hostname:hostIP myWebSite:172.17.0.2   ==> this added to hosts file. 


Docker Network Types:
	- Bridge (show out network )
	- Host (the containers exposes him self to host and deals as a host )
	- none (dose not take network card  only loop back itself)
	- internal switch (close to bridge but dose not see the out network)
- docker network create myNet
- docker network connect/disconnect myNet containerName 

containers should be immutable ==> nor read /write and stateless, as it simulates applications 


docker data under host is ==  /var/lib/docker/ 
-v hostpath:dockerpath -----> to mount updated dir from host to container 


any instruction make change on file system, adds a new layer 