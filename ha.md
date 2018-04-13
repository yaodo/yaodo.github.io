## centos6.5+heartbeat-3.0.4

```
  yum install wget
  wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
  rpm -ivH epel-release-6-8.noarch.rpm
  
  yum –y install heartbeat
   20  cd /etc/ha.d
   21  ls
   22  cd  /usr/share/doc/heartbeat-3.0.4/
   23  ls
   配置文档模板copy
   24  cp ha.cf /etc/ha.d
   25  cp haresources /etc/ha.d
   26  cp authkey /etc/ha.d
   27  cp authkeys /etc/ha.d
   28  vi /etc/ha.d/ha.cf
   配置心跳线参数
   29  vi /etc/sysconfig/network-scripts/ifcfg-eth1
   30  cd /etc/sysconfig/network-scripts
   31  ls
   32  ifconfig eth1 up
   配置认证参数
   45  vi authkeys
   配置服务
   46  vi haresources
   47   netstat -nlp | grep httpd
   48  service heartbeat start
   49  chmod -R 600 authkeys 
   50  ls
   51  ll -l
   52  service heartbeat start
   53  cd /etc/
   54  ls
   55  vi hosts
   56  service heartbeat start
   57  service iptables stop

```
## ha.cf
```
[root@nodea ~]# cat /etc/ha.d/ha.cf
#
#	There are lots of options in this file.  All you have to h
#	of nodes listed {"node ...} one of {serial, bcast, mcast, 
#	and a value for "auto_failback".
#
#	ATTENTION: As the configuration file is read line by line,
#		   THE ORDER OF DIRECTIVE MATTERS!
#
#	In particular, make sure that the udpport, serial baud rat
#	etc. are set before the heartbeat media are defined!
#	debug and log file directives go into effect when they
#	are encountered.
#
#	All will be fine if you keep them ordered as in this examp
#
#
#       Note on logging:
#       If all of debugfile, logfile and logfacility are not defin
#       logging is the same as use_logd yes. In other case, they a
#       respectively effective. if detering the logging to syslog,
#       logfacility must be "none".
#
#	File to write debug messages to
#debugfile /var/log/ha-debug
#
#
# 	File to write other messages to
#
logfile	/var/log/ha-log
#
#
#	Facility to use for syslog()/logger 
#
logfacility	local0
#
#
#	A note on specifying "how long" times below...
#
#	The default time unit is seconds
#		10 means ten seconds
#
#	You can also specify them in milliseconds
#		1500ms means 1.5 seconds
#
#
#	keepalive: how long between heartbeats?
#
keepalive 2
#
#	deadtime: how long-to-declare-host-dead?
#
#		If you set this too low you will get the problemat
#		split-brain (or cluster partition) problem.
#		See the FAQ for how to use warntime to tune deadti
#
deadtime 30
#
#	warntime: how long before issuing "late heartbeat" warning
#	See the FAQ for how to use warntime to tune deadtime.
#
warntime 10
#
#
#	Very first dead time (initdead)
#
#	On some machines/OSes, etc. the network takes a while to c
#	and start working right after you've been rebooted.  As a 
#	we have a separate dead time for when things first come up
#	It should be at least twice the normal dead time.
#
initdead 120
#
#
#	What UDP port to use for bcast/ucast communication?
#
udpport	694
#
#	Baud rate for serial ports...
#
#baud	19200
#	
#	serial	serialportname ...
#serial	/dev/ttyS0	# Linux
#serial	/dev/cuaa0	# FreeBSD
#serial /dev/cuad0      # FreeBSD 6.x
#serial	/dev/cua/a	# Solaris
#
#
#	What interfaces to broadcast heartbeats over?
#
#bcast	eth0		# Linux
#bcast	eth1 eth2	# Linux
#bcast	le0		# Solaris
#bcast	le1 le2		# Solaris
#
#	Set up a multicast heartbeat medium
#	mcast [dev] [mcast group] [port] [ttl] [loop]
#
#	[dev]		device to send/rcv heartbeats on
#	[mcast group]	multicast group to join (class D multicast
#			224.0.0.0 - 239.255.255.255)
#	[port]		udp port to sendto/rcvfrom (set this value
#			same value as "udpport" above)
#	[ttl]		the ttl value for outbound heartbeats.  th
#			how far the multicast packet will propagat
#			Must be greater than zero.
#	[loop]		toggles loopback for outbound multicast he
#			if enabled, an outbound packet will be loo
#			received by the interface it was sent on. 
#			Set this value to zero.
#		
#
#mcast eth0 225.0.0.1 694 1 0
#
#	Set up a unicast / udp heartbeat medium
#	ucast [dev] [peer-ip-addr]
#
#	[dev]		device to send/rcv heartbeats on
#	[peer-ip-addr]	IP address of peer to send packets to
#
ucast eth1 192.168.1.3
#
#
#	About boolean values...
#
#	Any of the following case-insensitive values will work for
#		true, on, yes, y, 1
#	Any of the following case-insensitive values will work for
#		false, off, no, n, 0
#
#
#
#	auto_failback:  determines whether a resource will
#	automatically fail back to its "primary" node, or remain
#	on whatever node is serving it until that node fails, or
#	an administrator intervenes.
#
#	The possible values for auto_failback are:
#		on	- enable automatic failbacks
#		off	- disable automatic failbacks
#		legacy	- enable automatic failbacks in systems
#			where all nodes do not yet support
#			the auto_failback option.
#
#	auto_failback "on" and "off" are backwards compatible with
#		"nice_failback on" setting.
#
#	See the FAQ for information on how to convert
#		from "legacy" to "on" without a flash cut.
#		(i.e., using a "rolling upgrade" process)
#
#	The default value for auto_failback is "legacy", which
#	will issue a warning at startup.  So, make sure you put
#	an auto_failback directive in your ha.cf file.
#	(note: auto_failback can be any boolean or "legacy")
#
auto_failback on
#
#
#       Basic STONITH support
#       Using this directive assumes that there is one stonith 
#       device in the cluster.  Parameters to this device are 
#       read from a configuration file. The format of this line is
#
#         stonith <stonith_type> <configfile>
#
#       NOTE: it is up to you to maintain this file on each node i
#       cluster!
#
#stonith baytech /etc/ha.d/conf/stonith.baytech
#
#       STONITH support
#       You can configure multiple stonith devices using this dire
#       The format of the line is:
#         stonith_host <hostfrom> <stonith_type> <params...>
#         <hostfrom> is the machine the stonith device is attached
#              to or * to mean it is accessible from any host. 
#         <stonith_type> is the type of stonith device (a list of
#              supported drives is in /usr/lib/stonith.)
#         <params...> are driver specific parameters.  To see the
#              format for a particular device, run:
#           stonith -l -t <stonith_type> 
#
#
#	Note that if you put your stonith device access informatio
#	here, and you make this file publically readable, you're a
#	for a denial of service attack ;-)
#
#	To get a list of supported stonith devices, run
#		stonith -L
#	For detailed information on which stonith devices are supp
#	and their detailed configuration options, run this command
#		stonith -h
#
#stonith_host *     baytech 10.0.0.3 mylogin mysecretpassword
#stonith_host ken3  rps10 /dev/ttyS1 kathy 0 
#stonith_host kathy rps10 /dev/ttyS1 ken3 0 
#
#	Watchdog is the watchdog timer.  If our own heart doesn't 
#	a minute, then our machine will reboot.
#	NOTE: If you are using the software watchdog, you very lik
#	wish to load the module with the parameter "nowayout=0" or
#	compile it without CONFIG_WATCHDOG_NOWAYOUT set. Otherwise
#	an orderly shutdown of heartbeat will trigger a reboot, wh
#	very likely NOT what you want.
#
watchdog /dev/watchdog
#       
#	Tell what machines are in the cluster
#	node	nodename ...	-- must match uname -n
node	nodea
node	nodeb
#
#	Less common options...
#
#	Treats 10.10.10.254 as a psuedo-cluster-member
#	Used together with ipfail below...
#	note: don't use a cluster node as ping node	
#
ping 192.168.17.1
#
#	Treats 10.10.10.254 and 10.10.10.253 as a psuedo-cluster-m
#       called group1. If either 10.10.10.254 or 10.10.10.253 are 
#       then group1 is up
#	Used together with ipfail below...
#
#ping_group group1 10.10.10.254 10.10.10.253
#
#	HBA ping derective for Fiber Channel
#	Treats fc-card-name as psudo-cluster-member
#	used with ipfail below ...
#
#	You can obtain HBAAPI from http://hbaapi.sourceforge.net. 
#	to get the library specific to your HBA directly from the 
#	To install HBAAPI stuff, all You need to do is to compile 
#	part you obtained from the sourceforge. This will produce 
#	which you need to copy to /usr/lib. You need also copy hba
#	/usr/include.
#	
#	The fc-card-name is the name obtained from the hbaapitest 
#	that is part of the hbaapi package. Running hbaapitest wil
#	a verbose output. One of the first line is similar to:
#		Apapter number 0 is named: qlogic-qla2200-0
#	Here fc-card-name is qlogic-qla2200-0. 	
#
#hbaping fc-card-name
#
#
#	Processes started and stopped with heartbeat.  Restarted u
#		they exit with rc=100
#
#respawn userid /path/name/to/run
#respawn hacluster /usr/lib/heartbeat/ipfail
#
#	Access control for client api
#       	default is no access
#
#apiauth client-name gid=gidlist uid=uidlist
#apiauth ipfail gid=haclient uid=hacluster

###########################
#
#	Unusual options.
#
###########################
#
#	hopfudge maximum hop count minus number of nodes in config
hopfudge 1
#
#	deadping - dead time for ping nodes
deadping 30
#
#	hbgenmethod - Heartbeat generation number creation method
#		Normally these are stored on disk and incremented 
#hbgenmethod time
#
#	realtime - enable/disable realtime execution (high priorit
#		defaults to on
#realtime off
#
#	debug - set debug level
#		defaults to zero
#debug 1
#
#	API Authentication - replaces the fifo-permissions-based s
#
#
#	You can put a uid list and/or a gid list.
#	If you put both, then a process is authorized if it qualif
#	the uid list, or under the gid list.
#
#	The groupname "default" has special meaning.  If it is spe
#	this will be used for authorizing groupless clients, and a
#	not otherwise specified.
#	
#	There is a subtle exception to this.  "default" will never
#	following cases (actual default auth directives noted in b
#		  ipfail 	(uid=HA_CCMUSER)
#		  ccm 	 	(uid=HA_CCMUSER)
#		  ping		(gid=HA_APIGROUP)
#		  cl_status	(gid=HA_APIGROUP)
#
#	This is done to avoid creating a gaping security hole and 
#	likely desired configuration.
#
#apiauth ipfail uid=hacluster
#apiauth ccm uid=hacluster
#apiauth cms uid=hacluster
#apiauth ping gid=haclient uid=alanr,root
#apiauth default gid=haclient

# 	message format in the wire, it can be classic or netstring
#	default: classic
#msgfmt  classic/netstring

#	Do we use logging daemon?
#	If logging daemon is used, logfile/debugfile/logfacility i
#	are not meaningful any longer. You should check the config
#	daemon (the default is /etc/logd.cf)
#	more infomartion can be fould in the man page.
#	Setting use_logd to "yes" is recommended
#	
# use_logd yes/no
#
#	the interval we  reconnect to logging daemon if the previo
#	default: 60 seconds
#conn_logd_time 60
#
#
#	Configure compression module
#	It could be zlib or bz2, depending on whether u have the c
#	library	in the system.
#compression	bz2
#
#	Confiugre compression threshold
#	This value determines the threshold to compress a message,
#	e.g. if the threshold is 1, then any message with size gre
#	will be compressed, the default is 2 (KB)
#compression_threshold 2
```
## haresource
```
  [root@nodea ha.d]# vi haresources 
#
#
# <VERY IMPORTANT NOTE>
#       up on the preferred nodes - any time they're up.
#       the hb_standby {foreign,local} command.
#       won't work right.
#       taken over after going down.
#
#       /etc/ha.d
#       to line by ending the lines with backslashes ("\").
#
#
#       Multiple arguments are separated by the :: delimeter
#       implied.
#
#
#       up here -- we key off of it.
#
#
#
#
#       this as IPaddr::135.9.8.7/24 .
#       was 135.9.8.210, then you would specify that this way:
#               IPaddr::135.9.8.7/24/135.9.8.210
#
#
#       interface:
#       use to get at highly available services.
#       a single service address,
#       system.
#
#       be a short name or a FQDN.
#
#
#
#just.linux-ha.org      135.9.216.110 http
#
#       the IP address...
#
#
#       explicitly defined.
#
#just.linux-ha.org      135.9.216.3/28/eth0/135.9.216.12 httpd
#
nodea 192.168.17.200/24/eth0 httpd

#----------------------------------------------------------------
---
#
#       An example where a shared filesystem is to be used.
#       Note that multiple aguments are passed to this script usi
ng
#       the delimiter '::' to separate each argument.
#
#node1  10.0.0.170 Filesystem::/dev/sda1::/data1::ext2
#
#       Regarding the node-names in this file:
#
#       They must match the names of the nodes listed in ha.cf, w
hich in turn
#       must match the `uname -n` of some node in the cluster.  S
o they aren't
#       virtual in any sense of the word.
#
~                                                                
#       explicitly defined.
#
#just.linux-ha.org      135.9.216.3/28/eth0/135.9.216.12 httpd
#
nodea 192.168.17.200/24/eth0 httpd

#-----------------------------------------------------------------
#
#       An example where a shared filesystem is to be used.
#       Note that multiple aguments are passed to this script usin
#       the delimiter '::' to separate each argument.
#
#node1  10.0.0.170 Filesystem::/dev/sda1::/data1::ext2
#
#       Regarding the node-names in this file:
#
#       They must match the names of the nodes listed in ha.cf, wh
#       must match the `uname -n` of some node in the cluster.  So
#       virtual in any sense of the word.
#
~                                                                 
~                                                                 
~                                                                 
~                                                                 
~                                                                 
#
nodea 192.168.17.200/24/eth0 httpd

#----------------------------------------------------------------
---
#
#       An example where a shared filesystem is to be used.
#       Note that multiple aguments are passed to this script usi
ng
#       the delimiter '::' to separate each argument.
#
#node1  10.0.0.170 Filesystem::/dev/sda1::/data1::ext2
#
#       Regarding the node-names in this file:
#
#       They must match the names of the nodes listed in ha.cf, w
hich in turn
#       must match the `uname -n` of some node in the cluster.  S
o they aren't
#       virtual in any sense of the word.
#
~                                                                
~                                                                
~                                                                
~                                                                
~                                                                
nodea 192.168.17.200/24/eth0 httpd

#----------------------------------------------------------------
---
#
#       An example where a shared filesystem is to be used.
#       Note that multiple aguments are passed to this script usi
ng
#       the delimiter '::' to separate each argument.
#
#node1  10.0.0.170 Filesystem::/dev/sda1::/data1::ext2
#
#       Regarding the node-names in this file:
#
#       They must match the names of the nodes listed in ha.cf, w
hich in turn
#       must match the `uname -n` of some node in the cluster.  S
o they aren't
#       virtual in any sense of the word.
#
```
