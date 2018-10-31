# һ.Django Ȩ�޲���

### ��Զ�����˼�룺�û���Ȩ�ޱ���ɫ��
    - �����û����ɫ
    - �������Ȩ��
    - �����û�
    - ���û������ɫ
    - ���û����Ȩ�ޣ����������
- �û����Ȩ�ޱ����ManyToManyFiled() �����ʣ�user_permissions
- �û����������ManyToManyFiled() �����ʣ�groups
- ����Ȩ�ޱ����ManyToManyFiled() �����ʣ�permissions

### �����ɾ����add(), remove()

### ��ѯ����
```

# ͨ���û���ѯ��ӦȨ��
# ��ѯ�û�����Ȩ��
user.user_permissions.all()
# ��ѯ�����±�Ϊ0���û�����Ȩ��
user.groups.all()[0].permissions.all()


#Django �Դ���ѯ����
user.get_group_permissions()
user.get_all_permissions()
```
### Ȩ����֤
```
# ��ȡ�û���Ϊxxx��Ȩ���б�
user.user_permissions.filter(codename='xxx')
user.groups.all()[0].permissions.filter(codename='xxx')


# Django �Դ�Ȩ����֤
user.has_perm('app����.xxx')
```
### Ȩ����֤װ�������
```
# ���װ����ģʽ
def a(function):
    def b(request):
        return function(request)
    return b


# Django �Դ�װ��������
@permission_required('app����.xxx')
```
# ��.�������ʵ��

### app��views.py�д������£�
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
        # �����û�
        user = MyUser.objects.create_user(username='coco',password='123456',)
        # ָ���û�������Ȩ��
        permissions = Permission.objects.filter(codename__in=['add_my_user', 'all_my_user']).all()
        for permission in permissions:
            # ��Զ����
            user.user_permissions.add(permission)
            # ɾ�������ĳ��Ȩ��
            # user.user_permissions.remove(permission)

        return HttpResponse('�����û��ɹ�')


# ���coco�û�װ����ʵ�֣�ֻ��coco�û��в鿴�û��б�Ȩ�ޣ����ܷ���index����
@coco_show
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


# �����û��鲢������Ӷ�Ӧ��Ȩ��
def add_group_permission(request):
    if request.method == 'GET':
	# ����һ����Ϊ������顯���û���
        group = Group.objects.create(name='�����')
        # ��Ȩ���б��л�ȡ��Ҫ��Ȩ���б�
        permissions = Permission.objects.filter(codename__in=['add_my_user',
                                                              'change_my_user_username',
                                                              'change_my_user_password',
                                                              'all_my_user',
                                                            ])
        for permission in permissions:
            # ����������Ȩ������ȡ����Ȩ��
            group.permissions.add(permission)

        return HttpResponse('������Ȩ�޳ɹ�')


# ���û���ӵ��飬�̳����Ȩ��
def add_user_group(request):
    if request.method == 'GET':
        # ��coco�û�������
	# ��ȡcoco�û�����
        user = MyUser.objects.get(username='coco')
	# ��ȡ��������
        group = Group.objects.get(name='�����')
        # ��coco�û�����������
        user.groups.add(group)

        return HttpResponse('������ɹ�')


# �鿴�û���Ȩ��
def show_user_permission(request):
    if request.method == 'GET':
	# ��ȡcoco�û����󲢷���ǰ��ҳ�棬������html�в�ѯ�û���Ȩ�ޣ��������ο�permissions.html
        user = MyUser.objects.get(username='coco')
        return render(request, 'permissions.html', {'user': user})


# django�Դ���¼����֤
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


# django�Դ�Ȩ�޲�ѯ
def my_index(request):
    if request.method == 'GET':
        # ��ȡ��ǰ��¼�û�
        user = request.user
        # ��ȡ��ǰ�û����Ȩ��
        user.get_group_permissions()
        # ��ȡ��ǰ�û����е�Ȩ��
        user.get_all_permissions()
        # �ж��Ƿ���ĳ��Ȩ��
        user.has_perm('user.all_my_user')

        return render(request, 'my_index.html')


# django�Դ�Ȩ����֤װ����
@permission_required('user.all_my_user')
def new_index(request):
    if request.method == 'GET':
        return render(request, 'new_index.html')
```
### app��models.py�д�������:
```
from django.contrib.auth.models import AbstractUser, User, Permission, Group
from django.db import models

# Create your models here.
class MyUser(AbstractUser):
    class Meta:
        #djangoĬ�ϸ�ÿ��ģ�ͳ�ʼ������Ȩ��
        #Ĭ����change,delete,addȨ��
        permissions = (
            ('add_my_user', '�����û�Ȩ��'),
            ('change_my_user_username', '�޸��û���Ȩ��'),
            ('change_my_user_password', '�޸��û�����Ȩ��'),
            ('all_my_user', '�鿴�û�Ȩ��')
        )
```
### app��urls.py�������£�
```

from django.conf.urls import url

from user import views

# ����·��չʾ 
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
### setting�������ã�������������
```
# �滻����userģ������
AUTH_USER_MODEL = 'user.MyUser'


# Ȩ����֤��ͨ����תҳ������
LOGIN_URL = '/user/login'
```
### app��forms.py��֤login�Ĵ���
```
from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=10, min_length=2, required=True,
                               error_messages={
                                   'required': '����',
                                   'max_length': '���ܳ���10�ַ�',
                                   'min_length': '��������2�ַ�'
                               })
    password = forms.CharField(max_length=10, required=True,
                               error_messages={
                                   'required': '����',
                                   'max_length': '���ܳ���10�ַ�'
                               })
```
### permissions.html��ѯ����չʾ��д���е㲻ͬ��Ҫע�⣬����html�Ͳ���չʾ��
```
{% extends 'base.html' %}
{# ͨ���û���ѯ�飬���ѯȨ�� #}
{% block content %}
    <h1>��ʾ�û�Ȩ��ҳ��</h1>
    �û�����{{ user }}
{% for permission in user.groups.all.0.permissions.all %}
    <ul>{{ permission.codename }}</ul>
{% endfor %}
{% endblock %}
```


