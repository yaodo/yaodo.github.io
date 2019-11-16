'''bash
#
yum -y install gcc pam-devel zlib-devel openssl-devel

cp  /usr/lib64/libcrypto.so.10  /usr/lib64/libcrypto.so.10.old
cp  /usr/lib64/libssl.so.10  /usr/lib64/libssl.so.10.old
mv  /usr/lib64/libcrypto.so.10.old  /usr/lib64/libcrypto.so.10
mv  /usr/lib64/libssl.so.10.old  /usr/lib64/libssl.so.10

wget https://www.openssl.org/source/openssl-1.0.2t.tar.gz
tar -zxf openssl-1.0.2t.tar.gz 
cd openssl-1.0.2t
./config  --prefix=/usr --openssldir=/etc/ssl --shared 
make && make install
ssh -V
openssl version
ldconfig -v

wget https://openbsd.hk/pub/OpenBSD/OpenSSH/portable/openssh-8.1p1.tar.gz
tar -zxf openssh-8.1p1.tar.gz 
./configure --prefix=/usr --sysconfdir=/etc/ssh --with-pam --with-zlib --with-ssl-dir=/usr --with-md5-passwords --mandir=/usr/share/man
make && make install
ssh -V
vi /etc/ssh/sshd_config
sed -i '/^#PermitRootLogin/s/#PermitRootLogin yes/PermitRootLogin yes/' /etc/ssh/sshd_config
sed -i '/^#UseDNS yes/s/#UseDNS yes/UseDNS no/' /etc/ssh/sshd_config
sed -i '/^GSSAPICleanupCredentials/s/GSSAPICleanupCredentials yes/#GSSAPICleanupCredentials yes/' /etc/ssh/sshd_config
sed -i '/^GSSAPIAuthentication/s/GSSAPIAuthentication yes/#GSSAPIAuthentication yes/' /etc/ssh/sshd_config

cat /etc/init.d/sshd
service sshd restart

history
HISTTIMEFORMAT=''
history
history | sed 's/^[ ]*[0-9]\+[ ]*//'


'''
