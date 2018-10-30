# DjangoͼƬ�ϴ������أ���ҳ����־����ʵ��

## �ļ�Ŀ¼�ṹչʾ

![](./img/DjangoĿ¼�ṹ.png)

## һ.DjangoͼƬ���ϴ�������ʵ��

### ��app�ļ����е�models.py�д���ģ��
```
from django.db import models


# �����ݿ���ֻ����ͼƬ��·����ͼƬ���ļ�ʵ�ʱ�����app���ļ����е�mediaý���ļ�����
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=150)
    img = models.ImageField(upload_to='article')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'article'
```
### ��app�ļ����е�views.py�б�д���ܴ���
```
# �ϴ����ص���ͼƬ��������
def add_article(request):
    if request.method == 'GET':
        return render(request, 'articles.html')

    if request.method == 'POST':
        # ��ȡ����
        img = request.FILES.get('img')
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        # ����ͼƬ����
        Article.objects.create(img=img, title=title, desc=desc)

        return HttpResponse('����ͼƬ�ɹ�')

# ����ҳ����ʾͼƬ
def show_article(request, id):
    if request.method == 'GET':
	# ��ȡһ��ͼƬ
        article = Article.objects.get(pk=id)

        return render(request, 'show_articles.html', {'article': article})
```
### �ڹ����ļ����е�templates�ļ��д���articles.html��show_articles.html
```
# �ϴ�ͼƬҳ��
{% extends 'base.html' %}

{% block title %}
    �ϴ�ͼƬ
{% endblock %}


{% block content %}
    # enctype ���Թ涨�ڷ��͵�������֮ǰӦ����ζԱ����ݽ��б���,������ֵ��ʾ�����ַ����룬��ʹ�ð����ļ��ϴ��ؼ��ı�ʱ������ʹ�ø�ֵ
    <form action="" method="post" enctype="multipart/form-data">
        ���⣺<input type="text" name="title">
        ������<input type="text" name="desc">
        ͼƬ��<input type="file" name="img">
        <input type="submit" value="�ϴ�ͼƬ">
    </form>
{% endblock %}
```
```
# ��ʾͼƬҳ��
{% extends 'base.html' %}

{% block title %}
    ͼƬչʾ
{% endblock %}



{% block content %}
    ���⣺{{ article.title }}<br>
    ͼƬ��<img src="/media/{{article.img}}" alt=""><br>
    ������{{ article.desc }}<br>
{% endblock %}
```
### ��setting�����þ�̬�ļ�����mediaý���ļ���

```
# ����ý���ļ�·��
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
### �ڹ��̰���urls.py������mediaý���ļ��з���·��

```
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
```
### ��app�ļ�����urls.py����ӷ���·��
```
urlpatterns = [
    url(r'^add_article/', views.add_article, name='add_article'),
    url(r'^show_article/(\d+)', views.show_article, name='show_article'),
]
```

## ��.��ҳ����ʵ��
### app�ļ�����views.py����
```
# ��ҳ
def articles(request):
    if request.method == 'GET':
        # Ĭ���õ�һҳ
        page = request.GET.get('page', 1)
        # ��ѯ�����е�������Ϣ
        articles = Article.objects.all()
        # ִ�з�ҳ��ʾ����,���������½��з�ҳÿһҳ10������
        paginator = Paginator(articles,10)
        # ��ȡ��һҳ��������Ϣ
        arts = paginator.page(page)


        return render(request, 'arts.html', {'arts': arts})
```

### ģ�������articles.html
```
{% extends 'base.html' %}

{% block title %}
    ͼƬչʾ
{% endblock %}



{% block content %}
    {% for art in arts %}
    ���⣺{{ art.title }}<br>
    ͼƬ��<img src="/media/{{art.img}}">
    ������{{ art.desc }}<br>
    {% endfor %}
    <p>
	# ҳ����ʾarts.paginator.page_range������ʾ���µ�ҳ��
	# �������ҳ�õ���ҳ	
        {% if arts.has_previous  %}
	# �����ת����ҳ
            <a href="{% url 'user:articles' %}?page={{arts.previous_page_number}}">��һҳ</a>
        {% endif %}
	# ҳ����ʾarts.paginator.page_range������ʾ���µ�ҳ��
        {% for i in arts.paginator.page_range %}
            <a href="{% url 'user:articles' %}?page={{i}}">{{i}}</a>
        {% endfor %}
	# ������õ���һҳ
        {% if arts.has_next  %}
	# �����ת����һҳ
            <a href="{% url 'user:articles' %}?page={{arts.next_page_number}}">��һҳ</a>
        {% endif %}

    </p>

{% endblock %}

```
### app��urls����
```
urlpatterns = [
    url(r'^articles/', views.articles, name='articles'),
]
```

## ��.��־�ļ�����
### ��middleware �������м����ȡ��������Ӧ����־
```
# ��־�ļ����м��
class LoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # ��¼��ǰ������ʷ�������ʱ�䣬����Ĳ����������ݵ�
        request.init_time = time.time()
        request.init_body = request.body
        return None

    def process_response(self, request, response):
        try:
            # ��¼������Ӧ��ʱ��ͷ��ʷ�������ʱ�������ص�״̬��
            times = time.time() - request.init_time
            # ��Ӧ״̬��
            code = response.status_code
            # ��Ӧ����
            res_body = response.content
            # ��������
            req_body = request.init_body

            # ��־��Ϣ
            msg = '%s %s %s %s' % (times, code, res_body, req_body)
            # д����־
            logging.info(msg)
        except Exception as e:
            logging.critical('log error, Exception: %s' % e)
            
        return response
```

###  setting�е���־����
```
LOGGING = {
    # ������ 1
    'version': 1,
    # ������־��false��ʾ������
    'disable_existing_loggers': False,
    # ָ��д�뵽��־�ļ����е���־��ʽ
    'formatters': {
        'default': {
            'format': '%(name)s %(asctime)s %(message)s'
        }
    },
    'handlers': {
        'console': {
	    # ���մ���ȼ�
            'level': 'INFO',
	    # ����·��
            'filename': '%s/log.txt' % os.path.join(BASE_DIR, 'logs'),
            'formatter': 'default',
            # ��־�ļ�����5M�Զ�����
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 5 * 1024 * 1024,
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    },
}
```

