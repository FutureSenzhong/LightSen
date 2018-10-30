# һ������django�ļ��
����django��һ��python�е�web��ܣ��������õ�ʹ��������û�����HTML, CSS, JavaScript�ȷ����֪ʶ�������ص���Ҫ�����ڼ������棺ǿ������ݿ⣨�������apiͬʱ֧��ִ��sql��䣩���Դ�ǿ��ĺ�̨���ܡ�����������ʽƥ����ַ������ҳ������ģ������ͼһһ��Ӧ��������ơ����ʻ�֧�ֵȵȡ�

����django�ʺ������ݿ�����ֻ��Ҫ�������뼴�ɽ���������webӦ�á������Ѿ�����˿�����վ����ೣ�����룬���Լ����˴�����ظ��ȡ�Ok�����������ȿ���django����Ҫ�ļ���ɡ���Ҫ�ļ��������¼���py�ļ���

django������Ҫpy�ļ�
�ļ�	����
urls.py	��ַ��ڣ�������views�ж��ڵĺ���
models.py	�����ݿ������أ�����Ӧ������ģ��
views.py	�����û��������󣬴�urls�ж�Ӧ������ͨ����Ⱦtemplates����ҳ��ʾ����
settings.py	������ã��������ݿ����ã��ʼ����ã���̬�ļ����õ�
forms.py	�����û�����������ύ�ı�������
admin.py	��̨���룬�󲿷������
# ������������
�����������һ���־Ͳ������������Ͻ̳̺ܶࡣ�����������£�
```

# �½�django project
django-admin.py startproject project-name
# �½�django app����
django-admin.py startapp app-name (or) python manage.py startapp app-name
# ͬ�����ݿ�
python manage.py syncdb
# (django1.7.1�����ϰ汾��Ҫʹ����������)
python manage.py makemigrations
python manage.py migrate
# ����django��Ŀ������portĬ��Ϊ8000
python manage.py runserver port
# ex: python manage.py runserver 8080
# ������ݿ�
python manage.py flush
# ������������Ա
python manage.py createsuperuser
# �޸Ĺ���Ա����
python manage.py changepassword username
# ��������
python manage.py dumpdata appname > appname.json
# ��������
python manage.py loaddata appname.json
# ����django��Ŀ�����ն�
python manage.py shell
# �������ݿ�������
python manage.py dbshell
```
# ������ͼ
���������Ѿ�֪��views�еĺ�������urls�е���ַ��Ӧ�ģ�������������һ���򵥵�ʵ����ʾ��

1. ���Ƚ�Ӧ��������ӵ�settings.py��
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
2. ��views�ж�����ͼ����
```
def test(request):
    return render(request, 'test.html')
���ﷵ�صĽ���ж��֣��䱾�ʷ��صĽ����HttpResponse���������������

return HttpResponse("hello world")
return render_to_response('test.html', '')
return HttpResponseRedirect('/index/')
����render��render_to_respose��һ���ģ�ֻ��render����Ҫ˵��ResponseContext��render_to_respose����Ҫcoding������render�����᷵��һ���ֵ䣬����ģ���д������ݡ�

return render_to_response('checkmt.html', {'info': info})
return render(request, 'day2.html', {'info': info})
```
3. ������urls.py�еĵ�ַ
```
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login),
    url(r'^index/$', views.index, name="index"),   
)
```
����urls�����ж��ַ�ʽ��������Բ鿴�ٷ��ĵ�������Ҫ���������֣�������ʽ��ʽ����ַ+views������ͬʱ��ַ�л����Դ��ݲ�����

# �ġ�ģ��
����ģ����ͨ��views������Ⱦ�ģ���ʵ����һ��html��ҳ��һ�����app�µ�templates�У�����ģ��ʱdjango���Զ�Ѱ�ҡ���ô����һ���������ж��Ӧ�ã�ÿ��Ӧ�õ�templates�ж���һ��index.html��Ȼ��ֱ�ӵ���render(request, 'index.html')�ܲ����ҵ��أ����ǿ��ܻ������������̽����djangoģ����һ��ơ�djangoģ����ҹ�������ÿ��app��templates�ļ����в��ң������ǵ�ǰapp�е�templates����������ЩӦ�õ�templates�ļ����б��в��ҵ�index.htmlģ��ʱֹͣ������˵���ܳ��ִ����������û���ҵ��򷵻�һ��templates not found����

