# 一、关于django的简介
　　django是一个python中的web框架，如果想更好的使用它，最好还能有HTML, CSS, JavaScript等方面的知识。它的特点主要体现在几个方面：强大的数据库（具有许多api同时支持执行sql语句）、自带强大的后台功能、利用正则表达式匹配网址（简化网页管理）、模板与视图一一对应、缓存机制、国际化支持等等。

　　django适合于敏捷开发，只需要少量代码即可建立高性能web应用。因其已经完成了开发网站的许多常见代码，所以减少了代码的重复度。Ok，让我们首先看下django的主要文件组成。主要文件包括如下几个py文件：

django工程主要py文件
文件	功能
urls.py	网址入口，关联到views中对于的函数
models.py	与数据库操作相关，建立应用数据模型
views.py	处理用户发出请求，从urls中对应过来，通过渲染templates中网页显示内容
settings.py	相关设置，包括数据库设置，邮件设置，静态文件配置等
forms.py	表单，用户在浏览器端提交的表单数据类
admin.py	后台代码，大部分已完成
# 二、常用命令
　　环境搭建这一部分就不作叙述，网上教程很多。常用命令如下：
```

# 新建django project
django-admin.py startproject project-name
# 新建django app命令
django-admin.py startapp app-name (or) python manage.py startapp app-name
# 同步数据库
python manage.py syncdb
# (django1.7.1及以上版本需要使用以下命令)
python manage.py makemigrations
python manage.py migrate
# 运行django项目，不加port默认为8000
python manage.py runserver port
# ex: python manage.py runserver 8080
# 清空数据库
python manage.py flush
# 创建超级管理员
python manage.py createsuperuser
# 修改管理员密码
python manage.py changepassword username
# 导出数据
python manage.py dumpdata appname > appname.json
# 导入数据
python manage.py loaddata appname.json
# 进入django项目命令终端
python manage.py shell
# 进入数据库命令行
python manage.py dbshell
```
# 三、视图
　　我们已经知道views中的函数是与urls中的网址对应的，接下来我们做一个简单的实例演示。

1. 首先将应用名称添加到settings.py中
```
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'newReverse',
    'reverse',
)
```
2. 在views中定义视图函数
```
def test(request):
    return render(request, 'test.html')
这里返回的结果有多种，其本质返回的结果是HttpResponse。其他返回情况如

return HttpResponse("hello world")
return render_to_response('test.html', '')
return HttpResponseRedirect('/index/')
其中render与render_to_respose是一样的，只是render不需要说明ResponseContext而render_to_respose则需要coding出来。render，最后会返回一个字典，以向模板中传递数据。

return render_to_response('checkmt.html', {'info': info})
return render(request, 'day2.html', {'info': info})
```
3. 设置在urls.py中的地址
```
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login),
    url(r'^index/$', views.index, name="index"),   
)
```
这里urls设置有多种方式，具体可以查看官方文档，其主要包括两部分，正则表达式格式的网址+views函数。同时网址中还可以传递参数。

# 四、模板
　　模板是通过views函数渲染的，其实质是一个html网页。一般放在app下的templates中，加载模板时django会自动寻找。那么假如一个工程中有多个应用，每个应用的templates中都有一个index.html，然后直接调用render(request, 'index.html')能不能找到呢？答案是可能会出错。让我们来探究下django模板查找机制。django模板查找过程是在每个app的templates文件夹中查找（而不是当前app中的templates），当在这些应用的templates文件夹列表中查找到index.html模板时停止，所以说可能出现错误；如果最终没有找到则返回一个templates not found错误。

　　接下来我们来介绍一下关于模板代码的应用。一般地，网站中都会有一些模板设计，即很多网页都有很多相同的部分（如导航、底部、时间等），这时就可以用使用模板来减少代码重复度了。如假设有一个base.html

```
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}默认标题{% endblock %} - 自强学堂</title>
</head>
<body>
 
{% include 'nav.html' %}
 
{% block content %}
<div>这里是默认内容，所有继承自这个模板的，如果不覆盖就显示这里的默认内容。</div>
{% endblock %}
 
{% include 'bottom.html' %}
 
{% include 'tongji.html' %}
 
</body>
</html>
```
block就是模板可以重写的部分，include即包含其他文件内容，所以我们就可以设计如下index.html

