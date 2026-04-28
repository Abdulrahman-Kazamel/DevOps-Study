### Agent install
```powershell
# from kareem
cscript oainstall.vbs -i -a -s obm.ds-lab.com -cs obm.ds-lab.com
```

### Agent remove
```powershell
cscript oainstall.vbs -r -a
oainstall.sh -r -a
```

### Check agent status

```powershell
opcagt -status
# if the agent is buffering for some servers it will show here

bbcutil -ping ot-apm.ds-lab.com ## from oa server 	
# or
bbcutil -ping oa-agent-server 
# or
ovrc -ovrg -host oa-agent-server -status 
```


### install management pack

1- move the package to the obm server 
2- run the below command
```bash
cscript /nologo mpinstall.vbs -i
```

on the CI run
```bash
cd /opt/OV/
./bin/ovpolicy -list 
```



### find obm manger 

```
ovconfget -ovrg server | find "OPC_MGMT_SERVER"
```


### Export OBM Certificate
```
opr-cert-mgmt.bat -export "OBM Webserver CA Certificate" PEM "C:\ca_certificate.cert"
```





```
Set-PSSessionConfiguration -Name Microsoft.Powershell -ShowSecurityDescriptorUI
```



### Dashboards
-- Active Directory
MS AD Events ===>  Event filter = no filter || View filter = AD_Network_Deployment_view
*if you want drill down , choose the drill down from the advanced properties*

-- MS SQL
MS SQL Events ===>  Event filter = no filter || View filter = MS__Network_Deployment
*if you want drill down , choose the drill down from the advanced properties*

-- Widget processing
Widget processing (and this one is for business Application) ===>  Event filter = no filter || View filter = Widget processing


-- Detailed dashboards 
--
AD Over 30 mins
Event filter = major and critical events over 30 mins (Severity {}|| Lifecycle {in progress, resolved , open} || Time Created  {older than 30 mins} )
View filter = AD_Network_Deployment_view

first models
top view 
event browser

event browser 

mointering dashboards 



### Performance presective:

1- memory metric in the global class => GBL-MEM-Free or GBL-MEM-File-Page-cache or GBL-MEM-cache or GBL-MEM-SYS or GBL-MEM-USER 
2-Axis & Grid => Left Y => unit => data => Megabytes.
3-Display Styles => you are able to choose between line or bar or pie chart also line fill with 1. or *ToolTip* => to hover with showing all values. or *Link Label* add Process drill down and search for process drill down.


*Another Table:*

1- add Table => title (System Information) all under Configuration class
(GBL-Distribution or GBL-Machine or GBL-Machine-Model- GBL-collector ) to show the latest values for these metrics rather than time for each time interval go to Styles tab and choose structured == back to dashboard and set height to  350px for example.

*Another chart in same row* add single value chart => UpTime => Global => the agent collect up time in seconds or in hours and for example we want it in days ----> choose from (...) and name it UpTime Days and choose (GBL-System-Uptime-Hours / 24 ) *Note* this metirc available in this dashboard only. 
*Don't Forget *  go to Options and choose value to Current  Postfix days 
font size prefix (50%) Value 200% Postfix (80%)

### Save and name it for example Memory and Uptime 
also you can hover and Zoom in  and choose process drill down to see process causing the issue. 





### Management Pack 
Administration => Monitoring => 
in auto assignment => for Infra, we choose (HP with Operations agent View)
leave check of auto assignment rule to ( to run immediately )

to check what aspect deployed to what ==> assignment & tunning and choose your view



### OMi: How to combine and pre-set parameters in aspects or management templates
https://www.youtube.com/watch?v=7i90UuFf5V4&list=PLAs4wHjzVROfbClzIxoROVbAIEGbK9jer&index=9

### # Whitlock - KPI Data from HPE SiteScope to HPE OMi

[](https://www.youtube.com/@AlexUlbrich)
https://www.youtube.com/watch?v=UJzCdjhUEHY


Note in Monitoring Dashboard:  in Sitescope Events ==>it should show System Infra View (Topolgy).

### Creating a Drill Down OMi10.10 Dashboard 
it needs more than one dashboard 




## Operations Bridge Video Library   (Important)

https://community.microfocus.com/it_ops_mgt/ops-bdg/w/tips/46666/operations-bridge-video-library#mcetoc_1heq7jrqg7






