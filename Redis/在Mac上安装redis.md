# 在Mac上安装redis

一、安装

首先保证电脑上有brew然后使用下面的命令安装即可

```javascript
brew install redis
```

复制

二、常用命令

1.启动redis服务

```javascript
brew services start redis
```

复制

2.关闭redis服务

```javascript
brew services stop redis
```

复制

3.重启redis服务

```javascript
brew services restart redis
```

复制

4.打开图形化界面

```javascript
redis-cli
```

复制

5.开机启动redis命令

```javascript
ln -sfv /usr/local/opt/redis/*.plist ~/Library/LaunchAgents
```

复制

6.使用配置文件启动redis-server

```javascript
redis-server /usr/local/etc/redis.conf
```

复制

7.停止redis服务

```javascript
redis-cli shutdown
```

复制

\8. redis配置文件位置

```javascript
/usr/local/etc/redis.conf
```

复制

9.卸载redis

```javascript
brew uninstall redis rm ~/Library/LaunchAgents/homebrew.mxcl.redis.plist
```

复制

10.允许远程访问

```javascript
vim /usr/local/etc/redis.conf
```

复制

注释bind，默认情况下 redis不允许远程访问，只允许本机访问。

```javascript
#bind 127.0.0.1
```

复制

注：在redis3.2之后，redis增加了protected-mode，在这个模式下，即使注释掉了bind 127.0.0.1，再访问redisd时候还是报错，需要把protected-mode yes改为protected-mode no