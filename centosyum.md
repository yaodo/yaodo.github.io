first,make a centos yum to install the centos 6.5 ，7.0    and so on
## 1. install vsftpd as a ftp server
```
  yum install vsftpd
  mkdir /var/ftp/pub/1
  mkdir /var/ftp/pub/2
```
## 2. copy dvd to ftp folder
```
  mount -o loop /mnt/cdrom 1.iso
  cp -rf /mnt/cdrom /var/ftp/pub/1
  umount /mnt/cdrom
  mount -o loop /mnt/cdrom 2.iso
  cp -rf /mnt/cdrom /var/ftp/pub/2
```
## 3.check iptables
```
  service iptables status
  service iptables stop
  service vsftpd status
  service vsftpd start
```   
## 4.add yum list
```
  mkdir /etc/yum.repos.d/back -p
  mv /etc/yum.repos.d/Cent* /etc/yum.repos.d/back
  echo "[Ftp]
  name=aether
  baseurl=ftp://a.b.c.d/pub/1
  ftp://a.b.c.d/pub/2
  gpgcheck=0" >/etc/yum.repos.d/instal.repo
```
## 5.OK
  yum clean all
  yum list
