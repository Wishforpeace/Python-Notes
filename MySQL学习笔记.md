# MySQL学习笔记

## 一、登录MySQL

当 MySQL 服务已经运行时, 我们可以通过 MySQL 自带的客户端工具登录到 MySQL 数据库中, 首先打开命令提示符, 输入以下格式的命名:

```
mysql -h 主机名 -u 用户名 -p
```

参数说明：

- **-h** : 指定客户端所要登录的 MySQL 主机名, 登录本机(localhost 或 127.0.0.1)该参数可以省略;
- **-u** : 登录的用户名;
- **-p** : 告诉服务器将会使用一个密码来登录, 如果所要登录的用户名密码为空, 可以忽略此选项。

如果我们要登录本机的 MySQL 数据库，只需要输入以下命令即可：

```
mysql -u root -p
```

按回车确认, 如果安装正确且 MySQL 正在运行, 会得到以下响应:

```
Enter password:
```

若密码存在, 输入密码登录, 不存在则直接按回车登录。登录成功后你将会看到 Welcome to the MySQL monitor... 的提示语。

然后命令提示符会一直以 **mysq>** 加一个闪烁的光标等待命令的输入, 输入 **exit** 或 **quit** 退出登录。

## 二、MySQL管理

### 启动及关闭MySQL服务器

#### Linux系统

首先我们通过命令检查MySQL服务器是否启动

`ps -ef | grep mysqld`

如果MySql已经启动，以上命令将输出mysql进程列表， 如果mysql未启动，你可以使用以下命令来启动mysql服务器:

```
root@host# cd /usr/bin
./mysqld_safe &
```

如果你想关闭目前运行的 MySQL 服务器, 你可以执行以下命令:

```
root@host# cd /usr/bin
./mysqladmin -u root -p shutdown
Enter password: ******
```

### MySQL 用户设置

如果你需要添加 MySQL 用户，你只需要在 mysql 数据库中的 user 表添加新用户即可。

以下为添加用户的的实例，用户名为guest，密码为guest123，并授权用户可进行 SELECT, INSERT 和 UPDATE操作权限：

```
root@host# mysql -u root -p
Enter password:*******
mysql> use mysql;
Database changed

mysql> INSERT INTO user 
          (host, user, password, 
           select_priv, insert_priv, update_priv) 
           VALUES ('localhost', 'guest', 
           PASSWORD('guest123'), 'Y', 'Y', 'Y');
Query OK, 1 row affected (0.20 sec)

mysql> FLUSH PRIVILEGES;
Query OK, 1 row affected (0.01 sec)

mysql> SELECT host, user, password FROM user WHERE user = 'guest';
+-----------+---------+------------------+
| host      | user    | password         |
+-----------+---------+------------------+
| localhost | guest | 6f8c114b58f2ce9e |
+-----------+---------+------------------+
1 row in set (0.00 sec)
```

在添加用户时，请注意使用MySQL提供的 PASSWORD() 函数来对密码进行加密。 你可以在以上实例看到用户密码加密后为： 6f8c114b58f2ce9e.

**注意：**在 MySQL5.7 中 user 表的 password 已换成了**authentication_string**。

**注意：**password() 加密函数已经在 8.0.11 中移除了，可以使用 MD5() 函数代替。

**注意：**在注意需要执行 **FLUSH PRIVILEGES** 语句。 这个命令执行后会重新载入授权表。

如果你不使用该命令，你就无法使用新创建的用户来连接mysql服务器，除非你重启mysql服务器。

你可以在创建用户时，为用户指定权限，在对应的权限列中，在插入语句中设置为 'Y' 即可，用户权限列表如下：

- Select_priv
- Insert_priv
- Update_priv
- Delete_priv
- Create_priv
- Drop_priv
- Reload_priv
- Shutdown_priv
- Process_priv
- File_priv
- Grant_priv
- References_priv
- Index_priv
- Alter_priv

另外一种添加用户的方法为通过SQL的 GRANT 命令，以下命令会给指定数据库TUTORIALS添加用户 zara ，密码为 zara123 。

```
root@host# mysql -u root -p
Enter password:*******
mysql> use mysql;
Database changed

mysql> GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,DROP
    -> ON TUTORIALS.*
    -> TO 'zara'@'localhost'
    -> IDENTIFIED BY 'zara123';
```

以上命令会在mysql数据库中的user表创建一条用户信息记录。

**注意:** MySQL 的SQL语句以分号 (;) 作为结束标识。

### /etc/my.cnf 文件配置

一般情况下，你不需要修改该配置文件，该文件默认配置如下：

```
[mysqld]
datadir=/var/lib/mysql
socket=/var/lib/mysql/mysql.sock

[mysql.server]
user=mysql
basedir=/var/lib

[safe_mysqld]
err-log=/var/log/mysqld.log
pid-file=/var/run/mysqld/mysqld.pid
```

