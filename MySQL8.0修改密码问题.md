# MySQL8.0修改密码问题

 原创

[80后小菜鸟](https://blog.51cto.com/zhangxinqi)2018-09-19 17:40:44博主文章分类：[数据库](https://blog.51cto.com/zhangxinqi/category5)©著作权

*文章标签*[MySQL8](https://blog.51cto.com/topic/mysql8.html)[修改密码](https://blog.51cto.com/search/result?q=修改密码)*文章分类*[Linux](https://blog.51cto.com/nav/linux)[系统/运维](https://blog.51cto.com/nav/ops)*阅读数*1.9万

MySQL5.7和之前的用户修改密码方式：

```sql
mysql -uroot -e "Set password=password(‘123’);"
mysql -uroot -p123.com -e "use mysql;update user set authentication_string=password('456') where user='root';"
update mysql.user set authentication_string=password("123") where user='root';1.2.3.
```

以上三种方法在MySQL8.0以后版本中将不能使用，如果使用了将会导致在正确修改密码是报如下错误：

```sql
mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123';
ERROR 1396 (HY000): Operation ALTER USER failed for 'root'@'localhost'1.2.
```

如遇上以上问题请使用update语句先清空authentication_string字段，然后再修改密码即可

```sql
update user set authentication_string='' where user='root';
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '你的密码';1.2.
```

所以特别提醒童鞋们：

MySQL8.0后请使用alter修改用户密码，因为在MySQL8.0以后的加密方式为caching_sha2_password，如果使用update修改密码会给user表中root用户的authentication_string字段下设置newpassowrd值，当再使用alter user 'root'@'localhost' identified by 'newpassword'修改密码时会一直报错，必须清空后再修改，因为authentication_string字段下只能是MySQL加密后的43位字符串密码，其他的会报格式错误，所以在MySQL8.0以后能修改密码的方法只能是：ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '你的密码';