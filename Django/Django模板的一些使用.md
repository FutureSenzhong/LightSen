
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
### ע��˵��
```
<!--  Django�еĻ���ش��룬���ױ���   -->

# ����ע��
{#  #}
# ����ע��
{% comment %}

{% endcomment %}

```
### ��̬�ļ�·������
```
STATIC_URL = '/static/'
STATICFILES_DIRS = [

    os.path.join(BASE_DIR, 'static')
]

### ���ؾ�̬�ļ�

{% load static %}
        <link rel="stylesheet" href="{% static 'css/index.css' %}">

```
### ��������ύ������form����ǩ

#### ������÷�
<p>\<form> ��ǩ����Ϊ�û����봴�� HTML ����

<p>���ܹ����� input Ԫ�أ������ı��ֶΡ���ѡ�򡢵�ѡ���ύ��ť�ȵȡ�

<p>�������԰��� menus��textarea��fieldset��legend �� label Ԫ�ء�

<p>��������������������ݡ�

### Djangoģ���ֶ���

���ֶ����Ƶ�����

- �ֶ���������Python�ı����֣�����ᵼ���﷨����
- �ֶ��������ж�������»��ߣ�����Ӱ��ORM��ѯ����

| �ֶ���                |  ˵��                                                         |
| --------------------- | ------------------------------------------------------------ |
| AutoField             |����ID�ֶ�                                                   |
| BigIntegerField       |64λ�з�������                                               |
| BinaryField           | �洢���������ݵ��ֶΣ���ӦPython��bytes����                  |
| BooleanField          | �洢True��False                                              |
| CharField             | ���Ƚ�С���ַ���                                             |
| DateField             | �洢���ڣ���auto_now��auto_now_add����                       |
| DateTimeField         | �洢���ں����ڣ�������������ͬ��                             |
| DecimalField          |�洢�̶�����С������max_digits����Чλ������decimal_places��С������棩������Ҫ�Ĳ��� |
| DurationField         |�洢ʱ����                                                 |
| EmailField            | ��CharField��ͬ��������EmailValidator��֤                    |
| FileField             | �ļ��ϴ��ֶ�                                                 |
| FloatField            | �洢������                                                   |
| ImageField            | ����ͬFileFiled��Ҫ��֤�ϴ����ǲ�����Чͼ��                  |
| IntegerField          | �洢32λ�з���������                                         |
| GenericIPAddressField | �洢IPv4��IPv6��ַ                                           |
| NullBooleanField      | �洢True��False��nullֵ                                      |
| PositiveIntegerField  | �洢�޷���������ֻ�ܴ洢������                               |
| SlugField             | �洢slug����̱�ע��                                         |
| SmallIntegerField     | �洢16λ�з�������                                           |
| TextField             | �洢�������ϴ���ı�                                         |
| TimeField             | �洢ʱ��                                                     |
| URLField              | �洢URL��CharField                                           |
| UUIDField             | �洢ȫ��Ψһ��ʶ��                                           |


### �ֶ�����

ͨ���ֶ�����

