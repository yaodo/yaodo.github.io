## git&github.com使用指南

### github.com
1. github.com 注册github.com,建立主目录username.github.io

2. 启用web访问，打开username.github.io可以访问网页版

3. 根据注册用户名生成ssh公钥，添加到github.com settings.

   ssh-keygen -C ‘username@email.com’ -t rsa   
   
   rsa公钥在～/.ssh/中cat id_rsa.pub,复制到github.com.
      
   ssh -T git@github.com可以验证成功与否。
   
### git
1. 安装git  apt-get install git-core

2. 创建本地原始目录 git init mywork

3. 添加github远程源 git add remote origin git@github.com：username/username.github.io.git

4. pull远程源到本地 git pull origin master

5. push本地文件到远程源 git push origin master

6. 如在本地文件夹mywork下修改或删除a.md

   git add a.md   
   
   git  commit -m "txt"   
   
   版本提交更改
   
   git push origin master   
   
   更改后的版本推送到网站
