
from django.conf.urls import url

from user import views

urlpatterns = [
    # 登录
    url(r'login/', views.login, name='login'),
    # 首页
    url(r'^index/', views.index, name='index'),
]