在配置文件中，你可以指定不同的错误日志文件存放的目录，一般你不需要改动这些配置。

------

### 管理MySQL的命令

以下列出了使用Mysql数据库过程中常用的命令：

- **USE \*数据库名\*** :
  选择要操作的Mysql数据库，使用该命令后所有Mysql命令都只针对该数据库。

  ```
  mysql> use RUNOOB;
  Database changed
  ```

- **SHOW DATABASES:**
  列出 MySQL 数据库管理系统的数据库列表。

  ```
  mysql> SHOW DATABASES;
  +--------------------+
  | Database           |
  +--------------------+
  | information_schema |
  | RUNOOB             |
  | cdcol              |
  | mysql              |
  | onethink           |
  | performance_schema |
  | phpmyadmin         |
  | test               |
  | wecenter           |
  | wordpress          |
  +--------------------+
  10 rows in set (0.02 sec)
  ```

- **SHOW TABLES:**
  显示指定数据库的所有表，使用该命令前需要使用 use 命令来选择要操作的数据库。

  ```
  mysql> use RUNOOB;
  Database changed
  mysql> SHOW TABLES;
  +------------------+
  | Tables_in_runoob |
  +------------------+
  | employee_tbl     |
  | runoob_tbl       |
  | tcount_tbl       |
  +------------------+
  3 rows in set (0.00 sec)
  ```

- **SHOW COLUMNS FROM \*数据表\*:**
  显示数据表的属性，属性类型，主键信息 ，是否为 NULL，默认值等其他信息。

  ```
  mysql> SHOW COLUMNS FROM runoob_tbl;
  +-----------------+--------------+------+-----+---------+-------+
  | Field           | Type         | Null | Key | Default | Extra |
  +-----------------+--------------+------+-----+---------+-------+
  | runoob_id       | int(11)      | NO   | PRI | NULL    |       |
  | runoob_title    | varchar(255) | YES  |     | NULL    |       |
  | runoob_author   | varchar(255) | YES  |     | NULL    |       |
  | submission_date | date         | YES  |     | NULL    |       |
  +-----------------+--------------+------+-----+---------+-------+
  4 rows in set (0.01 sec)
  ```

- **SHOW INDEX FROM \*数据表\*:**
  显示数据表的详细索引信息，包括PRIMARY KEY（主键）。

  ```
  mysql> SHOW INDEX FROM runoob_tbl;
  +------------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
  | Table      | Non_unique | Key_name | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
  +------------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
  | runoob_tbl |          0 | PRIMARY  |            1 | runoob_id   | A         |           2 |     NULL | NULL   |      | BTREE      |         |               |
  +------------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
  1 row in set (0.00 sec)
  ```

- **SHOW TABLE STATUS [FROM db_name] [LIKE 'pattern'] \G:**
  该命令将输出Mysql数据库管理系统的性能及统计信息。

  ```
  mysql> SHOW TABLE STATUS  FROM RUNOOB;   # 显示数据库 RUNOOB 中所有表的信息
  
  mysql> SHOW TABLE STATUS from RUNOOB LIKE 'runoob%';     # 表名以runoob开头的表的信息
  mysql> SHOW TABLE STATUS from RUNOOB LIKE 'runoob%'\G;   # 加上 \G，查询结果按列打印
  ```

Gif 图演示：

