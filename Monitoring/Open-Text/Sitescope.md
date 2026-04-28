### WINRM
```
winrm e winrm/config/listener 
winrm set winrm/config/service/Auth @{Basic="false"} #will authintacte from kerbos service
winrm set winrm/config/service @{AllowUnencrypted="true"} #incase of http


winrm set winrm/config/winrs @{MaxMemoryPerShellMB="4096"
winrm s winrm/config/winrs '@{IdleTimeout="180000"}'
winrm s winrm/config/winrs '@{MaxTimeout="180000"}'

https://docs.microfocus.com/doc/SiteScope/24.2/WinRMServiceWinMonitoring

# From Powershell 
Enter-PSSession -ComputerName EUOTtest -Credential ot-poc@domain.com
Enter-PSSession -ComputerName EUOTtest -Credential Administrator@ds-lab.com

```


```
### Enable  RDP to firewall
```

```
#in powershell 
 Enable-NetFirewallRule -DisplayGroup "Remote Desktop" 

```

### WMI
```powershell

#to check wmi port
1- go to run and type dcomcnfg 
2- find Windows Management and Instrumentation

# start configration one by one
winmgmt -standalonehost
net stop winmgmt
net start winmgmt

# Enable DCOM (TCP port 135)
netsh advfirewall firewall add rule name="DCOM-In" protocol=TCP dir=in localport=135 action=allow

# Enable WMI (dynamic RPC ports)
netsh advfirewall firewall add rule name="WMI-RPCSS-In" protocol=TCP dir=in localport=RPC action=allow

# Enable WMI (fixed ports)
netsh advfirewall firewall add rule name="WMI-WINMGMT-In" protocol=TCP dir=in localport=24158 action=allow

```
###  WBEMTest
```powershell
Networkpath \\ \\    
#as example  

\\ot-sis.ds-lab.com\root\cimv2
\\domain\user 

*WMI query*   : select * from Win32_Processor 
```

### importance of templates container 

by default if you don't name the monitor, it will name it self as service/ cpu / mem on the server name, but when redeploy it as container it will not change the server name to the new name.


### Vmware

1. Install the certificate of vcenter in sitecope.

2. verify the login credentials by login vsphere (vcenter) and check whether that host is available or not. From sitescope server only

3. if all are part of same domain. Then nslookup must work fine for vcenter, VM host by IP and hostname.

connection URL -https://IPaddress/sdk
            -https://vcenter.ds-lab.com/sdk


![[Sitescope vmware Host.png]]

![[sitescope vmware datastore.png]]




### Font size
Go to sitescope-client_win\java\bin
- javaw.exe -->  properties --> compatibility --> edit DPI setting to override wit hsystem
- ref: https://community.microfocus.com/it_ops_mgt/ops-bdg/f/discussions/525541/how-do-i-adjust-the-font-size-when-on-the-sitescope-page
### Ldap Security Principle
```powershell

Get-ADUser -Identity Administrator -Properties DistinguishedName
###result CN=Administrator,CN=Users,DC=DS-LAB,DC=COM



Get-ADDomainController \| ft Name,IsGlobalCatalog|
```

## SiteScope Monitor Categories
https://docs.microfocus.com/doc/SiteScope/2018.11/Use/SIS_mon_categories
## Monitor Permissions and Credentials
https://docs.microfocus.com/doc/SiteScope/2018.11/Use/perm_cred


check windows logs.