| ѡ��           | ˵��                                                         |
| -------------- | ------------------------------------------------------------ |
| null           | ���ݿ��ж�Ӧ���ֶ��Ƿ�����ΪNULL��Ĭ��ΪFalse                |
| blank          | ��̨ģ�͹�����֤����ʱ���Ƿ�����ΪNULL��Ĭ��ΪFalse          |
| choices        | �趨�ֶε�ѡ���Ԫ���еĵ�һ��ֵ��������ģ���ϵ�ֵ���ڶ�ֵ������ɶ���ֵ |
| db_column      | �ֶζ�Ӧ�����ݿ���е�������δָ��ʱֱ��ʹ���ֶε�����       |
| db_index       | ����ΪTrueʱ���ڸ��ֶδ�������                               |
| db_tablespace  | Ϊ���������ֶ�����ʹ�õı�ռ䣬Ĭ��ΪDEFAULT_INDEX_TABLESPACE |
| default        | �ֶε�Ĭ��ֵ                                                 |
| editable       | �ֶ��ں�̨ģ�͹����ModelForm���Ƿ���ʾ��Ĭ��ΪTrue          |
| error_messages | �趨�ֶ��׳��쳣ʱ��Ĭ����Ϣ���ֵ䣬���еļ�����null��blank��invalid��invalid_choice��unique��unique_for_date |
| help_text      | ��С����Ա���ʾ�Ķ���İ����ı���                         |
| primary_key    | ���ֶ�ָ��Ϊģ�͵�������δָ��ʱ���Զ����AutoField����������ֻ���� |
| unique         | ����ΪTrueʱ�������ֶε�ֵ������Ψһ��                       |
| verbose_name   | �ֶ��ں�̨ģ�͹�����ʾ�����ƣ�δָ��ʱʹ���ֶε�����         |

ForeignKey����

1. limit_choices_to��ֵ��һ��Q����򷵻�һ��Q�����������ƺ�̨��ʾ��Щ����
2. related_name�����ڻ�ȡ��������Ĺ������������󣨷����ѯ��������������򣬸�����Ӧ�ñ�����Ϊ`'+'`��������`'+'`��β��
3. to_field��ָ���������ֶΣ�Ĭ�Ϲ�������������ֶΡ�
4. db_constraint���Ƿ�Ϊ�������Լ����Ĭ��ֵΪTrue��
5. on_delete����������Ķ���ɾ��ʱ��Ӧ�Ķ�������ȡ��ֵ����django.db.models�ж���ģ�
   - CASCADE������ɾ����
   - PROTECT���׳�ProtectedError�쳣����ֹɾ�����õĶ���
   - SET_NULL�����������Ϊnull����null���Ա�����ΪTrueʱ������ô����
   - SET_DEFAULT�����������ΪĬ��ֵ���ṩ��Ĭ��ֵ������ô����

ManyToManyField����

1. symmetrical���Ƿ����ԳƵĶ�Զ��ϵ��
2. through��ָ��ά�ֶ�Զ��ϵ���м���Djangoģ�͡�
3. throughfields���������м�ģ��ʱ����ָ��������Զ��ϵ���ֶΡ�
4. db_table��ָ��ά�ֶ�Զ��ϵ���м��ı�����

### ģ��Ԫ����ѡ��

| ѡ��                  | ˵��                                                         |
| --------------------- | ------------------------------------------------------------ |
| abstract              | ����ΪTrueʱģ���ǳ�����                                   |
| app_label             | �������ģ�͵�Ӧ�ò���INSTALLED_APPS�п����ø�����ָ��       |
| db_table              | ģ��ʹ�õ����ݱ�����                                         |
| db_tablespace         | ģ��ʹ�õ����ݱ�ռ�                                         |
| default_related_name  | ���������ָ���ģ��ʱĬ��ʹ�õ����ƣ�Ĭ��Ϊ<model_name>_set |
| get_latest_by         | ģ���п������ֶε����ơ�                                     |
| managed               | ����ΪTrueʱ��Django��Ǩ���д������ݱ���ִ��flush��������ʱ�ѱ��Ƴ� |
| order_with_respect_to | ��Ƕ���Ϊ�������                                           |
| ordering              | �����Ĭ������                                               |
| permissions           | ��������ʱд��Ȩ�ޱ�Ķ���Ȩ��                               |
| default_permissions   | Ĭ��Ϊ`('add', 'change', 'delete')`                          |
| unique_together       | �趨�����һ��ʱ�����һ�޶����ֶ���                         |
| index_together        | �趨һ���������Ķ���ֶ���                                 |
| verbose_name          | Ϊ�����趨����ɶ�������                                     |
| verbose_name_plural   | �趨����ĸ�������                                           |