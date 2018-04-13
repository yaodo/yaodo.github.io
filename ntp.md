## debian9.4 ntp同步
1. NTP时间同步方式选择

   NTP同步方式在linux下一般两种：使用ntpdate命令直接同步和使用NTPD服务平滑同步。有什么区别?
   现有一台设备，系统时间是 13:00 , 真实的当前时间是: 12:30  。如果我们使用ntpdate同步（ntpdate -u 目标NTP服务器IP），
   操作系统的时间立即更新为12:30,假如，我们的系统有一个定时应用，是在每天12:40运行，那么实际今天这个的任务已经运行过了
   （当前时间是13:00嘛），现在被ntpdate修改为12:30，那么意味作10分钟后，又会执行一次任务，这就糟糕了，这个任务只能执行一次的嘛！！
   ntpdate时间同步的隐患，当然这个例子有些极端，但的确是有风险的。所以解决该问题的办法就是时间平滑更改，不会让一个时间点在一天内经历两次.
   一般先手动同步一次，开启ntpdate定时任务。
   
2. ntp server端
  与上级时间服务器同步，作为下级时间客户端的服务器。

```
# /etc/ntp.conf, configuration for ntpd; see ntp.conf(5) for help
driftfile /var/lib/ntp/ntp.drift

# Enable this if you want statistics to be logged.
#statsdir /var/log/ntpstats/

statistics loopstats peerstats clockstats
filegen loopstats file loopstats type day enable
filegen peerstats file peerstats type day enable
filegen clockstats file clockstats type day enable

# You do need to talk to an NTP server or two (or three).
#server ntp.your-provider.example

# pool.ntp.org maps to about 1000 low-stratum NTP servers.  Your server will
# pick a different set every time it starts up.  Please consider joining the
# pool: <http://www.pool.ntp.org/join.html>
#pool 0.debian.pool.ntp.org iburst
#pool 1.debian.pool.ntp.org iburst
#pool 2.debian.pool.ntp.org iburst
#pool 3.debian.pool.ntp.org iburst
server 210.72.145.44 prefer
server 202.112.10.36

# Access control configuration; see /usr/share/doc/ntp-doc/html/accopt.html for
# details.  The web page <http://support.ntp.org/bin/view/Support/AccessRestrictions>
# might also be helpful.
#
# Note that "restrict" applies to both servers and clients, so a configuration
# that might be intended to block requests from certain clients could also end
# up blocking replies from your own upstream servers.

# By default, exchange time with everybody, but don't allow configuration.
restrict -4 default kod notrap nomodify nopeer noquery limited
restrict -6 default kod notrap nomodify nopeer noquery limited

# Local users may interrogate the ntp server more closely.
restrict 127.0.0.1
restrict ::1

# Needed for adding pool entries
restrict source notrap nomodify noquery

# Clients from this (example!) subnet have unlimited access, but only if
# cryptographically authenticated.
#restrict 192.168.123.0 mask 255.255.255.0 notrust
restrict 192.168.17.0 mask 255.255.255.0 nomodify notrap

# If you want to provide time to your local subnet, change the next line.
# (Again, the address is an example only.)
#broadcast 192.168.123.255

# If you want to listen to time broadcasts on your local subnet, de-comment the
# next lines.  Please do this only if you trust everybody on the network!
#disable auth
#broadcastclient
server 127.127.1.0
fudge 127.127.1.0 stratum 10

```

3. ntp client端
  与指定的服务器同步。
