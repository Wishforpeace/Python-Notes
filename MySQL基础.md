# `MySQL`基础

## 数据库的相关概念

> `DB`：数据库：存储数据的“仓库”，保存了一系列有组织的数据
>
> `DBMS`：数据库管理系统（Database Management System),数据库是通过DBMS创建和操作的容器
>
> `SQL`：结构化查询语言(Structure Query Language),专门用来与数据库通信的语言。



## `SQL`语言概述

### `SQL`的优点:

> 1、不是某个特定数据库供应商专有的语言,几乎所有
> `DBMS`都支持`SQL`
> 2、简单易学
> 3、虽然简单,但实际上是一种强有力的语言,灵活使
> 用其语言元素,可以进行非常复杂和高级的数据库操作。

## 数据库的特点

> • 1、将数据放到表中,表再放到库中
> • 2、一个数据库中可以有多个表,每个表都有一个的名字,用来
> 标识自己。表名具有唯一性。
> • 3、表具有一些特性,这些特性定义了数据在表中如何存储,类
> 似`java`中 “类”的设计。
> • 4、表由列组成,我们也称为字段。所有表都是由一个或多个列
> 组成的,每一列类似`java` 中的”属性”
> • 5、表中的数据是按行存储的,每一行类似于`java`中的“对象”。
>
> 

## `SQL`语言分类

> 1、`DML`(Data Manipulation Language):数据操纵语句,用于添
> 加、删除、修改、查询数据库记录,并检查数据完整性
> 2、`DDL`(Data Definition Language):数据定义语句,用于库和
> 表的创建、修改、删除。
> 3、`DCL`(Data Control Language):数据控制语句,用于定义用
> 户的访问权限和安全级别。

## `DML`

`DML`用于查询与修改数据记录,包括如下`SQL`语句:

+ INSERT:==添加==数据到数据库中
+ UPDATE:==修改==数据库中的数据
+ DELETE:==删除==数据库中的数据
+ SELECT:==选择(查询)==数据
+  SELECT是`SQL`语言的基础,最为重要。

## `DDL`

`DDL`用于定义数据库的结构,比如创建、修改或删除
数据库对象,包括如下`SQL`语句:

+ CREATE TABLE:==创建==数据库表
+ ALTER TABLE: ==更改==表结构、添加、删除、修改列长度
+ DROP TABLE:==删除表==
+ CREATE INDEX`:在表上建立==索引==
+ `DROP INDEX`:==删除索引==

## `DCL`

`DCL`用来控制数据库的访问,包括如下`SQL`语句:

+ `GRANT`:授予访问权限
+ `REVOKE`:撤销访问权限
+ `COMMIT`:提交事务处理
+ `ROLLBACK`:事务处理回退
+ `SAVEPOINT`:设置保存点
+ `LOCK`:对数据库的特定部分进行锁定

```
## List of all `MySQL` commands:

Note that all text commands must be first on line and end with ';'
?         (\?) Synonym for `help'.
clear     (\c) Clear the current input statement.
connect   (\r) Reconnect to the server. Optional arguments are db and host.
delimiter (\d) Set statement delimiter.
edit      (\e) Edit command with $EDITOR.
ego       (\G) Send command to mysql server, display result vertically.
exit      (\q) Exit mysql. Same as quit.
go        (\g) Send command to mysql server.
help      (\h) Display this help.
nopager   (\n) Disable pager, print to stdout.
notee     (\t) Don't write into outfile.
pager     (\P) Set PAGER [to_pager]. Print the query results via PAGER.
print     (\p) Print current command.
prompt    (\R) Change your mysql prompt.
quit      (\q) Quit mysql.
rehash    (\#) Rebuild completion hash.
source    (\.) Execute an SQL script file. Takes a file name as an argument.
status    (\s) Get status information from the server.
system    (\!) Execute a system shell command.
tee       (\T) Set outfile [to_outfile]. Append everything into given outfile.
use       (\u) Use another database. Takes database name as argument.
charset   (\C) Switch to another charset. Might be needed for processing binlog with multi-byte charsets.
warnings  (\W) Show warnings after every statement.
nowarning (\w) Don't show warnings after every statement.
resetconnection(\x) Clean session context.
query_attributes Sets string parameters (name1 value1 name2 value2 ...) for the next query to pick up.
```





```
所有 MySQL 命令的列表：
请注意，所有文本命令必须排在第一行并以“;”结尾
? (\?) “帮助”的同义词。
clear (\c) 清除当前输入语句。
连接 (\r) 重新连接到服务器。可选参数是 db 和 host。
分隔符 (\d) 设置语句分隔符。
编辑 (\e) 使用 $EDITOR 编辑命令。
ego (\G) 向mysql服务器发送命令，垂直显示结果。
退出 (\q) 退出 mysql。和放弃一样。
go (\g) 向 mysql 服务器发送命令。
帮助 (\h) 显示此帮助。
nopager (\n) 禁用寻呼机，打印到标准输出。
notee (\t) 不要写入输出文件。
寻呼机 (\P) 设置 PAGER [to_pager]。通过 PAGER 打印查询结果。
打印 (\p) 打印当前命令。
提示 (\R) 更改您的 mysql 提示。
退出 (\q) 退出 mysql。
rehash (\#) 重建完成哈希。
源 (\.) 执行 SQL 脚本文件。将文件名作为参数。
status (\s) 从服务器获取状态信息。
system (\!) 执行系统 shell 命令。
tee (\T) 设置输出文件 [to_outfile]。将所有内容附加到给定的输出文件中。
使用 (\u) 使用另一个数据库。以数据库名称作为参数。
字符集 (\C) 切换到另一个字符集。可能需要处理多字节字符集的 binlog。
警告 (\W) 在每条语句后显示警告。
nowarning (\w) 不要在每个语句之后显示警告。
resetconnection(\x) 清理会话上下文。
query_attributes 设置字符串参数（name1 value1 name2 value2 ...）以供下一个查询使用。
```