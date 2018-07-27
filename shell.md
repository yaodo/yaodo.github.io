```
ifconfig 10.0.0.1 netmask 255.255.255.0 eth0:1
ip addr add 10.0.0.2/24 eth0
```
```
ifconfig eth0 |awk '/inet/{print $2}'|sed -e s/addr://
```
ifconfig
```
ifconfig eth0 |grep -o "inet addr:[^ ]*" Igrep -o "[0-9.]*"
```

crontab -e
```
crontab -l
* * * * * ntpdate 1.1.1.1;&& hwclock -w;
```
# lsof
```
找到使用某个端口的进程
# lsof -i :25
:25和-i选项组合可以让lsof列出占用TCP或UDP的25端口的进程。
也可以使用/etc/services中制定的端口名称来代替端口号，比如：
# lsof -i :smtp
找到使用某个udp端口号的进程
# lsof -i udp:53

同样的，也可以找到使用某个tcp端口的进程：

# lsof -i tcp:80
找到某个用户的所有网络连接
# lsof -a -u hacker -i
使用-a将-u和-i选项组合可以让lsof列出某个用户的所有网络行为。
列出所有NFS（网络文件系统）文件
# lsof -N
这个参数很好记，-N就对应NFS。
列出所有UNIX域Socket文件
# lsof -U
这个选项也很好记，-U就对应UNIX。
列出所有对应某个组id的进程
# lsof -g 1234
```
循环列出文件
# lsof -r 1
-r选项让lsof可以循环列出文件直到被中断，参数1的意思是每秒钟重复打印一次，这个选项最好同某个范围比较小的查询组合使用，比如用来监测网络活动：
# lsof -r 1 -u john -i -a
```
[root@host1 ~]#  lsof -r 5 -u root -i -a
COMMAND    PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
vmware-au 1553 root    8u  IPv4  13013      0t0  TCP *:ideafarm-door (LISTEN)
dhclient  1617 root    6u  IPv4  13429      0t0  UDP *:bootpc 
cupsd     1620 root    6u  IPv6  13440      0t0  TCP localhost:ipp (LISTEN)
cupsd     1620 root    7u  IPv4  13441      0t0  TCP localhost:ipp (LISTEN)
cupsd     1620 root    9u  IPv4  13444      0t0  UDP *:ipp 
sshd      1819 root    3u  IPv4  14121      0t0  TCP *:ssh (LISTEN)
sshd      1819 root    4u  IPv6  14125      0t0  TCP *:ssh (LISTEN)
hostd-wor 1983 root   30u  IPv4  15636      0t0  TCP *:https (LISTEN)
hostd-wor 1983 root   32u  IPv6  15637      0t0  TCP *:https (LISTEN)
hostd-wor 1983 root   37u  IPv6  15643      0t0  TCP localhost:8307 (LISTEN)
hostd-wor 1983 root   38u  IPv4  15644      0t0  TCP localhost:8307 (LISTEN)
vsftpd    1994 root    3u  IPv4  14367      0t0  TCP *:ftp (LISTEN)
master    2079 root   12u  IPv4  14606      0t0  TCP localhost:smtp (LISTEN)
master    2079 root   13u  IPv6  14608      0t0  TCP localhost:smtp (LISTEN)
clock-app 2570 root   21u  IPv4  24115      0t0  TCP 192.168.17.201:42085->61.131.208.210:http (CLOSE_WAIT)
sshd      2735 root    3r  IPv4  20108      0t0  TCP 192.168.17.201:ssh->192.168.17.1:53867 (ESTABLISHED)

```

lsof是系统管理/安全的尤伯工具。我大多数时候用它来从系统获得与网络连接相关的信息，但那只是这个强大而又鲜为人知的应用的第一步。将这个工具称之为lsof真实名副其实，因为它是指“列出打开文件（lists openfiles）”。而有一点要切记，在Unix中一切（包括网络套接口）都是文件。

