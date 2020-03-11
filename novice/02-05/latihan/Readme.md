```
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 39
Server version: 10.0.38-MariaDB-0ubuntu0.16.04.1 Ubuntu 16.04

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> create database bulan;
Query OK, 1 row affected (0.06 sec)

MariaDB [(none)]> use bulan
Database changed

MariaDB [bulan]> create table lis (urutan INT(50), nama VARCHAR(100), umur INT(2));
Query OK, 0 rows affected (1.24 sec)

MariaDB [bulan]> show tables
    -> ;
+-----------------+
| Tables_in_bulan |
+-----------------+
| lis             |
+-----------------+
1 row in set (0.06 sec)

MariaDB [bulan]> insert into lis values('1','Cuncunmaru','50');
Query OK, 1 row affected (0.26 sec)

MariaDB [bulan]> select * from lis;
+--------+------------+------+
| urutan | nama       | umur |
+--------+------------+------+
|      1 | Cuncunmaru |   50 |
+--------+------------+------+
1 row in set (0.05 sec)

MariaDB [bulan]> insert into lis values('2','Arwindows','90');
Query OK, 1 row affected (0.42 sec)

MariaDB [bulan]> select * from lis;
+--------+------------+------
| urutan | nama       | umur |
+--------+------------+------+
|      1 | Cuncunmaru |   50 |
|      2 | Arwindows  |   90 |
+--------+------------+------+
2 rows in set (0.00 sec)
```