# djiango框架

mvc: 软件设计典范（设计模式），核心思想是解耦合，让代码变得更独立，更易与维护 Model（模型）管理数据负责程序在数据库的数据存储的操作，View（视图）处理数据库的数据并显示出来，Controller（控制器）关联模型与视图。

===>mvt


### 安装python 虚拟隔离环境

创建一个干净的：
```
virtualenv --no-site-packages -p 加python版本路径（如果有多个版本） 加虚拟环境文件名称
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


### 生成迁移文件
```
python manage.py makemigrations

```
### 在数据库生成django默认数据表
```
python manage.py migrate
```
- 权限配置表
    - auth_group
    - auth_group_permissions
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




# django 实例

### 创建一个app模型
```
python manage.py startapp app
```
- 在setting中添加app功能名称
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app'
```
### 对象关系映射
将原生数据库查询语句转化成通用的查询
ORM object-relational-mapping

### 生成迁移文件
```
python manage.py makemigrations
```
### 设置urls.py访问路径
```
from django.conf.urls import url
from django.contrib import admin


from app import views


urlpatterns = [
    # 127.0.0.1:8080/admin/
    url(r'^admin/', admin.site.urls),
    # 127.0.0.1:8080/hello/
    url(r'^hello/', views.hello),
    # 127.0.0.1:8080/create_stu/
    url(r'^create_stu/', views.create_stu),
    # 127.0.0.1:8080/sel_stu/
    url(r'^sel_stu/', views.sel_stu),
]
```
### 设置models.py模型数据创建
```
from django.db import models

# Create your models here.


class Student(models.Model):
    # 定义数字符串字段
    s_name = models.CharField(max_length=10,unique=True)
    #定义整型字段
    s_age = models.IntegerField(default=18)
    s_gender = models.BooleanField(default=1)
    #创建时间（添加固定的时间）
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    # 修改时间(每次修改添加最新的时间)
    operate_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        # 定义模型迁移到数据库的表名
        db_table = 'student'
```

### 设置views.py返回视图
```

from django.shortcuts import render
from django.http import HttpResponse
from app.models import Student
# Create your views here.


def hello(request):
    return HttpResponse('你好，千锋')


def create_stu(request):
    # 第一种
    # stu = Student()
    # stu.s_name = '小李'
    # stu.s_age = 20
    # stu.save()
    # 第二种
    # Student.objects.create(s_name='小明')
    Student.objects.create(s_name='小花')
    Student.objects.create(s_name='莉哥')
    Student.objects.create(s_name='大锤')
    Student.objects.create(s_name='小锤')
    Student.objects.create(s_name='温婉')
    Student.objects.create(s_name='张三')
    Student.objects.create(s_name='李四')
    Student.objects.create(s_name='王五')
    Student.objects.create(s_name='张麻子')

    return HttpResponse('创建成功')


def sel_stu(request):
    stus = Student.objects.all()
    print(stus)
    # filter(过滤)拿到学生对象列表，不成立返回空
    # first/last 拿到学生对象
    stus = Student.objects.filter(s_name='小明').first()
    # get 拿到学生对象,拿不到值会报错，只能返回一个值
    stus = Student.objects.get(s_name='小明')
    # 多个查询条件
    stus = Student.objects.filter(s_age=20).filter(s_gender=0)
    stus = Student.objects.filter(s_age=20, s_gender=0)

    # 模糊查询
    # 包含查询
    stus = Student.objects.filter(s_name__contains='锤')
    stu_names = [stu.s_name for stu in stus]
    print(stu_names)
    # 以什么开始查询
    stus = Student.objects.filter(s_name__startswith='小')
    stu_names = [stu.s_name for stu in stus]
    print(stu_names)
    # 以什么结束查询
    stus = Student.objects.filter(s_name__endswith='锤')
    stu_names = [stu.s_name for stu in stus]
    print(stu_names)

    # gt大于，gte等于，lte小于等于
    stus = Student.objects.filter(s_age__gt=18)
    stu_names = [stu.s_name for stu in stus]
    print(stu_names)

    # 排序 order_by
    stus = Student.objects.order_by('id')
    stu_names = [stu.s_name for stu in stus]
    print(stu_names)
    # 降序
    stus = Student.objects.order_by('-id')
    stu_names = [stu.s_name for stu in stus]
    print(stu_names)

    # 不包含查询
    stus = Student.objects.exclude(s_age=18)
    stu_names = [stu.s_name for stu in stus]
    print(stu_names)

    # 统计个数 count（）
    stus_count = stus.count()

    # 转换成字典数据
    stus_values = stus.values()

    # id=pk
    stus = Student.objects.filter(id=2)
    stus = Student.objects.filter(pk=2)

    return HttpResponse('查询所有学生成功')
```