```
{% extends 'base.html' %}
 
{% block title %}欢迎光临首页{% endblock %}
 
{% block content %}
{% include 'ad.html' %}
 欢迎光临
{% endblock %}
```
django模板还提供了用于处理传递过来的字典数据的技术，如循环、条件判断、过滤器、常用标签等。如下就是这些技术的一些相关应用。

```
<!-- 双重循环加载表格数据， if判断输出什么数据-->
        <table border="1">
            <tr>
                <td>会议室\时间</td>
                {%for each in info.time%}
                <td>{{each}}</td>
                {%endfor%}
            </tr>
            {% for each in info.rvsdest %}
            <tr>
                <td>{{each.mtrname}}</td>
                {% for ev in each.time%}
                {% if ev == 1%} <td>NO</td> {%else%} <td></td> {%endif%}
                {% endfor%}
            </tr>
            {% endfor%}
        </table>
```
其他的诸如(==, !=, >=, <=, >, <, and, or, not, in, not in)等也可以在模板中使用。

# 五、数据模型
　　Django模型与数据库相关，其相关代码一般写在models.py中。django支持的数据库包括sqlite3，mysql，PostgreSQL等，只需在settings.py中配置即可，同时数据模型提供了丰富的api。如下即可settings.py的配置样例。

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'reverse',
        'USER': 'root',
        'PASSWORD': '******',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```
1. 关于数据模型，首先我们来介绍下field，如下为一个model实例

```
class RoomReverse(models.Model):
    mtno = models.IntegerField(default=0)
    STATE_CHOICES = (('st', 'stale'), ('ing', 'underway'), ('ns', 'notstart'), )
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='ns')
    rvstime = models.DateTimeField(auto_now_add=True)
    mtdate = models.CharField(max_length=100, default=None)
    mtrno = models.ForeignKey(Meetingroom)
    emails = models.TextField(default=None)
    rpemail = models.EmailField(default=None)
    class Meta:
        table_name = 'RoomReverse'
    def __getstr__():
        return str(mtno)
```
其中包括的field有CharField、DateTimeField、IntegerField、TextField、ForeignKey、EmailField等等，其可以实现数据库的主键设置、外键设置，还能实现一对多、多对一、多对多设置等。另一方面，如果觉得django自带的field不够用，还可以使用自己定义的field。

2. 接下来我们来介绍下关于数据库的一些操作。首先是将数据模型同步到数据库操作，命令如下：
```
python manage.py syncdb
# (django1.7.1及以上版本需要使用以下命令)
python manage.py makemigrations
python manage.py migrate
```
对数据进行增删改查操作，一般的方法有：
```
# 新建对象
User.objects.create(name=name,pwd=pwd) #1
# 处理重复，是否创建
User.objects.get_or_create(name=name,pwd=pwd)
# 用save创建
us = User(name=name,pwd=pwd)
us.save()
# 批量创建
User.objects.bulk_create(user_object_list)
User.objects.all()# 获取全部对象
User.objects.all()[:10]# 切片操作
User.objects.get(name=name1)# 获取单个数据，第一个查找到的数据
User.objects.filter(name=name1)# =User.objects.filter(name_exact=name1)获取多个数据
User.objects.filter(name__iexact="abc")# 不区分大小写
User.objects.filter(name__contains="abc")# name包含abc
User.objects.filter(name__icontains="abc")# name不包含abc，且不区分大小写
User.objects.filter(name__regex="^abc")# 正则表达式查询
User.objects.filter(name__iregex="^abc")# 正则表达式不区分大小写
User.objects.exclude(name__contains="abc")# 排除包含abc的对象
User.objects.filter(name__contains="abc").exclude(pwd=111)# name等于abc但pwd不等于111的对象
User.objects.filter(name__in=[])# 相当于将所有name在列表中的对象提取出来
```
 4. 对django中的数据模型，存在一些内部方法来设置或修改模型属性值
```
model._meta.get_fields()    # 获取所有属性
model._meta.get_field_by_name('id')    # 按属性名获取属性
model._meta.get_all_field_names()    # 获取模型所有属性名称
object.__setattr__(attr, data)    # 按属性名设置模型对象对应的属性值
getattr(model, attr)    # 获取模型某一列属性
```
5. 在模型对象中还可以设置虚类来实现继承方法

```
class BaseInfo(models.Model):
    '''
    模板基本信息，包括创建时间、更新时间、更新人、操作人，为虚类
    '''
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    ISVALID = ((CHECKING, 0), (VALID, 1), (INVALID, 2))
    valid = models.IntegerField(choices=ISVALID, default=CHECKING)
    creator = models.CharField(max_length=30, default=None)
    operator = models.CharField(max_length=30, default=None)
    class Meta:
        abstract = True
 