有趣的是，lsof也是有着最多开关的Linux/Unix命令之一。它有那么多的开关，它有许多选项支持使用-和+前缀。
usage: [-?abhlnNoOPRstUvV] [+|-c c] [+|-d s] [+D D] [+|-f[cgG]]
 [-F [f]] [-g [s]] [-i [i]] [+|-L [l]] [+|-M] [-o [o]]
 [-p s] [+|-r [t]] [-S [t]] [-T [t]] [-u s] [+|-w] [-x [fl]] [--] [names]

	
usage: [-?abhlnNoOPRstUvV] [+|-c c] [+|-d s] [+D D] [+|-f[cgG]]
 [-F [f]] [-g [s]] [-i [i]] [+|-L [l]] [+|-M] [-o [o]]
 [-p s] [+|-r [t]] [-S [t]] [-T [t]] [-u s] [+|-w] [-x [fl]] [--] [names]

正如你所见，lsof有着实在是令人惊讶的选项数量。你可以使用它来获得你系统上设备的信息，你能通过它了解到指定的用户在指定的地点正在碰什么东西，或者甚至是一个进程正在使用什么文件或网络连接。

对于我，lsof替代了netstat和ps的全部工作。它可以带来那些工具所能带来的一切，而且要比那些工具多得多。那么，让我们来看看它的一些基本能力吧：
关键选项

理解一些关于lsof如何工作的关键性东西是很重要的。最重要的是，当你给它传递选项时，默认行为是对结果进行“或”运算。因此，如果你正是用-i来拉出一个端口列表，同时又用-p来拉出一个进程列表，那么默认情况下你会获得两者的结果。

下面的一些其它东西需要牢记：

    默认 : 没有选项，lsof列出活跃进程的所有打开文件
    组合 : 可以将选项组合到一起，如-abc，但要当心哪些选项需要参数
    -a : 结果进行“与”运算（而不是“或”）
    -l : 在输出显示用户ID而不是用户名
    -h : 获得帮助
    -t : 仅获取进程ID
    -U : 获取UNIX套接口地址
    -F : 格式化输出结果，用于其它命令。可以通过多种方式格式化，如-F pcfn（用于进程id、命令名、文件描述符、文件名，并以空终止）

获取网络信息

主要将lsof用于获取关于系统怎么和网络交互的信息。这里提供了关于此信息的一些主题：

