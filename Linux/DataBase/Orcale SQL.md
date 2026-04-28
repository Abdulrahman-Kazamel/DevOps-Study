On delete cascase delete all employee with that foreign key 
Set null is allowed if I didn't set before Not null,
also with default ,  allowed only if I set the default before. 

On update cascase , for example if i update to 5 , update all emp department number to 5 instead of 1 
 
Orcale 10G supports on delete (Set Null, Cascade) and dose not support On update

alter table table name modify column_name varchar(50) instead of varchar(30), but no constraint could be modified but i'm able to add


fundamental of database systems 7th Copyright © 2016 Ramez Elmasri and Shamkant B. Navathe




```sql
Select Fname,Dname,salay From Employee E  , Department D , project P where E.Dno = D.Dnumber And P.Dnum = D.Dnumber And P.Pnumber Exist(Select Pno From Works_on ,Employee where works_on.Essn = Employee.Ssn and Employee.Fname Like 'HANY');
```