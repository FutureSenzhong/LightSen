# djiango���

mvc: �����Ƶ䷶�����ģʽ��������˼���ǽ���ϣ��ô����ø�������������ά�� Model��ģ�ͣ��������ݸ�����������ݿ�����ݴ洢�Ĳ�����View����ͼ���������ݿ�����ݲ���ʾ������Controller��������������ģ������ͼ��
mvt


### ��װpython ������뻷��

����һ���ɾ��ģ�
```
viryualenv --no-site-packages -p ��python�汾·��������ж���汾�� �����⻷���ļ�����
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

```
### �����ݿ�����djangoĬ�����ݱ�
```
python manage.py migtate
```
- Ȩ�����ñ�
    - attu_group
    - attu_group_permissions
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