��������������������һ�¹���ģ������Ӧ�á�һ��أ���վ�ж�����һЩģ����ƣ����ܶ���ҳ���кܶ���ͬ�Ĳ��֣��絼�����ײ���ʱ��ȣ�����ʱ�Ϳ�����ʹ��ģ�������ٴ����ظ����ˡ��������һ��base.html

```
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Ĭ�ϱ���{% endblock %} - ��ǿѧ��</title>
</head>
<body>
 
{% include 'nav.html' %}
 
{% block content %}
<div>������Ĭ�����ݣ����м̳������ģ��ģ���������Ǿ���ʾ�����Ĭ�����ݡ�</div>
{% endblock %}
 
{% include 'bottom.html' %}
 
{% include 'tongji.html' %}
 
</body>
</html>
```
block����ģ�������д�Ĳ��֣�include�����������ļ����ݣ��������ǾͿ����������index.html

```
{% extends 'base.html' %}
 
{% block title %}��ӭ������ҳ{% endblock %}
 
{% block content %}
{% include 'ad.html' %}
 ��ӭ����
{% endblock %}
```
djangoģ�廹�ṩ�����ڴ����ݹ������ֵ����ݵļ�������ѭ���������жϡ������������ñ�ǩ�ȡ����¾�����Щ������һЩ���Ӧ�á�

```
<!-- ˫��ѭ�����ر�����ݣ� if�ж����ʲô����-->
        <table border="1">
            <tr>
                <td>������\ʱ��</td>
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
����������(==, !=, >=, <=, >, <, and, or, not, in, not in)��Ҳ������ģ����ʹ�á�

# �塢����ģ��
����Djangoģ�������ݿ���أ�����ش���һ��д��models.py�С�django֧�ֵ����ݿ����sqlite3��mysql��PostgreSQL�ȣ�ֻ����settings.py�����ü��ɣ�ͬʱ����ģ���ṩ�˷ḻ��api�����¼���settings.py������������

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
1. ��������ģ�ͣ�����������������field������Ϊһ��modelʵ��

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
���а�����field��CharField��DateTimeField��IntegerField��TextField��ForeignKey��EmailField�ȵȣ������ʵ�����ݿ���������á�������ã�����ʵ��һ�Զࡢ���һ����Զ����õȡ���һ���棬�������django�Դ���field�����ã�������ʹ���Լ������field��

2. �����������������¹������ݿ��һЩ�����������ǽ�����ģ��ͬ�������ݿ�������������£�
```
python manage.py syncdb
# (django1.7.1�����ϰ汾��Ҫʹ����������)
python manage.py makemigrations
python manage.py migrate
```
�����ݽ�����ɾ�Ĳ������һ��ķ����У�
```
# �½�����
User.objects.create(name=name,pwd=pwd) #1
# �����ظ����Ƿ񴴽�
User.objects.get_or_create(name=name,pwd=pwd)
# ��save����
us = User(name=name,pwd=pwd)
us.save()
# ��������
User.objects.bulk_create(user_object_list)
User.objects.all()# ��ȡȫ������
User.objects.all()[:10]# ��Ƭ����
User.objects.get(name=name1)# ��ȡ�������ݣ���һ�����ҵ�������
User.objects.filter(name=name1)# =User.objects.filter(name_exact=name1)��ȡ�������
User.objects.filter(name__iexact="abc")# �����ִ�Сд
User.objects.filter(name__contains="abc")# name����abc
User.objects.filter(name__icontains="abc")# name������abc���Ҳ����ִ�Сд
User.objects.filter(name__regex="^abc")# ������ʽ��ѯ
User.objects.filter(name__iregex="^abc")# ������ʽ�����ִ�Сд
User.objects.exclude(name__contains="abc")# �ų�����abc�Ķ���
User.objects.filter(name__contains="abc").exclude(pwd=111)# name����abc��pwd������111�Ķ���
User.objects.filter(name__in=[])# �൱�ڽ�����name���б��еĶ�����ȡ����
```
 4. ��django�е�����ģ�ͣ�����һЩ�ڲ����������û��޸�ģ������ֵ
```
model._meta.get_fields()    # ��ȡ��������
model._meta.get_field_by_name('id')    # ����������ȡ����
model._meta.get_all_field_names()    # ��ȡģ��������������
object.__setattr__(attr, data)    # ������������ģ�Ͷ����Ӧ������ֵ
getattr(model, attr)    # ��ȡģ��ĳһ������
```
5. ��ģ�Ͷ����л���������������ʵ�ּ̳з���

```
class BaseInfo(models.Model):
    '''
    ģ�������Ϣ����������ʱ�䡢����ʱ�䡢�����ˡ������ˣ�Ϊ����
    '''
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    ISVALID = ((CHECKING, 0), (VALID, 1), (INVALID, 2))
    valid = models.IntegerField(choices=ISVALID, default=CHECKING)
    creator = models.CharField(max_length=30, default=None)
    operator = models.CharField(max_length=30, default=None)
    class Meta:
        abstract = True
 
