```
2024-07-18 16:20:47,919 [EUCSEX01 Exchnage best Practice Base(1951502875/3) ] (ExchangeBaseMonitor.java:225) ERROR - Error Code: 30300.  Error Description: Failed to connect to Server, please check Server availability. Connect output:  Connect Error Message:New-PSSession : [eucsex01.elarabygroup.com] Processing data from remote server eucsex01.elarabygroup.com failed with the following error message: [ClientAccessServer=EUCSEX01,BackEndServer=eucsex01.elarabygroup.com,RequestId=d02f1341-330c-4584-8991-1b802035e6a1,TimeStamp=7/18/2024 1:20:47 PM] [FailureCategory=WSMan-InvalidShellID] The request for the Windows Remote Shell with ShellId FD102A60-BE08-445F-B128-EEF563F22579 failed because the shell was not found on the server. Possible causes are: the specified ShellId is incorrect or the shell no longer exists on the server. Provide the correct ShellId or create a new shell and retry the operation. For more information, see the about_Remote_Troubleshooting Help topic.At line:1 char:1+ New-PSSession -ConnectionURI "$connectionUri" -ConfigurationName Micr ...+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    + CategoryInfo          : OpenError: (System.Manageme....RemoteRunspace:RemoteRunspace) [New-PSSession], PSRemotin    gTransportException    + FullyQualifiedErrorId : CannotConnectTargetSessionDoesNotExist,PSSessionOpenFailedFailed to connect to an Exchange server in the current site.
```

=================================================================================

```

#Get-ManagementRoleAssignment -RoleAssignee <Username>
#Enter-PSSession -ComputerName eucsex01.elarabygroup.com -ConfigurationName Microsoft.Exchange
#Enter-PSSession -ComputerName EUOTtest -Credential ot-poc@elarabygroup.com
#$PSVersionTable
$PsHome
# i prefer to add powershell V2 feature and disable V5 as test

Get-Item WSMan:\localhost\Client\TrustedHosts
Set-Item WSMan:\localhost\Client\TrustedHosts *.yourdomain.local
Set-Item WSMan:\localhost\Client\TrustedHosts *.ds-lab.com

https://docs.devolutions.net/server/kb/how-to-articles/winrm-trustedhostslist/
```

=================================================================================

```
2024-07-18 17:00:34,327 [EUCSEX01 Exchange Mailbox default(1951502875/2) ] (ExchMngtShellParser.java:101) ERROR - Error occurred while running cmdlet: Mail Flow. The Error:
Test-MailFlow : [Microsoft.Mapi.MapiExceptionSendAsDenied]: MapiExceptionSendAsDenied: Unable to submit message. 
```


================================================================================= 

```
2024-07-18 17:00:34,328 [EUCSEX01 Exchange Mailbox default(1951502875/2) ] (ExchMngtShellParser.java:101) ERROR - Error occurred while running cmdlet: Web Services Connectivity. The Error:
Cannot find information about the local server EUWOTSIS2D.elarabygroup.com in Active Directory. This may be related to 
a change in the server name.
At C:\SiteScope\templates.applications\scripts.exchange2007\ExchangeTestCmdlets.ps1:85 char:6
+         Test-WebServicesConnectivity -ClientAccessServer $exchangeSer ...
+         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [], LocalServerNotFoundException
    + FullyQualifiedErrorId : [Server=EUWOTSIS2D,RequestId=44929dbe-18e2-4ee2-b0d3-743dea14de37,TimeStamp=7/18/2024 2: 
   00:34 PM] [FailureCategory=Cmdlet-LocalServerNotFoundException] FE3C918B

#nslookup EUWOTSIS2D.elarabygroup.com
i'm confused with this error 
```

================================================================================= 

