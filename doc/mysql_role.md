# MySQL role

This role install the mySQL database

To test the mysql installation:

    service mysql status
    ● mysql.service - MySQL Community Server
     Loaded: loaded (/lib/systemd/system/mysql.service; enabled; vendor preset:>
     Active: active (running) since Sat 2023-02-04 06:37:40 UTC; 5min ago
    Process: 458 ExecStartPre=/usr/share/mysql/mysql-systemd-start pre (code=ex>
   Main PID: 577 (mysqld)
     Status: "Server is operational"
      Tasks: 38 (limit: 1143)
     Memory: 365.0M
        CPU: 2.878s
     CGroup: /system.slice/mysql.service
             └─577 /usr/sbin/mysqld

 mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.32-0ubuntu0.22.04.2 (Ubuntu)

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.03 sec)

To test it once the password has been changed:

    mysql -u root -p

mysql> use mysql;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> SELECT user FROM user;
+------------------+
| user             |
+------------------+
| root             |
| root             |
| root             |
| debian-sys-maint |
| mysql.infoschema |
| mysql.session    |
| mysql.sys        |
| root             |
+------------------+
8 rows in set (0.00 sec)




