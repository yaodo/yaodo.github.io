## docker container ssh login
### 1.docker拉取ubuntu镜像运行 
```
PS C:\Windows\system32> docker run -it -d -p 50000:22 ubuntu
dc3570034a85849caa6e8d8c078e0af69ea27b3883c8778c00325f3d9e6d24d9
PS C:\Windows\system32> docker ps
CONTAINER ID   IMAGE     COMMAND       CREATED         STATUS         PORTS                   NAMES
dc3570034a85   ubuntu    "bash"        5 seconds ago   Up 3 seconds   0.0.0.0:50000->22/tcp   nice_colden
PS C:\Windows\system32> docker exec -it dc3570034a85 /bin/bash
```

### 2.进入容器修改密码，安装openssh-server，装了个nano，修改/etc/ssh/sshd_config配置
```
root@dc3570034a85:/# passwd
New password:
Retype new password:
passwd: password updated successfully
root@dc3570034a85:/# apt-get update
root@dc3570034a85:/# apt-get install openssh-server
```

```
root@dc3570034a85:/# apt-get install nano
#PermitRootLogin prohibit-password
PermitRootLogin yes
```
### 3.service ssh restart
root@localhost's password: 
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.10.16.3-microsoft-standard-WSL2 x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.
Last login: Wed Jan 23 16:23:43 2022 from 172.17.0.1
root@f07948b6d9f4:~#

### 4.打包正在运行的容器为新的镜像ubuntussh并测试ssh登录正常
```
PS C:\Windows\system32> docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED          STATUS          PORTS                   NAMES
dc3570034a85   ubuntu    "bash"    16 minutes ago   Up 16 minutes   0.0.0.0:50000->22/tcp   nice_colden
PS C:\Windows\system32> docker commit dc3570034a85 ubuntussh
sha256:516f27f0cc8c1fb1acb4c61def56d9c5ef22a87e60914a851d479f5aa2bc7450
PS C:\Windows\system32> docker run -it -d -p 51000:22 ubuntussh
e7bc819d7a57ca5e6ba17a211cc7868fbffd7a06e8ed9b531f021bd668d2ef6e
PS C:\Windows\system32> docker ps
CONTAINER ID   IMAGE       COMMAND   CREATED          STATUS          PORTS                   NAMES
e7bc819d7a57   ubuntussh   "bash"    5 seconds ago    Up 4 seconds    0.0.0.0:51000->22/tcp   crazy_faraday
PS C:\Windows\system32> docker image ls
REPOSITORY                                                                   TAG                                                     IMAGE ID       CREATED             SIZE
ubuntussh                                                                    latest              
```
