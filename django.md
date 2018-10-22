# djiango框架

mvc: 软件设计典范（设计模式），核心思想是解耦合，让代码变得更独立，更易与维护 Model（模型）管理数据负责程序在数据库的数据存储的操作，View（视图）处理数据库的数据并显示出来，Controller（控制器）关联模型与视图。
mvt


### 安装python 虚拟隔离环境

创建一个干净的：
```
viryualenv --no-site-packages -p 加python版本路径（如果有多个版本） 加虚拟环境文件名称
```
激活虚拟环境命令 activate（在虚拟环境安装依赖库的时候）

退出虚拟环境命令 deactivate

```
# 显示pip包
pip list
# 版本信息
pip freeze 
# 创建一个名为day01的工程
django-admin startproject day01

```
### 项目文件说明
__init__.py 表示一个开发包所需要的文件，一般不需要修改
manage.py  项目启动文件
settings.py  项目配置文件
urls.py  资源定位文件


### 启动django服务
```
# 默认端口是8000
python manges.py runserver
# 修改端口
python manges.py runserver 127.0.0.1:8080
```
输入http://127.0.0.1:8080 就可以访问本地django服务器了，看到欢饮界面就说明配置成功了，
输入python manges.py runserver 0.0.0.0:8080 命令就能共享服务器让别人连接到你自己的django服务器了。


### setting.py 数据库配置
```

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dj',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': 3306
    }
}
```
### _init_.py 数据库配置
```
import pymysql

pymysql.install_as_MySQLdb()

```
### 在数据库生成django默认数据表
```
python manage.py migtate
```
- 权限配置表
    - attu_group
    - attu_group_permissions
    - auth_permission
    - auth_user
    - auth_user_groups
    - auth_user_user_permissions
- 其他信息
    - django_admin_logo
    - django_content_type
    - django_migrations
    - django_session

### 访问后台
```
http://127.0.0.1:8080/admin
```

### 创建超级管理员
```
python manage.py createsuperuser
 
# 按照提示输入用户名和对应的密码就好了邮箱可以留空，用户名和密码必填
 
# 修改 用户密码可以用：
python manage.py changepassword username

```