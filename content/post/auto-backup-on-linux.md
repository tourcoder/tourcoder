---
title: "Linux 下利用 crontab 自动备份"
slug: "auto-backup-on-linux"
author: "Bin Hua"
lastmod: 2020-07-18 06:18:06
date: 2014-03-22 06:37:07
tags: ["crontab", "linux", "mysql"]
---

数据有多重要，不用我详说，如果每天人工备份，又太繁琐，所以利用 crontab 来自动备份文件就是一个很不错的办法。

**导出文件或打包压缩文件**

- Mysql 数据库 
    
    首先需要导出数据库的内容
    
    - 导出到文件 
    
        ```
        /usr/bin/mysqldump -u root -ppwd database > database.sql 
        ```
        
    - 或者导出成压缩文件
    
        ```
        /usr/bin/mysqldump -u root -ppwd database  | gzip > database.sql.gz
        ```
        
    - 补充：导入到数据库
    
        ```
        mysql -u root -p database < database.sql //从文件导入到数据库 
        gzip < database.sql.gz | mysql -u root -p database //从压缩文件导入到数据库
        ```
        
    - 其他文件
    
        其他比如网站的文件等，可以直接用压缩命令打包压缩成压缩文件即可。 
        
        ```
        tar -zvcf packagename.tar file/forlder 
        ```
        
- mongodb

    直接上脚本
    
    ```
    #!/bin/sh
    DUMP=/usr/bin/mongodump
    OUT_DIR=/home/backup/mongodb_backup
    DATE=`date +%Y-%m-%d`
    DB_NAME=DBNAME
    DB_USER=dbusername
    DB_PASS=dbuserpassword
    TAR_BAK="mongodb_$DATE.tar.gz"
    cd $OUT_DIR
    mkdir -p $OUT_DIR/$DATE
    $DUMP -h 127.0.0.1:27017 -u $DB_USER -p $DB_PASS -d $DB_NAME -o $OUT_DIR/$DATE
    tar -zcvf $OUT_DIR/$TAR_BAK $OUT_DIR/$DATE
    exit
    ```
    
    如果 mongodb 没有设置数据库的话，则使用 `$DUMP -h 127.0.0.1:27017 -d $DB_NAME -o $OUT_DIR/$DATE`。
    
**Crontab 定时器备份**

- 创建备份目录 
    
    ```
    mkdir -p /backup/mysqlbackup cd /backup/mysqlbackup 
    ```
    
- 编写脚本
    
    ```
    vi /usr/sbin/backupmysql.sh
    ```
    
    ```
    #!/bin/bash 
    # backupdir=/bak/mysqlbackup time=`date +%Y%m%d%H` mysql_bin_dir/mysqldump -u root -ppwd database | gzip > $backupdir/database$time.sql.gz 
    ```
    
- 执行权限 

    ```
    chmod +x /usr/sbin/backupmysql.sh
    ```
    
- 设置 crontab 定时执行

    ```
    vi /etc/crontab
    ```
    
    在最后一行中加入 
    
    ```
    00 8 * * * root /usr/sbin/backupmysql.sh //表示每天8点00分执行备份
    ```
    
    注：crontab配置文件格式：分　时　日　月　周　 命令

- 最后重启

#### 定时器的介绍

- 第1列分钟0～59

- 第2列小时0～23（0表示子夜）

- 第3列日1～31

- 第4列月1～12

- 第5列星期0～7（0和7表示星期天）

- 第6列要运行的命令

执行命令

```
crontab -e
```

编辑里面的内容，如我的内容是

```
# minute hour day mon week  command
* * * * * /backup.sh //每分钟
10 12 * * * /backup.sh //每天十二点十分
10,30 15-20 * * * /backup.sh //每天下午三点到晚上八点的第 10 分钟和第 30 分钟
10,30 * * * * /backup.sh //每小时的第 10 和 30 分钟
10,30 2-10 * * * /backup.sh //每天 2 点到 10 点（上午）
10,30 2-10 */2 * * /backup.sh //每隔两天 2 点到 10 点（上午）
10,30 2-10 */2 * 2 /backup.sh //每周二 2 点到 10 点（上午）
* */4 * * * /backup.sh //每四个小时
```

更多 crontab 的用法，如 `crontab -l，crontab -r，/sbin/service crond restart|start|stop|reload` 等，请自行搜索。当 linux 中没有 service 这个命令的时候 `sudo /etc/init.d/cron restart|start|stop`

比如每十秒执行一次，还可以用这种方式

```
* * * * * /usr/bin/curl http://127.0.0.1:3003
* * * * * sleep 10; /usr/bin/curl http://127.0.0.1:3003
* * * * * sleep 20; /usr/bin/curl http://127.0.0.1:3003
* * * * * sleep 30; /usr/bin/curl http://127.0.0.1:3003
* * * * * sleep 40; /usr/bin/curl http://127.0.0.1:3003
* * * * * sleep 50; /usr/bin/curl http://127.0.0.1:3003
```

