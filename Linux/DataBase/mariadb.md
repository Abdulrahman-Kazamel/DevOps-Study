
```
[peter@stdb01 ~]$ systemctl start mariadb
==== AUTHENTICATING FOR org.freedesktop.systemd1.manage-units ====
Authentication is required to start 'mariadb.service'.
Authenticating as: peter
Password: 
==== AUTHENTICATION COMPLETE ====
Job for mariadb.service failed because the control process exited with error code.
See "systemctl status mariadb.service" and "journalctl -xeu mariadb.service" for de
× mariadb.service - MariaDB 10.5 database server
     Loaded: loaded (/usr/lib/systemd/system/mariadb.service; enabled; preset: dis>
     Active: failed (Result: exit-code) since Sun 2026-04-05 19:23:55 UTC; 17s ago
       Docs: man:mariadbd(8)
             https://mariadb.com/kb/en/library/systemd/
    Process: 20751 ExecStartPre=/usr/libexec/mariadb-check-socket (code=exited, st>
    Process: 20773 ExecStartPre=/usr/libexec/mariadb-prepare-db-dir mariadb.servic>
    Process: 20900 ExecStart=/usr/libexec/mariadbd --basedir=/usr $MYSQLD_OPTS $_W>
   Main PID: 20900 (code=exited, status=1/FAILURE)
        CPU: 288ms

Apr 05 19:23:55 stdb01 mariadb-prepare-db-dir[20836]: After connecting you can set>
Apr 05 19:23:55 stdb01 mariadb-prepare-db-dir[20836]: able to connect as any of th>
Apr 05 19:23:55 stdb01 mariadb-prepare-db-dir[20836]: See the MariaDB Knowledgebas>
Apr 05 19:23:55 stdb01 mariadb-prepare-db-dir[20836]: Please report any problems a>
Apr 05 19:23:55 stdb01 mariadb-prepare-db-dir[20836]: The latest information about>
Apr 05 19:23:55 stdb01 mariadb-prepare-db-dir[20836]: Consider joining MariaDB's s>
Apr 05 19:23:55 stdb01 mariadb-prepare-db-dir[20836]: https://mariadb.org/get-invo>
Apr 05 19:23:55 stdb01 systemd[1]: mariadb.service: Main process exited, code=exit>
Apr 05 19:23:55 stdb01 systemd[1]: mariadb.service: Failed with result 'exit-code'.
Apr 05 19:23:55 stdb01 systemd[1]: Failed to start MariaDB 10.5 database server.
~
~
lines 1-21/21 (END)

[peter@stdb01 ~]$ 
[peter@stdb01 ~]$ 
[peter@stdb01 ~]$ 
[peter@stdb01 ~]$ cat /etc/log/mariadb/error.log
cat: /etc/log/mariadb/error.log: No such file or directory
[peter@stdb01 ~]$ journalctl -xeu mariadb.service
Apr 05 19:23:55 stdb01 mariadb-prepare-db-dir[20836]: https://mariadb.org/get-invo>
Apr 05 19:23:55 stdb01 systemd[1]: mariadb.service: Main process exited, code=exit>
░░ Subject: Unit process exited
░░ Defined-By: systemd
░░ Support: https://access.redhat.com/support
░░ 
░░ An ExecStart= process belonging to unit mariadb.service has exited.
░░ 
░░ The process' exit code is 'exited' and its exit status is 1.
Apr 05 19:23:55 stdb01 systemd[1]: mariadb.service: Failed with result 'exit-code'.
░░ Subject: Unit failed
░░ Defined-By: systemd
░░ Support: https://access.redhat.com/support
░░ 
░░ The unit mariadb.service has entered the 'failed' state with result 'exit-code'.
Apr 05 19:23:55 stdb01 systemd[1]: Failed to start MariaDB 10.5 database server.
░░ Subject: A start job for unit mariadb.service has failed
[root@stdb01 ~]# journalctl -xeu mariadb.service
Apr 05 19:29:14 stdb01 mariadb-prepare-db-dir[22589]: If this is not the case, make sure the /var/lib/mysql is empty before r>
Apr 05 19:29:14 stdb01 systemd[1]: mariadb.service: Main process exited, code=exited, status=1/FAILURE
░░ Subject: Unit process exited
░░ Defined-By: systemd
░░ Support: https://access.redhat.com/support
░░ 
░░ An ExecStart= process belonging to unit mariadb.service has exited.
░░ 
░░ The process' exit code is 'exited' and its exit status is 1.
Apr 05 19:29:14 stdb01 systemd[1]: mariadb.service: Failed with result 'exit-code'.
░░ Subject: Unit failed
░░ Defined-By: systemd
░░ Support: https://access.redhat.com/support
░░ 
░░ The unit mariadb.service has entered the 'failed' state with result 'exit-code'.
Apr 05 19:29:14 stdb01 systemd[1]: Failed to start MariaDB 10.5 database server.
░░ Subject: A start job for unit mariadb.service has failed
░░ Defined-By: systemd
░░ Support: https://access.redhat.com/support
░░ 
░░ A start job for unit mariadb.service has finished with a failure.
░░ 
░░ The job identifier is 57047 and the job result is failed.
```

