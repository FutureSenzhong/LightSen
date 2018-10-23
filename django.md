# djiango���

mvc: �����Ƶ䷶�����ģʽ��������˼���ǽ���ϣ��ô����ø�������������ά�� Model��ģ�ͣ��������ݸ�����������ݿ�����ݴ洢�Ĳ�����View����ͼ���������ݿ�����ݲ���ʾ������Controller��������������ģ������ͼ��

===>mvt


### ��װpython ������뻷��

����һ���ɾ��ģ�
```
virtualenv --no-site-packages -p ��python�汾·��������ж���汾�� �����⻷���ļ�����
```
�������⻷������ activate�������⻷����װ�������ʱ��

�˳����⻷������ deactivate

```
# ��ʾpip��
pip list
# �汾��Ϣ
pip freeze 
# ����һ����Ϊday01�Ĺ���
django-admin startproject day01

```
### ��Ŀ�ļ�˵��
__init__.py ��ʾһ������������Ҫ���ļ���һ�㲻��Ҫ�޸�
manage.py  ��Ŀ�����ļ�
settings.py  ��Ŀ�����ļ�
urls.py  ��Դ��λ�ļ�


### ����django����
```
# Ĭ�϶˿���8000
python manges.py runserver
# �޸Ķ˿�
python manges.py runserver 127.0.0.1:8080
```
����http://127.0.0.1:8080 �Ϳ��Է��ʱ���django�������ˣ��������������˵�����óɹ��ˣ�
����python manges.py runserver 0.0.0.0:8080 ������ܹ���������ñ������ӵ����Լ���django�������ˡ�


### setting.py ���ݿ�����
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
### _init_.py ���ݿ�����
```
import pymysql

pymysql.install_as_MySQLdb()


### ����Ǩ���ļ�
```
python manage.py makemigrations

```
### �����ݿ�����djangoĬ�����ݱ�
```
python manage.py migrate
```
- Ȩ�����ñ�
    - auth_group
    - auth_group_permissions
    - auth_permission
    - auth_user
    - auth_user_groups
    - auth_user_user_permissions
- ������Ϣ
    - django_admin_logo
    - django_content_type
    - django_migrations
    - django_session

### ���ʺ�̨
```
http://127.0.0.1:8080/admin
```

### ������������Ա
```
python manage.py createsuperuser
 
# ������ʾ�����û����Ͷ�Ӧ������ͺ�������������գ��û������������
 
# �޸� �û���������ã�
python manage.py changepassword username

```




# django ʵ��

### ����һ��appģ��
```
python manage.py startapp app
```
- ��setting�����app��������
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
### �����ϵӳ��
��ԭ�����ݿ��ѯ���ת����ͨ�õĲ�ѯ
ORM object-relational-mapping

### ����Ǩ���ļ�
```
python manage.py makemigrations
```
### ����urls.py����·��
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
### ����models.pyģ�����ݴ���
```
from django.db import models

# Create your models here.


class Student(models.Model):
    # �������ַ����ֶ�
    s_name = models.CharField(max_length=10,unique=True)
    #���������ֶ�
    s_age = models.IntegerField(default=18)
    s_gender = models.BooleanField(default=1)
    #����ʱ�䣨��ӹ̶���ʱ�䣩
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    # �޸�ʱ��(ÿ���޸�������µ�ʱ��)
    operate_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        # ����ģ��Ǩ�Ƶ����ݿ�ı���
        db_table = 'student'
```

### ����views.py������ͼ
```

from django.shortcuts import render
from django.http import HttpResponse
from app.models import Student
# Create your views here.


def hello(request):
    return HttpResponse('��ã�ǧ��')


def create_stu(request):
    # ��һ��
    # stu = Student()
    # stu.s_name = 'С��'
    # stu.s_age = 20
    # stu.save()
    # �ڶ���
    # Student.objects.create(s_name='С��')
    Student.objects.create(s_name='С��')
    Student.objects.create(s_name='���')
    Student.objects.create(s_name='��')
    Student.objects.create(s_name='С��')
    Student.objects.create(s_name='����')
    Student.objects.create(s_name='����')
    Student.objects.create(s_name='����')
    Student.objects.create(s_name='����')
    Student.objects.create(s_name='������')

    return HttpResponse('�����ɹ�')


def sel_stu(request):
    stus = Student.objects.all()
    print(stus)
    # filter(����)�õ�ѧ�������б����������ؿ�
    # first/last �õ�ѧ������
    stus = Student.objects.filter(s_name='С��').first()
    # get �õ�ѧ������,�ò���ֵ�ᱨ��ֻ�ܷ���һ��ֵ
    stus = Student.objects.get(s_name='С��')
    # �����ѯ����
    stus = Student.objects.filter(s_age=20).filter(s_gender=0)
    stus = Student.objects.filter(s_age=20, s_gender=0)

    # ģ����ѯ
    # ������ѯ
    stus = Student.objects.filter(s_name__contains='��')
    stu_names = [stu.s_name for stu in stus]
    print(stu_names)
    # ��ʲô��ʼ��ѯ
    stus = Student.objects.filter(s_name__startswith='С')
    stu_names = [stu.s_name for stu in stus]
    print(stu_names)
    # ��ʲô������ѯ
    stus = Student.objects.filter(s_name__endswith='��')
    stu_names = [stu.s_name for stu in stus]
    print(stu_names)

    # gt���ڣ�gte���ڣ�lteС�ڵ���
    stus = Student.objects.filter(s_age__gt=18)
    stu_names = [stu.s_name for stu in stus]
    print(stu_names)

    # ���� order_by
    stus = Student.objects.order_by('id')
    stu_names = [stu.s_name for stu in stus]
    print(stu_names)
    # ����
    stus = Student.objects.order_by('-id')
    stu_names = [stu.s_name for stu in stus]
    print(stu_names)

    # ��������ѯ
    stus = Student.objects.exclude(s_age=18)
    stu_names = [stu.s_name for stu in stus]
    print(stu_names)

    # ͳ�Ƹ��� count����
    stus_count = stus.count()

    # ת�����ֵ�����
    stus_values = stus.values()

    # id=pk
    stus = Student.objects.filter(id=2)
    stus = Student.objects.filter(pk=2)

    return HttpResponse('��ѯ����ѧ���ɹ�')
```