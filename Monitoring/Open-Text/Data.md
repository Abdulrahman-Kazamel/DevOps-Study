
OPTIC concept , one dashboard tool for each product
COSO  collect once, store once , one database as (ware house) to give more insights and more intelligent report

Operation Bridge (Monitoring for change "most 70%-80% incidents comes after a change or fault configuration " you will be able to see every change happens in your environment ),
as management console for whole of my data and able to integrate with variety of technologies 
Infra monitor& management /Application Monitor& management

Manger of manger (MOM) => capable  to integrate with a lot of vendors 
OB => it makes monitor / Observability / AIOps 


by data lake ware house AI  (actionable insights)and RCA / Anomaly detection 

OB dashboard  => 
services dependency tree (Application topology automatic discovery by management pack  & Network topology automatic discovery through NOM  ) /
KPI grouped Health indicators (impacted business services  ) / 
Event details for RCA (automatic correlate network & application dependent failure &"ability to train the algorithm to customer specific needs") /
performance graph 

OB = integrate with all products and with 3th party products 


OB APM
1- Visualize App Health and business impact 
2- track real user performance and availability  
3- visualize business services by region 
4- access server response time to isolate  individual transaction calls  

OB BVD business value dashboard or stakeholders dashboard (reduce MTTR with cross domain insights in real time)
1- System, Network, Application Availability from multiple source and locations.
2- System, Network, Application Performance in a single pane to detect problem hotspots 



    
### DB
Each product has it's own database for it's (configuration / Topology / Metrics / Users / everything related to it/ runtime )

### Historical  Data for reporting 
Vertica-DB  or at OPTIC Data lake  (Vertica)





### to get all variables in windows
in PowerShell ``` set ``` command == to get all variables 

cd %variableName% that will change to that var directory   


### windows
domain\username 

https://support.microsoft.com/en-us/windows/install-java-in-internet-explorer-e9fde175-f750-2902-d6da-a97a83587856

https://www.java.com/en/download/



```bash
yum install bsdtar
bsdtar -xf OA_12.24_Linux.iso
```



```bash
[ FAIL ] Check if Motif is installed Motif toolkit not installed, xglance functionality will be affected.
```

```bash
yum install openmotif -y 
yum install libnsl.so.1 libncurses.so.5 libnsl -y 
yum install m4 -y 

```

### Sap 
presentation layer => any browser or mobile application to access the sap with
Application layer (ABAP Server Central Service) ASCS => contains three central sap services (Start - Message - enqueue)  and ACT as administrative unit. 
1- Start service = keep track of all system health , on-stat or off stat
2- massage service == manage queue
3-enqueue service == manage locks and make sure no transactions are trying to update  same field  to the same  tables on same time. to avoid sync issues (if I'm updating a table {enqueue service} will lock the table until I finish updating it)


Application server :
1- Start service 
2- Gateway 
3- ICM (Internal communication manager)
4- ABAP Dispatcher - - - - - - --> contains of multiple work process 
DB layer 