```
2024-07-18 14:22:37,499 [EUCSEX01 Exchnage best Practice Base(1951502875/3) ] (AbstractCmdletBase.java:164) ERROR - Starting a command on the remote server failed with the following error message : The I/O operation has been aborted because of either a thread exit or an application request. For more information, see the about_Remote_Troubleshooting Help topic.    + CategoryInfo          : OperationStopped: (eucsex01.elarabygroup.com:String) [], PSRemotingTransportException    + FullyQualifiedErrorId : JobFailure    + PSComputerName        : eucsex01.elarabygroup.com 
```
============================================================================
```
2024-07-18 14:22:37,499 [EUCSEX01 Exchnage best Practice Base(1951502875/3) ] (AbstractCmdletBase.java:164) ERROR - Creating a new session for implicit remoting of "Test-ServiceHealth" command...
```
============================================================================
```
2024-07-18 15:02:24,582 [EUCSEX01 Exchnage best Practice Base(1951502875/3) ] (AbstractCmdletBase.java:164) ERROR - Object: MsExchange Assistants - Per DatabaseCounter: Elapsed Time since Last Database Status Update AttemptInstance: msexchangemailboxassistants-totalValue: 0Object: WatsonCounter: CrashDumpCountInstance: MsExchangeMailboxAssistantsValue: 0
```
============================================================================
```
2024-07-18 15:42:42,352 [EUCSEX01 Exchnage best Practice Base(1951502875/3) ] (AbstractCmdletBase.java:164) ERROR - Object: MsExchange Assistants - Per DatabaseCounter: Elapsed Time since Last Database Status Update AttemptInstance: msexchangemailboxassistants-totalValue: 0Object: WatsonCounter: CrashDumpCountInstance: MsExchangeMailboxAssistantsValue: 0
```
============================================================================

```
2024-07-18 15:42:45,240 [EUCSEX01 Exchnage best Practice Base(1951502875/3) ] (AbstractCmdletBase.java:164) ERROR - Creating a new session for implicit remoting of "Get-StoreUsageStatistics" command...

```

================================================================================= 

```
17:00:34 07/18/2024	error	1951502875	EUCSEX01 Exchange Mailbox default	Exchange Search/ResultFound = False, Exchange Search/SearchTime = -1, For getting more information look at the log files., For getting more information look at the log files., For getting more information look at the log files., For getting more information look at the log files., For getting more information look at the log files., For getting more information look at the log files., For getting more information look at the log files., For getting more information look at the log files., For getting more information look at the log files., For getting more information look at the log files., MAPI Connectivity/Latency = 00:00:00, MAPI Connectivity/Result = *FAILURE*, Mail Flow/MessageLatencyTime = Error occurred while trying to retrieve Mail Flow counters, Mail Flow/TestMailflowResult = Error occurred while trying to retrieve Mail Flow counters, OWA Connectivity/Latency = 00:00:00.0219935, OWA Connectivity/Result = Failure, Web Services Connectivity/CreateItem/Latency = Error occurred while trying to retrieve Web Services Connectivity counters, Web Services Connectivity/CreateItem/Result = Error occurred while trying to retrieve Web Services Connectivity counters, Web Services Connectivity/DeleteItem/Latency = Error occurred while trying to retrieve Web Services Connectivity counters, Web Services Connectivity/DeleteItem/Result = Error occurred while trying to retrieve Web Services Connectivity counters, Web Services Connectivity/GetFolder/Latency = Error occurred while trying to retrieve Web Services Connectivity counters, Web Services Connectivity/GetFolder/Result = Error occurred while trying to retrieve Web Services Connectivity counters, Web Services Connectivity/SyncFolderItems/Latency = Error occurred while trying to retrieve Web Services Connectivity counters, Web Services Connectivity/SyncFolderItems/Result = Error occurred while trying to retrieve Web Services Connectivity counters	2:131	10	*FAILURE*	00:00:00	n/a	n/a	False	-1	Failure	00:00:00.0219935	n/a	n/a	n/a	n/a	n/a	n/a	n/a	n/a	nonfailure
```

=================================================================================

```
https://stackoverflow.com/questions/45989166/winrm-cannot-process-the-request-error-0x80090311



<SiteScope_Home>/groups/master.config by setting _sishostnameoverride=<SiS server FQDN>.

```

=================================================================================


```
(bbc-289) status=eSSLError time=94 ms in linux

 ./bin/ovcert -trust ot-obm.ds-lab.com

ovconfget sec.core.auth

ovconfget  sec.cm.certificates

ovconfget sec.cm.client

ovcert -certreq

/opt/OV/bin/OpC/opcagt -status


./bin/ovconfchg -ns sec.cm.client -set CERTIFICATE_SERVER ot-obm.ds-lab.com

./bin/ovcert -trust ot-obm.ds-lab.com


./bin/ovc -stop                                                                                                                           

[root@AppD-SuperCarTrader OV]# ./bin/ovc -start


tail -f /var/opt/OV/log/System.txt



./bin/OpC/install/opcactivate -srv ot-obm.ds-lab.com
./bin/OpC/install/opcactivate -srv ot-obm.ds-lab.com -cert_srv ot-obm.ds-lab.com


sudo ./bin/ovcert -importtrusted -file ~/.ssh/ot-obm.ds-lab.com
```