# 单个节点
class NodeData(BaseInfo):
    id = models.AutoField(verbose_name='配置id', primary_key=True, auto_created=True)
    script = models.CharField(verbose_name='中文简述', max_length=50, default=None)
    category = models.CharField(verbose_name='类别', max_length=30, default=None)
    ensuper_class = models.CharField(verbose_name='实体父类', max_length=30, default=None)
    evsuper_class = models.CharField(verbose_name='事件父类', max_length=30, default=None)
    prsuper_class = models.CharField(verbose_name='属性父类', max_length=30, default=None)
    roleid = models.CharField(verbose_name='角色宿主', max_length=30, default=None)
    define_area = models.CharField(verbose_name='定义域', max_length=50, default=None)
    value_area = models.CharField(verbose_name='值域', max_length=50, default=None)
    location_area = models.CharField(verbose_name='位置域', max_length=50, default=None)
    statement = models.CharField(verbose_name='声明', max_length=50, default=None)
    illustrate = models.CharField(verbose_name='举例', max_length=50, default=None)
    combination = models.CharField(verbose_name='中文简述 + 类别', max_length=80, default=None, unique=True)

    class Meta(BaseInfo.Meta):
        # managed = True
         db_table = 'node_data'

    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)
        d = {}
        for attr in fields:
            if isinstance(getattr(self, attr), datetime.datetime):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(getattr(self, attr), datetime.date):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d')
            else:
                d[attr] = getattr(self, attr)
        return json.dumps(d)
```
# 六、基于CBS编程
Class-based views是Django为解决建站过程中的常见的呈现模式而建立的。具有如下几个原则：

- 代码越少越好
- 永远不要重复代码
- View应当只包含呈现逻辑, 不应包括业务逻辑
- 保持view逻辑清晰简单
- 不要将CBVs用作403, 404, 500的错误处理程序
- 保持mixin简单明了

1. 使用django自身的cbvs

    cbvs是可扩展的，但在也增加了复杂度，有时甚至出现8个import引入关系。django自带的view如下表所示：

 

|类名	      | 功能	                    | 例子
|------------ | --------------------------- | ----------------------------------------
|View	      | 基本View, 可以在任何时候使用| 见后面详细介绍
|RedirectView |	重新定向到其他URL	    | 将访问"/log-in/"的用户重新定向到"/login/"
|TemplateView |	显示Django HTML template    | 一般网站中使用模板显示的页
|ListView     |	显示对象列表	            | 文章列表页
|DetailView   | 显示对象详情	            | 文章详细页
|FormView     |	提交From	            | 网站联系我们或emai订阅form
|CreateView   |	创建对象	            | 创建新文章页
|UpdateView   |	更新对象	            | 修改文章页
|DeleteView   |	删除对象	            | 删除文章页
|Generic date views| 显示一段时间内的对象   | 按时间归类的博客|

2. View中基本元素


```
class ModelCreatView(CreateView):
    def __init__(self, model, template_name, context_object_name, success_url, success_msg, fields):
        """
        初始化函数，这里以creatview为例，其他view大同小异
        :param model:  对应要操作的模型
        :param template_name: 对应的模板名称，一般为html页面
        :param context_object_name: 返回给前台的对象
        :param success_url: 操作成功定向地址
        :param success_msg: 返回的成功信息
        :param fields: 需要操作的对应的模型中的属性
        """
        self.model = model 
        self.template_name = template_name
        self.context_object_name = context_object_name
        self.success_url = success_url
        self.success_msg = success_msg
        self.fields = fields

```
3. ListView简介

      listview是一个展示列表的view，返回的是一个template，包含两个关键方法：
```
def get_context_data(self, **kwargs):
def get_queryset(self):
```
      第一个方法返回一个字典给前端，包括分页信息，列表信息，已经其他自定义的信息；第二个方法返回数据库中获取到的数据（可能经过条件迭代），具体实现的实例代码如下：

```
def get_context_data(self, **kwargs):
    """
    用来获取返回给前端页面的dict数据，前端页面可直接通过应用dict中的key来获取value
    :param kwargs:
    :return: context，一个字典类型的数据
    """
    try:
        context = super(ModelListView, self).get_context_data(**kwargs)
        log.debug("get_context_data")
        page_obj = context['page_obj']
        pages = []
        for i in range(1, page_obj.paginator.num_pages + 1):
            if i == 1 or i == page_obj.paginator.num_pages:
                pages.append(i)
            elif i >= page_obj.number - 2 and i <= page_obj.number + 2:
                pages.append(i)
            elif pages[-1] != None:
                pages.append(None)
            else:
                 pass
        context['pages'] = pages
        context['order_type'] = self.order_type
        context['length'] = len(self.object_list)
        if 'pagination_num' not in context:
            context['pagination_num'] = self.paginate_by
        self.echo_search(context)
        if self.model == NodeData:
            context['tree'] = self.get_tree()
        return context
