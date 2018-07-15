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
