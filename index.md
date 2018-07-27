## Cloud Note,Hello!
github is simple&clean,to save something useful.just like linux,router&switch.

Bigdata Cloud

1. [kubernetes conjure-up](conjure-up.html)
2. [openstack](openstack.html)
3. [hadoop](hadoop.html)
4. [ceph](ceph.html)
 
SystemTroubleshooting

1. [tcpdump](tcpdump.html)
2. [nettools](nettools.html)
3. [wiresharks](wiresharks.html)

Linux servers System centos6&7

1. [shell](shell.html)
2. [yum vsftpd](centosyum.html)
3. [ntp](ntp.html)
4. [iptables](iptables.html)  [iptables1](iptables1.html)
5. [centos7firewalld](firewalld.html)
6. [binddns](dns.html)

HA webserver Database Balance

1. [mysql Master&Slave](mysql.html)
2. [nginx](nginx.html)
3. [Tomacat](tomcat.html)
4. [oracle11g2](oracle11g2.html)
5. [keepalived](keepalived.html)
6. [heartbeat&keepalived](ha.html)

Programming language

1. [JavaEclipse](java.html)

Operation remote control

1. [ssh](ssh.html)
2. [cobbler](cobbler.html)
3. [fabric](fabric.html)
4. [puppet](puppet.html)
5. [ansible](ansible.html)

Network Monitor

1. [nagios](nagios.html)
2. [zabbix](zabbix.html)
3. [elk](elk.html)

[windows](windows.html)  
[vmware](vmware.html)

Hardware

1. [uefi&logacy](uefi.html)
2. [ipmi](ipmi.html)

Network Router&Switch

1. [cisco](cisco1.html)
2. [Jupiter](jupiter.html)
3. [HUAWEI](huawei.html)
4. [H3C](h3c1.html)
5. [GNS3](gns.html)
6. [asa9k](asa9K.html)

vpn

1. [shadowsocks](ss.html)
2. [openvpn](openvpn.html)

debian 

1. [debian install & config](debian1.html)
2. [use git & github](gituse.html)

[Link](url) and 
![Image](./images/debian.png)

Commands
```
[root@host1 ~]# netstat -antlp
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address               Foreign Address             State       PID/Program name   
tcp        0      0 0.0.0.0:111                 0.0.0.0:*                   LISTEN      1336/rpcbind        
tcp        0      0 127.0.0.1:8307              0.0.0.0:*                   LISTEN      1983/vmware-hostd   
tcp        0      0 0.0.0.0:21                  0.0.0.0:*                   LISTEN      1994/vsftpd         
tcp        0      0 0.0.0.0:22                  0.0.0.0:*                   LISTEN      1819/sshd           
```

```
[root@host1 ~]# ethtool eth0
Settings for eth0:
	Supported ports: [ TP ]
	Supported link modes:   10baseT/Half 10baseT/Full 
	                        100baseT/Half 100baseT/Full 
	                        1000baseT/Full 
	Supported pause frame use: No
	Supports auto-negotiation: Yes
	Advertised link modes:  10baseT/Half 10baseT/Full 
	                        100baseT/Half 100baseT/Full 
	                        1000baseT/Full 
	Advertised pause frame use: No
	Advertised auto-negotiation: Yes
	Speed: 1000Mb/s
	Duplex: Full
	Port: Twisted Pair
	PHYAD: 0
	Transceiver: internal
	Auto-negotiation: on
	MDI-X: Unknown
	Supports Wake-on: d
	Wake-on: d
	Current message level: 0x00000007 (7)
			       drv probe link
	Link detected: yes

```

**Bold** and _Italic_ and `Code` text

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.
### Markdown
Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for
```markdown
Syntax highlighted code block
# Header 1
## Header 2
### Header 3
- Bulleted
- List
1. Numbered
2. List
**Bold** and _Italic_ and `Code` text
```
