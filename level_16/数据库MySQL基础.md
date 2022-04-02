# 数据库My SQL基础

## 一、安装My SQL（UOS）

### 1.下载MySQL：https://dev.mysql.com/downloads/

### 2.解压tar.gz 包

```undefined
tar -xvf mysql-8.0.20-linux-glibc2.12-x86_64.tar.xz 
```

### 3.重命名

```bash
mv mysql-8.0.20-linux-glibc2.12-x86_64/ mysql-8.0.20
```

### 4.复制到/usr/local

```bash
sudo mv mysql-8.0.20 /usr/local/
```

### 5.创建用户组

```undefined
sudo groupadd mysql
```

### 6.添加用户

```undefined
useradd -r -g mysql mysql
```

### 7.创建MySQL数据目录

```bash
sudo mkdir -p /data
cd data
sudo mkdir -p mysql
```

### 8.修改拥有者

```bash
sudo chown mysql:mysql -R /data/mysql
```

### 9.生成编辑配置文件

```bash
sudo vim /etc/my.cnf
[mysqld]
bind-address=0.0.0.0
port=3306
user=mysql
basedir=/usr/local/mysql-8.0.20
datadir=/data/mysql
socket=/tmp/mysql.sock
log-error=/data/mysql/mysql.err
pid-file=/data/mysql/mysql.pid
#character config
character_set_server=utf8mb4
symbolic-links=0
```

### 10.初始化MYSQL

```bash
cd /usr/local/mysql-8.0.20/
sudo ./mysqld --defaults-file=/etc/my.cnf --basedir=/usr/local/mysql-5.7.26/ --datadir=/data/mysql/ --user=mysql --initialize
```

### 11.查看初始密码

```bash
sudo cat /data/mysql/mysql.err 
```

![img](https://img2020.cnblogs.com/blog/724874/202007/724874-20200719173350193-549963915.png)

### 12.启动mysql

1. service mysql start 出现问题
   Failed to start mysqld.service: Unit mysqld.service not found.
2. ps -ef|grep mysql 检查，确实没有相关进程启来
3. sudo find / -name mysql.server 查找
   ![img](https://img2020.cnblogs.com/blog/724874/202007/724874-20200719173706535-2118900466.png)
4. sudo cp /usr/local/mysql-8.0.20/support-files/mysql.server /etc/init.d/mysql
5. sudo /etc/init.d/mysql status
   ![img](https://img2020.cnblogs.com/blog/724874/202007/724874-20200719174051487-589634621.png)
6. sudo service mysql status
   ![img](https://img2020.cnblogs.com/blog/724874/202007/724874-20200719174233221-894039338.png)
   发现问题是因为权限问题导致的，服务进程没有问题

### 13.修改密码

![img](https://img2020.cnblogs.com/blog/724874/202007/724874-20200719174432203-1030137997.png)

```sql
alter user 'root'@'localhost' identified by '123456';
```

![img](https://img2020.cnblogs.com/blog/724874/202007/724874-20200719174556499-1267375033.png)