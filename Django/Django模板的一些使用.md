
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
### 注释说明
```
<!--  Django中的会加载代码，容易报错   -->

# 单行注释
{#  #}
# 多行注释
{% comment %}

{% endcomment %}

```
### 静态文件路径配置
```
STATIC_URL = '/static/'
STATICFILES_DIRS = [

    os.path.join(BASE_DIR, 'static')
]

### 加载静态文件

{% load static %}
        <link rel="stylesheet" href="{% static 'css/index.css' %}">

```
### 向服务器提交数据用form表单标签

#### 定义和用法
<p>\<form> 标签用于为用户输入创建 HTML 表单。

<p>表单能够包含 input 元素，比如文本字段、复选框、单选框、提交按钮等等。

<p>表单还可以包含 menus、textarea、fieldset、legend 和 label 元素。

<p>表单用于向服务器传输数据。

### Django模型字段类

对字段名称的限制

- 字段名不能是Python的保留字，否则会导致语法错误
- 字段名不能有多个连续下划线，否则影响ORM查询操作

| 字段类                |  说明                                                         |
| --------------------- | ------------------------------------------------------------ |
| AutoField             |自增ID字段                                                   |
| BigIntegerField       |64位有符号整数                                               |
| BinaryField           | 存储二进制数据的字段，对应Python的bytes类型                  |
| BooleanField          | 存储True或False                                              |
| CharField             | 长度较小的字符串                                             |
| DateField             | 存储日期，有auto_now和auto_now_add属性                       |
| DateTimeField         | 存储日期和日期，两个附加属性同上                             |
| DecimalField          |存储固定精度小数，有max_digits（有效位数）和decimal_places（小数点后面）两个必要的参数 |
| DurationField         |存储时间跨度                                                 |
| EmailField            | 与CharField相同，可以用EmailValidator验证                    |
| FileField             | 文件上传字段                                                 |
| FloatField            | 存储浮点数                                                   |
| ImageField            | 其他同FileFiled，要验证上传的是不是有效图像                  |
| IntegerField          | 存储32位有符号整数。                                         |
| GenericIPAddressField | 存储IPv4或IPv6地址                                           |
| NullBooleanField      | 存储True、False或null值                                      |
| PositiveIntegerField  | 存储无符号整数（只能存储正数）                               |
| SlugField             | 存储slug（简短标注）                                         |
| SmallIntegerField     | 存储16位有符号整数                                           |
| TextField             | 存储数据量较大的文本                                         |
| TimeField             | 存储时间                                                     |
| URLField              | 存储URL的CharField                                           |
| UUIDField             | 存储全局唯一标识符                                           |


### 字段属性

通用字段属性

| 选项           | 说明                                                         |
| -------------- | ------------------------------------------------------------ |
| null           | 数据库中对应的字段是否允许为NULL，默认为False                |
| blank          | 后台模型管理验证数据时，是否允许为NULL，默认为False          |
| choices        | 设定字段的选项，各元组中的第一个值是设置在模型上的值，第二值是人类可读的值 |
| db_column      | 字段对应到数据库表中的列名，未指定时直接使用字段的名称       |
| db_index       | 设置为True时将在该字段创建索引                               |
| db_tablespace  | 为有索引的字段设置使用的表空间，默认为DEFAULT_INDEX_TABLESPACE |
| default        | 字段的默认值                                                 |
| editable       | 字段在后台模型管理或ModelForm中是否显示，默认为True          |
| error_messages | 设定字段抛出异常时的默认消息的字典，其中的键包括null、blank、invalid、invalid_choice、unique和unique_for_date |
| help_text      | 表单小组件旁边显示的额外的帮助文本。                         |
| primary_key    | 将字段指定为模型的主键，未指定时会自动添加AutoField用于主键，只读。 |
| unique         | 设置为True时，表中字段的值必须是唯一的                       |
| verbose_name   | 字段在后台模型管理显示的名称，未指定时使用字段的名称         |

ForeignKey属性

1. limit_choices_to：值是一个Q对象或返回一个Q对象，用于限制后台显示哪些对象。
2. related_name：用于获取关联对象的关联管理器对象（反向查询），如果不允许反向，该属性应该被设置为`'+'`，或者以`'+'`结尾。
3. to_field：指定关联的字段，默认关联对象的主键字段。
4. db_constraint：是否为外键创建约束，默认值为True。
5. on_delete：外键关联的对象被删除时对应的动作，可取的值包括django.db.models中定义的：
   - CASCADE：级联删除。
   - PROTECT：抛出ProtectedError异常，阻止删除引用的对象。
   - SET_NULL：把外键设置为null，当null属性被设置为True时才能这么做。
   - SET_DEFAULT：把外键设置为默认值，提供了默认值才能这么做。

ManyToManyField属性

1. symmetrical：是否建立对称的多对多关系。
2. through：指定维持多对多关系的中间表的Django模型。
3. throughfields：定义了中间模型时可以指定建立多对多关系的字段。
4. db_table：指定维持多对多关系的中间表的表名。

### 模型元数据选项

| 选项                  | 说明                                                         |
| --------------------- | ------------------------------------------------------------ |
| abstract              | 设置为True时模型是抽象父类                                   |
| app_label             | 如果定义模型的应用不在INSTALLED_APPS中可以用该属性指定       |
| db_table              | 模型使用的数据表名称                                         |
| db_tablespace         | 模型使用的数据表空间                                         |
| default_related_name  | 关联对象回指这个模型时默认使用的名称，默认为<model_name>_set |
| get_latest_by         | 模型中可排序字段的名称。                                     |
| managed               | 设置为True时，Django在迁移中创建数据表并在执行flush管理命令时把表移除 |
| order_with_respect_to | 标记对象为可排序的                                           |
| ordering              | 对象的默认排序                                               |
| permissions           | 创建对象时写入权限表的额外权限                               |
| default_permissions   | 默认为`('add', 'change', 'delete')`                          |
| unique_together       | 设定组合在一起时必须独一无二的字段名                         |
| index_together        | 设定一起建立索引的多个字段名                                 |
| verbose_name          | 为对象设定人类可读的名称                                     |
| verbose_name_plural   | 设定对象的复数名称                                           |