**update@20170401:VPS 备份到 Gdrive**

Dropbox 被塞满了，想到我还有 600G 的 Google Drive 空间，索性就将数据备份到 Google Drive 里吧。

GitHub 上有个项目符合我的需求，访问 [https://github.com/prasmussen/gdrive](https://github.com/prasmussen/gdrive)

下载对应的版本，我这里选择了 `gdrive-linux-x64`，下载执行命令

```
wget -O /usr/bin/gdrive http://download-url/gdrive-linux-x64
chmod +x /usr/bin/gdrive
```

执行命令 `gdrive about`，会提示你通过浏览器访问显示的地址，确定完成授权。

设置备份脚本，`vi backup.sh`

```
# 备份信息的设置
REMOTE_DIR="$(date +%Y-%m-%d)"
BACKUP_UPLOAD_DIR="backup"
# 需备份的文件
BACKUP_DIR="/home"
COMPRESS_FILE=$(date +%Y%m%d).tar.gz //有时候多次备份，预防名称重叠，可以用时间戳 $(date +%s)

# 判断本地文件是否存在，如果不存在则创建
if [ ! -d $BACKUP_UPLOAD_DIR ]; then
mkdir -p $BACKUP_UPLOAD_DIR
fi

# 压缩
tar -zcvf $COMPRESS_FILE $BACKUP_DIR

# 上传
cd ~
gdrive upload $COMPRESS_FILE

# 删除本地压缩文件
rm -rf $COMPRESS_FILE

# gdrive info
gdrive about

exit 0
```

这里测试下，执行命令 `./backup.sh`，完成后检查是否正常。这里上传文件都是上传到 gdrive 的根目录，会显得很凌乱，可以通过参数上传到指定的目录。

- 先在 gdrive 目录下新建一个文件夹，然后通过 `gdrive list` 命令获取它的 id

- 修改上面的上传命令 `gdrive upload -p <id> $COMPRESS_FILE`，即可完成上传到指定的文件夹。

有时候会需要重新更换用户，目前没有一个官方方式，但可以通过 `rm -rf ~/.gdrive/token_*.json`，然后执行备份命令即可。

我们还需要设置自动备份功能，利用 crontab，具体参考上面写的相关内容

**延伸内容**

导出 `Mysql/Mariadb` 数据库，然后备份上传

```
#!/bin/sh
DB_USER="username"
DB_PASS="password"
DB_HOST="localhost"
DB_NAME="database_name"
BIN_DIR="/usr/bin"            #the mysql bin path
BACKUP_DIR="/root"    #the backup file directory
DATE=`date +%Y%m%d%H`
$BIN_DIR/mysqldump —single-transaction -u$DB_USER -p$DB_PASS -h$DB_HOST $DB_NAME > $BACKUP_DIR/db_$DATE.sql
cd ~
gdrive upload db_$DATE.sql
# 删除本地压缩文件
rm db_$DATE.sql
# gdrive info
gdrive about
exit 0
```

**自动备份到 Dropbox**

这里使用了脚本 `dropbox_uploader.sh`，该项目地址是 [https://github.com/andreafabrizi/Dropbox-Uploader](https://github.com/andreafabrizi/Dropbox-Uploader)

- 准备工作

    - 先登录到 [https://www.dropbox.com/developers/apps/](https://www.dropbox.com/developers/apps/) 创建一个 App，然后获取 AccessToken.

    - dropbox_uploader.sh 脚本

        根据上面脚本项目的说明，下载文件并执行

        ```
        curl "https://raw.githubusercontent.com/andreafabrizi/Dropbox-Uploader/master/dropbox_uploader.sh" -o dropbox_uploader.sh
        chmod +x dropbox_uploader.sh
        ./dropbox_uploader.sh
        ```
        
        此时会要求你填入上面步骤中获取到的 accesstoken，输入 accesstoken 后，选择 y 即可完成授权

    - 备份脚本

        新建一个脚本文件，比如 backup.sh，填入如下内容

        ```
        #!/bin/bash
        DROPBOX_DIR=/$(date +%Y-%m-%d)
        BACKUP_FOLDER=~/backup
        TARGET_FOLDER=/root/html/tc
        TC=TC_$(date +%Y-%m-%d).tar.gz
        echo -ne "Start"
        cd $TARGET_FOLDER
        tar zvcf $BACKUP_FOLDER/$TC *
        echo -e "Done"
        cd ~
        ./dropbox_uploader.sh upload  $BACKUP_FOLDER/$TC $DROPBOX_DIR/$TC
        ```
        
        上面的脚本内容可以根据自己的情况尽心修改，然后执行该文件，即可测试下是否正常。

    - 自动化

        自动化部分如上面的备份到 Gdrive 一样的利用 crontab 来执行，一样的。