# �����ڵ�
class NodeData(BaseInfo):
    id = models.AutoField(verbose_name='����id', primary_key=True, auto_created=True)
    script = models.CharField(verbose_name='���ļ���', max_length=50, default=None)
    category = models.CharField(verbose_name='���', max_length=30, default=None)
    ensuper_class = models.CharField(verbose_name='ʵ�常��', max_length=30, default=None)
    evsuper_class = models.CharField(verbose_name='�¼�����', max_length=30, default=None)
    prsuper_class = models.CharField(verbose_name='���Ը���', max_length=30, default=None)
    roleid = models.CharField(verbose_name='��ɫ����', max_length=30, default=None)
    define_area = models.CharField(verbose_name='������', max_length=50, default=None)
    value_area = models.CharField(verbose_name='ֵ��', max_length=50, default=None)
    location_area = models.CharField(verbose_name='λ����', max_length=50, default=None)
    statement = models.CharField(verbose_name='����', max_length=50, default=None)
    illustrate = models.CharField(verbose_name='����', max_length=50, default=None)
    combination = models.CharField(verbose_name='���ļ��� + ���', max_length=80, default=None, unique=True)

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
# ��������CBS���
Class-based views��DjangoΪ�����վ�����еĳ����ĳ���ģʽ�������ġ��������¼���ԭ��

- ����Խ��Խ��
- ��Զ��Ҫ�ظ�����
- ViewӦ��ֻ���������߼�, ��Ӧ����ҵ���߼�
- ����view�߼�������
- ��Ҫ��CBVs����403, 404, 500�Ĵ��������
- ����mixin������

1. ʹ��django�����cbvs

    cbvs�ǿ���չ�ģ�����Ҳ�����˸��Ӷȣ���ʱ��������8��import�����ϵ��django�Դ���view���±���ʾ��

 

|����	      | ����	                    | ����
|------------ | --------------------------- | ----------------------------------------
|View	      | ����View, �������κ�ʱ��ʹ��| ��������ϸ����
|RedirectView |	���¶�������URL	    | ������"/log-in/"���û����¶���"/login/"
|TemplateView |	��ʾDjango HTML template    | һ����վ��ʹ��ģ����ʾ��ҳ
|ListView     |	��ʾ�����б�	            | �����б�ҳ
|DetailView   | ��ʾ��������	            | ������ϸҳ
|FormView     |	�ύFrom	            | ��վ��ϵ���ǻ�emai����form
|CreateView   |	��������	            | ����������ҳ
|UpdateView   |	���¶���	            | �޸�����ҳ
|DeleteView   |	ɾ������	            | ɾ������ҳ
|Generic date views| ��ʾһ��ʱ���ڵĶ���   | ��ʱ�����Ĳ���|

2. View�л���Ԫ��


```
class ModelCreatView(CreateView):
    def __init__(self, model, template_name, context_object_name, success_url, success_msg, fields):
        """
        ��ʼ��������������creatviewΪ��������view��ͬС��
        :param model:  ��ӦҪ������ģ��
        :param template_name: ��Ӧ��ģ�����ƣ�һ��Ϊhtmlҳ��
        :param context_object_name: ���ظ�ǰ̨�Ķ���
        :param success_url: �����ɹ������ַ
        :param success_msg: ���صĳɹ���Ϣ
        :param fields: ��Ҫ�����Ķ�Ӧ��ģ���е�����
        """
        self.model = model 
        self.template_name = template_name
        self.context_object_name = context_object_name
        self.success_url = success_url
        self.success_msg = success_msg
        self.fields = fields

```
3. ListView���

      listview��һ��չʾ�б��view�����ص���һ��template�����������ؼ�������
```
def get_context_data(self, **kwargs):
def get_queryset(self):
```
      ��һ����������һ���ֵ��ǰ�ˣ�������ҳ��Ϣ���б���Ϣ���Ѿ������Զ������Ϣ���ڶ��������������ݿ��л�ȡ�������ݣ����ܾ�������������������ʵ�ֵ�ʵ���������£�

```
def get_context_data(self, **kwargs):
    """
    ������ȡ���ظ�ǰ��ҳ���dict���ݣ�ǰ��ҳ���ֱ��ͨ��Ӧ��dict�е�key����ȡvalue
    :param kwargs:
    :return: context��һ���ֵ����͵�����
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
4. Mixinʵ��

     view����������Դ���post��get���������ã�Ҳ������дpost��get�������������뺯��ʽ���û��ʲô������ʱ��Ҫǰ����첽��ʽ�������ݣ�����Ҫʹ��ajax����ɣ���ʱ�Ϳ���ʹ��mixin�������

     ʹ��mixin����Ϊclass�ṩ����Ĺ��ܣ���������ȴ���ܵ���ʹ�õ���. �ھ��ж�̳������ı��������, mixin����Ϊ�����Ӷ��⹦�ܻ򷽷�. ��Django��, ���ǿ���ʹ��mixinΪCBVs�ṩ�������չ��, ��Ȼ����̳й�����, �����Ƽ�����ԭ��:

Django�����ṩ��View��Զ�����ұ�
mixin����������view�����
mixin��Զ�̳���Python��object����
�Ƽ�mixin��django-braces
```
class ModelValidView(LoginRequiredMixin, AjaxResponseMixin, View):
    def __init__(self, model):
        self.model = model
    def post_ajax(self, request, *args, **kwargs):
        pass
```
# �ߡ��ļ��ϴ�����

django���ļ��ϴ�һ���ǽ��ļ��������������ϣ�Ȼ����ʷ����������ݣ������ļ������ֱ��ͨ������url��ɡ�

1. �ļ��ϴ���

ǰ�ˣ�
```
{% include "./_meta.html" %}
{% load staticfiles %}
 

</head>
<body>
<article class="page-container">
        <form action="{% url 'freedomSegger_fileupload' %}" method="post" class="form form-horizontal" id="form-admin-role-add" enctype="multipart/form-data">{% csrf_token %}
                <div class="row cl">
                        <label class="form-label col-xs-4 col-sm-3">ģ�����أ�</label>
                        <div class="formControls col-xs-8 col-sm-9">
                                <a href="TODO">��������</a>
                        </div>
                </div>
                <div class="row cl">
                        <label class="form-label col-xs-4 col-sm-3"><span class="c-red">*</span>�ϴ��ļ���</label>
                        <div class="formControls col-xs-8 col-sm-9">
                                <input type="file" class="input-text"  name="file">
                        </div>
                </div>
                <div class="row cl">
                        <div class="col-xs-8 col-sm-9 col-xs-offset-4 col-sm-offset-3">
                                <button  type="submit" class="btn btn-success radius" id="admin-role-save" name="admin-role-save"><i class="icon-ok"></i> ȷ��</button>
                        </div>
                </div>
        </form>
</article>

{% include "./_footer.html" %}
 