``` 
[root@stdb01 ~]# cat /var/log/mariadb/mariadb.log 
2026-04-05 19:23:55 0 [Note] Starting MariaDB 10.5.29-MariaDB source revision c461188ca6ad6ec3a54201eb87ebd75797d296df server_uid ukkvBbdw6PnM+beOz0gHvD5taN4= as process 20900
2026-04-05 19:23:55 0 [Note] InnoDB: Uses event mutexes
2026-04-05 19:23:55 0 [Note] InnoDB: Compressed tables use zlib 1.2.11
2026-04-05 19:23:55 0 [Note] InnoDB: Number of pools: 1
2026-04-05 19:23:55 0 [Note] InnoDB: Using AVX512 instructions
2026-04-05 19:23:55 0 [Note] mariadbd: O_TMPFILE is not supported on /var/tmp (disabling future attempts)
2026-04-05 19:23:55 0 [Note] InnoDB: Using Linux native AIO
2026-04-05 19:23:55 0 [Note] InnoDB: Initializing buffer pool, total size = 134217728, chunk size = 134217728
2026-04-05 19:23:55 0 [Note] InnoDB: Completed initialization of buffer pool
2026-04-05 19:23:55 0 [Note] InnoDB: 128 rollback segments are active.
2026-04-05 19:23:55 0 [Note] InnoDB: Creating shared tablespace for temporary tables
2026-04-05 19:23:55 0 [Note] InnoDB: Setting file './ibtmp1' size to 12 MB. Physically writing the file full; Please wait ...
2026-04-05 19:23:55 0 [Note] InnoDB: File './ibtmp1' size is now 12 MB.
2026-04-05 19:23:55 0 [Note] InnoDB: 10.5.29 started; log sequence number 45079; transaction id 20
2026-04-05 19:23:55 0 [Note] InnoDB: Loading buffer pool(s) from /var/lib/mysql/ib_buffer_pool
2026-04-05 19:23:55 0 [Note] Plugin 'FEEDBACK' is disabled.
2026-04-05 19:23:55 0 [Note] InnoDB: Buffer pool(s) load completed at 260405 19:23:55
2026-04-05 19:23:55 0 [Note] Server socket created on IP: '::'.
2026-04-05 19:23:55 0 [ERROR] mariadbd: Can't create/write to file '/run/mariadb/mariadb.pid' (Errcode: 13 "Permission denied")
2026-04-05 19:23:55 0 [ERROR] Can't start server: can't create PID file: Permission denied
2026-04-05 19:29:14 0 [Note] Starting MariaDB 10.5.29-MariaDB source revision c461188ca6ad6ec3a54201eb87ebd75797d296df server_uid ukkvBbdw6PnM+beOz0gHvD5taN4= as process 22648
2026-04-05 19:29:14 0 [Note] InnoDB: Uses event mutexes
2026-04-05 19:29:14 0 [Note] InnoDB: Compressed tables use zlib 1.2.11
2026-04-05 19:29:14 0 [Note] InnoDB: Number of pools: 1
2026-04-05 19:29:14 0 [Note] InnoDB: Using AVX512 instructions
2026-04-05 19:29:14 0 [Note] mariadbd: O_TMPFILE is not supported on /var/tmp (disabling future attempts)
2026-04-05 19:29:14 0 [Note] InnoDB: Using Linux native AIO
2026-04-05 19:29:14 0 [Note] InnoDB: Initializing buffer pool, total size = 134217728, chunk size = 134217728
2026-04-05 19:29:14 0 [Note] InnoDB: Completed initialization of buffer pool
2026-04-05 19:29:14 0 [Note] InnoDB: Starting crash recovery from checkpoint LSN=45079,45079
2026-04-05 19:29:14 0 [Note] InnoDB: 128 rollback segments are active.
2026-04-05 19:29:14 0 [Note] InnoDB: Removed temporary tablespace data file: "ibtmp1"
2026-04-05 19:29:14 0 [Note] InnoDB: Creating shared tablespace for temporary tables
2026-04-05 19:29:14 0 [Note] InnoDB: Setting file './ibtmp1' size to 12 MB. Physically writing the file full; Please wait ...
2026-04-05 19:29:14 0 [Note] InnoDB: File './ibtmp1' size is now 12 MB.
2026-04-05 19:29:14 0 [Note] InnoDB: 10.5.29 started; log sequence number 45091; transaction id 20
2026-04-05 19:29:14 0 [Note] Plugin 'FEEDBACK' is disabled.
2026-04-05 19:29:14 0 [Note] InnoDB: Loading buffer pool(s) from /var/lib/mysql/ib_buffer_pool
[root@stdb01 ~]# cat /var/log/mariadb/mariadb.log 
2026-04-05 19:23:55 0 [Note] Starting MariaDB 10.5.29-MariaDB source revision c461188ca6ad6ec3a54201eb87ebd75797d296df server_uid ukkvBbdw6PnM+beOz0gHvD5taN4= as process 20900
2026-04-05 19:23:55 0 [Note] InnoDB: Uses event mutexes
2026-04-05 19:23:55 0 [Note] InnoDB: Compressed tables use zlib 1.2.11
2026-04-05 19:23:55 0 [Note] InnoDB: Number of pools: 1
2026-04-05 19:23:55 0 [Note] InnoDB: Using AVX512 instructions
2026-04-05 19:23:55 0 [Note] mariadbd: O_TMPFILE is not supported on /var/tmp (disabling future attempts)
2026-04-05 19:23:55 0 [Note] InnoDB: Using Linux native AIO
2026-04-05 19:23:55 0 [Note] InnoDB: Initializing buffer pool, total size = 134217728, chunk size = 134217728
2026-04-05 19:23:55 0 [Note] InnoDB: Completed initialization of buffer pool
2026-04-05 19:23:55 0 [Note] InnoDB: 128 rollback segments are active.
2026-04-05 19:23:55 0 [Note] InnoDB: Creating shared tablespace for temporary tables
2026-04-05 19:23:55 0 [Note] InnoDB: Setting file './ibtmp1' size to 12 MB. Physically writing the file full; Please wait ...
2026-04-05 19:23:55 0 [Note] InnoDB: File './ibtmp1' size is now 12 MB.
2026-04-05 19:23:55 0 [Note] InnoDB: 10.5.29 started; log sequence number 45079; transaction id 20
2026-04-05 19:23:55 0 [Note] InnoDB: Loading buffer pool(s) from /var/lib/mysql/ib_buffer_pool
2026-04-05 19:23:55 0 [Note] Plugin 'FEEDBACK' is disabled.
2026-04-05 19:23:55 0 [Note] InnoDB: Buffer pool(s) load completed at 260405 19:23:55
2026-04-05 19:23:55 0 [Note] Server socket created on IP: '::'.
2026-04-05 19:23:55 0 [ERROR] mariadbd: Can't create/write to file '/run/mariadb/mariadb.pid' (Errcode: 13 "Permission denied")
2026-04-05 19:23:55 0 [ERROR] Can't start server: can't create PID file: Permission denied
2026-04-05 19:29:14 0 [Note] Starting MariaDB 10.5.29-MariaDB source revision c461188ca6ad6ec3a54201eb87ebd75797d296df server_uid ukkvBbdw6PnM+beOz0gHvD5taN4= as process 22648
2026-04-05 19:29:14 0 [Note] InnoDB: Uses event mutexes
2026-04-05 19:29:14 0 [Note] InnoDB: Compressed tables use zlib 1.2.11
2026-04-05 19:29:14 0 [Note] InnoDB: Number of pools: 1
2026-04-05 19:29:14 0 [Note] InnoDB: Using AVX512 instructions
2026-04-05 19:29:14 0 [Note] mariadbd: O_TMPFILE is not supported on /var/tmp (disabling future attempts)
2026-04-05 19:29:14 0 [Note] InnoDB: Using Linux native AIO
2026-04-05 19:29:14 0 [Note] InnoDB: Initializing buffer pool, total size = 134217728, chunk size = 134217728
2026-04-05 19:29:14 0 [Note] InnoDB: Completed initialization of buffer pool
2026-04-05 19:29:14 0 [Note] InnoDB: Starting crash recovery from checkpoint LSN=45079,45079
2026-04-05 19:29:14 0 [Note] InnoDB: 128 rollback segments are active.
2026-04-05 19:29:14 0 [Note] InnoDB: Removed temporary tablespace data file: "ibtmp1"
2026-04-05 19:29:14 0 [Note] InnoDB: Creating shared tablespace for temporary tables
2026-04-05 19:29:14 0 [Note] InnoDB: Setting file './ibtmp1' size to 12 MB. Physically writing the file full; Please wait ...
2026-04-05 19:29:14 0 [Note] InnoDB: File './ibtmp1' size is now 12 MB.
2026-04-05 19:29:14 0 [Note] InnoDB: 10.5.29 started; log sequence number 45091; transaction id 20
2026-04-05 19:29:14 0 [Note] Plugin 'FEEDBACK' is disabled.
2026-04-05 19:29:14 0 [Note] InnoDB: Loading buffer pool(s) from /var/lib/mysql/ib_buffer_pool
2026-04-05 19:29:14 0 [Note] InnoDB: Buffer pool(s) load completed at 260405 19:29:14
2026-04-05 19:29:14 0 [Note] Server socket created on IP: '::'.
2026-04-05 19:29:14 0 [ERROR] mariadbd: Can't create/write to file '/run/mariadb/mariadb.pid' (Errcode: 13 "Permission denied")
2026-04-05 19:29:14 0 [ERROR] Can't start server: can't create PID file: Permission denied
2026-04-05 19:35:55 0 [Note] Starting MariaDB 10.5.29-MariaDB source revision c461188ca6ad6ec3a54201eb87ebd75797d296df server_uid ukkvBbdw6PnM+beOz0gHvD5taN4= as process 24494
2026-04-05 19:35:55 0 [Note] InnoDB: Uses event mutexes
2026-04-05 19:35:55 0 [Note] InnoDB: Compressed tables use zlib 1.2.11
2026-04-05 19:35:55 0 [Note] InnoDB: Number of pools: 1
2026-04-05 19:35:55 0 [Note] InnoDB: Using AVX512 instructions
2026-04-05 19:35:55 0 [Note] mariadbd: O_TMPFILE is not supported on /var/tmp (disabling future attempts)
2026-04-05 19:35:55 0 [Note] InnoDB: Using Linux native AIO
2026-04-05 19:35:55 0 [Note] InnoDB: Initializing buffer pool, total size = 134217728, chunk size = 134217728
2026-04-05 19:35:55 0 [Note] InnoDB: Completed initialization of buffer pool
2026-04-05 19:35:55 0 [Note] InnoDB: Starting crash recovery from checkpoint LSN=45079,45079
2026-04-05 19:35:55 0 [Note] InnoDB: 128 rollback segments are active.
2026-04-05 19:35:55 0 [Note] InnoDB: Removed temporary tablespace data file: "ibtmp1"
2026-04-05 19:35:55 0 [Note] InnoDB: Creating shared tablespace for temporary tables
2026-04-05 19:35:55 0 [Note] InnoDB: Setting file './ibtmp1' size to 12 MB. Physically writing the file full; Please wait ...
2026-04-05 19:35:55 0 [Note] InnoDB: File './ibtmp1' size is now 12 MB.
2026-04-05 19:35:55 0 [Note] InnoDB: 10.5.29 started; log sequence number 45103; transaction id 20
2026-04-05 19:35:55 0 [Note] Plugin 'FEEDBACK' is disabled.
2026-04-05 19:35:55 0 [Note] InnoDB: Loading buffer pool(s) from /var/lib/mysql/ib_buffer_pool
2026-04-05 19:35:55 0 [Note] Server socket created on IP: '::'.
2026-04-05 19:35:55 0 [Note] InnoDB: Buffer pool(s) load completed at 260405 19:35:55
2026-04-05 19:35:55 0 [ERROR] mariadbd: Can't create/write to file '/run/mariadb/mariadb.pid' (Errcode: 13 "Permission denied")
2026-04-05 19:35:55 0 [ERROR] Can't start server: can't create PID file: Permission denied
2026-04-05 19:36:07 0 [Note] Starting MariaDB 10.5.29-MariaDB source revision c461188ca6ad6ec3a54201eb87ebd75797d296df server_uid ukkvBbdw6PnM+beOz0gHvD5taN4= as process 24734
2026-04-05 19:36:07 0 [Note] InnoDB: Uses event mutexes
2026-04-05 19:36:07 0 [Note] InnoDB: Compressed tables use zlib 1.2.11
2026-04-05 19:36:07 0 [Note] InnoDB: Number of pools: 1
2026-04-05 19:36:07 0 [Note] InnoDB: Using AVX512 instructions
2026-04-05 19:36:07 0 [Note] mariadbd: O_TMPFILE is not supported on /var/tmp (disabling future attempts)
2026-04-05 19:36:07 0 [Note] InnoDB: Using Linux native AIO
2026-04-05 19:36:07 0 [Note] InnoDB: Initializing buffer pool, total size = 134217728, chunk size = 134217728
2026-04-05 19:36:07 0 [Note] InnoDB: Completed initialization of buffer pool
2026-04-05 19:36:07 0 [Note] InnoDB: Starting crash recovery from checkpoint LSN=45079,45079
2026-04-05 19:36:07 0 [Note] InnoDB: 128 rollback segments are active.
2026-04-05 19:36:07 0 [Note] InnoDB: Removed temporary tablespace data file: "ibtmp1"
2026-04-05 19:36:07 0 [Note] InnoDB: Creating shared tablespace for temporary tables
2026-04-05 19:36:07 0 [Note] InnoDB: Setting file './ibtmp1' size to 12 MB. Physically writing the file full; Please wait ...
2026-04-05 19:36:07 0 [Note] InnoDB: File './ibtmp1' size is now 12 MB.
2026-04-05 19:36:07 0 [Note] InnoDB: 10.5.29 started; log sequence number 45115; transaction id 20
2026-04-05 19:36:07 0 [Note] Plugin 'FEEDBACK' is disabled.
2026-04-05 19:36:07 0 [Note] InnoDB: Loading buffer pool(s) from /var/lib/mysql/ib_buffer_pool
2026-04-05 19:36:07 0 [Note] InnoDB: Buffer pool(s) load completed at 260405 19:36:07
2026-04-05 19:36:07 0 [Note] Server socket created on IP: '::'.
2026-04-05 19:36:07 0 [ERROR] mariadbd: Can't create/write to file '/run/mariadb/mariadb.pid' (Errcode: 13 "Permission denied")
2026-04-05 19:36:07 0 [ERROR] Can't start server: can't create PID file: Permission denied
[root@stdb01 ~]# ls -l /run/mariadb
total 0
[root@stdb01 ~]# ls -l /run/mariadb/
total 0
[root@stdb01 ~]# ls -l /run/
total 8
drwxr-xr-x  2 root     root       40 Apr  5 18:12 console
drwxr-xr-x  6 root     root      120 Apr  5 18:27 credentials
drwx------  2 root     root       40 Apr  5 18:12 cryptsetup
drwxr-xr-x  2 root     root       60 Apr  5 18:12 dbus
drwxr-xr-x  2 root     root       40 Apr  5 18:12 faillock
drwx--x---  3 root     apache     60 Apr  5 18:12 httpd
prw-------  1 root     root        0 Apr  5 18:12 initctl
drwxr-xr-x  3 root     root       60 Apr  5 18:12 lock
drwxr-xr-x  3 root     root       60 Apr  5 18:12 log
drwxr-xr-x  2 root     mysql      40 Apr  5 18:12 mariadb
```


chown mysql /run/mariadb




