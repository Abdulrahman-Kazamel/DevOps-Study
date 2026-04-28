51ba0595-0af4-4e68-be59-f3c055649325			NULL	admin@example.com	ADMIN@EXAMPLE.COM	admin@example.com	ADMIN@EXAMPLE.COM	True	AQAAAAIAAYagAAAAEMjahr5JsafGSstAI5hmWuMBs2wzQW/XKYGAprJHWuEm9rgecR+bU1b5mkajHttXkw==	ZYL3DFJKP4HMXD3BD6TC3Q44H2BXO7WJ	93f67df6-08df-4571-99ec-046cea50194c	NULL	False	False	NULL	True	0

================================================================
Get-CimInstance -ClassName Win32_StartupCommand |
 Select-Object Name, Command, Location, User |
================================================================

function proccescount($processName){
$count = (Get-Process -Name $processName -ErrorAction SilentlyContinue).Count
 Write-Output "$processName process has count : $count"
 Get-Process -Name $processName
 }

===========================
sudo systemctl list-units --type=service | grep -i nexthink
vi /var/nexthink/engine/02/etc/nxengine.xml
vi /var/nexthink/engine/01/etc/nxengine.xml
eFXDF?///////,MNJR```	Q2SEFJKGKLO"'KK'K/KKNJVGJWETT;8UP808O9[O[''OYI	QEW2336
   (where device
       (gt number_of_days_since_last_boot (integer 30)
================================================================
(select (*)
   (from device
   (where device
       (eq antivirus_up_to_date (enum "no")
================================================================
(select (*)
   (from device
   (where device
       (gt total_active_days (day 30)

================================================================
(select (*)
    (from domain
         (where domain 
        ( eq protocol (enum "HTTP" ))
        (eq hosting_country (string "Netherlands")))
================================================================

##Nexthink Study
1-what is the difference between binary and execution?

A-I need to create powershell script to get info about which apps is consuming the startup.
	 
nxtcfg /restart

entity in nexthink is the location, how many entities / locations?  
hirerachies / levels , and those two concepts are used in calculating the complexity of the deployment.

I want to check , shall i add both 90 days and the details of the disk ??

what is the diffrence between internal and external dns server?
what are the different places to change timezone in nexthink..


data retention in nexthink 
what is the difference between local user and domain user?
application and program? p(kind of package) office / (app) word app / (exectutable) all exe files



//
destinations / domains?
destination --> 

warning exextion for spesefic application-->over 70 % for 5 minuties 
device warning --> for the device over all 

network view / web view ??

raci matrix......

how could i know the output of some query ?
also am i able to run nql ? sure but where?

Get-CimInstance

3 important questions in dealing with collector installer>>>
A-the collector execution policy ?
{ by trusted publisher or nexthink///nexthink only // unristricted} 
B- Default root CA / or create one and sign it by him.
c- do you want it to show in control panel or not??
d- know the costomer domain 
e- download customer key from the console. 

-150 the limit of leaf and composite in the score //50 the limit for the leaf score. but you could add some scores and disable it but this way is not practical.

-computation through NQL //field is collected directly from the collector
-in score range ,, if we write a range in the same row it will take between it,if we wrote the start range only in each row, it will take fixed integer number.


**in category creation <the order maters> and i could create one on the bottom like matching * to match this tag if didn't match the top tags

*available with data privacy {first option ,available for everyone}

هل أقدر أبحث مثلا عن مجموعه من البرامج exe اللي انا معملتهاش  و الناس بتستخدمها ولا دي داتا بتيجي مثلا من السي أم دي بي

what is nexthink use cases

day 14 is missing from my side/not understoud