```
4. Mixin实现

     view中如果觉得自带的post、get方法不够好，也可以重写post、get方法，这样就与函数式编程没有什么区别。有时需要前后端异步方式加载数据，就需要使用ajax来完成，这时就可以使用mixin来解决。

     使用mixin可以为class提供额外的功能，但它自身却不能单独使用的类. 在具有多继承能力的编程语言中, mixin可以为类增加额外功能或方法. 在Django中, 我们可以使用mixin为CBVs提供更多的扩展性, 当然在类继承过程中, 我们推荐以下原则:

Django自身提供的View永远在最右边
mixin依次在以上view的左边
mixin永远继承自Python的object类型
推荐mixin库django-braces
```
class ModelValidView(LoginRequiredMixin, AjaxResponseMixin, View):
    def __init__(self, model):
        self.model = model
    def post_ajax(self, request, *args, **kwargs):
        pass
```
# 七、文件上传下载

django中文件上传一般是将文件拷本到服务器上，然后访问服务器上数据；下载文件则可以直接通过访问url完成。

1. 文件上传：

前端：
```
{% include "./_meta.html" %}
{% load staticfiles %}
 

</head>
<body>
<article class="page-container">
        <form action="{% url 'freedomSegger_fileupload' %}" method="post" class="form form-horizontal" id="form-admin-role-add" enctype="multipart/form-data">{% csrf_token %}
                <div class="row cl">
                        <label class="form-label col-xs-4 col-sm-3">模板下载：</label>
                        <div class="formControls col-xs-8 col-sm-9">
                                <a href="TODO">点我下载</a>
                        </div>
                </div>
                <div class="row cl">
                        <label class="form-label col-xs-4 col-sm-3"><span class="c-red">*</span>上传文件：</label>
                        <div class="formControls col-xs-8 col-sm-9">
                                <input type="file" class="input-text"  name="file">
                        </div>
                </div>
                <div class="row cl">
                        <div class="col-xs-8 col-sm-9 col-xs-offset-4 col-sm-offset-3">
                                <button  type="submit" class="btn btn-success radius" id="admin-role-save" name="admin-role-save"><i class="icon-ok"></i> 确定</button>
                        </div>
                </div>
        </form>
</article>

{% include "./_footer.html" %}
 
</body>
</html>
```
后台：

1）工具方法：


```
def handle_uploaded_file(f):
    """
    将上传的文件写入服务器对应目录下
    :param f: 上传文件
    :return: 
    """
    file_name = ""
    try:
        path = "uplodfile" + time.strftime('/%Y/%m/%d/%H/%M/%S/')
        if not os.path.exists(path):
            os.makedirs(path)
            file_name = path + f.name
            destination = open(file_name, 'wb+')
            for chunk in f.chunks():
                destination.write(chunk)
            destination.close()
    except Exception, e:
        print e
    return file_name
```
2）加载上传页面

```
@login_required
def tofileUpload(request):
   return render(request, "knowledge_graph/file_upload.html", )
```
3）上传文件并存入数据库中


```
@login_required
def fileUpload(request):
    success_url = '/knowledgeGraph/'
    failed_url = '/knowledgeGraph/toFileUpload'
    return common_file_upload(request, save_data, success_url, failed_url, MODEL)

def common_file_upload(request, save_data, success_url, failed_url, MODEL):
    """
    批量导入文件
    :param request:
    :param save_data: 针对每个model，在对应的view文件中自定义
    :param success_url: 导入成功时返回的url
    :param failed_url: 导入失败时返回的url
    :param MODEL: 对应的模型
    :return: 返回对应的页面
    """
    file_path = file_upload.handle_uploaded_file(request.FILES['file'])
    try:
        text = list(set(open(file_path).readlines()))
    except Exception as e:
        log.error(MODEL._meta.object_name + " 文件打开错误"+str(e))
        messages.info(request, "文件打开错误"+str(e))
        return HttpResponseRedirect(failed_url)
    except_info, failed = save_data(text, request)
    if failed == 0:
        messages.success(request,"400")
        messages.info(request, "导入成功")
        log.info(MODEL._meta.object_name + " 文件上传成功")
        return HttpResponseRedirect(success_url)
    else:
        log.warning(MODEL._meta.object_name + " " + except_info)
        messages.info(request, except_info)
        return HttpResponseRedirect(failed_url)
