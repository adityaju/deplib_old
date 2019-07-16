sutshekhar
kamdudhaa
provisional patent
indian patent 



Framework:
Database, Actions, templates

************************Database****************************

dbname is 'deplib' @ mysql

Entities:

1)Books

mysql> desc books
    -> ;
+------------------+--------------+------+-----+---------+----------------+
| Field            | Type         | Null | Key | Default | Extra          |
+------------------+--------------+------+-----+---------+----------------+
| accession_number | varchar(30)  | NO   | PRI | NULL    |                |
| shelf_no         | varchar(10)  | YES  |     | NULL    |                |
| title            | varchar(120) | YES  |     | NULL    |                |
| price            | float        | YES  |     | NULL    |                |
| author           | varchar(200) | YES  |     | NULL    |                |
| sno              | int(11)      | NO   | UNI | NULL    | auto_increment |
| publisher        | varchar(50)  | YES  |     | NULL    |                |
| is_available     | tinyint(4)   | YES  |     | NULL    |                |
+------------------+--------------+------+-----+---------+----------------+
8 rows in set (0.11 sec)

2)Members
mysql> desc members;
+---------------+-------------+------+-----+---------+----------------+
| Field         | Type        | Null | Key | Default | Extra          |
+---------------+-------------+------+-----+---------+----------------+
| member_type   | varchar(7)  | YES  |     | NULL    |                |
| member_id     | int(11)     | NO   | PRI | NULL    | auto_increment |
| mobile_number | varchar(12) | YES  |     | NULL    |                |
| email_id      | varchar(45) | YES  |     | NULL    |                |
| full_name     | varchar(70) | YES  | UNI | NULL    |                |
+---------------+-------------+------+-----+---------+----------------+
5 rows in set (0.00 sec)


3)borrows

mysql> desc members;
+---------------+-------------+------+-----+---------+----------------+
| Field         | Type        | Null | Key | Default | Extra          |
+---------------+-------------+------+-----+---------+----------------+
| member_type   | varchar(7)  | YES  |     | NULL    |                |
| member_id     | int(11)     | NO   | PRI | NULL    | auto_increment |
| mobile_number | varchar(12) | YES  |     | NULL    |                |
| email_id      | varchar(45) | YES  |     | NULL    |                |
| full_name     | varchar(70) | YES  | UNI | NULL    |                |
+---------------+-------------+------+-----+---------+----------------+
5 rows in set (0.00 sec)
