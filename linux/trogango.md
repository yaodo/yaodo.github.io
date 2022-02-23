
1、Trojan-GFW 是什么？
Trojan-GFW，简称Trojan，是一把通往自由互联网世界的万能钥匙。Trojan原版不使用 Websocket 混淆，Trojan-GFW 仅支持Websocket，但是均不支持 Cloudflare CDN 流量中转。

Trojan-GFW项目地址：https://github.com/trojan-gfw/trojan

2、Trojan-Go 是什么？相比于 Trojan-GFW 有哪些优点？
Trojan-Go 是使用Go语言实现的完整Trojan代理，与Trojan协议以及Trojan-GFW版本的配置文件格式完全兼容，而且更加安全、高效、轻巧、易用。Trojan-Go 支持使用多路复用提升并发性能，使用路由模块实现国内直连；支持CDN流量中转(基于WebSocket over TLS/SSL)；支持基于ACME协议从Let’s Encrypt自动申请和更新HTTPS证书，只需提供域名和邮箱；直接运行解压得到的执行文件即可，无其他组件依赖。

Trojan-Go项目官网：https://github.com/p4gefau1t/trojan-go

Trojan-Go支持并且兼容Trojan-GFW的绝大多数功能，包括但不限于：

TLS/SSL隧道传输
透明代理 (NAT模式，iptables设置参见这里)
UDP代理
对抗GFW被动/主动检测的机制
MySQL数据库支持
流量统计，用户流量配额限制
从数据库中的用户列表进行认证
TCP Keep Alive，TCP Fast Open，端口复用等TCP选项
同时，Trojan-Go还扩展了更多高效易用的功能特性：

简易模式，快速部署使用
Socks5/HTTP代理自动适配
多平台和多操作系统支持，无特殊依赖
多路复用，降低延迟，提升并发性能
自定义路由模块，可实现国内直连/广告屏蔽等功能
Websocket传输支持，用于实现CDN流量中转(基于WebSocket over TLS/SSL)和对抗GFW中间人攻击
自动化HTTPS证书申请，从Let’s Encrypt自动申请和更新HTTPS证书
TLS指纹伪造，绕过GFW针对TLS Client Hello的特征识别
基于gRPC的API支持，支持动态用户管理和流量速度限制
服务端支持处理Trojan协议明文（TCP明文传输），以适应前置nginx等服务器的场景
简单地说，那就是 trojan-gfw 和 trojan-go 均支持Trojan协议；trojan-go 兼容 trojan-gfw 配置文件，服务端可以兼容所有Trojan-GFW的客户端，如Trajan-Qt5、Igniter、ShadowRocket等；trojan-go 支持多路复用提高并发性能，而且还支持 CDN 流量中转。trojan-go 比 trojan-gfw 使用更简单，而且功能更强大，未来可期。从众多实际测试来看，Trojan-Go是目前表现最好的Trojan翻墙上网协议，比VLESS协议还要出色不少。

3、Trojan-Go 一键搭建教程
为了更加简单方便地搭建 Trojan-Go 服务器，我们使用傻瓜式Trojan-Go一键安装脚本，是 “Trojan-Go+Websocket+Tls+CDN”2合1一键搭建脚本，只需要按照脚本提示信息一步步操作即可。


准备工作：至少一个域名、一台非大陆地区的VPS，并已经将域名成功解析到VPS的IP地址。注册域名推荐您使用NameSilo 或 Namecheap，购买VPS推荐使用Vultr、Hostwinds 或 搬瓦工(BandwagonHOST，Trojan-Go 一键搭建脚本的整个安装过程大约需要30分钟以上。另外，在 Trojan-Go 服务器搭建完成之前，请不要为域名加上 Cloudflare CDN 防护（也就是部署完成之前小云朵必须是灰色的），否则会造成安装部署失败。

Trojan-Go 一键脚本支持的系统环境：

Debian 9、10
Ubuntu 16.04 、18.04、19.10
Centos 7、8

（1）安装 curl
yum -y install curl #CentOS
apt -y install curl #Debian/Ubuntu
（2）执行 Trojan-Go 一键安装脚本
bash -c "$(curl -fsSL https://raw.githubusercontent.com/JeannieStudio/all_install/master/trojan-go_install.sh)"
（3）安装BBR加速
wget -N --no-check-certificate "https://raw.githubusercontent.com/chiakge/Linux-NetSpeed/master/tcp.sh"
chmod +x tcp.sh
./tcp.sh
安装成功后，有如下提示信息，如图所示：


（4）脚本管理命令
/etc/trojan_mgr.sh

如果你要开启 “Websocket+TLS+CDN”，可执行以上管理命令，结果如下图所示：


我们选择“6”即可，另外，我们还可以修改密码，关闭或重启Trojan-Go，以及关闭或重启nginx，更新HTTPS证书等。

至此，Trojan-Go 服务器就搭建完成了！你现在就可以配合Trojan-Go客户端进行科学上网了。

注意事项：如果你的 Trojan-Go 开启了 CDN，那么暂时是不支持手机端客户端使用的，只能在Windows、MacOS和Linux上面使用。

