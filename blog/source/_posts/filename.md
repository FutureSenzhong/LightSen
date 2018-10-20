---
title: CentOS+Hexo博客搭建
tags: 基于阿里云服务器CentOS系统搭建Hexo博客git自动化部署
grammar_cjkRuby: true
---


## 前言
本文介绍的是如何在CentOS系统上使用Hexo博客框架搭建一个完全属于自己的博客系统。

# 知识储备
### CentOS是什么?
### Hexo是什么?
### Nginx是什么?
### Git是什么?
### Node.js是什么?
## CentOS是什么?
CentOS（Community Enterprise Operating System）是Linux发行版之一，它是来自于Red Hat Enterprise Linux依照开放源代 码规定发布的源代码所编译而成。由于出自同样的源代码，因此有些要求高度稳定性的服务器以CentOS替代商业版的Red Hat Enterprise Linux使用。两者的不同，在于CentOS并不包含封閉源码软件。CentOS 对上游代码的主要修改是为了移除不能自由使用的商标。2014年，CentOS宣布与Red Hat合作，但CentOS将会在新的委员会下继续运作，并不受RHEL的影响。

## Hexo是什么?
Hexo是一个快速、简洁且高效的博客框架。Hexo使用Markdown（或其他渲染引擎）解析文章，在几秒内，即可利用靓丽的主题生成静态网页。Hexo使用Node.js来渲染页面，因此渲染速度极快。只需一条指令即可部署到 GitHub Pages, Heroku 或其他网站。同时，Hexo 拥有强大的插件系统，安装插件可以让 Hexo 支持 Jade, CoffeeScript。

## Nginx是什么?
Nginx是一个 Web服务器，也可以用作反向代理，负载平衡器和 HTTP缓存。该软件由 Igor Sysoev 创建，并于2004年首次公开发布。同名公司成立于2011年，以提供支持。Nginx是一款面向性能设计的HTTP服务器，相较于Apache、lighttpd具有占有内存少，稳定性高等优势。与旧版本（<=2.2）的Apache不同，Nginx不采用每客户机一线程的设计模型，而是充分使用异步逻辑从而削减了上下文调度开销，所以并发服务能力更强。整体采用模块化设计，有丰富的模块库和第三方模块库，配置灵活。 在Linux操作系统下，Nginx使用epoll事件模型，得益于此，Nginx在Linux操作系统下效率相当高。同时Nginx在OpenBSD或FreeBSD操作系统上采用类似于epoll的高效事件模型kqueue。

## Git是什么?
git是用于Linux内核开发的版本控制工具。与CVS、Subversion一类的集中式版本控制工具不同，它采用了分布式版本库的作法，不需要服务器端软件，就可以运作版本控制，使得源代码的发布和交流极其方便。git的速度很快，这对于诸如Linux内核这样的大项目来说自然很重要。git最为出色的是它的合并追踪（merge tracing）能力。实际上内核开发团队决定开始开发和使用git来作为内核开发的版本控制系统的时候，世界上开源社区的反对声音不少，最大的理由是git太艰涩难懂，从git的内部工作机制来说，的确是这样。但是随着开发的深入，git的正常使用都由一些友善的命令稿来执行，使git变得非常好用。现在，越来越多的著名项目采用git来管理项目开发，例如：wine、U-boot等。

## Node.js是什么？
Node.js是一个能够在服务器端运行JavaScript的开放源代码、跨平台JavaScript运行环境。Node.js采用Google开发的V8运行代码，使用事件驱动、非阻塞和异步输入输出模型等技术来提高性能，可优化应用程序的传输量和规模。这些技术通常用于数据密集的事实应用程序。Node.js的出现使JavaScript也能用于服务器端编程。Node.js含有一系列内置模块，使得程序可以脱离Apache HTTP Server或IIS，作为独立服务器运行。

## 总体思路
以下为了统一说法，统一将云主机称为服务端，将本地电脑称为客户端。 
本次搭建博客需要在客户端以及服务端进行一系列配置。先说一下整体的实现思路。总的来说分两大步。 
### 第一步，在客户端进行以下工作： 
* 安装Git服务以及配置Git 
* 安装nodejs 
* 安装Hexo框架

### 第二步，在服务端进行以下工作： 
* 安装Nginx服务 
* 安装Git服务以及nodejs 
* 搭建Git服务器以及配置自动部署

### 软件下载
现在，罗列一下过程所需的软件：
* Git for Windows 密码：ftoc 
* Git for Mac 密码：a5uz 
* Nodejs for Windows 密码：zmh7 
* putty for Windows 密码：k42f

## 客户端配置
### 安装Git以及进行相关配置
1、首先通过前面提供的链接下载Git客户端，然后进行安装。
2、安装完成之后，打开Git Bash进行以下配置.在客户端输入以下代码，生成SSH KEY,用于免密登录服务器，更新服务器git仓库。
```
# 将此处的"youremail"替换成自己服务器 “仓库名@ip”
ssh-keygen -t rsa -C "youremail"
```


  接着继续输入cat ~/.ssh/id_rsa.pub,然后将得到的秘钥先复制一下，待会服务器配置需要用到。 
  ```
  cat ~/.ssh/id_rsa.pub
  ```
 ### 安装Nodejs
  通过前面提供的链接下载Nodejs，然后进行安装。安装完成后，输入node -v以及npm -v查看node以及npm的版本信息。
  ```
  node -v
  npm -v
  ```
  