![img](https://www.runoob.com/wp-content/uploads/2014/03/mysql-admin.gif)

## 三、MySQL PHP语法

MySQL 可应用于多种语言，包括 PERL, C, C++, JAVA 和 PHP，在这些语言中，MySQL 在 PHP 的 web 开发中是应用最广泛。

在本教程中我们大部分实例都采用了 PHP 语言。如果你想了解 MySQL 在 PHP 中的应用，可以访问我们的 [PHP 中使用 Mysqli 介绍](https://www.runoob.com/php/php-mysql-intro.html)。

PHP 提供了多种方式来访问和操作Mysql数据库记录。PHP MySQL 函数格式如下：

```
mysqli_function(value,value,...);
```

以上格式中 function部分描述了mysql函数的功能，如

```
mysqli_connect($connect);
mysqli_query($connect,"SQL 语句");
mysqli_fetch_array()
mysqli_close()
```

以下实例展示了PHP调用mysql函数的语法：

### 实例 (MySQLi)

```
<?php
$retval = mysqli_function(value, [value,...]);
if( !$retval )
{
   die ( "相关错误信息" );
}
// 其他 MySQL 或 PHP 语句
?>
```

## 四、MySQL连接

### 使用mysql二进制方式连接

您可以使用MySQL二进制方式进入到mysql命令提示符下来连接MySQL数据库。

#### 实例

以下是从命令行中连接mysql服务器的简单实例：

```
[root@host]# mysql -u root -p
Enter password:******
```

在登录成功后会出现 mysql> 命令提示窗口，你可以在上面执行任何 SQL 语句。

以上命令执行后，登录成功输出结果如下:

```
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 2854760 to server version: 5.0.9

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.
```

在以上实例中，我们使用了root用户登录到mysql服务器，当然你也可以使用其他mysql用户登录。

如果用户权限足够，任何用户都可以在mysql的命令提示窗口中进行SQL操作。

退出 mysql> 命令提示窗口可以使用 exit 命令，如下所示：

```
mysql> exit
Bye
```

------

### 使用 PHP 脚本连接 MySQL

PHP 提供了 mysqli_connect() 函数来连接数据库。

该函数有 6 个参数，在成功链接到 MySQL 后返回连接标识，失败返回 FALSE 。

#### 语法

```
mysqli_connect(host, username, password, dbname,port, socket);
```

**参数说明：**

| 参数       | 描述                                        |
| :--------- | :------------------------------------------ |
| *host*     | 可选。规定主机名或 IP 地址。                |
| *username* | 可选。规定 MySQL 用户名。                   |
| *password* | 可选。规定 MySQL 密码。                     |
| *dbname*   | 可选。规定默认使用的数据库。                |
| *port*     | 可选。规定尝试连接到 MySQL 服务器的端口号。 |
| *socket*   | 可选。规定 socket 或要使用的已命名 pipe。   |

你可以使用 PHP 的 mysqli_close() 函数来断开与 MySQL 数据库的链接。

该函数只有一个参数为 mysqli_connect() 函数创建连接成功后返回的 MySQL 连接标识符。

### 语法

```
bool mysqli_close ( mysqli $link )
```

本函数关闭指定的连接标识所关联的到 MySQL 服务器的非持久连接。如果没有指定 link_identifier，则关闭上一个打开的连接。

**提示：**通常不需要使用 mysqli_close()，因为已打开的非持久连接会在脚本执行完毕后自动关闭。



### 实例

你可以尝试以下实例来连接到你的 MySQL 服务器:

### 连接 MySQL

```
<?php $dbhost = 'localhost';  // mysql服务器主机地址 
$dbuser = 'root';            // mysql用户名 
$dbpass = '123456';          // mysql用户名密码 
$conn = mysqli_connect($dbhost, $dbuser, $dbpass); 
if(! $conn ) 
{    
	die('Could not connect: ' . mysqli_error()); 
} 
echo '数据库连接成功！'; 
mysqli_close($conn); 
?>




```

## 五、创建数据库

```
CREATE DATABASE 数据库名;
```

以下命令简单的演示了创建数据库的过程，数据名为 RUNOOB:

```
[root@host]# mysql -u root -p   
Enter password:******  # 登录后进入终端

mysql> create DATABASE RUNOOB;
```

## 六、删除数据库

### drop 命令删除数据库

drop 命令格式：

```
drop database <数据库名>;
```

例如删除名为 RUNOOB 的数据库：

```
mysql> drop database RUNOOB;
```

### 使用 mysqladmin 删除数据库

你也可以使用 mysql **mysqladmin** 命令在终端来执行删除命令。

以下实例删除数据库 RUNOOB(该数据库在前一章节已创建)：



```
[root@host]# mysqladmin -u root -p drop RUNOOB
Enter password:******
```

执行以上删除数据库命令后，会出现一个提示框，来确认是否真的删除数据库：

```
Dropping the database is potentially a very bad thing to do.
Any data stored in the database will be destroyed.

Do you really want to drop the 'RUNOOB' database [y/N] y
Database "RUNOOB" dropped
```

## 七、选择数据库

### 从命令提示窗口中选择MySQL数据库

在 mysql> 提示窗口中可以很简单的选择特定的数据库。你可以使用SQL命令来选择指定的数据库。

#### 实例

以下实例选取了数据库 RUNOOB:

```
[root@host]# mysql -u root -p
Enter password:******
mysql> use RUNOOB;
Database changed
mysql>
```

执行以上命令后，你就已经成功选择了 RUNOOB 数据库，在后续的操作中都会在 RUNOOB 数据库中执行。

## 八、数据类型

### 数值类型

MySQL 支持所有标准 SQL 数值数据类型。

这些类型包括严格数值数据类型(INTEGER、SMALLINT、DECIMAL 和 NUMERIC)，以及近似数值数据类型(FLOAT、REAL 和 DOUBLE PRECISION)。

关键字INT是INTEGER的同义词，关键字DEC是DECIMAL的同义词。

BIT数据类型保存位字段值，并且支持 MyISAM、MEMORY、InnoDB 和 BDB表。

作为 SQL 标准的扩展，MySQL 也支持整数类型 TINYINT、MEDIUMINT 和 BIGINT。下面的表显示了需要的每个整数类型的存储和范围。

| 类型         | 大小                                     | 范围（有符号）                                               | 范围（无符号）                                               | 用途            |
| :----------- | :--------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- | :-------------- |
| TINYINT      | 1 Bytes                                  | (-128，127)                                                  | (0，255)                                                     | 小整数值        |
| SMALLINT     | 2 Bytes                                  | (-32 768，32 767)                                            | (0，65 535)                                                  | 大整数值        |
| MEDIUMINT    | 3 Bytes                                  | (-8 388 608，8 388 607)                                      | (0，16 777 215)                                              | 大整数值        |
| INT或INTEGER | 4 Bytes                                  | (-2 147 483 648，2 147 483 647)                              | (0，4 294 967 295)                                           | 大整数值        |
| BIGINT       | 8 Bytes                                  | (-9,223,372,036,854,775,808，9 223 372 036 854 775 807)      | (0，18 446 744 073 709 551 615)                              | 极大整数值      |
| FLOAT        | 4 Bytes                                  | (-3.402 823 466 E+38，-1.175 494 351 E-38)，0，(1.175 494 351 E-38，3.402 823 466 351 E+38) | 0，(1.175 494 351 E-38，3.402 823 466 E+38)                  | 单精度 浮点数值 |
| DOUBLE       | 8 Bytes                                  | (-1.797 693 134 862 315 7 E+308，-2.225 073 858 507 201 4 E-308)，0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308) | 0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308) | 双精度 浮点数值 |
| DECIMAL      | 对DECIMAL(M,D) ，如果M>D，为M+2否则为D+2 | 依赖于M和D的值                                               | 依赖于M和D的值                                               | 小数值          |

