
### index.php
```
 cat index.php 
<?php
$dbname = 'devops_db';
$dbuser = 'devops_admin';
$dbpass = 'Passw0rd';
$dbhost = 'devops-rds.cb6yywkim97u.us-east-1.rds.amazonaws.com';

$link = mysqli_connect($dbhost, $dbuser, $dbpass) or die("Unable to Connect to '$dbhost'");
mysqli_select_db($link, $dbname) or die("Could not open the db '$dbname'");

$test_query = "SHOW TABLES FROM $dbname";
$result = mysqli_query($link, $test_query);

$tblCnt = 0;
while($tbl = mysqli_fetch_array($result)) {
  $tblCnt++;
}

if (!$tblCnt) {
  echo "Connected successfully<br />\n";
} else {
  echo "Connected successfully<br />\n";
}
?>
```




```bash
 cat /etc/apache2/mods-enabled/dir.conf 
<IfModule mod_dir.c>
        DirectoryIndex index.php  index.html index.cgi index.pl index.php index.xhtml index.htm
</IfModule>

# vim: syntax=apache ts=4 sw=4 sts=4 sr noet
```