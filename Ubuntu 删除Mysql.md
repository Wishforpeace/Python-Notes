# Ubuntu 删除Mysql

**1. 删除mysql**

```
a. sudo apt-get autoremove --purge mysql-server-5.0
b. sudo apt-get remove mysql-server
c. sudo apt-get autoremove mysql-server
d. sudo apt-get remove mysql-common (非常重要)
```

上面的其实有一些是多余的，建议还是按照顺序执行一遍

**2. 清理残留数据**

```
dpkg -l |grep ^rc|awk '{print $2}' |sudo xargs dpkg -P
（这一步很重要，这完成上面步骤会有残留数据，无法安装成功）
```