
```
ifconfig eth0 |awk '/inet/{print $2}'|sed -e s/addr://
```
ifconfig
```
ifconfig eth0 |grep -o "inet addr:[^ ]*" Igrep -o "[0-9.]*"
```

crontab -e
crontab -l
* * * * * ntpdate 1.1.1.1;&& hwclock -w;

