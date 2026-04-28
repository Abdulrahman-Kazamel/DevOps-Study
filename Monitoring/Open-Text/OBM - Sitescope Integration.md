
*some data needed from Al-Kashif video *

### Integration 

1- Install OA on SiteScope Server 
```powershell
cscript oainstall.vbs -i -a  ## on ==> from Operation agent home directory
cscript oainstall.vbs -i -a ####Wrong in integration -srv ot-obm.ds-lab.com
##under /opt/oa/    
./oainstall.sh -i -a -srv ot-obm.ds-lab.com  ## after this command it will send cert request in OMI	
```



2- Configure SiteScope to use OA  tab from sitescope server 
     from windows search for sitescope  and configure to configure to be installed separately
	sitescope => general preferences => 

3-Restart Sitescope service
4- From SiteScope create integration temp 

![[integration temp to obm from sitescope.png]]

![[Screen After integration temp from sitescope.png]]

5- Import Certificate from SiteScope 


6- in obm infra trust and sitescope 

7- From OMI Setup a connected server 
![[from OMI create connected server.png]]




### last point, make sure to find and replace integration settings as below to not flood OMI 

![[integration settings.png]]

also from site scope common event mapping 
![[integration log only.png]]

select all mointors and keep going 
and find and replace from monitors to do the same
![[integration and disable and enable.png]]
disable reporting
send events (true)
bsm health affected by events



==need_to_understand 

The CIs are created only for the monitored entities according to the counters that you select. The monitors are represented in the RTSM as SiteScope Measurement Groups and SiteScope Measurement CIs.
so How again topology is sent from sitescope to operationsbridge. 


Enable topology reporting - optional

To enable topology reporting, make sure that Report monitor and related CI topology is selected in Integration Settings (the default setting). For details on the monitor topology, see [SAP CCMS Topology](https://docs.microfocus.com/doc/SiteScope/24.2/SAPCCMSMonitor#SAP_CCMS_Topology).

For user interface details, see [APM Integration Data and Topology Settings](https://docs.microfocus.com/doc/SiteScope/24.2/IntegrationSettings "SiteScope:24.2/IntegrationSettings").

++++++++++++++

1. Enable topology reporting - optional
    
    To enable topology reporting, make sure that **Report monitor and related CI topology** is selected in **Integration Settings** (the default setting). For details on the monitor topology, see [SAP CCMS Topology](https://docs.microfocus.com/doc/SiteScope/24.2/SAPCCMSMonitor#SAP_CCMS_Topology).
    
    For user interface details, see [APM Integration Data and Topology Settings](https://docs.microfocus.com/doc/SiteScope/24.2/IntegrationSettings "SiteScope:24.2/IntegrationSettings").





![[SiteScope_OBM_Integration.pdf]]


