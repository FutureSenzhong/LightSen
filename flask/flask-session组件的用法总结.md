# Flask-session�÷�
## ���
flask-session��flask��ܵ�session���������ԭ��flask����sessionʹ��ǩ��cookie���棬�������֧��session���浽����ط����磺

- redis���������ݵ�һ�ֹ��ߣ�������͡��ǹ�ϵ�����ݿ�
- memcached
- filesystem
- mongodb
- sqlalchmey�������ݴ浽���ݿ������

## ��װ
```
pip3 install flask-session
```
## �洢��ʽ
### redis

```
import redis
from flask import Flask, session
from flask_session import Session

app = Flask(__name__)
app.debug = True
app.secret_key = 'xxxx'

app.config['SESSION_TYPE'] = 'redis'  # session����Ϊredis
app.config['SESSION_PERMANENT'] = False  # �������ΪTrue����ر������session��ʧЧ��
app.config['SESSION_USE_SIGNER'] = False  # �Ƿ�Է��͵��������session��cookieֵ���м���
app.config['SESSION_KEY_PREFIX'] = 'session:'  # ���浽session�е�ֵ��ǰ׺
app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port='6379', password='123123')  # ��������redis������

Session(app)


@app.route('/index')
def index():
    session['k1'] = 'v1'
    return 'xx'


if __name__ == '__main__':
    app.run()
```
### memcached
```

import redis
from flask import Flask, session
from flask_session import Session
import memcache

app = Flask(__name__)
app.debug = True
app.secret_key = 'xxxx'


app.config['SESSION_TYPE'] = 'memcached' # session����Ϊredis
app.config['SESSION_PERMANENT'] = True # �������ΪTrue����ر������session��ʧЧ��
app.config['SESSION_USE_SIGNER'] = False # �Ƿ�Է��͵��������session��cookieֵ���м���
app.config['SESSION_KEY_PREFIX'] = 'session:' # ���浽session�е�ֵ��ǰ׺
app.config['SESSION_MEMCACHED'] = memcache.Client(['10.211.55.4:12000'])


Session(app)


@app.route('/index')
def index():
    session['k1'] = 'v1'
    return 'xx'


if __name__ == '__main__':
    app.run()
```
### filesystem
```
import redis
from flask import Flask, session
from flask_session import Session

app = Flask(__name__)
app.debug = True
app.secret_key = 'xxxx'

app.config['SESSION_TYPE'] = 'filesystem'  # session����Ϊredis
app.config[
    'SESSION_FILE_DIR'] = '/Users/wupeiqi/PycharmProjects/grocery/96.Flask�¿γ�/���/2.flask-session'  # session����Ϊredis
app.config['SESSION_FILE_THRESHOLD'] = 500  # �洢session�ĸ�������������ֵʱ����Ҫ��ʼ����ɾ����
app.config['SESSION_FILE_MODE'] = 384  # �ļ�Ȩ������

app.config['SESSION_PERMANENT'] = True  # �������ΪTrue����ر������session��ʧЧ��
app.config['SESSION_USE_SIGNER'] = False  # �Ƿ�Է��͵��������session��cookieֵ���м���
app.config['SESSION_KEY_PREFIX'] = 'session:'  # ���浽session�е�ֵ��ǰ׺

Session(app)


@app.route('/index')
def index():
    session['k1'] = 'v1'
    session['k2'] = 'v1'
    return 'xx'


if __name__ == '__main__':
    app.run()
```
### mongodb
```
import redis
from flask import Flask, session
from flask_session import Session
import pymongo

app = Flask(__name__)
app.debug = True
app.secret_key = 'xxxx'

app.config['SESSION_TYPE'] = 'mongodb'  # session����Ϊredis

app.config['SESSION_MONGODB'] = pymongo.MongoClient()
app.config['SESSION_MONGODB_DB'] = 'mongo��db���ƣ����ݿ����ƣ�'
app.config['SESSION_MONGODB_COLLECT'] = 'mongo��collect���ƣ������ƣ�'

app.config['SESSION_PERMANENT'] = True  # �������ΪTrue����ر������session��ʧЧ��
app.config['SESSION_USE_SIGNER'] = False  # �Ƿ�Է��͵��������session��cookieֵ���м���
app.config['SESSION_KEY_PREFIX'] = 'session:'  # ���浽session�е�ֵ��ǰ׺

Session(app)


@app.route('/index')
def index():
    session['k1'] = 'v1'
    session['k2'] = 'v1'
    return 'xx'


if __name__ == '__main__':
    app.run()
```
#### mongodb������ʾ����

```
from pymongo import MongoClient

# ��������
conn = MongoClient('47.93.4.198', 27017)

# ѡ�����ݿ�
db = conn['db1']

# ѡ���
posts = db['posts']

post_data = {
    'name': 'alex',
    'age': 18
}

# ���в�������
# result = posts.insert_one(post_data)

# ��ȡһ������
# row = posts.find_one()
# print(row)

# # ��ȡ��������
# rows = posts.find()
# for row in rows:
#     print(row)

# ɾ����������
# rows = posts.delete_many(filter={})
# print(rows)

# ���¶�������
# posts.update({}, {'name': 'wupeiqi'})
```
### sqlalchemy
```
import redis
from flask import Flask, session
from flask_session import Session as FSession
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.secret_key = 'xxxx'

# �������ݿ�����
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123@127.0.0.1:3306/fssa?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# ʵ����SQLAlchemy
db = SQLAlchemy(app)



app.config['SESSION_TYPE'] = 'sqlalchemy'  # session����Ϊsqlalchemy
app.config['SESSION_SQLALCHEMY'] = db # SQLAlchemy����
app.config['SESSION_SQLALCHEMY_TABLE'] = 'session' # sessionҪ����ı�����
app.config['SESSION_PERMANENT'] = True  # �������ΪTrue����ر������session��ʧЧ��
app.config['SESSION_USE_SIGNER'] = False  # �Ƿ�Է��͵��������session��cookieֵ���м���
app.config['SESSION_KEY_PREFIX'] = 'session:'  # ���浽session�е�ֵ��ǰ׺
FSession(app)


@app.route('/index')
def index():

    session['k1'] = 'v1'
    session['k2'] = 'v1'

    return 'xx'


if __name__ == '__main__':
    app.run()
```
## PS: ��д�ô���󣬲�Ҫ�ż����У���Ҫ��ִ�н����ն�ִ��һ���������ݿ������
```
bogon:pro-flask wupeiqi$ python3
Python 3.5.1 (v3.5.1:37a07cee5969, Dec  5 2015, 21:12:44)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from app import db
>>> db.create_all()
>>>
```
## Ӧ�ó����ܽ�:

- ���Ӧ�ó���Ƚ�С������ԭ���ļ���ccokie ����session(����)

- ���Ӧ�ó���Ƚϴ󣬾���redis��flask-session��