```
4）url设置

```
# toFileUpload
url(r'^knowledgeGraph/toFileUpload/$', knowledge_graph.tofileUpload, name="knowledgeGraph_to_fileupload"),
# FileUpload
url(r'^knowledgeGraph/FileUpload/$', knowledge_graph.fileUpload, name="knowledgeGraph_fileupload"),
```
2. 文件下载：

文件下载可通过直接的url访问然后返回response完成，注意此时不能使用ajax异步操作。

1）下载单个文件：

```
def download_file(request,data):
    try:
        write_model(data)
        file_name = "/".join(str(os.path.dirname(__file__)).replace("\\", "/").split("/")[0:-2]) + "/download/" + data
        wrapper = FileWrapper(file(file_name))
        response = HttpResponse(wrapper, content_type="application/octet-stream")
        response['Content-Length'] = os.path.getsize(file_name)
        response['Content-Disposition'] = 'attachment;filename=%s'% data
        messages.info(request, "下载成功")
        log.info("下载成功")
        return response
    except Exception as e:
        messages.warning(request, "下载失败 " + str(e))
        log.warning("下载失败 " + str(e))
        return HttpResponseRedirect("/index/")
```
2）下载多个文件，此时一般情况下使用zip下载，或者使用服务器推送服务（并不知道怎么实现）

这种方法是网上可以轻松找到，但是我实现的时候每次下载的zip包大小都是0kb，通过调试，猜测应该是临时文件问题，无法把临时文件放入压缩包内，导致压缩包大小为空。


```
def download_zipfile(request,data):

    try:
        write_model(model="KnowledgeGraph")
        temp = tempfile.TemporaryFile()
        archive = zipfile.ZipFile(temp, mode='w')
        dir_name = "/".join(str(os.path.dirname(__file__)).replace("\\", "/").split("/")[0:-2]) + "/download/"
        filelist = []
        for root, dirlist, files in os.walk(dir_name):
            for filename in files:
                filelist.append(os.path.join(root, filename))
        for eachfile in filelist:
            destfile = eachfile[len(dir_name):]
            print "Zip file %s..." % destfile
            archive.write(eachfile, destfile)
        archive.close()
        wrapper = FileWrapper(temp)
        response = http.HttpResponse(wrapper, content_type='application/x-zip-compressed')
        response['Content-Disposition'] = 'attachment; filename=model.zip'
        response['Content-Length'] = temp.tell()
        print temp.tell()
        temp.seek(0)
        return response
    except Exception as e:
        print e
        messages.info(request, "下载失败")
        return HttpResponseRedirect("/index/")
```
第二种方法成功实现压缩包下载，这种方法是在github上找到，供参考：


```
def download_zipfile(request,data):
    try:
        dir_name = "/".join(str(os.path.dirname(__file__)).replace("\\", "/").split("/")[0:-2]) + "/download/"
        files = []
        for ev in data:
            input_file = dir_name + ev
            text = open(input_file).readlines()
            #创建临时文件
            output_file = tempfile.NamedTemporaryFile(mode='w+b', prefix='base', suffix='.txt', delete=False)
            #output_file = tempfile.NamedTemporaryFile(mode='w+b', prefix='editor', suffix='.xml', delete=False)
            output_file.writelines(text)
            files.append(output_file.name)
            output_file.close()
        zip_filename = "model.zip"
        s = StringIO.StringIO()
        zf = zipfile.ZipFile(s, "a")
        #将临时文件加入zip包
        for i in range(0, len(files)):
            #设置文件名
            zip_path = os.path.join(data[i])
            zf.write(files[i], zip_path)
        zf.close()
        response = HttpResponse(s.getvalue(), content_type="application/x-zip-compressed")
        response['Content-Disposition'] = 'attachment; filename=%s' % zip_filename
        messages.info(request, "下载成功")
        log.info("下载成功")
        return response
    except Exception as e:
        messages.warning(request, "下载失败 " + str(e))
        log.warning("下载失败 " + str(e))
        return HttpResponseRedirect("/index/")
```