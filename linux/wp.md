忽略ftp权限

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