------

### 日期和时间类型

表示时间值的日期和时间类型为DATETIME、DATE、TIMESTAMP、TIME和YEAR。

每个时间类型有一个有效值范围和一个"零"值，当指定不合法的MySQL不能表示的值时使用"零"值。

TIMESTAMP类型有专有的自动更新特性，将在后面描述。

| 类型      | 大小 ( bytes) | 范围                                                         | 格式                | 用途                     |
| :-------- | :------------ | :----------------------------------------------------------- | :------------------ | :----------------------- |
| DATE      | 3             | 1000-01-01/9999-12-31                                        | YYYY-MM-DD          | 日期值                   |
| TIME      | 3             | '-838:59:59'/'838:59:59'                                     | HH:MM:SS            | 时间值或持续时间         |
| YEAR      | 1             | 1901/2155                                                    | YYYY                | 年份值                   |
| DATETIME  | 8             | 1000-01-01 00:00:00/9999-12-31 23:59:59                      | YYYY-MM-DD HH:MM:SS | 混合日期和时间值         |
| TIMESTAMP | 4             | 1970-01-01 00:00:00/2038结束时间是第 **2147483647** 秒，北京时间 **2038-1-19 11:14:07**，格林尼治时间 2038年1月19日 凌晨 03:14:07 | YYYYMMDD HHMMSS     | 混合日期和时间值，时间戳 |

------

### 字符串类型

字符串类型指CHAR、VARCHAR、BINARY、VARBINARY、BLOB、TEXT、ENUM和SET。该节描述了这些类型如何工作以及如何在查询中使用这些类型。

| 类型       | 大小                  | 用途                            |
| :--------- | :-------------------- | :------------------------------ |
| CHAR       | 0-255 bytes           | 定长字符串                      |
| VARCHAR    | 0-65535 bytes         | 变长字符串                      |
| TINYBLOB   | 0-255 bytes           | 不超过 255 个字符的二进制字符串 |
| TINYTEXT   | 0-255 bytes           | 短文本字符串                    |
| BLOB       | 0-65 535 bytes        | 二进制形式的长文本数据          |
| TEXT       | 0-65 535 bytes        | 长文本数据                      |
| MEDIUMBLOB | 0-16 777 215 bytes    | 二进制形式的中等长度文本数据    |
| MEDIUMTEXT | 0-16 777 215 bytes    | 中等长度文本数据                |
| LONGBLOB   | 0-4 294 967 295 bytes | 二进制形式的极大文本数据        |
| LONGTEXT   | 0-4 294 967 295 bytes | 极大文本数据                    |

**注意**：char(n) 和 varchar(n) 中括号中 n 代表字符的个数，并不代表字节个数，比如 CHAR(30) 就可以存储 30 个字符。

