# Flask中的session详细用法教程

**Flask session 概念解释：**

session 是基于cookie实现， 保存在服务端的键值对（形式为 {随机字符串：‘xxxxxx’}）, 同时在浏览器中的cookie中也对应一相同的随机字符串，用来再次请求的 时候验证；

注意 ：Flask中的session是存在浏览器中  默认key是session(加密的cookie)， 也可以像Django一样基于上述的方式实现保存在数据库

 

## 一、配置SECRET_KEY

因为flask的session是通过加密之后放到了cookie中。所以有加密就有密钥用于解密，所以，只要用到了flask的session模块就一定要配置“SECRET_KEY”这个全局宏。一般设置为24位的字符。配置方法一般有两种。

  

### 配置方法一：

新建一个config.py的文件配置secret_key 

config.py

    SECRET_KEY = 'XXXXXXXXX'


 然后在主运行文件里面添加config文件里面的内容。 

main.py

    #encoding: utf-8
    from flask import Flask,session
    import config
    app = Flask(__name__)
### 配置方法二：

直接在主运行文件里面配置。配置config的时候也是和操作字典是一样的 
main.py

    encoding: utf-8
     
    from flask import Flask,session
     
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'XXXXX' 或者随机数（os.urandom(24)）
    # 或者
    app.secret_key = 'why would I tell you my secret key?'
    # key值可以使用随机数，或者自定义
## 二、操作session –操作session就如同操作字典！
### 1.设置session
    from flask import Flask,session
    import os
     
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
     
    # 设置session
     @app.route('/')
    def set():
         session['username'] = 'liefyuan' # 设置“字典”键值对（正式开发时候，值需要session.get('user')获取）
         return 'success'
     
     if __name__ == '__main__':
         app.run()


### 2.读取session
 因为session就像字典一样所以，操作它的时候有两种方法：

（1）result = session[‘key’] ：如果内容不存在，将会报异常

（2）result = session.get(‘key’) ：如果内容不存在，将返回None（推荐用法）

所以，使用第二种方法获取session较好。

    from flask import Flask,session
    import os
     
     app = Flask(__name__)
     app.config['SECRET_KEY'] = os.urandom(24)
     
     # 设置session
     @app.route('/')
     def set():
         session['username'] = 'liefyuan' # 设置“字典”键值对
         return 'success'
     
     # 读取session
     @app.route('/get')
     def get():
         # session['username']
         # session.get('username')
         return session.get('username')
     
     if __name__ == '__main__':
         app.run()




### 3.删除session
     # encoding: utf-8
     from flask import Flask,session
     import os
     app = Flask(__name__)
     app.config['SECRET_KEY'] = os.urandom(24)
     
     # 设置session
     @app.route('/')
     def set():
         session['username'] = 'liefyuan'
         return 'success'
         
     # 读取session
     @app.route('/get/')
     def get():
         # session['username']
         # session.get('username')
         return session.get('username')
         
     # 删除session
     @app.route('/delete/')
     def delete():
         print session.get('username')
         session.pop('username',None) 或者 session['username'] = False
         print session.get('username')
         return 'success'
     if __name__ == '__main__':
         app.run()
### 4.清除session中所有数据
     # encoding: utf-8
     
     from flask import Flask,session
     import os
     
     app = Flask(__name__)
     app.config['SECRET_KEY'] = os.urandom(24)
     
     
     # 设置session
     @app.route('/')
     def set():
         session['username'] = 'liefyuan'
         return 'success'
     
     
     # 读取session
     @app.route('/get')
     def get():
         # session['username']
         # session.get('username')
         return session.get('username')
     
     
     # 删除session
     @app.route('/delete')
     def delete():
         print session.get('username')
         session.pop('username') 或者 session['username'] = False
         print session.get('username')
         return 'success'
     
     
     # 清除session中所有数据
     @app.route('/clear')
     def clear():
         print session.get('username')
         # 清除session中所有数据
         session.clear
         print session.get('username')
         return 'success'
     
     if __name__ == '__main__':
         app.run()


##三、设置session的过期时间
 如果没有指定session的过期时间，那么默认是浏览器关闭后就自动结束。session.permanent = True在flask下则可以将有效期延长至一个月。下面有方法可以配置具体多少天的有效期。

如果没有指定session的过期时间，那么默认是浏览器关闭后就自动结束

如果设置了session的permanent属性为True，那么过期时间是31天。

可以通过给app.config设置PERMANENT_SESSION_LIFETIME来更改过期时间，这个值的数据类型是datetime.timedelay类型。

使用的需求：

1.在登录网页界面，下面有一个“记住我”选项，如果点击了则设置session的有效期长一点。就是设置这个！



     # 设置session
     @app.route('/')
     def set():
         session['username'] = 'liefyuan'
         session.permanent = True # 长期有效，一个月的时间有效
         return 'success'


一种更先进的配置有效期的方法：（比如配置7天有效）

1.引入包：from datetime import timedelta

2.配置有效期限：app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7) # 配置7天有效

3.设置：session.permanent = True

    # encoding: utf-8
    from flask import Flask,session
    from datetime import timedelta
    import os 
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7) # 配置7天有效 
    
    # 设置session
    @app.route('/')
    def set():
        session['username'] = 'liefyuan'
        session.permanent = True
        return 'success'