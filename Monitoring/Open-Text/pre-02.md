```powershell
Test-Connection -ComputerName dc.ds-lab.com -Count 4      
Get-ADUser -Identity Administrator | Select-Object Name, SID
##=> tested and correct
```


```powershell
# Replace with your actual credentials and LDAP details
$Username = "CN=Administrator,CN=Builtin,DC=DS-LAB,DC=COM"  #ldap security principle
$Password = "your-password"
$LDAPServer = "dc.ds-lab.com"
$Port = 389

# Create a DirectoryEntry object with credentials
$LDAPPath = "LDAP://${LDAPServer}:${Port}"
$DirectoryEntry = New-Object System.DirectoryServices.DirectoryEntry($LDAPPath, $Username, $Password)

# Attempt to bind to the LDAP server
try {
    # Use the NativeObject property to force a bind to the server
    $DirectoryEntry.NativeObject
    Write-Host "Successfully bound to the LDAP server."
}
catch {
    Write-Host "Failed to bind to the LDAP server. Error: $_"
}


```