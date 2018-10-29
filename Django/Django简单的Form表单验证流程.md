# Django中Forms 表单验证

### 在app中新建forms.py文件来存放验证功能代码块
```
from django import forms
from django.contrib.auth.models import User


# 用户注册字段的验证，required=True必须有值
class UserRegisterForm(forms.Form):
    # 用户名字段验证
    username = forms.CharField(max_length=10, min_length=2, required=True,
                               error_messages={
                                   'required': '必填',
                                   'max_length': '不能超过10字符',
                                   'min_length': '不能少于2字符'
                               })
    # 密码字段验证
    password = forms.CharField(max_length=10, required=True,
                               error_messages={
                                   'required': '必填',
                                   'max_length': '不能超过10字符'
                               })
    # 确认密码字段验证
    password2 = forms.CharField(max_length=10, required=True,
                               error_messages={
                                   'required': '必填',
                                   'max_length': '不能超过10字符'
                               })

    # clean()方法主要用于验证相互依赖的字段，例如注册时，填写的“密码”和“确认密码”要相等时才符合要求。
    def clean(self):
        # 获取数据库中的用户名，self.cleaned_data是一个字典类型的数据对象，他获取的是表单中输入的数据对象
        user = User.objects.filter(username=self.cleaned_data.get('username')).first()
	# 如果存在，则已注册
        if user:
            raise forms.ValidationError({'username': '账号已注册，请去登陆'})
	# 验证注册时两次输入的密码是否一致
        pasword = self.cleaned_data.get('password')
        pasword2 = self.cleaned_data.get('password2')
	# 密码不一致提示信息
        if pasword != pasword2:
            raise forms.ValidationError({'password': '密码不一致'})
	# 返回表单数据这是一个字典类型的数据
        return self.cleaned_data


# 用户登录字段验证
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

    def clean(self):
        user = User.objects.filter(username=self.cleaned_data.get('username')).first()
        if not user:
            raise forms.ValidationError({'username':'该账号没有注册，请去注册'})

        return self.cleaned_data


```
### 在app中的views.py文件中定义登录网页的功能代码模块

```
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from user.forms import UserRegisterForm, UserLoginForm

# 注册功能
def register(request):
    # 获取到注册页面
    if request.method == 'GET':
        return render(request, 'register.html')
    # 向服务器提交用户信息并，注册用户
    if request.method == 'POST':
        data = request.POST
        # 校验form表单传递的参数
        form = UserRegisterForm(data)
	# 校验正确的注册信息进入注册
        if form.is_valid():
	    # 向服务器数据库中写入用户信息
            User.objects.create_user(username=form.cleaned_data.get('username'),
                                     password=form.cleaned_data.get('password'))
	    # 注册成功跳转到登录页面
            return HttpResponseRedirect(reverse('user:login'))
	# 注册信息校验失败，注册失败返回注册页面和错误信息
        else:
            return render(request, 'register.html', {'errors': form.errors})

# 登录功能
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
	# 用一个data变量保存请求中的数据
        data = request.POST
	# 调用验证方法验证数据
        form = UserLoginForm(data)
	# 
        if form.is_valid():
            # 使用随机标识符也叫做签名token
	    # authenticate() 函数。它接受两个参数，用户名 username 和 密码 password ，并在密码对给出的用户名合法的情况下返回一个 User 对象。 如果密码不合法，authenticate()返回None。
            # authenticate() 只是验证一个用户的证书而已。 而要登录一个用户，使用 login() 。该函数接受一个 HttpRequest 对象和一个 User 对象作为参数并使用Django的会话（ session ）框架把用户的ID保存在该会话中。
            user = auth.authenticate(username=form.cleaned_data.get('username'),
                                     password=form.cleaned_data.get('password'))
            if user:
                # 登录, 向request.user属性赋值，赋值为登录系统的用户对象
                # 1. 向页面的cookie中设置sessionid值，(标识符)
                # 2. 向django_session表中设置对应的标识符
                auth.login(request, user)
                return HttpResponseRedirect(reverse('user:index'))
            else:
                return render(request, 'login.html', {'msg': '密码错误'})
        else:
            return render(request, 'login.html', {'errors': form.errors})


# 修饰器验证跳转到主页，@login_required标签。其作用就是告诉程序，使用这个方法是要求用户登录的
@login_required
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


# 修饰器验证注销
@login_required()
def logout(request):
    if request.method == 'GET':
        # 研究logout实现的功能？
        auth.logout(request)
        return HttpResponseRedirect(reverse('user:login'))


```
### urls.py中的路由设置
```

from django.conf.urls import url

from user import views


urlpatterns = [
    # 注册，使用django自带的User模型
    url(r'^register/', views.register, name='register'),
    # 登录
    url(r'^login/', views.login, name='login'),
    # 首页
    url(r'^index/', views.index, name='index'),
    # 注销
    url(r'^logout/', views.logout, name='logout'),
]

```