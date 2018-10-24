[TOC]

# Djangoģ���һЩʹ�÷���

### ʵ��һ����ʾһ���������ַ�������ҳ��

��views.py�ж���һ���ַ���

```
from django.shortcuts import render
 
 
def home(request):
    # 'u'��ʾunicode�����ַ���
    string = u"����ѧϰDjango������������վ"
    return render(request, 'home.html', {'string': string})
```
���ַ�����Ⱦ����ҳ��home.thml

```
{{ string }}
```
### ʵ������������forѭ����List���ݵ���ʾ

��views.py�ж���һ���ַ���

```
def home(request):
    List = ["HTML", "CSS", "jQuery", "Python", "Django"]
    return render(request, 'home.html', {'List': List})
```
���ַ�����Ⱦ����ҳ��home.thml

```
# ֵ��ע�����forѭ��Ҫ���һ��endfor������{%   %}�������жϱ�ǩ
{% for i in TutorialList %}
{{ i }}
{% endfor %}
```
### ʵ��������ʾ�ֵ�������

��views.py�ж���һ���ֵ�
```
def home(request):
    info_dict = {'a': u'��', 'b': u'ҪѧϰDjango��վ����'}
    return render(request, 'home.html', {'info_dict': info_dict})
```
���ַ�����Ⱦ����ҳ��home.thml

```
# ��һ��д��
˭��{{ info_dict.a }} ��ɶ��{{ info_dict.b }}

# ��ģ����ȡ�ֵ�ļ����õ�info_dict.a��������Python�е� info_dict['a']
# �ڶ���д��,ʵ�ʾ��Ǳ���һ��Ԫ���б�[('a': u'��'), ('b': u'ҪѧϰDjango��վ����')]

{% for key, value in info_dict.items %}
    {{ key }}: {{ value }}
{% endfor %}
```
### ʵ���ģ������жϺ�forѭ������ϸ����

```
#����һ���б�
def home(request):
    List = map(str, range(100))# һ������Ϊ100�� List
    return render(request, 'home.html', {'List': List})

```
��ҳ������Ⱦ�����ö�������
```
{% for item in List %}
    {{ item }}, 
{% endfor %}


# �����ж�
{% for item in List %}
    {{ item }}{% if not forloop.last %},{% endif %} 
{% endfor %}

```
- �ܽ�
    - forloop.counter	        ������ 1 ��ʼ��
    - forloop.counter0	        ������ 0 ��ʼ��
    - forloop.revcounter	��������󳤶ȵ� 1
    - forloop.revcounter0	��������󳤶ȵ� 0
    - forloop.first	        ��������Ԫ��Ϊ��һ��ʱΪ��
    - forloop.last	        ��������Ԫ��Ϊ���һ��ʱΪ��
    - forloop.parentloop	����Ƕ�׵� for ѭ���У���ȡ��һ�� for ѭ���� forloop

### �б��ֵ�ж�
```
<ul>
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% empty %}
    <li>��Ǹ���б�Ϊ��</li>
{% endfor %}
</ul>

```