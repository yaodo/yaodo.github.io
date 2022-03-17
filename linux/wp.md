## wordpress ftp权限

每当我们想在wordpress上升级插件或者是升级wordpress的时候，就会弹出一个ftp登录，但是我们怎么跳过ftp登录呢

解决方法

打开我们的word press配置文件wp-config.php



[18:35:08 root@zhang ~]#vim /apps/nginx/html/wordpress/wp-config.php

然后在这个文件的最后一行下面添加上这两个777权限



define("FS_CHMOD_DIR", 0777);

define("FS_CHMOD_FILE", 0777);

在给word press这个目录添加用户权限，假如我们用的是nginx用户执行word press这个服务。


[18:37:31 root@zhang ~]#chmod -R 777 /apps/nginx/html/wordpress/

[18:37:50 root@zhang ~]#chown -R nginx:nginx /apps/nginx/html/wordpress/

以上就是wordpress升级需设置ftp的解决方法。

## lnmp安装脚本

[lnmp安装脚本](https://www.lnmp.org/install.html)
安装步骤:
### 1、使用putty或类似的SSH工具登陆VPS或服务器；防止掉线

登陆后运行：screen -S lnmp
如果提示screen: command not found 命令不存在可以执行：yum install screen 或 apt-get install screen安装，详细内容参考screen教程。

### 2、下载并安装LNMP一键安装包：

您可以选择使用下载版(推荐美国及海外VPS或空间较小用户使用)或者完整版(推荐国内VPS使用，国内用户可用在下载中找国内下载地址替换)，两者没什么区别，只是完整版把一些需要的源码文件预先放到安装包里。

### 3、安装LNMP稳定版
如需无人值守安装，请使用 无人值守命令生成工具，或查看无人值守说明教程
[lnmp无人值守安装脚本](https://lnmp.org/auto.html)
```
wget http://soft.vpser.net/lnmp/lnmp1.8.tar.gz -cO lnmp1.8.tar.gz && tar zxf lnmp1.8.tar.gz && cd lnmp1.8 && LNMP_Auto="y" DBSelect="4" DB_Root_Password="lnmp.org" InstallInnodb="y" PHPSelect="10" SelectMalloc="1" ./install.sh lnmp
```

### 4、lnmp add vhost