使用-i显示所有连接
有些人喜欢用netstat来获取网络连接，但是我更喜欢使用lsof来进行此项工作。结果以对我来说很直观的方式呈现，我仅仅只需改变我的语法，就可以通过同样的命令来获取更多信息。
```
# lsof -i
COMMAND PID USER FD TYPE DEVICE SIZE NODE NAME
dhcpcd 6061 root 4u IPv4 4510 UDP *:bootpc
sshd 7703 root 3u IPv6 6499 TCP *:ssh (LISTEN)
sshd 7892 root 3u IPv6 6757 TCP 10.10.1.5:ssh->192.168.1.5:49901 (ESTABLISHED)

	
# lsof -i
COMMAND PID USER FD TYPE DEVICE SIZE NODE NAME
dhcpcd 6061 root 4u IPv4 4510 UDP *:bootpc
sshd 7703 root 3u IPv6 6499 TCP *:ssh (LISTEN)
sshd 7892 root 3u IPv6 6757 TCP 10.10.1.5:ssh->192.168.1.5:49901 (ESTABLISHED)

使用-i 6仅获取IPv6流量
# lsof -i 6
1
	
# lsof -i 6

仅显示TCP连接（同理可获得UDP连接）
你也可以通过在-i后提供对应的协议来仅仅显示TCP或者UDP连接信息。
# lsof -iTCP
COMMAND PID USER FD TYPE DEVICE SIZE NODE NAME
sshd 7703 root 3u IPv6 6499 TCP *:ssh (LISTEN)
sshd 7892 root 3u IPv6 6757 TCP 10.10.1.5:ssh->192.168.1.5:49901 (ESTABLISHED)

	
# lsof -iTCP
COMMAND PID USER FD TYPE DEVICE SIZE NODE NAME
sshd 7703 root 3u IPv6 6499 TCP *:ssh (LISTEN)
sshd 7892 root 3u IPv6 6757 TCP 10.10.1.5:ssh->192.168.1.5:49901 (ESTABLISHED)

使用-i:port来显示与指定端口相关的网络信息

或者，你也可以通过端口搜索，这对于要找出什么阻止了另外一个应用绑定到指定端口实在是太棒了。
# lsof -i :22
COMMAND PID USER FD TYPE DEVICE SIZE NODE NAME
sshd 7703 root 3u IPv6 6499 TCP *:ssh (LISTEN)
sshd 7892 root 3u IPv6 6757 TCP 10.10.1.5:ssh->192.168.1.5:49901 (ESTABLISHED)

	
# lsof -i :22
COMMAND PID USER FD TYPE DEVICE SIZE NODE NAME
sshd 7703 root 3u IPv6 6499 TCP *:ssh (LISTEN)
sshd 7892 root 3u IPv6 6757 TCP 10.10.1.5:ssh->192.168.1.5:49901 (ESTABLISHED)

使用@host来显示指定到指定主机的连接
这对于你在检查是否开放连接到网络中或互联网上某个指定主机的连接时十分有用。
# lsof -i@172.16.12.5
sshd 7892 root 3u IPv6 6757 TCP 10.10.1.5:ssh->172.16.12.5:49901 (ESTABLISHED)

	
# lsof -i@172.16.12.5
sshd 7892 root 3u IPv6 6757 TCP 10.10.1.5:ssh->172.16.12.5:49901 (ESTABLISHED)

使用@host:port显示基于主机与端口的连接

你也可以组合主机与端口的显示信息。
# lsof -i@172.16.12.5:22
sshd 7892 root 3u IPv6 6757 TCP 10.10.1.5:ssh->172.16.12.5:49901 (ESTABLISHED)

	
# lsof -i@172.16.12.5:22
sshd 7892 root 3u IPv6 6757 TCP 10.10.1.5:ssh->172.16.12.5:49901 (ESTABLISHED)

找出监听端口

找出正等候连接的端口。
# lsof -i -sTCP:LISTEN

	
# lsof -i -sTCP:LISTEN

你也可以grep “LISTEN”来完成该任务。
# lsof -i | grep -i LISTEN
iTunes 400 daniel 16u IPv4 0x4575228 0t0 TCP *:daap (LISTEN)

	
# lsof -i | grep -i LISTEN
iTunes 400 daniel 16u IPv4 0x4575228 0t0 TCP *:daap (LISTEN)

找出已建立的连接

你也可以显示任何已经连接的连接。
# lsof -i -sTCP:ESTABLISHED

	
# lsof -i -sTCP:ESTABLISHED

你也可以通过grep搜索“ESTABLISHED”来完成该任务。
# lsof -i | grep -i ESTABLISHED
firefox-b 169 daniel 49u IPv4 0t0 TCP 1.2.3.3:1863->1.2.3.4:http (ESTABLISHED)

	
# lsof -i | grep -i ESTABLISHED
firefox-b 169 daniel 49u IPv4 0t0 TCP 1.2.3.3:1863->1.2.3.4:http (ESTABLISHED)

用户信息

你也可以获取各种用户的信息，以及它们在系统上正干着的事情，包括它们的网络活动、对文件的操作等。

使用-u显示指定用户打开了什么
# lsof -u daniel
-- snipped --
 Dock 155 daniel txt REG 14,2 2798436 823208 /usr/lib/libicucore.A.dylib
 Dock 155 daniel txt REG 14,2 1580212 823126 /usr/lib/libobjc.A.dylib
 Dock 155 daniel txt REG 14,2 2934184 823498 /usr/lib/libstdc++.6.0.4.dylib
 Dock 155 daniel txt REG 14,2 132008 823505 /usr/lib/libgcc_s.1.dylib
 Dock 155 daniel txt REG 14,2 212160 823214 /usr/lib/libauto.dylib
 -- snipped --
	
# lsof -u daniel
-- snipped --
 Dock 155 daniel txt REG 14,2 2798436 823208 /usr/lib/libicucore.A.dylib
 Dock 155 daniel txt REG 14,2 1580212 823126 /usr/lib/libobjc.A.dylib
 Dock 155 daniel txt REG 14,2 2934184 823498 /usr/lib/libstdc++.6.0.4.dylib
 Dock 155 daniel txt REG 14,2 132008 823505 /usr/lib/libgcc_s.1.dylib
 Dock 155 daniel txt REG 14,2 212160 823214 /usr/lib/libauto.dylib
 -- snipped --

使用-u user来显示除指定用户以外的其它所有用户所做的事情
# lsof -u ^daniel
-- snipped --
 Dock 155 jim txt REG 14,2 2798436 823208 /usr/lib/libicucore.A.dylib
 Dock 155 jim txt REG 14,2 1580212 823126 /usr/lib/libobjc.A.dylib
 Dock 155 jim txt REG 14,2 2934184 823498 /usr/lib/libstdc++.6.0.4.dylib
 Dock 155 jim txt REG 14,2 132008 823505 /usr/lib/libgcc_s.1.dylib
 Dock 155 jim txt REG 14,2 212160 823214 /usr/lib/libauto.dylib
 -- snipped --
	
# lsof -u ^daniel
-- snipped --
 Dock 155 jim txt REG 14,2 2798436 823208 /usr/lib/libicucore.A.dylib
 Dock 155 jim txt REG 14,2 1580212 823126 /usr/lib/libobjc.A.dylib
 Dock 155 jim txt REG 14,2 2934184 823498 /usr/lib/libstdc++.6.0.4.dylib
 Dock 155 jim txt REG 14,2 132008 823505 /usr/lib/libgcc_s.1.dylib
 Dock 155 jim txt REG 14,2 212160 823214 /usr/lib/libauto.dylib
 -- snipped --

杀死指定用户所做的一切事情

可以消灭指定用户运行的所有东西，这真不错。
# kill -9 `lsof -t -u daniel`
	
# kill -9 `lsof -t -u daniel`

命令和进程

可以查看指定程序或进程由什么启动，这通常会很有用，而你可以使用lsof通过名称或进程ID过滤来完成这个任务。下面列出了一些选项：

使用-c查看指定的命令正在使用的文件和网络连接
# lsof -c syslog-ng
COMMAND PID USER FD TYPE DEVICE SIZE NODE NAME
 syslog-ng 7547 root cwd DIR 3,3 4096 2 /
 syslog-ng 7547 root rtd DIR 3,3 4096 2 /
 syslog-ng 7547 root txt REG 3,3 113524 1064970 /usr/sbin/syslog-ng
 -- snipped --

# lsof -c syslog-ng
COMMAND PID USER FD TYPE DEVICE SIZE NODE NAME
 syslog-ng 7547 root cwd DIR 3,3 4096 2 /
 syslog-ng 7547 root rtd DIR 3,3 4096 2 /
 syslog-ng 7547 root txt REG 3,3 113524 1064970 /usr/sbin/syslog-ng
 -- snipped --

使用-p查看指定进程ID已打开的内容
# lsof -p 10075
-- snipped --
 sshd 10068 root mem REG 3,3 34808 850407 /lib/libnss_files-2.4.so
 sshd 10068 root mem REG 3,3 34924 850409 /lib/libnss_nis-2.4.so
 sshd 10068 root mem REG 3,3 26596 850405 /lib/libnss_compat-2.4.so
 sshd 10068 root mem REG 3,3 200152 509940 /usr/lib/libssl.so.0.9.7
 sshd 10068 root mem REG 3,3 46216 510014 /usr/lib/liblber-2.3
 sshd 10068 root mem REG 3,3 59868 850413 /lib/libresolv-2.4.so
 sshd 10068 root mem REG 3,3 1197180 850396 /lib/libc-2.4.so
 sshd 10068 root mem REG 3,3 22168 850398 /lib/libcrypt-2.4.so
 sshd 10068 root mem REG 3,3 72784 850404 /lib/libnsl-2.4.so
 sshd 10068 root mem REG 3,3 70632 850417 /lib/libz.so.1.2.3
 sshd 10068 root mem REG 3,3 9992 850416 /lib/libutil-2.4.so
 -- snipped --

	
# lsof -p 10075
-- snipped --
 sshd 10068 root mem REG 3,3 34808 850407 /lib/libnss_files-2.4.so
 sshd 10068 root mem REG 3,3 34924 850409 /lib/libnss_nis-2.4.so
 sshd 10068 root mem REG 3,3 26596 850405 /lib/libnss_compat-2.4.so
 sshd 10068 root mem REG 3,3 200152 509940 /usr/lib/libssl.so.0.9.7
 sshd 10068 root mem REG 3,3 46216 510014 /usr/lib/liblber-2.3
 sshd 10068 root mem REG 3,3 59868 850413 /lib/libresolv-2.4.so
 sshd 10068 root mem REG 3,3 1197180 850396 /lib/libc-2.4.so
 sshd 10068 root mem REG 3,3 22168 850398 /lib/libcrypt-2.4.so
 sshd 10068 root mem REG 3,3 72784 850404 /lib/libnsl-2.4.so
 sshd 10068 root mem REG 3,3 70632 850417 /lib/libz.so.1.2.3
 sshd 10068 root mem REG 3,3 9992 850416 /lib/libutil-2.4.so
 -- snipped --

-t选项只返回PID
# lsof -t -c Mail
350
	
# lsof -t -c Mail
350

文件和目录

通过查看指定文件或目录，你可以看到系统上所有正与其交互的资源——包括用户、进程等。

显示与指定目录交互的所有一切
# lsof /var/log/messages/
COMMAND PID USER FD TYPE DEVICE SIZE NODE NAME
 syslog-ng 7547 root 4w REG 3,3 217309 834024 /var/log/messages

	
# lsof /var/log/messages/
COMMAND PID USER FD TYPE DEVICE SIZE NODE NAME
 syslog-ng 7547 root 4w REG 3,3 217309 834024 /var/log/messages

显示与指定文件交互的所有一切
# lsof /home/daniel/firewall_whitelist.txt
1
	
# lsof /home/daniel/firewall_whitelist.txt

高级用法

与tcpdump类似，当你开始组合查询时，它就显示了它强大的功能。

显示daniel连接到1.1.1.1所做的一切
# lsof -u daniel -i @1.1.1.1
bkdr 1893 daniel 3u IPv6 3456 TCP 10.10.1.10:1234->1.1.1.1:31337 (ESTABLISHED)

	
# lsof -u daniel -i @1.1.1.1
bkdr 1893 daniel 3u IPv6 3456 TCP 10.10.1.10:1234->1.1.1.1:31337 (ESTABLISHED)

同时使用-t和-c选项以给进程发送 HUP 信号
# kill -HUP `lsof -t -c sshd`

# kill -HUP `lsof -t -c sshd`

lsof +L1显示所有打开的链接数小于1的文件

这通常（当不总是）表示某个攻击者正尝试通过删除文件入口来隐藏文件内容。
# lsof +L1
(hopefully nothing)

	
# lsof +L1
(hopefully nothing)

显示某个端口范围的打开的连接
# lsof -i @fw.google.com:2150=2180

	
# lsof -i @fw.google.com:2150=2180
```