CHAR 和 VARCHAR 类型类似，但它们保存和检索的方式不同。它们的最大长度和是否尾部空格被保留等方面也不同。在存储或检索过程中不进行大小写转换。

BINARY 和 VARBINARY 类似于 CHAR 和 VARCHAR，不同的是它们包含二进制字符串而不要非二进制字符串。也就是说，它们包含字节字符串而不是字符字符串。这说明它们没有字符集，并且排序和比较基于列值字节的数值值。

BLOB 是一个二进制大对象，可以容纳可变数量的数据。有 4 种 BLOB 类型：TINYBLOB、BLOB、MEDIUMBLOB 和 LONGBLOB。它们区别在于可容纳存储范围不同。

有 4 种 TEXT 类型：TINYTEXT、TEXT、MEDIUMTEXT 和 LONGTEXT。对应的这 4 种 BLOB 类型，可存储的最大长度不同，可根据实际情况选择。

## 九、创建数据表

创建MySQL数据表需要以下信息：

+ 表名
+ 表字段名
+ 定义每个表字段

### 语法

以下为创建MySQL数据表的SQL通用语法：

`CREATE TABLE table_name(column_name column_type):`

以下例子中我们将在RUNOOB数据库中创建数据表runoob_tbl:

```mysql
CREATE TABLE IF NOT EXISTS `runoob_tbl`(
   `runoob_id` INT UNSIGNED AUTO_INCREMENT,
   `runoob_title` VARCHAR(100) NOT NULL,
   `runoob_author` VARCHAR(40) NOT NULL,
   `submission_date` DATE,
   PRIMARY KEY ( `runoob_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

实例解析：

+ 如果你不想字段为NULL可以设置字段的属性为NOT NULL，在操作数据库时如果输入该字段的数据为NULL，就会报错；
+ AUTO_INCREMENT定义列为自增的属性，一般用于主键，数值会自动+1；
+ PRIMARY KEY关键字用于定义为主键。您可以使用多列来定义主键，列间以逗号分隔。
+ ENGINE设置存储引擎，CHARSET设置编码。

### 通过命令提示符创建表

通过 mysql> 命令窗口可以很简单的创建MySQL数据表。你可以使用 SQL 语句 **CREATE TABLE** 来创建数据表。

#### 实例

以下为创建数据表 runoob_tbl 实例:

```
root@host# mysql -u root -p
Enter password:*******
mysql> use RUNOOB;
Database changed
mysql> CREATE TABLE runoob_tbl(
   -> runoob_id INT NOT NULL AUTO_INCREMENT,
   -> runoob_title VARCHAR(100) NOT NULL,
   -> runoob_author VARCHAR(40) NOT NULL,
   -> submission_date DATE,
   -> PRIMARY KEY ( runoob_id )
   -> )ENGINE=InnoDB DEFAULT CHARSET=utf8;
Query OK, 0 rows affected (0.16 sec)
mysql>
```

**注意：**MySQL命令终止符为分号 **;** 。

**注意：** **->** 是换行符标识，不要复制

## 十、删除数据表

### 语法

以下为删除MySQL数据表的通用语法：

```
DROP TABLE table_name ;
```

## 在命令提示窗口中删除数据表

在mysql>命令提示窗口中删除数据表SQL语句为 **DROP TABLE** ：

### 实例

以下实例删除了数据表runoob_tbl:

```mysql
root@host# mysql -u root -p
Enter password:*******
mysql> use RUNOOB;
Database changed
mysql> DROP TABLE runoob_tbl;
Query OK, 0 rows affected (0.8 sec)
mysql>
```

## 十一、插入数据

### 语法

以下为向MySQL数据表插入数据通用的 **INSERT INTO** SQL语法：

```mysql
INSERT INFO table_name (field1,field2,...fieldN)
						VALUES
						(value1, value2,...valueN);
```

### 通过命令提示窗口插入数据

```mysql
root@host# mysql -u root -p password;
Enter password:*******
mysql> use RUNOOB;
Database changed
mysql> Query OK, 1 rows affected, 1 warnings (0.01 sec)
mysql> INSERT INTO runoob_tbl
    -> (runoob_title, runoob_author, submission_date)
    -> VALUES
    -> ("学习 PHP", "菜鸟教程", NOW());
Query OK, 1 rows affected, 1 warnings (0.01 sec)
mysql> INSERT INTO runoob_tbl
    -> (runoob_title, runoob_author, submission_date)
    -> VALUES
    -> ("学习 MySQL", "菜鸟教程", NOW());
Query OK, 1 rows affected, 1 warnings (0.01 sec)
mysql> INSERT INTO runoob_tbl
    -> (runoob_title, runoob_author, submission_date)
    -> VALUES
    -> ("JAVA 教程", "RUNOOB.COM", '2016-05-06');
Query OK, 1 rows affected (0.00 sec)
mysql>
```

