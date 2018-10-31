# 一.Django 权限操作

### 多对多表设计思想：用户表，权限表，角色表
    - 创建用户组角色
    - 给组添加权限
    - 创建用户
    - 给用户分配角色
    - 给用户添加权限（特殊情况）
- 用户表和权限表关联ManyToManyFiled() 关联词：user_permissions
- 用户表和组表关联ManyToManyFiled() 关联词：groups
- 组表和权限表关联ManyToManyFiled() 关联词：permissions

### 添加与删除：add(), remove()

### 查询功能
```

# 通过用户查询对应权限
# 查询用户所有权限
user.user_permissions.all()
# 查询组中下标为0的用户所有权限
user.groups.all()[0].permissions.all()


#Django 自带查询方法
user.get_group_permissions()
user.get_all_permissions()
```
### 权限验证
```
# 获取用户名为xxx的权限列表
user.user_permissions.filter(codename='xxx')
user.groups.all()[0].permissions.filter(codename='xxx')


# Django 自带权限验证
user.has_perm('app名称.xxx')
```
### 权限验证装饰器编程
```
# 设计装饰器模式
def a(function):
    def b(request):
        return function(request)
    return b


# Django 自带装饰器函数
@permission_required('app名称.xxx')
```
# 二.具体代码实现

### app中views.py中代码如下：
```
from django.contrib import auth
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Permission, Group
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from user.forms import UserLoginForm
from user.function import coco_show
from user.models import MyUser


# Create your views here.
def add_user_permission(request):
    if request.method == 'GET':
        # 创建用户
        user = MyUser.objects.create_user(username='coco',password='123456',)
        # 指定用户并分配权限
        permissions = Permission.objects.filter(codename__in=['add_my_user', 'all_my_user']).all()
        for permission in permissions:
            # 多对多添加
            user.user_permissions.add(permission)
            # 删除分配的某个权限
            # user.user_permissions.remove(permission)

        return HttpResponse('创建用户成功')


# 设计coco用户装饰器实现，只有coco用户有查看用户列表权限，才能访问index函数
@coco_show
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


# 创建用户组并给组添加对应的权限
def add_group_permission(request):
    if request.method == 'GET':
	# 创建一个名为‘审查组’的用户组
        group = Group.objects.create(name='审查组')
        # 在权限列表中获取需要的权限列表
        permissions = Permission.objects.filter(codename__in=['add_my_user',
                                                              'change_my_user_username',
                                                              'change_my_user_password',
                                                              'all_my_user',
                                                            ])
        for permission in permissions:
            # 给审查组添加权限上面取到的权限
            group.permissions.add(permission)

        return HttpResponse('创建组权限成功')


# 将用户添加到组，继承组的权限
def add_user_group(request):
    if request.method == 'GET':
        # 给coco用户分配组
	# 获取coco用户对象
        user = MyUser.objects.get(username='coco')
	# 获取审查组对象
        group = Group.objects.get(name='审查组')
        # 将coco用户分配给审查组
        user.groups.add(group)

        return HttpResponse('分配组成功')


# 查看用户的权限
def show_user_permission(request):
    if request.method == 'GET':
	# 获取coco用户对象并返给前端页面，可以在html中查询用户的权限，具体代码参考permissions.html
        user = MyUser.objects.get(username='coco')
        return render(request, 'permissions.html', {'user': user})


# django自带登录表单验证
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        data = request.POST
        form = UserLoginForm(data)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data.get('username'),
                                     password=form.cleaned_data.get('password'))
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('user:my_index'))
            else:
                return render(request, 'login.html')
        else:
            return render(request, 'login.html', {'errors': form.errors})


# django自带权限查询
def my_index(request):
    if request.method == 'GET':
        # 获取当前登录用户
        user = request.user
        # 获取当前用户组的权限
        user.get_group_permissions()
        # 获取当前用户所有的权限
        user.get_all_permissions()
        # 判断是否有某个权限
        user.has_perm('user.all_my_user')

        return render(request, 'my_index.html')


# django自带权限验证装饰器
@permission_required('user.all_my_user')
def new_index(request):
    if request.method == 'GET':
        return render(request, 'new_index.html')
```
### app中models.py中代码如下:
```
from django.contrib.auth.models import AbstractUser, User, Permission, Group
from django.db import models

# Create your models here.
class MyUser(AbstractUser):
    class Meta:
        #django默认给每个模型初始化三个权限
        #默认是change,delete,add权限
        permissions = (
            ('add_my_user', '新增用户权限'),
            ('change_my_user_username', '修改用户名权限'),
            ('change_my_user_password', '修改用户密码权限'),
            ('all_my_user', '查看用户权限')
        )
```
### app中urls.py代码如下：
```

from django.conf.urls import url

from user import views

# 访问路由展示 
urlpatterns = [
    url(r'^add_user_permission/', views.add_user_permission, name='add_user_permission'),
    url(r'^index/', views.index, name='index'),
    url(r'^add_group_permission/', views.add_group_permission, name='add_group_permission'),
    url(r'^add_user_group/', views.add_user_group, name='add_user_group'),
    url(r'^show_user_permission/', views.show_user_permission, name='show_user_permission'),
    url(r'^login/', views.login, name='login'),
    url(r'^my_index/', views.my_index, name='my_index'),
    url(r'^new_index/', views.new_index, name='new_index'),
]
```
### setting部分配置，其他配置依旧
```
# 替换本地user模型配置
AUTH_USER_MODEL = 'user.MyUser'


# 权限验证不通过跳转页面设置
LOGIN_URL = '/user/login'
```
### app中forms.py验证login的代码
```
from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=10, min_length=2, required=True,
                               error_messages={
                                   'required': '必填',
                                   'max_length': '不能超过10字符',
                                   'min_length': '不能少于2字符'
                               })
    password = forms.CharField(max_length=10, required=True,
                               error_messages={
                                   'required': '必填',
                                   'max_length': '不能超过10字符'
                               })
```
### permissions.html查询代码展示，写法有点不同需要注意，其他html就不做展示了
```
{% extends 'base.html' %}
{# 通过用户查询组，组查询权限 #}
{% block content %}
    <h1>显示用户权限页面</h1>
    用户名：{{ user }}
{% for permission in user.groups.all.0.permissions.all %}
    <ul>{{ permission.codename }}</ul>
{% endfor %}
{% endblock %}
```


