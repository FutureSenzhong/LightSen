from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse

from user.forms import UserRegisterForm, UserAddressForm
from user.models import User, UserAddress


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        data = request.POST
        form = UserRegisterForm(data)
        if form.is_valid():
            password = make_password(form.cleaned_data.get('pwd'))
            # 实现注册
            User.objects.create(username=form.cleaned_data.get('username'),
                                password=password)
            return HttpResponseRedirect(reverse('user:login'))
        else:
            return render(request, 'register.html', {'errors': form.errors})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        # 验证完整性
        if not all([username, pwd]):
            msg = '用户名或密码必填'
            return render(request, 'login.html', {'msg': msg})
        # 验证用户
        user = User.objects.filter(username=username).first()
        if not user:
            msg = '该用户没有注册'
            return render(request, 'login.html', {'msg': msg})

        if check_password(pwd, user.password):
            # 验证成功
            # django自带auth模块，签名token，会话上下文session
            # request.user
            request.session['user_id'] = user.id
            return HttpResponseRedirect(reverse('goods:index'))
        else:
            msg = '密码错误'
            return render(request, 'login.html', {'msg': msg})


def is_login(request):
    if request.method == 'GET':
        # 清空session
        user = request.user
        return JsonResponse({'code': 200, 'msg': '请求成功', 'username': user.username})


def logout(request):
    if request.method == 'GET':
        # 清空session
        request.session.flush()
        return HttpResponseRedirect(reverse('goods:index'))


def user_center_order(request):
    if request.method == 'GET':
        return render(request, 'user_center_info.html')


def address(request):
    if request.method == 'GET':
        user = request.user
        # 获取用户的收货地址信息
        user_addresses = UserAddress.objects.filter(user=user).order_by('-id')
        return render(request, 'user_center_site.html', {'user_addresses': user_addresses})

    if request.method == 'POST':
        # 使用表单验证，验证收货地址的参数是否填写完整
        form = UserAddressForm(request.POST)
        if form.is_valid():
            user = request.user
            address_info = form.cleaned_data
            # 保存收货地址信息
            UserAddress.objects.create(**address_info, user=user)
            # 保存成功收货地址
            return HttpResponseRedirect(reverse('user:user_address'))
        else:
            user = request.user
            # 获取用户的收货地址信息
            user_addresses = UserAddress.objects.filter(user=user).order_by('-id')
            return render(request, 'user_center_site.html', {'form': form, 'user_addresses': user_addresses})



