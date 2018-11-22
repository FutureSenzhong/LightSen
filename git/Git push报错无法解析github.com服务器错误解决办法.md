## 关于错误:ssh: Could not resolve hostname github.com: Name or service not known.fatal: Could not read from remote repository.


在我配置完公钥后想要进行远端Github上clone时出现了错误。经过网上查询发现在配置git时要验证是否成功。要在git bash 下输出$ ssh -T git@github.com如果是第一次的会提示是否continue，输入yes就会看到：You’ve successfully authenticated, but GitHub does not provide shell access 。这就表示已成功连上github。

如果有朋友出现了以下三条错误可以按我下面的操作试试。

### 错误1

clone
ssh:无法解析主机名github.com：名称或服务不知道
无法读取远程存储库。
请确保您有正确的访问权限
和存储库存在。(错误代码)

### 错误2

在git bash 下输出$ ssh -T git@github.com也显示错误。（表示git连接github失败）

### 错误3

在git bash 下打出ping github.com 不显示ip。

原因有可能是本地DNS无法解析导致的。造成该问题的因素可能有多种，安全防护类软件、病毒、优化或清理等导致本地DNS解析文件被清除或更改，DNS缓存问题，Winsock目录问题等。

## 解决办法

打开hosts 该文件在C:\Windows\System32\drivers\etc路径下
然后用记事本打开，在最后一行加：

    192.30.253.113    github.com
    192.30.252.131 github.com
    185.31.16.185 github.global.ssl.fastly.net
    74.125.237.1 dl-ssl.google.com
    173.194.127.200 groups.google.com
    192.30.252.131 github.com
    185.31.16.185 github.global.ssl.fastly.net
    74.125.128.95 ajax.googleapis.com

进入cmd (开始->搜索文件和程序->打入cmd->enter)
输入：ipconfig /flushdns 释放DNS缓存。
输入：netsh winsock reset 重置Winsock目录。
会有提示：必须重启计算机才能完成重置。
