
a. Create a database user `kodekloud_tim` and set its password to `8FmzjvFU6S`.

```
sudo -u postgres psql


CREATE USER kodekloud_tim WITH PASSWORD '8FmzjvFU6S';
```


b. Create a database `kodekloud_db1` and grant full permissions to user `kodekloud_tim` on this database.


```
CREATE DATABASE kodekloud_db1 OWNER kodekloud_tim;
GRANT ALL PRIVILEGES ON DATABASE kodekloud_db1 TO kodekloud_tim;

---

psql -h localhost -d kodekloud_db1 -U kodekloud_tim -p 5432

OR

psql -U kodekloud_tim -d kodekloud_db1

---
### Check database privilege:

\l  ---> output ctc 


```