## 十二、查询数据

MySQL 数据库使用SQL SELECT语句来查询数据。

### 语法

以下为在MySQL数据库中查询数据通用的 SELECT 语法：

```mysql
SELECT column_name,column_name
FROM table_name
[WHERE Clause]
[LIMIT N][ OFFSET M]
```

- 查询语句中你可以使用一个或者多个表，表之间使用逗号(,)分割，并使用WHERE语句来设定查询条件。

- SELECT 命令可以读取一条或者多条记录。

- 你可以使用星号（*）来代替其他字段，SELECT语句会返回表的所有字段数据

- 你可以使用 WHERE 语句来包含任何条件。

- 你可以使用 LIMIT 属性来设定返回的记录数。

- 你可以通过OFFSET指定SELECT语句开始查询的数据偏移量。默认情况下偏移量为0。通过命令提示符获取数据

  以下实例我们将通过 SQL SELECT 命令来获取 MySQL 数据表 runoob_tbl 的数据：

  ### 实例

  以下实例将返回数据表 runoob_tbl 的所有记录:

  ### 读取数据表：

  `select * from runoob_tbl;`

  输出结果：

  ![img](https://www.runoob.com/wp-content/uploads/2014/03/DB742246-84F3-4447-BD43-6BAEADD7CA91.jpg)

## 十三、MySQL WHERE字句

我们知道从 MySQL 表中使用 SQL SELECT 语句来读取数据。

如需有条件地从表中选取数据，可将 WHERE 子句添加到 SELECT 语句中。

### 语法

以下是 SQL SELECT 语句使用 WHERE 子句从数据表中读取数据的通用语法：

```mysql
SELECT field1, field2,...fieldN FROM table_name1, table_name2...
[WHERE condition1 [AND [OR]] condition2.....
```

- 查询语句中你可以使用一个或者多个表，表之间使用逗号**,** 分割，并使用WHERE语句来设定查询条件。
- 你可以在 WHERE 子句中指定任何条件。
- 你可以使用 AND 或者 OR 指定一个或多个条件。
- WHERE 子句也可以运用于 SQL 的 DELETE 或者 UPDATE 命令。
- WHERE 子句类似于程序语言中的 if 条件，根据 MySQL 表中的字段值来读取指定的数据。

以下为操作符列表，可用于 WHERE 子句中。

下表中实例假定 A 为 10, B 为 20

| 操作符 | 描述                                                         | 实例                 |
| :----- | :----------------------------------------------------------- | :------------------- |
| =      | 等号，检测两个值是否相等，如果相等返回true                   | (A = B) 返回false。  |
| <>, != | 不等于，检测两个值是否相等，如果不相等返回true               | (A != B) 返回 true。 |
| >      | 大于号，检测左边的值是否大于右边的值, 如果左边的值大于右边的值返回true | (A > B) 返回false。  |
| <      | 小于号，检测左边的值是否小于右边的值, 如果左边的值小于右边的值返回true | (A < B) 返回 true。  |
| >=     | 大于等于号，检测左边的值是否大于或等于右边的值, 如果左边的值大于或等于右边的值返回true | (A >= B) 返回false。 |
| <=     | 小于等于号，检测左边的值是否小于或等于右边的值, 如果左边的值小于或等于右边的值返回true | (A <= B) 返回 true。 |

如果我们想在 MySQL 数据表中读取指定的数据，WHERE 子句是非常有用的。

使用主键来作为 WHERE 子句的条件查询是非常快速的。

如果给定的条件在表中没有任何匹配的记录，那么查询不会返回任何数据。

### 从命令提示符中读取数据

我们将在SQL SELECT语句使用WHERE子句来读取MySQL数据表 runoob_tbl 中的数据：

实例

以下实例将读取 runoob_tbl 表中 runoob_author 字段值为 Sanjay 的所有记录：

### SQL SELECT WHERE 子句

SELECT * from runoob_tbl WHERE runoob_author='菜鸟教程';

输出结果：

![img](https://www.runoob.com/wp-content/uploads/2014/03/CED9CA9C-E4C7-4809-875C-A7E48F430059.jpg)



MySQL 的 WHERE 子句的字符串比较是不区分大小写的。 你可以使用 BINARY 关键字来设定 WHERE 子句的字符串比较是区分大小写的。

如下实例:

### BINARY 关键字

```mysql
mysql> SELECT * from runoob_tbl WHERE BINARY runoob_author='runoob.com';
Empty set (0.01 sec)
 
mysql> SELECT * from runoob_tbl WHERE BINARY runoob_author='RUNOOB.COM';
+-----------+---------------+---------------+-----------------+
| runoob_id | runoob_title  | runoob_author | submission_date |
+-----------+---------------+---------------+-----------------+
| 3         | JAVA 教程   | RUNOOB.COM    | 2016-05-06      |
| 4         | 学习 Python | RUNOOB.COM    | 2016-03-06      |
+-----------+---------------+---------------+-----------------+
2 rows in set (0.01 sec)
```



实例中使用了 **BINARY** 关键字，是区分大小写的，所以 **runoob_author='runoob.com'** 的查询条件是没有数据的。

## 十四、MySQL UPDATE更新

如果我们需要修改或更新 MySQL 中的数据，我们可以使用 SQL UPDATE 命令来操作。

### 语法

以下是UPDATE命令修改MySQL数据表数据通用的SQL语法：

```mysql
UPDATE table_name SET field1=new-value1, field2=new-value2
[WHERE Clause]
```

- 你可以同时更新一个或多个字段。
- 你可以在 WHERE 子句中指定任何条件。
- 你可以在一个单独表中同时更新数据。

当你需要更新数据表中指定行的数据时 WHERE 子句是非常有用的。

通过命令提示符更新数据

以下我们将在 SQL UPDATE 命令使用 WHERE 子句来更新 runoob_tbl 表中指定的数据：

### 实例

以下实例将更新数据表中 runoob_id 为 3 的 runoob_title 字段值：

### SQL UPDATE 语句：

```mysql
mysql> UPDATE runoob_tbl SET runoob_title='学习 C++' WHERE runoob_id=3;
Query OK, 1 rows affected (0.01 sec)
 
mysql> SELECT * from runoob_tbl WHERE runoob_id=3;
+-----------+--------------+---------------+-----------------+
| runoob_id | runoob_title | runoob_author | submission_date |
+-----------+--------------+---------------+-----------------+
| 3         | 学习 C++   | RUNOOB.COM    | 2016-05-06      |
+-----------+--------------+---------------+-----------------+
1 rows in set (0.01 sec)
```



从结果上看，runoob_id 为 3 的 runoob_title 已被修改

## 十五、DELETE语句

你可以使用 SQL 的 DELETE FROM 命令来删除 MySQL 数据表中的记录。

你可以在 **mysql>** 命令提示符或 PHP 脚本中执行该命令。

### 语法

以下是SQL DELETE语句从MySQL数据表中删除数据的通用语法

```mysql
DELETE FROM table_name [WHERE Clause]
```

- 如果没有指定 WHERE 子句，MySQL 表中的所有记录将被删除。
- 你可以在 WHERE 子句中指定任何条件
- 您可以在单个表中一次性删除记录。

当你想删除数据表中指定的记录时 WHERE 子句是非常有用的。

### 从命令行中删除数据

这里我们将在 SQL DELETE 命令中使用 WHERE 子句来删除 MySQL 数据表 runoob_tbl 所选的数据。

### 实例

以下实例将删除 runoob_tbl 表中 runoob_id 为3 的记录：

```mysql
mysql> use RUNOOB;
Database changed
mysql> DELETE FROM runoob_tbl WHERE runoob_id=3;
Query OK, 1 row affected (0.23 sec)

```

## 十六、LIKE字句

我们知道在 MySQL 中使用 SQL SELECT 命令来读取数据， 同时我们可以在 SELECT 语句中使用 WHERE 子句来获取指定的记录。

WHERE 子句中可以使用等号 **=** 来设定获取数据的条件，如 "runoob_author = 'RUNOOB.COM'"。

但是有时候我们需要获取 runoob_author 字段含有=="COM"== 字符的所有记录，这时我们就需要在 WHERE 子句中使用 SQL LIKE 子句。

SQL LIKE 子句中使用百分号 **%**字符来表示任意字符，类似于UNIX或正则表达式中的星号 *****。

如果没有使用百分号 **%**, LIKE 子句与等号 **=** 的效果是一样的。

### 语法

以下是 SQL SELECT 语句使用 LIKE 子句从数据表中读取数据的通用语法：

```mysql
SELECT field1, field2,...fieldN 
FROM table_name
WHERE field1 LIKE condition1 [AND [OR]] filed2 = 'somevalue'
```

- 你可以在 WHERE 子句中指定任何条件。

- 你可以在 WHERE 子句中使用LIKE子句。

- 你可以使用==LIKE子句代替等号 **=**。==

- LIKE 通常与 **%** 一同使用，类似于一个元字符的搜索。

- 你可以使用 AND 或者 OR 指定一个或多个条件。

- 你可以在 DELETE 或 UPDATE 命令中使用 WHERE...LIKE 子句来指定条件。

  ### 在命令提示符中使用 LIKE 子句

  以下我们将在 SQL SELECT 命令中使用 WHERE...LIKE 子句来从MySQL数据表 runoob_tbl 中读取数据。

  实例

  以下是我们将 runoob_tbl 表中获取 runoob_author 字段中以 **COM** 为结尾的的所有记录：

  ### SQL LIKE 语句：

  ```mysql
  mysql> use RUNOOB;
  Database changed
  mysql> SELECT * from runoob_tbl  WHERE runoob_author LIKE '%COM';
  +-----------+---------------+---------------+-----------------+
  | runoob_id | runoob_title  | runoob_author | submission_date |
  +-----------+---------------+---------------+-----------------+
  | 3         | 学习 Java   | RUNOOB.COM    | 2015-05-01      |
  | 4         | 学习 Python | RUNOOB.COM    | 2016-03-06      |
  +-----------+---------------+---------------+-----------------+
  2 rows in set (0.01 sec)
  ```

  

## 十七、UNION操作符

### 描述

MySQL UNION 操作符用于连接==两个以上的 SELECT 语句==的结果组合到一个结果集合中。多个 SELECT 语句会删除重复的数据。

### 语法

MySQL UNION 操作符语法格式：

```mysql
SELECT expression1, expression2, ... expression_n
FROM tables
[WHERE conditions]
UNION [ALL | DISTINCT]
SELECT expression1, expression2, ... expression_n
FROM tables
[WHERE conditions];
```

### 参数

- **expression1, expression2, ... expression_n**: 要检索的列。
- **tables:** 要检索的数据表。
- **WHERE conditions:** 可选， 检索条件。
- **DISTINCT:** 可选，删除结果集中重复的数据。默认情况下 UNION 操作符已经删除了重复数据，所以 DISTINCT 修饰符对结果没啥影响。
- **ALL:** 可选，返回所有结果集，包含重复数据。

### 演示数据库

在本教程中，我们将使用 RUNOOB 样本数据库。

下面是选自 "Websites" 表的数据：

```mysql
mysql> SELECT * FROM Websites;
+----+--------------+---------------------------+-------+---------+
| id | name         | url                       | alexa | country |
+----+--------------+---------------------------+-------+---------+
| 1  | Google       | https://www.google.cm/    | 1     | USA     |
| 2  | 淘宝          | https://www.taobao.com/   | 13    | CN      |
| 3  | 菜鸟教程      | http://www.runoob.com/    | 4689  | CN      |
| 4  | 微博          | http://weibo.com/         | 20    | CN      |
| 5  | Facebook     | https://www.facebook.com/ | 3     | USA     |
| 7  | stackoverflow | http://stackoverflow.com/ |   0 | IND     |
+----+---------------+---------------------------+-------+---------+
```

下面是 "apps" APP 的数据：

```mysql
mysql> SELECT * FROM apps;
+----+------------+-------------------------+---------+
| id | app_name   | url                     | country |
+----+------------+-------------------------+---------+
|  1 | QQ APP     | http://im.qq.com/       | CN      |
|  2 | 微博 APP | http://weibo.com/       | CN      |
|  3 | 淘宝 APP | https://www.taobao.com/ | CN      |
+----+------------+-------------------------+---------+
3 rows in set (0.00 sec)
```

### SQL UNION 实例

下面的 SQL 语句从 "Websites" 和 "apps" 表中选取所有**不同的**country（只有不同的值）：

```mysql
SELECT country FROM Websites
UNION
SELECT country FROM apps
ORDER BY country;
```

执行以上 SQL 输出结果如下：

![img](https://www.runoob.com/wp-content/uploads/2013/09/union1.jpg)

**注释：**UNION 不能用于列出两个表中所有的country。如果一些网站和APP来自同一个国家，每个国家只会列出一次。UNION 只会选取不同的值。请使用 UNION ALL 来选取重复的值！

### SQL UNION ALL 实例

下面的 SQL 语句使用 UNION ALL 从 "Websites" 和 "apps" 表中选取**所有的**country（也有重复的值）：

```mysql
SELECT country FROM Websites
UNION ALL
SELECT country FROM apps
ORDER BY country;
```

执行以上 SQL 输出结果如下：

![img](https://www.runoob.com/wp-content/uploads/2013/09/union2.jpg)

### 带有 WHERE 的 SQL UNION ALL

下面的 SQL 语句使用 UNION ALL 从 "Websites" 和 "apps" 表中选取**所有的**中国(CN)的数据（也有重复的值）：

```mysql
SELECT country, name FROM Websites
WHERE country='CN'
UNION ALL
SELECT country, app_name FROM apps
WHERE country='CN'
ORDER BY country;
```

执行以上 SQL 输出结果如下：

![img](https://www.runoob.com/wp-content/uploads/2013/09/AAA99C7B-36A5-43FB-B489-F8CE63B62C71.jpg)
