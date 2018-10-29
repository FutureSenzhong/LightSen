# Django��Forms ����֤

### ��app���½�forms.py�ļ��������֤���ܴ����
```
from django import forms
from django.contrib.auth.models import User


# �û�ע���ֶε���֤��required=True������ֵ
class UserRegisterForm(forms.Form):
    # �û����ֶ���֤
    username = forms.CharField(max_length=10, min_length=2, required=True,
                               error_messages={
                                   'required': '����',
                                   'max_length': '���ܳ���10�ַ�',
                                   'min_length': '��������2�ַ�'
                               })
    # �����ֶ���֤
    password = forms.CharField(max_length=10, required=True,
                               error_messages={
                                   'required': '����',
                                   'max_length': '���ܳ���10�ַ�'
                               })
    # ȷ�������ֶ���֤
    password2 = forms.CharField(max_length=10, required=True,
                               error_messages={
                                   'required': '����',
                                   'max_length': '���ܳ���10�ַ�'
                               })

    # clean()������Ҫ������֤�໥�������ֶΣ�����ע��ʱ����д�ġ����롱�͡�ȷ�����롱Ҫ���ʱ�ŷ���Ҫ��
    def clean(self):
        # ��ȡ���ݿ��е��û�����self.cleaned_data��һ���ֵ����͵����ݶ�������ȡ���Ǳ�����������ݶ���
        user = User.objects.filter(username=self.cleaned_data.get('username')).first()
	# ������ڣ�����ע��
        if user:
            raise forms.ValidationError({'username': '�˺���ע�ᣬ��ȥ��½'})
	# ��֤ע��ʱ��������������Ƿ�һ��
        pasword = self.cleaned_data.get('password')
        pasword2 = self.cleaned_data.get('password2')
	# ���벻һ����ʾ��Ϣ
        if pasword != pasword2:
            raise forms.ValidationError({'password': '���벻һ��'})
	# ���ر���������һ���ֵ����͵�����
        return self.cleaned_data


# �û���¼�ֶ���֤
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

    def clean(self):
        user = User.objects.filter(username=self.cleaned_data.get('username')).first()
        if not user:
            raise forms.ValidationError({'username':'���˺�û��ע�ᣬ��ȥע��'})

        return self.cleaned_data


```
### ��app�е�views.py�ļ��ж����¼��ҳ�Ĺ��ܴ���ģ��

```
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from user.forms import UserRegisterForm, UserLoginForm

# ע�Ṧ��
def register(request):
    # ��ȡ��ע��ҳ��
    if request.method == 'GET':
        return render(request, 'register.html')
    # ��������ύ�û���Ϣ����ע���û�
    if request.method == 'POST':
        data = request.POST
        # У��form�����ݵĲ���
        form = UserRegisterForm(data)
	# У����ȷ��ע����Ϣ����ע��
        if form.is_valid():
	    # ����������ݿ���д���û���Ϣ
            User.objects.create_user(username=form.cleaned_data.get('username'),
                                     password=form.cleaned_data.get('password'))
	    # ע��ɹ���ת����¼ҳ��
            return HttpResponseRedirect(reverse('user:login'))
	# ע����ϢУ��ʧ�ܣ�ע��ʧ�ܷ���ע��ҳ��ʹ�����Ϣ
        else:
            return render(request, 'register.html', {'errors': form.errors})

# ��¼����
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
	# ��һ��data�������������е�����
        data = request.POST
	# ������֤������֤����
        form = UserLoginForm(data)
	# 
        if form.is_valid():
            # ʹ�������ʶ��Ҳ����ǩ��token
	    # authenticate() �����������������������û��� username �� ���� password ����������Ը������û����Ϸ�������·���һ�� User ���� ������벻�Ϸ���authenticate()����None��
            # authenticate() ֻ����֤һ���û���֤����ѡ� ��Ҫ��¼һ���û���ʹ�� login() ���ú�������һ�� HttpRequest �����һ�� User ������Ϊ������ʹ��Django�ĻỰ�� session ����ܰ��û���ID�����ڸûỰ�С�
            user = auth.authenticate(username=form.cleaned_data.get('username'),
                                     password=form.cleaned_data.get('password'))
            if user:
                # ��¼, ��request.user���Ը�ֵ����ֵΪ��¼ϵͳ���û�����
                # 1. ��ҳ���cookie������sessionidֵ��(��ʶ��)
                # 2. ��django_session�������ö�Ӧ�ı�ʶ��
                auth.login(request, user)
                return HttpResponseRedirect(reverse('user:index'))
            else:
                return render(request, 'login.html', {'msg': '�������'})
        else:
            return render(request, 'login.html', {'errors': form.errors})


# ��������֤��ת����ҳ��@login_required��ǩ�������þ��Ǹ��߳���ʹ�����������Ҫ���û���¼��
@login_required
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


# ��������֤ע��
@login_required()
def logout(request):
    if request.method == 'GET':
        # �о�logoutʵ�ֵĹ��ܣ�
        auth.logout(request)
        return HttpResponseRedirect(reverse('user:login'))


```
### urls.py�е�·������
```

from django.conf.urls import url

from user import views


urlpatterns = [
    # ע�ᣬʹ��django�Դ���Userģ��
    url(r'^register/', views.register, name='register'),
    # ��¼
    url(r'^login/', views.login, name='login'),
    # ��ҳ
    url(r'^index/', views.index, name='index'),
    # ע��
    url(r'^logout/', views.logout, name='logout'),
]

```