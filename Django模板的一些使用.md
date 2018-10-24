[TOC]

# Django模板的一些使用方法

### 实例一，显示一个基本的字符串在网页上

在views.py中定义一个字符串

```
from django.shortcuts import render
 
 
def home(request):
    # 'u'表示unicode编码字符串
    string = u"我在学习Django，用它来建网站"
    return render(request, 'home.html', {'string': string})
```
将字符串渲染到网页上home.thml

```
{{ string }}
```
### 实例二，基本的for循环和List内容的显示

在views.py中定义一个字符串

```
def home(request):
    List = ["HTML", "CSS", "jQuery", "Python", "Django"]
    return render(request, 'home.html', {'List': List})
```
将字符串渲染到网页上home.thml

```
# 值得注意的是for循环要添加一个endfor来结束{%   %}是条件判断标签
{% for i in TutorialList %}
{{ i }}
{% endfor %}
```
### 实例三，显示字典中内容

在views.py中定义一个字典
```
def home(request):
    info_dict = {'a': u'我', 'b': u'要学习Django网站技术'}
    return render(request, 'home.html', {'info_dict': info_dict})
```
将字符串渲染到网页上home.thml

```
# 第一种写法
谁：{{ info_dict.a }} 干啥：{{ info_dict.b }}

# 在模板中取字典的键是用点info_dict.a，而不是Python中的 info_dict['a']
# 第二种写法,实质就是遍历一个元组列表[('a': u'我'), ('b': u'要学习Django网站技术')]

{% for key, value in info_dict.items %}
    {{ key }}: {{ value }}
{% endfor %}
```
### 实例四，条件判断和for循环的详细操作

```
#定义一个列表
def home(request):
    List = map(str, range(100))# 一个长度为100的 List
    return render(request, 'home.html', {'List': List})

```
在页面上渲染出来用逗号连接
```
{% for item in List %}
    {{ item }}, 
{% endfor %}


# 引入判断
{% for item in List %}
    {{ item }}{% if not forloop.last %},{% endif %} 
{% endfor %}

```
- 总结
    - forloop.counter	        索引从 1 开始算
    - forloop.counter0	        索引从 0 开始算
    - forloop.revcounter	索引从最大长度到 1
    - forloop.revcounter0	索引从最大长度到 0
    - forloop.first	        当遍历的元素为第一项时为真
    - forloop.last	        当遍历的元素为最后一项时为真
    - forloop.parentloop	用在嵌套的 for 循环中，获取上一层 for 循环的 forloop

### 列表空值判断
```
<ul>
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% empty %}
    <li>抱歉，列表为空</li>
{% endfor %}
</ul>

```