</body>
</html>
```
��̨��

1�����߷�����


```
def handle_uploaded_file(f):
    """
    ���ϴ����ļ�д���������ӦĿ¼��
    :param f: �ϴ��ļ�
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
2�������ϴ�ҳ��

```
@login_required
def tofileUpload(request):
   return render(request, "knowledge_graph/file_upload.html", )
```
3���ϴ��ļ����������ݿ���


```
@login_required
def fileUpload(request):
    success_url = '/knowledgeGraph/'
    failed_url = '/knowledgeGraph/toFileUpload'
    return common_file_upload(request, save_data, success_url, failed_url, MODEL)

def common_file_upload(request, save_data, success_url, failed_url, MODEL):
    """
    ���������ļ�
    :param request:
    :param save_data: ���ÿ��model���ڶ�Ӧ��view�ļ����Զ���
    :param success_url: ����ɹ�ʱ���ص�url
    :param failed_url: ����ʧ��ʱ���ص�url
    :param MODEL: ��Ӧ��ģ��
    :return: ���ض�Ӧ��ҳ��
    """
    file_path = file_upload.handle_uploaded_file(request.FILES['file'])
    try:
        text = list(set(open(file_path).readlines()))
    except Exception as e:
        log.error(MODEL._meta.object_name + " �ļ��򿪴���"+str(e))
        messages.info(request, "�ļ��򿪴���"+str(e))
        return HttpResponseRedirect(failed_url)
    except_info, failed = save_data(text, request)
    if failed == 0:
        messages.success(request,"400")
        messages.info(request, "����ɹ�")
        log.info(MODEL._meta.object_name + " �ļ��ϴ��ɹ�")
        return HttpResponseRedirect(success_url)
    else:
        log.warning(MODEL._meta.object_name + " " + except_info)
        messages.info(request, except_info)
        return HttpResponseRedirect(failed_url)
```
4��url����

```
# toFileUpload
url(r'^knowledgeGraph/toFileUpload/$', knowledge_graph.tofileUpload, name="knowledgeGraph_to_fileupload"),
# FileUpload
url(r'^knowledgeGraph/FileUpload/$', knowledge_graph.fileUpload, name="knowledgeGraph_fileupload"),
```
2. �ļ����أ�

�ļ����ؿ�ͨ��ֱ�ӵ�url����Ȼ�󷵻�response��ɣ�ע���ʱ����ʹ��ajax�첽������

1�����ص����ļ���

```
def download_file(request,data):
    try:
        write_model(data)
        file_name = "/".join(str(os.path.dirname(__file__)).replace("\\", "/").split("/")[0:-2]) + "/download/" + data
        wrapper = FileWrapper(file(file_name))
        response = HttpResponse(wrapper, content_type="application/octet-stream")
        response['Content-Length'] = os.path.getsize(file_name)
        response['Content-Disposition'] = 'attachment;filename=%s'% data
        messages.info(request, "���سɹ�")
        log.info("���سɹ�")
        return response
    except Exception as e:
        messages.warning(request, "����ʧ�� " + str(e))
        log.warning("����ʧ�� " + str(e))
        return HttpResponseRedirect("/index/")
```
2�����ض���ļ�����ʱһ�������ʹ��zip���أ�����ʹ�÷��������ͷ��񣨲���֪����ôʵ�֣�

���ַ��������Ͽ��������ҵ���������ʵ�ֵ�ʱ��ÿ�����ص�zip����С����0kb��ͨ�����ԣ��²�Ӧ������ʱ�ļ����⣬�޷�����ʱ�ļ�����ѹ�����ڣ�����ѹ������СΪ�ա�


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
        messages.info(request, "����ʧ��")
        return HttpResponseRedirect("/index/")
```
�ڶ��ַ����ɹ�ʵ��ѹ�������أ����ַ�������github���ҵ������ο���


```
def download_zipfile(request,data):
    try:
        dir_name = "/".join(str(os.path.dirname(__file__)).replace("\\", "/").split("/")[0:-2]) + "/download/"
        files = []
        for ev in data:
            input_file = dir_name + ev
            text = open(input_file).readlines()
            #������ʱ�ļ�
            output_file = tempfile.NamedTemporaryFile(mode='w+b', prefix='base', suffix='.txt', delete=False)
            #output_file = tempfile.NamedTemporaryFile(mode='w+b', prefix='editor', suffix='.xml', delete=False)
            output_file.writelines(text)
            files.append(output_file.name)
            output_file.close()
        zip_filename = "model.zip"
        s = StringIO.StringIO()
        zf = zipfile.ZipFile(s, "a")
        #����ʱ�ļ�����zip��
        for i in range(0, len(files)):
            #�����ļ���
            zip_path = os.path.join(data[i])
            zf.write(files[i], zip_path)
        zf.close()
        response = HttpResponse(s.getvalue(), content_type="application/x-zip-compressed")
        response['Content-Disposition'] = 'attachment; filename=%s' % zip_filename
        messages.info(request, "���سɹ�")
        log.info("���سɹ�")
        return response
    except Exception as e:
        messages.warning(request, "����ʧ�� " + str(e))
        log.warning("����ʧ�� " + str(e))
        return HttpResponseRedirect("/index/")
```