###  安装Hexo框架
  接下来，就是重头戏：安装Hexo框架了。 
  首先，继续在刚刚打开的Git Bash里面输入以下代码，通过npm进行全局安装hexo 框架。
  
  ```
  npm install -g hexo-cli
  ```
  
  安装完hexo框架，就可以开始初始化hexo了，选择一个目录存放你的博客文件， 然后把Git Bash切换到那个目录。 
  接着，输入hexo init blog进行初始化hexo并创建一个blog文件。
  ```
  hexo init blog
  ```
  
  
  初始化完毕之后，打开博客根目录的package.json文件，在dependencies的配置中，追加一项："hexo-deployer-git": "^0.3.1"，如下图，然后，返回Git Bash,先输入cd blog，在输入npm install进行包的安装。(git的新版本不用安装)
  ```
  vim package.json
  ```
  安装完包之后，接着在Git Bash输入：hexo s，然后在浏览器输入localhost:4000,就可以看到hexo已经搭建成功了.
  ```
  hexo s
  ```
  至此，客户端的配置就告一段落了。接下来开始服务端的配置。
  
 ##  服务端配置 
   首先，进行服务端的系统更新。待更新完系统之后再进行以下操作。(注：putty软件的粘贴快捷键为：“Shift”+“Insert”) 
   输入以下代码，可进行系统更新：
   ```
   yum update -y
   
 ```
 更新完系统，输入以下代码，可查看系统版本：
 
 ```
 cat /etc/centos-release
 
 ```
 
 ### 安装Nginx
安装Nginx分为以下几步。第一，配置Nginx官方源。第二，安装Nginx。第三，配置Nginx配置文件。 

1、配置Nginx官方源 
输入以下代码，新建一个文件以配置Nginx源
```

vi /etc/yum.repos.d/nginx.repo

```
在打开的文件中输入以下代码，输入完毕之后，按 “esc” 键退出编辑模式， 输入 “:wq” 保存退出。
```

[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/mainline/centos/7/$basearch/
gpgcheck=0
enabled=1

```
2、安装Nginx 
输入以下代码进行安装。
```

yum install nginx -y

```
3、启动Nginx并设置开机自启 
输入以下代码:
```
systemctl start nginx
systemctl enable nginx
```
进行到这里，你已经可以把服务器ip复制到浏览器进行访问了~安装成功的话就会出现下面的欢迎界面。 

4、配置Nginx 
接下来，需要修改一下nginx的相关配置，包括设置网站根目录以及配置域名。输入以下代码，打开Nginx的配置文件。(注：此处假定读者已完成了域名备案以及域名解析。)
```
vi /etc/nginx/conf.d/default.conf
```
在server配置中将“/usr/share/nginx/html”改为“/usr/share/nginx/html/blog”。 （若是空文件先执行其他操作）

至此，Nginx的配置就基本完成了。

### 安装Nodejs
输入以下代码进行Nodejs的安装。
```
yum install nodejs

  ```
  
 ### 安装Git以及进行相关配置
1、输入以下代码，进行Git的安装
```

yum install git
  ```
  2、创建git用户以及设置密码 
输入以下代码：
```
#创建用户,用户名为git
adduser git
#设置密码
passwd git
```
3、把git用户添加到sudo用户组中 
输入以下代码sudo vi /etc/sudoers，打开sudoers文件，输入:/root进行搜索，搜索到代码行root ALL=(ALL) ALL,然后在这一行下添加以下代码git ALL=(ALL) ALL。输入完毕之后，按wq!强制保存退出vi。 
```
sudo vi /etc/sudoers
```
4、切换到git用户，添加SSH Key文件并且设置相应的读写与执行权限。 
输入以下代码：
```
# 切换用户
su git
# 创建目录
mkdir ~/.ssh
# 新建文件
vim ~/.ssh/authorized_keys
```

然后把之前在客户端设置的SSH Key,复制到authorized_keys文件中，保存后退出。

接下来设置文件权限，把authorized_keys文件设置成只有属主有读写权限，把ssh目录设置为只有属主有读、写、执行权限。代码如下：
```
chmod 600 ~/.ssh/authorized_keys
chmod 700 ~/.ssh
```
设置完后，返回客户端，打开Git Bash，输入以下代码，测试是否能连接上服务器：
```
# ServerIP为你自己服务器的ip
ssh -v git@ServerIP
```
5、重新回到服务器，在网站根目录新建一个blog文件夹，用于客户端上传文件，并且把该文件授权给git用户。代码如下：
```
# 使用sudo指令，需要输入git用户的密码
sudo mkdir -p /usr/share/nginx/html/blog
sudo chown -R git:git /usr/share/nginx/html/blog
```
在服务器上初始化一个git裸库 
切换到git用户，然后切换到git用户目录，接着初始化裸库，代码如下：
```
su git
cd ~
git init --bare blog.git
````
接着新建一个post-receive文件
```
vim ~/blog.git/hooks/post-receive
```
然后在该文件中输入以下内容：
```
#！/bin/sh
git --work-tree=/usr/share/nginx/html/blog --git-dir=/home/git/blog.git checkout -f
```
保存退出之后，再输入以下代码，赋予该文件可执行权限。
```
chmod +x ~/blog.git/hooks/post-receive
```
7、返回客户端，设置博客根目录下的_config.yml文件。
```
deploy:
    type: git
    repo: git@SERVER:/home/git/blog.git       #此处的SERVER需改为你自己服务器的ip
    branch: master                            #这里填写分支
    message:                                  #提交的信息
```
保存后，在博客根目录打开Git Bash，输入以下命令：
```
hexo clean
hexo g
hexo d
```
部署完毕之后，即可在浏览器输入你的服务器ip进行访问你的博客了。 