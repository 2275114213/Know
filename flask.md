##### Flask与Django  的对比

```js
django: 优点:大而全   缺点:浪费资源
flask: 优点:小而精,三方组件全  缺点: 稳定性差
```

```js
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
	return "hello"
app.run()
```

##### Response 三剑客

```js
HttpRsonse: return "hello"

from flask import render_template
render : return render_tempalte("login.html")
// 与Django 中的render 使用一致,返回模板由浏览器渲染

from flask import  redirect
redirect: return redirect ("/login")
// 跳转,路由的重定向

# flask 中小儿子
from flask import jsonify
return jsonify({"name":111})   
Content-Type:application/json
// 返回json 标准的字符串

from flask import send_file
return send_file(path)
// 打开文件并返回文件内容(自动识别文件格式)

```

##### request

```js
from flask import request
request.method   请求的方式
# request.form     存放FormData中的数据   to_dict 序列化成字典
# request.args     存放url 中的数据  to_dict 序列化成字典
request.url	     访问的完整路径
request.path     路由地址
request.host     主机地址
# request.values 	 获取formdata  and url 中的数据
[{request.form},{request.args}]
request.json     如果提交时候请求头中的Content-Type:application/json  字典操作
request.data     如果提交时请求头中的Content-Type 无法识别将请求体中的原始数据存放byte
request.cookies	 获取Cookies 中的数据
request.headers  获取请求头中的数据
request.files    序列化文件存储   save()   // filename可以获取文件名
```

##### jinja2

```js
{{}}  引用变量
{%%}  逻辑代码
前端   |safe  或者  后端Markup   安全标签字符串
@app.template_global()
 // 后端不用传,全局可以直接调用
 
 // 自定义过滤器
@app.template_filter()
 
 // 宏, 知道就行不怎么常用
 {%macro create_input(na,ty)%}
 <input type="{{ ty }}" name="{{ na }}">
 {% endmacro %}
 {{ create_input("username","text") }} 
```

##### Session

```js
app.secret_key = "加密字符串" 
// 用于序列化和反序列化 session 信息
// 或者 app.config["SECRET_KEY"] = ''
由于Flask 中默认Session 存放位置 - 客户端的Cookies 中
所以Session 需要加密,用到secret_key
请求进入视图函数 带上cookies 将Session 从cookie序列化出来  通过secret_key 反序列化成字典
Flask-Session
```

##### 多个装饰器修饰一个视图函数

```js
每个视图函数都要进行登录认证
所以使用装饰器
但是多个装饰器同时装饰一个视图函数的时候,会报错
# 方法一
装饰器
from functools import wraps
def wai(func):
	@warps(func)   # 保留原始函数名
	def inner(*args,**kwargs):
        if session.get("user"):
            ret = func(*args,**kwargs)
            return ret
        else:
            return redirect("/login")
    return inner
@app.route('/index')
@wai
def index():
    return render_template("index.html")
# 方式二
def wai(func):
    # @wraps(func)   #  保留原始视图函数名
    def nei(*args,**kwargs):
        if session.get("user"):
            ret = func(*args,**kwargs)
            return ret
        else:
            return redirect("/login")
    return nei
@app.route('/index',endpoint="index")   # 默认视图函数名
@wai
def index():
    print(url_for("index")
    return render_template("index.html",func=func)
@app.route("/index2",endpoint="index2")
@wai
def index2():
    return "index2"
```

##### flask 中的路由

```js
1. endpoint 反向生成url 地址标志  ,默认视图函数名  url_for 反向解析
2. methods  视图函数允许的请求方法
3. 动态路由:
	'/index/<page>'   动态路由路由参数
    def index(page)
4. defaults={"nid":"123"}
5. stricts_slashes=True    是否严格遵循路由地址
6. redirect_to='/login'	   永久重定向
```

##### flask 实例化配置

```js  
1. template_folder = "temp"  # 默认模板路径
2. static_folder = "static"  # 默认静态文件路径static
3. static_url_path = "/static"  # 访问静态文件路由地址  默认是"/" + static_folder
```

##### flask 对象配置

```js
"DEBUG":False   是否开启debug 模式
"TESTING" : Flase  是否开启测试模式
"SECRET_KEY":None  在启用Flask 内置的Session 的时候/开启flash,一定要有他

class FlaskDebug(object):
	DEBUG = True
	SECRET_KEY="DEBUGmoshidesecret_key"
	PERMANENT_SESSION_LIFETIME = 7  // days,Session 的生命周期的默认31天
    SESSION_COOKIE_NAME = "debug_session" // 在cookies 中存放session 加密字符串的名字

app.config.from_object(FlaskDebug)
```



##### flask 蓝图

```js
Blueprint  当成一个不能被启动的 app 
from flask import Blueprint,render_template
sapp = Blueprint("sapp",__name__,template_folder="apptemp",url_prefix="/blue")
@sapp.route('/sapp')
def sappfunc():
	return "haha"


在要使用的主程序里面:
(1) 第一步引入
(2) 第二步注册,在地址栏输入路由即可使用
	app.register_blueprint(addha.s4app)
```

##### flask 特殊装饰器

```js
@app.before_request  // 请求进入视图函数之前
@app.after_request // 响应返回客户端之前
正常情况下: be1- be2 -be3 - af3- af2- af1
异常情况下流程：be1 - af3 - af2 - af1
// 重定义错误页面
@app.errorhandler(404)
	return 
```

##### flask 的上下文

```js
app = Flask(__name__)
app.run() 源码

// 
from werkzeug.serving import run_simple
        try:
            run_simple(host, port, self, **options)
			# 相当于  
		   app() // __call__

def __call__(self, environ, start_response): //self =app=flask(__name__)
        return self.wsgi_app(environ, start_response)

	// environ 请求的原始信息  包括请求头,请求体
def wsgi_app(self, environ, start_response):
    	// self = app = Flash(__name__)
        ctx = self.request_context(environ)
		// ctx = request,session
        error = None
        try:
            try:
                ctx.push()
                response = self.full_dispatch_request()
            except Exception as e:
                error = e
                response = self.handle_exception(e)
            except:
                error = sys.exc_info()[1]
                raise
            return response(environ, start_response)
        finally:
            if self.should_ignore_error(error):
                error = None
            ctx.auto_pop(error)
def request_context(self, environ):  //  self = app= flash(__name__)
        return RequestContext(self, environ)
class RequestContext(object):
    def __init__(self, app, environ, request=None):  // self = RequestContext()
    // app= flash(__name__)  
        self.app = app
        if request is None:
            request = app.request_class(environ)   # 孵化器
        self.request = request
        self.session = None

    def push(self):  //self  =ctx - request,session
        top = _request_ctx_stack.top
		//  _request_ctx_stack=  /{“_local”： {"__storage__":{},"__ident_func__":get_id}}
        if top is not None and top.preserved:
            top.pop(top._preserved_exc)
        app_ctx = _app_ctx_stack.top
        if app_ctx is None or app_ctx.app != self.app:
            app_ctx = self.app.app_context()
            app_ctx.push()
            self._implicit_app_ctx_stack.append(app_ctx)
        else:
            self._implicit_app_ctx_stack.append(None)

        if hasattr(sys, 'exc_clear'):
            sys.exc_clear()
		#  self  = ctx - request,session
        _request_ctx_stack.push(self)
        if self.session is None:
            session_interface = self.app.session_interface
            self.session = session_interface.open_session(
                self.app, self.request
            )

            if self.session is None:
                self.session = session_interface.make_null_session(self.app)
_request_ctx_stack = LocalStack() //  //{“_local”： {"__storage__":{},"__ident_func__":get_ident}}
# 
class LocalStack(object): 
  def __init__(self):
        self._local = Local()   // {"__storage__":{},"__ident_func__":get_ident}
 @property
def top(self):
    try:
   		 return self._local.stack[-1]
    except (AttributeError, IndexError):
    	 return None
ef push(self, obj):
        """Pushes a new item to the stack"""
        rv = getattr(self._local, 'stack', None)
        if rv is None:
            self._local.stack = rv = []
        rv.append(obj)
        return rv
# 
class Local(object):   // {"__storage__":{},"__ident_func__":get_ident}
    __slots__ = ('__storage__', '__ident_func__')

    def __init__(self):
        object.__setattr__(self, '__storage__', {})
        object.__setattr__(self, '__ident_func__', get_ident)
    def __getattr__(self, name):  // name = stack
        try:
            return self.__storage__[self.__ident_func__()][name]
			//  self.__ident_func__()  线程或协程的id  
        except KeyError:
            raise AttributeError(name)

   def __setattr__(self, name, value):
        ident = self.__ident_func__()
        storage = self.__storage__
        try:
            storage[ident][name] = value
        except KeyError:
            storage[ident] = {name: value}


```

##### flask 的下文

```js
request = LocalProxy(partial(_lookup_req_object, 'request'))
def _lookup_req_object(name):     // name = request
    top = _request_ctx_stack.top  // {“_local”： {"__storage__":{"stack":[ctx]},"__ident_func__":get_ident}}
    if top is None:
        raise RuntimeError(_request_ctx_err_msg)
    return getattr(top, name)  // request




```



```js
from werkzeug.serving import run_simple
from werkzeug.wrappers import Response,Request

@Request.application
def app(request):
	return Response('200 ok')
// run_simple 监听函数,服务,端口
run_simple("0.0.0.0",5000,app)
```

##### flask_session

![1547471117071](assets/1547471117071.png)

```js
from flask import Flask,session
// 引入Session
from flask_session import Session
from redis import Redis
app = Flask(__name__)

// 配置Session
app.config["SESSION_TYPE"] = "redis"
app.config["SESSION_REDIS"] = Redis(host='127.0.0.1',port=6379,db=6)
Session(app)
@app.route('/')
def index():
	// 用session   Flask_session  替换了 原始的session
    session["user"] = "value"
    return "haha'
app.run(debug=True)

```

##### Flask _session 的源码解析

```js
# 这是原来的session
// Flask 中的session 需要执行 session_interface
if self.session is None:
// 接口
session_interface = self.app.session_interface
// 打开session
self.session = session_interface.open_session(
    self.app, self.request
)

if self.session is None:
self.session = session_interface.make_null_session(self.app)
```

```js
// 正经代码
app.config["SESSION_TYPE"] = "redis"
app.config["SESSION_REDIS"] = Redis(host='127.0.0.1',port=6379,db=6)
Session(app)
// 源码
class Session(object):
	def __init__(self, app=None):   // app = Flask(__name__)
        self.app = app
        if app is not None:
            self.init_app(app)
    def _get_interface(self, app):
        config = app.config.copy()
		// 如果有值就不用默认值,如果没值就设置
        config.setdefault('SESSION_TYPE', 'null')
        config.setdefault('SESSION_PERMANENT', True)
        config.setdefault('SESSION_USE_SIGNER', False)
        config.setdefault('SESSION_KEY_PREFIX', 'session:')
        config.setdefault('SESSION_REDIS', None)
        config.setdefault('SESSION_MEMCACHED', None)
        config.setdefault('SESSION_FILE_DIR',
                          os.path.join(os.getcwd(), 'flask_session'))
        config.setdefault('SESSION_FILE_THRESHOLD', 500)
        config.setdefault('SESSION_FILE_MODE', 384)
        config.setdefault('SESSION_MONGODB', None)
        config.setdefault('SESSION_MONGODB_DB', 'flask_session')
        config.setdefault('SESSION_MONGODB_COLLECT', 'sessions')
        config.setdefault('SESSION_SQLALCHEMY', None)
        config.setdefault('SESSION_SQLALCHEMY_TABLE', 'sessions')

        if config['SESSION_TYPE'] == 'redis':
            session_interface = RedisSessionInterface(
                config['SESSION_REDIS'], config['SESSION_KEY_PREFIX'],
                config['SESSION_USE_SIGNER'], config['SESSION_PERMANENT'])
        elif config['SESSION_TYPE'] == 'memcached':
            session_interface = MemcachedSessionInterface(
                config['SESSION_MEMCACHED'], config['SESSION_KEY_PREFIX'],
                config['SESSION_USE_SIGNER'], config['SESSION_PERMANENT'])
        elif config['SESSION_TYPE'] == 'filesystem':
            session_interface = FileSystemSessionInterface(
                config['SESSION_FILE_DIR'], config['SESSION_FILE_THRESHOLD'],
                config['SESSION_FILE_MODE'], config['SESSION_KEY_PREFIX'],
                config['SESSION_USE_SIGNER'], config['SESSION_PERMANENT'])
        elif config['SESSION_TYPE'] == 'mongodb':
            session_interface = MongoDBSessionInterface(
                config['SESSION_MONGODB'], config['SESSION_MONGODB_DB'],
                config['SESSION_MONGODB_COLLECT'],
                config['SESSION_KEY_PREFIX'], config['SESSION_USE_SIGNER'],
                config['SESSION_PERMANENT'])
        elif config['SESSION_TYPE'] == 'sqlalchemy':
            session_interface = SqlAlchemySessionInterface(
                app, config['SESSION_SQLALCHEMY'],
                config['SESSION_SQLALCHEMY_TABLE'],
                config['SESSION_KEY_PREFIX'], config['SESSION_USE_SIGNER'],
                config['SESSION_PERMANENT'])
        else:
            session_interface = NullSessionInterface()

        return session_interface





class RedisSessionInterface(SessionInterface):
    serializer = pickle
    session_class = RedisSession

    def __init__(self, redis, key_prefix, use_signer=False, permanent=True):
        if redis is None:
            from redis import Redis
            redis = Redis()
        self.redis = redis
        self.key_prefix = key_prefix
        self.use_signer = use_signer
        self.permanent = permanent
	// 从cookie 里面序列化取出session
    def open_session(self, app, request):
        sid = request.cookies.get(app.session_cookie_name)
        if not sid:
            sid = self._generate_sid()
            return self.session_class(sid=sid, permanent=self.permanent)
        if self.use_signer:
            signer = self._get_signer(app)
            if signer is None:
                return None
            try:
                sid_as_bytes = signer.unsign(sid)
                sid = sid_as_bytes.decode()
            except BadSignature:
                sid = self._generate_sid()
                return self.session_class(sid=sid, permanent=self.permanent)

        if not PY2 and not isinstance(sid, text_type):
            sid = sid.decode('utf-8', 'strict')
        val = self.redis.get(self.key_prefix + sid)
        if val is not None:
            try:
                data = self.serializer.loads(val)
                return self.session_class(data, sid=sid)
            except:
                return self.session_class(sid=sid, permanent=self.permanent)
        return self.session_class(sid=sid, permanent=self.permanent)

    def save_session(self, app, session, response):
        domain = self.get_cookie_domain(app)
        path = self.get_cookie_path(app)
        if not session:
            if session.modified:
                self.redis.delete(self.key_prefix + session.sid)
                response.delete_cookie(app.session_cookie_name,
                                       domain=domain, path=path)
            return

        httponly = self.get_cookie_httponly(app)
        secure = self.get_cookie_secure(app)
        expires = self.get_expiration_time(app, session)
        val = self.serializer.dumps(dict(session))
        self.redis.setex(name=self.key_prefix + session.sid, value=val,
                         time=total_seconds(app.permanent_session_lifetime))
        if self.use_signer:
            session_id = self._get_signer(app).sign(want_bytes(session.sid))
        else:
            session_id = session.sid
        response.set_cookie(app.session_cookie_name, session_id,
                            expires=expires, httponly=httponly,
                            domain=domain, path=path, secure=secure)

```

##### WTForms

```js
from flask import Flask,render_template,request
from wtforms.fields import simple,core
from wtforms import validators
from wtforms import Form
app = Flask(__name__)
class LoginForm(Form):
	username = simple.StringField(
    label = "用户名",
    validators=[validators.DataRequire(message="用户名不能为空")]
    
    )


```

```js
import pymysql
from DBUtils.PooledDB import PooledDB
// 数据库连接方式一
POOL = PooledDB(creator = pymysql)

conn = pymysql.connect(
host='',
user='',
password="123",
database = "POOL",
charset="utf8")


// 数据库连接方式二 
POOL = PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
    mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
    maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
    maxshared=3,  # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
    blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
    maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
    setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
    ping=0,
    # ping MySQL服务端，检查是否服务可用。
    #  如：0 = None = never,
    # 1 = default = whenever it is requested,
    # 2 = when a cursor is created,
    # 4 = when a query is executed,
    # 7 = always
    host="127.0.0.1",
    port=3306,
    user="root",
    password="",
    charset="utf8",
    db="day115"
)

// 如果全参数直接用就行
conn = POOL.connection() # pymysql - conn
# cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
#
# sql = "select * from users WHERE name='jwb' and age=73 "
#
# res = cur.execute(sql)
#
#
# print(cur.fetchall())
#
# conn.close()
```



##### Websocket  握手

```js
1. 什么是Websocket
	是给浏览器新建的一套协议
    协议规定: 创建连接后不断开
    通过'\r\n'分割,让客户端和服务端创建连接后不断开.验证+数据加密
2. 本质
	就是创建一个连接后不断开的socket
    当连接成功后:
		- 客户端(浏览器)会自动向服务端发送消息
         - 服务端接收后,会对数据加密:base64()
		- 构造响应头
		- 发送给客户端
	建立双工通道,进行收发数据
	
```



```js
import socket, base64, hashlib
// 建立socket  服务端 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('127.0.0.1', 9527))
sock.listen(5)
# 获取客户端socket对象
conn, address = sock.accept()
# 获取客户端的【握手】信息
data = conn.recv(1024)
print(data)
"""
b'GET /ws HTTP/1.1\r\n
Host: 127.0.0.1:9527\r\n
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0\r\n
Accept: text/html,application/xhtml+xml,application/xml;q=0.9;q=0.8\r\n
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2\r\n
Accept-Encoding: gzip, deflate\r\n
Sec-WebSocket-Version: 13\r\n
Origin: http://localhost:63342\r\n
Sec-WebSocket-Extensions: permessage-deflate\r\n
Sec-WebSocket-Key: jocLOLLq1BQWp0aZgEWL5A==\r\n
Cookie: session=6f2bab18-2dc4-426a-8f06-de22909b967b\r\n
Connection: keep-alive, Upgrade\r\n
Pragma: no-cache\r\n
Cache-Control: no-cache\r\n
Upgrade: websocket\r\n\r\n'
"""

# magic string为：258EAFA5-E914-47DA-95CA-C5AB0DC85B11
magic_string = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'

def get_headers(data):
    header_dict = {}
    header_str = data.decode("utf8")
    for i in header_str.split("\r\n"):
        if str(i).startswith("Sec-WebSocket-Key"):
            header_dict["Sec-WebSocket-Key"] = i.split(":")[1].strip()
    return header_dict
headers = get_headers(data)  # 提取请求头信息
# 对请求头中的sec-websocket-key进行加密
response_tpl = "HTTP/1.1 101 Switching Protocols\r\n" \
               "Upgrade:websocket\r\n" \
               "Connection: Upgrade\r\n" \
               "Sec-WebSocket-Accept: %s\r\n" \
               "WebSocket-Location: ws://127.0.0.1:9527\r\n\r\n"

value = headers['Sec-WebSocket-Key'] + magic_string
print(value)
ac = base64.b64encode(hashlib.sha1(value.encode('utf-8')).digest())
response_str = response_tpl % (ac.decode('utf-8'))
# 响应【握手】信息
conn.send(response_str.encode("utf8"))

while True:
    msg = conn.recv(8096)
    print(msg)


```

```js
#   Websocket 解密
#b'\x81\x89\xf3\x99\x81-\x15\x05\x01\xcbO\x1be\x97]'    最漂亮
#b'\x81\x85s\x92a\x10\x1b\xf7\r|\x1c'               hello
#b'\x81\x83H\xc0x\xa6y\xf2K'                        123 


// 计算的结果只能是三种  127  126  <=125
hashstr = b'\x81\x85s\x92a\x10\x1b\xf7\r|\x1c'
# b'\x81 \x85s \x92a\x10\x1b\xf7  \r|\x1c' <126
// \x81  标识   \x85s 位运算 <125  3-6 位  \x92a\x10\x1b\xf7  是解密的钥匙
1111111   127   2^0
0111111	  63
0111111	  63
# \x85s = 5
hashstr = b'\x81\xfe\x02\xdc\x8d\xe8-\xb2hm\xa5W5u\xc8:\x16\x0c\x95(kt\x87W\x00b\xc52\x01\x0c\x95\x1fdi\xbeW9A\xcb\x1c\x0f\x07\x91>iS\xa7W)A\xc9\n\x06\x0c\x95;h`\xab]1d\xca)\x07\r\x9a,j~\x9fW1b\xc2\x0e\x01\x0e\x80\x16eG\xb7W\x00Y\xcb2(\r\x80*iR\x8cV4c\xca\x15\x06\x0c\x94-nh\xafU\t^\xc9\x0c\x00\r\xa0\x19iQ\xa6Z\nK\xc9\n\x00\x0e\xaa:iR\xa3W\x0bm\xc2\x0e\x01\r\x92\x12hW\xbaV4c\xc8\x11&\r\x92*eR\x86V7f\xc8\x16\x1b\x00\xad7bT\xa1U\x16~\xc5\r0\r\xa8:hP\xb0V4c\xcb\x1c\x07\x01\xac5bT\xa1T!Z\xcb8(\x0c\x949iR\xa3[\x14s\xc9\n\x06\x0c\x94-nh\xafZ"r\xc8\x1c\x11\r\x912hT\x8dW\x11K\xc8"!\x07\x91>iS\x88W\x08a\xc87\x05\r\x95/di\xbaW3_\xc2\x0e\x01\x0e\xac\x10hT\xb5W2\x7f\xc8\x11&\x0c\x949kX\xb9]1d\xc9\n\x00\r\x83.hN\xa9Z\nB\xc5=?\x00\xbb6bT\xa1W1}\xc8$6\r\x89\x03iQ\xa4]1d\xc9\t(\r\x8c,hW\x8dZ=g\xc9\x0b\x06\x00\x9a\x1diQ\xb2Q\rj\xc8\x1c&\x0c\x95\x1fhR\xb1V5E\xc2\x0e\x01\x0c\x92\x03iP\x97V5h\xc9\x0f\x1e\x07\x91>dq\xb2U0r\xc55*\r\xbd\x14bT\xa1V5e\xc8\x1c\x11\r\x910hx\xa1Q\rj\xc59(\x0e\xb1;iU\xb1W(P\xca8"\x0f\x8a#hg\xa7V5R\xc8\r-\r\xbb6eh\xa8]1d\xc8\x1c\x11\x0c\x96*kt\xa4W\x02P\xc5\x1c7\r\xa8\x04h`\xbcZ8g\xc2\x0e\x01\x0c\x96\x17kp\x80[\x14s\xc9\n\x06\r\x94\x01kp\xa3V4c\xca"\x0b\x07\x91>iP\xa0W#t\xc83\x02\x0f\x8a3bT\xa1V0W\xc84\x08\r\x89$hT\xafT>}\xc9\x0b\x12\x0b\xad0iV\xa0V5E\xce2\x0c\x0c\x93?dk\xa3[\x0eE\xcb&5\x0c\x949nh\xacZ9Q\xca\x17\x03\x0b\xad3ey\x8eW\x08i\xca\x1f\x04\x07\x91>kE\x89U\x17n\xc5;"\r\x83,bT\xa1W2\x7f\xc5+\x1c\r\x92\x12jR\x82]1d\xcb*"\x0c\x96\x17hm\xa5W5u\xca\x1c\r\x0e\xa6&iS\x88[\x0c\x7f\xc4+\x16\x0c\x959nh\xafT\tr\xc9\t(\x0c\x95\x08hF\x86V5E\xc9\x0b\x06\x0c\x979bT\xa1V7c\xcb%-\r\x89\x15hX\xa2]1d\xcb0\x04\x0c\x96\x17hz\x85V4c\xc2\x0e\x01\x0f\xa9\x04hx\xa3T\x1bU\xc5\x13\x01\x07\x91>hW\xa8Z\x0eU\xc5\x11%\x00\x8c\x17dp\xb4T1g\xc2\x0e\x01\x0e\xb1;ka\xadW4W\xca)\x07\x0b\xad0'
# print(chushibiao[1],chushibiao[1]&127)
# print(chushibiao[2:4],chushibiao[4:8])
# 将第二个字节也就是 \x83 第9-16位 进行与127进行位运算
payload = hashstr[1] & 127
print(payload)
if payload == 127:
    extend_payload_len = hashstr[2:10]
    mask = hashstr[10:14]
    decoded = hashstr[14:]
# 当位运算结果等于127时,则第3-10个字节为数据长度
# 第11-14字节为mask 解密所需字符串
# 则数据为第15字节至结尾

if payload == 126:
    extend_payload_len = hashstr[2:4]
    mask = hashstr[4:8]
    decoded = hashstr[8:]
# 当位运算结果等于126时,则第3-4个字节为数据长度
# 第5-8字节为mask 解密所需字符串
# 则数据为第9字节至结尾


if payload <= 125:
    extend_payload_len = None
    mask = hashstr[2:6]
    decoded = hashstr[6:]

# 当位运算结果小于等于125时,则这个数字就是数据的长度
# 第3-6字节为mask 解密所需字符串
# 则数据为第7字节至结尾

str_byte = bytearray()
# b'\x81 \x85s \x92a\x10\x1b \xf7\r|\x1c' <126
for i in range(len(decoded)): # 0  \xf7 ^ \x92a 1 \r ^ \x10 \x1c ^ \x1b
    byte = decoded[i] ^ mask[i % 4]
    str_byte.append(byte)

print(str_byte.decode("utf8"))

#   Websocket 加密

```

##### mui

```js
index.html
# 绑定事件
document.getElementById('pause').addEventListener('tap',function () {
    // 对话框
    mui.toast("你点击我了")
    // tap  监听点击事件    
    d = {user:123} 
    
    //  object  对象如果要在控制台看一定要JSON.stingfy
    console.log(JSON.stringfy(d))
    myplayer.pause();  
    
    
    //  打开新页面
    // 简写mop
    mui.openWindow({
        "url":"new.html",
        "id":"new.html",
        styles:{
            top:"0px"
            bottom:"50px"
            
        }
        //  用来往new.html  页面传递数据
        extras:{
        name:"666"
    }
    });
    

    })


new.html
// 接收index.html 传递过来的参数
mui.plusReady(function(){ 
    // 获取当前页面的详细信息
   var Sdata =  plus.webview.currentWebview();
   console.log(JSON.stringfy(Sdata)) 
})

# 传递事件

index.html
mui.plusReady(function(){
    # 页面加载就执行的写在这
})
document.getElementById('pause').addEventListener('tap',function () {
        
    var  new_page  = plus.webview.getWebviewByID("new.html")
    mui.fire(new_page,"show_alter",{name:"haha"})
    })

new.html
#  整个页面监听
document.addEventListener("show_alter",function(data){
    // 自定义事件里面有一个data.detial 的属性里面有所有的值
    console.log(JSON.stringfy(data.detail).name)
    alter("欢迎光临")
})
```

















##### CBV

##### Mongdb









#### Flask

##### wsgi

```js
web服务网络接口,相当于一套协议,wsgiref
创建一个socket服务端,帮助我们接受请求
```

```js
我们写的程序是在web框架,和 wsgi(socket) 两大基础
django 依赖wsgi 
flask 依赖wsgi  werkzurg
```



```js
pip3 install flask
- 短小精悍, 可扩展性强 的一个Web框架
	- 上下文管理的机制
- wsgi : web服务访问接口, 相当于一套协议, django基于wsgiref模块实现 本质socket服务端, 帮助接受请求,
   	- flask 基于 werkzurg 模块
```

##### werkzurg

```js
 from werkzeug.wrappers import Request, Response

def run(environ,resposne):
    return Response(b'Hello World!')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, run)
    # 如果run的位置是一个对象, 那么会自动执行类里面的__call__
```

##### flask 简单应用

```js
from flask import Flask
app = Flask(__name__)


@app.route("/index")
def index():
    return "hello word"
if __name__ == '__main__':

    app.run()
```



```js
- static 文件夹
	- 111.jpg
<img src='/static/111.jpg'> 可以看见

- staticccc
	- 111.jpg
   <img src='/staticccc/111.jpg'>  看不见 src里面的 staticccc
   和文件夹的名字没有关系
- staticccc
	- 111.jpg
  <img src='/vvvvv/111.jpg'> 
  	# 实例化 Flask 
   app = Flask(__name__,template_folder='tempaltes', static_folder='staticccc', static_url_path='vvvvv')  这个上面的就可以看了

```

##### flask示例:用户登录

```js
from flask import Flask,render_template,request,redirect,session

# app = Flask(__name__,template_folder="templates",static_folder="staticccc",static_url_path='/vvvvv')
app = Flask(__name__,template_folder="templates",static_folder="static")

# 一定要加app.secret_key
app.secret_key = 'asdfasdf'



@app.route('/login',methods=["GET","POST"])
# methods = ['GET','POST']
def login():
    if request.method == 'GET':
        return render_template('login.html')
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    if user == 'oldboy' and pwd == '666':
        session['user'] = user
        return redirect('/index')
    return render_template('login.html',error='用户名或密码错误')
    # return render_template('login.html',**{"error":'用户名或密码错误'})

@app.route('/index')
def index():
    user = session.get('user')
    if not user:
        return redirect('/login')
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

```

##### 配置文件

```js
# 给你一个字符串路径, 可以导入这个模块, 可以找到类, 拿到类里面所有的大写的静态字段
import importlib
path = 'settings.Foo'
p,c = path.rsplit('.', maxsplit=1)
m = importlib.import_module(p)
cls = getattr(m,c)  # 找到了Foo这个类
for key in dir(cls):
	if key.isupper():
    	print(key,getattr(cls, key))
		# DEBUG True
         # TEST True

```

```js
app.config['DEBUG'] = True  # 这么写在应用程序里面不好


app.config.from_object('settings', "Dev") // 直接换里面的类名就可以

# 创建一个settings.py
class Base(object):
	xx = 123
    SESSION_COOKIE_NAME = 'session'
    SESSION_COOKIE_DOMAIN = None
    SESSION_COOKIE_PATH = None
    PERMANENT_SESSION_LIFETIME = timedelta(days=31),
    SESSION_REFRESH_EACH_REQUEST=True # 在最后访问时间加上时间限制
class Dev(Base):
	DEBUG = False  //上线环境
class Pro(Base):  
	DEBUG = True   //开发环境

```



##### 路由系统

```js
@app.route("/index", methods=["GET", "POST"], endpoint='index') # endpoint相当于django 里面的name, 默认是函数名
def index():
    print(url_for("index"))  # /index 相当于django 里面的reverse
    return "hello word"


- 动态路由匹配(不支持正则)
@app.route("/index/<int:nid>", methods=["GET", "POST"]) # endpoint相当于django 里面的name
def index(nid):
    print(nid)
     # /index 相当于django 里面的reverse
    return "hello word"

@app.route('/user/<username>')
@app.route('/post/<int:post_id>')
@app.route('/post/<float:post_id>')
@app.route('/post/<path:path>')
@app.route('/login', methods=['GET', 'POST'])

- 含参数的动态路由
	@app.route("/index/<int:nid>", methods=["GET", "POST"],endpoint='index') # endpoint相当于django 里面的name
def index(nid):
    print(nid)
    print(url_for("index", nid=nid))  #/index/1

- endpoint  
- url_for()
- 动态路由
```

```js
def auth(func):
    def inner(*args, **kwargs):
    	   print('前')
            ret = func(*args, **kwargs)
		   print('后')
            return  ret
    return inner
@auth
def index():
	print(index)
print(index())

@auth
def detail():
	print(index)
print(detail())
# 装饰之前 index 就是index , index.__name__  index,
# 装饰之后 就是执行inner    index.__name__   inner  里面的func就是index
						detail.__name__  inner 里面的func就是detail
                        
   
                        
import functools
def auth(func):
	@functools.wraps(func)
    def inner(*args, **kwargs):
    	   print('前')
            ret = func(*args, **kwargs)
		   print('后')
            return  ret
    return inner

变成自己名字了
```

```js
endpoint 如果不指定默认函数名, 
# 装饰器: 比较少的个数中    
# 装饰器的先后顺序, 先执行下面的
每个视图函数都要进行登录认证
所以使用装饰器
但是多个装饰器同时装饰一个视图函数的时候,会报错
# 方法一
装饰器
from functools import wraps
def wai(func):
	@warps(func)   # 保留原始函数名
	def inner(*args,**kwargs):
        if session.get("user"):
            ret = func(*args,**kwargs)
            return ret
        else:
            return redirect("/login")
    return inner
@app.route('/index')
@wai
def index():
    return render_template("index.html")
# 方式二
def wai(func):
    # @wraps(func)   #  保留原始视图函数名
    def nei(*args,**kwargs):
        if session.get("user"):
            ret = func(*args,**kwargs)
            return ret
        else:
            return redirect("/login")
    return nei
@app.route('/index',endpoint="index")   # 默认视图函数名
@wai
def index():
    print(url_for("index")
    return render_template("index.html",func=func)
@app.route("/index2",endpoint="index2")
@wai
def index2():
    return "index2"
```

##### Flask 中正则URL的实现

```js
@app.route('<URL>') 中URL显示支持 string, int, path, uuid, arry6种类型, 隐式支持正则
第一步:写正则类, 继承BaseConverter, 将匹配到的值设置为regex 的值,
from werkzeug.routing import BaseConverter
class RegexUrl(BaseConverter):
    def __init__(self, url_map, *args):
        super(RegexUrl, self).__init__(url_map)
        self.regex = args[0]
        print('hh',args)  # hh ('[a-z]{3}',)
	
     # 调用to_python (正则匹配的结果)  方法 
     def to_python(self, value):
                    """
                    路由匹配时，匹配成功后传递给视图函数中参数的值
                    :param value: 
                    :return: 
                    """
                    return int(value)

	def to_url(self, value):
    	"""
        使用url_for反向生成URL时，传递的参数经过该方法处理，返回的值用于生成URL中的参数
        :param value: 
        :return: 
        """
        val = super(RegexConverter, self).to_url(value)
        return val
# re 
app.url_map.converters['re'] = RegexUrl

@app.route('/regex/<re("[a-z]{3}"):id>')
def regex111(id):
    return 'id:%s'%id





```

![1553319586924](assets/1553319586924.png)

##### 视图

```js
FBV:
```



##### 请求相关

```js
 # 请求相关信息
 # request.method
 # request.args
 # request.form
 # request.values
 # request.cookies
 # request.headers
 request.path
 request.full_path
 request.script_root
 request.url
 request.base_url
 request.url_root
 request.host_url
 request.host
 request.files
 obj = request.files['the_file_name']
 obj.save('/var/www/uploads/' + secure_filename(f.filename))

# 响应体
 return "字符串"
 return render_template('html模板路径',**{})
 return redirect('/index.html')
 return jsonify(dic)
 return send_file()

# 自定义响应头cookie , headers
response = make_response(render_template('index.html'))
response是flask.wrappers.Response类型
response.delete_cookie('key')
response.set_cookie('key', 'value')
response.headers['X-Something'] = 'A value'
return response
```



##### 响应

##### 模板渲染

```js
 {% for k,v in  stu_dic.items() %} # item() 加括号 django 里面不加括号
                <tr>
                    <td>{{k}}</td>
                    <td>{{v.name }}</td>
                    <td>{{v.age}}</td>
                    <td>{{v.gender}}</td>
					// <td>{{v["gender"]</td>	
					// <td>{{v.get('gender','默认')</td>	
                    <td>
                        <a href="/detail/{{k}}">查看详细</a>
                        |
                        <a href="/delete/{{k}}">删除</a>

                    </td>
                </tr>
            {% endfor %}
```



```js
def func(arg):
	return arg+1
def tpl():

    context = {
        'users':['longtai','liusong','zhoahuhu'],
        // 后端处理
        'txt':Markup("<input type='text' />"),
        'func':func
    }

    return render_template('tpl.html',**context)


<body>
        {{users.0}}  // 都可以
        {{users[0]}}
		{{txt|safe}}  // 前端
		// {{func}} django 自动加括号,flask不行
		{{func(6)}}
        
</body>
```

```js
# 假设现在十个页面都要是用func, 函数
@app.template_global()
def func(args):
	return args

# 也不用传递, 自定义过滤器
@app.template_filter()
def db(a1, a2, a3):
    return a1 + a2 + a3


<body>
        {{func(1)}}  
        {{ 1|db(2,3) }}</body>
{{ 1|db(2,3) }}  //可以放在if 后面做条件
{%if  1|db(2,3) %}
	<div>666</div>
{%else%}
	<div>666</div>
 {%endif%}

{{func(1)}}  // 不可以放在if 后面做条件
```

```js
# 回顾django
simple_tag
1. 在app 下创建独立的templatetags 目录, 
2. 在templtetags 目录下创建tag.py ,任意名
3. 在tag.py
from django import template
register = template.Libraty()
@ register.simple_tag
def func(a1, a2):
	return 返回值
4. 网页中调用
{%load tag%}
{%func(1,2)%}
# 缺点不能作为IF条件
优点: 参数可以有多个
	



```

##### 模板继承

```js
# 主页面 layout.html
<h3>哈哈</h3>
{% block content%}
{%endblock%}
```

```js
想要继承<h3>哈哈</h3>, 自己需要定制业务
{%extend 'layout.html'%}
{%block content%}
{%endblock%}
```

```js
# 小的页面 form.html
<h2>haha</h2>


# 大的页面里需要下的=页面
{%include 'form.html' %}
```

```js
- 宏定义
#定义完了是不显示的,
{% macro ccc(name, type='text', value='')%}
	<input type='{{ type }}' name='{{name}}' value='{{ value
}}'>
{% endmacro %}

# 调用
{{ccc('na')}}
```

##### session

```js

当请求到来时, flask 读取cookie 中session对应的值, 将改值解密并反序列化成字典, 放入内存中以便视图函数使用

设置：session['username'] ＝ 'xxx'
删除：session.pop('username', None)

@app.route('/page2')
def page2():
    # print(session['uuuuu'])
    # del session['uuuuu']
    # session.pop('uuuuu')
    return "Session"

当请求结束时, flask会读取内存中的字典的值, 进行序列化+加密. 写入到用户cookie中

```

##### Session源码

![1552455549224](assets/1552455549224.png)

![1552455611502](assets/1552455611502.png)

```js
from werkzeug.wrappers import Request, Response

def run(environ,resposne):
    return Response(b'Hello World!')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, run)  # werkzeug 第三个参数自动加(), 如果是对象,就调用类里面__call__方法

app.run()
app.__call__
app.wgsi_app 
app.request_class
app.session_interface

	里面实例化了一个 ctx = self.request_context(environ)对象   // ctx = RequestContext(self, environ)
```



```js
from flask import Flask
app = Flask(__name__)


@app.route("/index")
def index():
    return "hello word"
if __name__ == '__main__':

    app.run()


#点击run()
 def __call__(self, environ, start_response):
       return self.wsgi_app(environ, start_response)
'''
environ 是请求相关的所有数据(由WSGI做了初步封装)
start_response 用于设置响应的相关数据
'''	
def wsgi_app(self, environ, start_response):
      
        ctx = self.request_context(environ)
	   	# ctx=RequestContext(self, environ)
        	class RequestContext(self,environ):
       		    def __init__(self, app, environ, request=None):
                    self.app = app
                    if request is None:
                        request = app.request_class(environ)
					  # cts.request = Request()
                    self.request = request
                    self.url_adapter = app.create_url_adapter(self.request)
                    self.flashes = None
                    self.session = None	
					#cts.session = None
       # self 是app对象, environ请求相关的原始数据
'''
1. 获取environ并对其进行再次封装
2. 从environ中获取名称为session 的cookie,解密,反序列化
3. 两个东西放到'某个神奇'的地方
'''	
	   error = None
        try:
            try:
            	'
			将ctx放到空调上
             执行 SecureCookieSessionInterface.open_session,去cookie中获取值并给ctx.session 赋值
				'
                ctx.push()
	'''
	if self.session is None:
            session_interface = self.app.session_interface
		   # obj = SecureCookieSessionInterface() 	
            self.session = session_interface.open_session(
                self.app, self.request
            )
			'''
				 def open_session(self, app, request):
                            s = self.get_signing_serializer(app)
                            if s is None:
                                return None
                            val = request.cookies.get(app.session_cookie_name)
                            if not val:
                                return self.session_class()
                            max_age = total_seconds(app.permanent_session_lifetime)
                            try:
                                data = s.loads(val, max_age=max_age)
                                return self.session_class(data)
                            except BadSignature:
                                return self.session_class()

			
			'''	
            if self.session is None:
                self.session = session_interface.make_null_session(self.app)

	'''
			   #4.执行视图函数
                #5. '某个神奇'获取session, 加密, 序列化 -> 写进cookie
                response = self.full_dispatch_request()
            except Exception as e:
                error = e
                response = self.handle_exception(e)
            except:
                error = sys.exc_info()[1]
                raise
            return response(environ, start_response)
        finally:
            if self.should_ignore_error(error):
                error = None
			'''
			1.'某个神奇的地方获取session,加密,序列化 ->写cookies'
			2.清空'某个神奇的地方'			
'''
            ctx.auto_pop(error)


open_session()  # 请求进来的时候执行open_session
save_session()  # 请求走的是佛执行save_session
```



##### 闪现

```js
flash
@app.route('/page1')
def page1():
    # session['uuuuu'] = 123
    flash('临时数据存储','error')# 可以分类
    flash('sdfsdf234234','error')
    flash('adasdfasdf','info')

    return "Session"

@app.route('/page2')
def page2():
    # print(session['uuuuu'])
    # del session['uuuuu']
    # session.pop('uuuuu')
    print(get_flashed_messages(category_filter=['error']))
    return "Session"

闪现: 在session中存储一个数据, 读取时通过pop将数据移除,

from flask import get_flashed_messages


```



##### 中间件

```js
from flask import Flask

app = Flask(__name__)


@app.route('/index')
def index():
    print('index')
    return "Index"

# 基本不会用
class Middleware(object):
    def __init__(self,old):
        self.old = old
	# app.run()的时候并不会执行__call__方法,但是请求来的时候会执行
    def __call__(self, *args, **kwargs):
        ret = self.old(*args, **kwargs)
        return ret


if __name__ == '__main__':
    app.wsgi_app = Middleware(app.wsgi_app)
    app.run() # run点进去
# 源码    
from werkzeug.serving import run_simple

        try:
            run_simple(host, port, self, **options)

# 对象() 调用__call__方法
```

```js
- call 方法什么时候触发:
	有请求来的时候
- 在请求来之前在请求来之后做一些事
	- 方法一:修改源码
```

































##### 蓝图

```js

# 目标: 给开发者提供的目录结构
	其他: 自定义模板路径,静态文件
          某一类url添加前缀
          给一类url添加before_request
    	 


# user.py
from flask import Blueprint
uc = Blueprint('uc',__name__,template_folder='xxxxx')
# 在全局的templates 里面找, 如果没有在去自己的app 下面找
@uc.route('/list')
def list():
	return 'List'











# 
app.register_blueprint(uc,url_prefix='/xxxx' )  # 可以加版本
```



##### 特殊装饰器

```js
@app.before_request  // 请求进入视图函数之前
def func():
	return 'haha'  // 如果有返回值就直接返回
# 限制有些页面可以登录之后可以看, 批量操作
@app.before_request
def xxxxxx():
    if request.path == '/login':
        return None  // None 也可以向下执行

    if session.get('user'):
        return None

    return redirect('/login')
@app.after_request // 响应返回客户端之前

// 重定义错误页面
@app.errorhandler(404)
	return 

正常情况下: be1- be2 -be3 - af3- af2- af1
异常情况下流程：be1 - af3 - af2 - af1
```



##### 装饰器

```js
# 装饰器形成的过程
# 装饰器的作用
# 原则: 开放封闭原则 开放对功能扩展的开放 封闭:对代码的修改
# 装饰器的固定模式

# 语法糖:  @ 装饰器函数名
          # 被装饰函数
          

# 不想修改函数的调用方式,但是还想再原来的函数前后添加功能
# timer 就是一个装饰器函数,只是对一个函数,有一些装饰作用
def timer(f):   # 装饰器函数
    def inner(*args,**kwargs):
        # (1,2) /(1)
        # l = [1,2,3]  *l  1,2,3
        print(args)   #  (1, 2)
        print(*args)  #   1 2
        start = time.time()  # 表示从1970 年 1 月 1 号 到现在多少秒
        f(*args)   # 被装饰函数
        end = time.time()
        print(end-start)
    return inner

# 原则: 开放封闭原则
# 开放: 对扩展是开放的
# 封闭: 对修改是封闭的
```



- 无参数的装饰器

  ```js
  def outer():
      def inner():
          return "inner"
      return inner()
  
  ret = outer()
  print(ret)
  # inner
  
  
  
  def outer():
      def inner():
          return "inner"
      inner()
  
  ret = outer()  # 因为outer 没有返回值
  print(ret)
  # None
  ```


```js
import functools
def wrapper(func):
	# 如果不加, 伪造的不彻底, 函数的原信息没有被复制
	@functools.wraps(func)
	def inner(*args, **kwargs):
    	ret = func(*args, **kwargs)
		return ret
	return inner

@wrapper   # index = wrapper(index)
def index():
	pass
    
index()  # 执行它就是执行里面的inner
```

```js
'''
1. 先执行app.route('/index'),返回decorator
2. @decorator
'''

@app.route('/index')
def index():
    print('index')
    return "Index"
```



- 带参数的装饰器

```js
# 带参数的装饰器



# 现在有500个函数, 都需要计算时间, 但是后来不需要了, 就要一个一个删除麻烦,所以引入FLAGE
import time
# FLAGE = True  # 调用时间
FLAGE = False
def timer_outer(flag):
    def timer(func):
        def inner(*args,**kwargs):
            if flag:
                start = time.time()
                ret = func(*args,**kwargs)
                end = time.time()
                print(start-end)
                return ret
            ret = func(*args, **kwargs)
            return ret
        return inner
    return timer


# timer = timer_out(FLAGE)
# 直接@timer

# 为了闭包
@timer_outer(FLAGE)   # wahahah = timer(wahahah)=inner,但是现在FLAGE传进去了, 所以需要多定义一层函数 先执行timer_outer(FLAGE) 返回timer
def wahaha():
    time.sleep(0.1)
    print("wahahahhaha")

@timer_outer(FLAGE)  # 加上括号就是调用 timer_outer(FLAGE) ,然后返回的值加上@ @timer
def erguotou():         # wahaha= timer(wahaha)
    time.sleep(1)
    print("erguotoutotuot")


wahaha()
erguotou()

```

- 多个装饰器装饰一个函数

![1552023829755](assets/1552023829755.png)



```js
# 多个装饰器装饰一个函数
def wrapper1(func):  # func -->f
    def inner1():
        print('wrapper1 ,before func')
        func()  # f()
        print('wrapper1 ,after func')
    return inner1

def wrapper2(func): # func --> inner1
    def inner2():
        print('wrapper2 ,before func')
        func()  # inner1()
        print('wrapper2 ,after func')
    return inner2

@wrapper2    # f = wrapper(inner1) = inner2
@wrapper1  # f = wrapper1（f） = inner1
def f():
    print('in f')
f() # ---> inner2()
```

##### 路由+视图

```js
# 方式一
def index():
	return 'index'
app.add_url_rule('/xxx',None,index)

# 方式二
@app.route('/index',endpoint='haha')
def index():
	return "index"

#注意事项:
	- endpoint一定不要重名

参数:
	strict_slashes=None,        对URL最后的 / 符号是否严格要求，
                                        如：
                                            @app.route('/index',strict_slashes=False)，
                                                访问 http://www.xx.com/index/ 或 h													ttp://www.xx.com/index均可
                                            @app.route('/index',strict_slashes=True)
                                                仅访问 http://www.xx.com/index 


	redirect_to=None,           重定向到指定地址
                                        如：
                                            @app.route('/index/<int:nid>', 															redirect_to='/home/<nid>')
                                            或
                                            def func(adapter, nid):
                                                return "/home/888"
                                            @app.route('/index/<int:nid>', 															redirect_to=func)
```

##### FBV与CBV

```js
from flask import Flask,views
app = Flask(__name__)
class UserView(views.MethodView):
	methods=['GET']# 写了之后只可以GET
	decorators = [] #加装饰器, 内部自动执行
	def get(self,*args,**kwargs):
    	return  'GET'

	def post(self,*args,**kwargs):
    	return "POST"
app.add_url_rule('/user',None,UserView.as_view("uuuu"))
```



##### 前戏

```js
# 偏函数,帮助开发者自动传递参数
import functools
def index(a1,a2):
    return a1+a2
new_func = functools.partial(index,6666)  # 将666 当第一个参数传递
ret = new_func(88)
print(ret)


# 主动调用其他类成员
class Base:
    def func(self):
        print('haha')
class Foo(Base):
    def func(self):
        # 方式一 主动执行父类的方法 根据__mro__ 来找的
        super(Foo,self).func()

        # 方式二 主动执行Base 方法
        Base.func(self)  # 类.func() 需要传参数
        print('hehe')
obj = Foo()
obj.func()



# 
class Foo(object):
    def __init__(self):
        object.__setattr__(self,'storage',{})  # 执行了__setattr__
    def __setattr__(self, key, value):
        print(key,value)
        if key in self.storage:
            print(self.storage)
    def __getattr__(self, item):
        print(item)

obj = Foo()
obj.xx='yuan'
print(obj.storage) 
```



##### super

![1552493921514](assets/1552493921514.png)



·

```js
 - 如何获取一个线程的唯一标识   threading.get_ident() 
{
    2131:
}
```

```js
ctx = self.request_context(environ)  # 实例化一个RequestContext(self, environ)实例对象

class RequestContext(object):
    def __init__(self, app, environ, request=None):
        self.app = app
        if request is None:
            request = app.request_class(environ)
        self.request = request
        self.url_adapter = app.create_url_adapter(self.request)
        self.flashes = None
        self.session = None
# 将包含了request/session 的对象放到空调(根据线程或协程id 放进去的)
# 将空调看成一个大字典:

{
    1231 : {ctx:ctx 对象},
    1232 : {ctx:ctx 对象},
    1233 : {ctx:ctx 对象},
    1234 : {ctx:ctx 对象},
    1235 : {ctx:ctx 对象},
    
    
}



```













```js
1. 请求进来先执行一个__call__ 方法, 
    
    
2. 执行wsgi_app  

def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

3.  ctx 对象实例化一个request, 
def wsgi_app:
	 ctx = self.request_context(environ)
4. def  request_context():
		return RequestContext(self, environ)

5. class RequestContext(object):
        def __init__(self, app, environ, request=None):
                self.app = app
                if request is None:
				   #  request = Request(environ)
                     #  environ 请求原始的相关信息
                    request = app.request_class(environ)
                self.request = request
                self.url_adapter = app.create_url_adapter(self.request)
                self.flashes = None
                self.session = None

6. 此时的ctx 对象里面包含request ,session

向下执行:
 	ctx.push()  # ctx 是 重新封装后的request 对象
    
    def push(self):
    	# 此时的self 是ctx 对象, 里面有重新封装的request ,session 
		#  _request_ctx_stack帮助我们维护一个__starage__={}
        
        _request_ctx_stack.push(self) 
		// _request_ctx_stack = {'__storage__':{}, '__ident_func__':get_ident}


		执行完push 以后: {'__storage__':{123:{'stack':[ctx(request,session)]}}, '__ident_func__':get_ident}
		# 全局变量:
		_request_ctx_stack = LocalStack()   // 这句话执行完在内存里面创建了一个'__storage__' 的 空{}
		
class LocalStack:
    	def __init__(self):
        	self._local = Local()  ///

class Local:
 	def __init__(self):
        object.__setattr__(self, '__storage__', {})
        object.__setattr__(self, '__ident_func__', get_ident)



def push(self, obj):
"""Pushes a new item to the stack"""
    rv = getattr(self._local, 'stack', None)
    if rv is None:
        self._local.stack = rv = []
        rv.append(obj)
    return rv



// local() 对象 就相当于是空调, LocalStark() 是刘松, 我帮助你们往空调里面放东西 
// 文大爷(wsgi)拿了水瓶, 交给早已(ctx)做了封装,一push ,把自己的东西交给刘松, 早已交给刘松LocalStark(), 刘松拿着东西放回去, 过好处理session, 还得找刘松

    


a . 文大爷: wsgi
b . 执行里面的__call__
c . 执行wsgi.app()  早已
d . 里面ctx 对象 重新封装了request,session
7 . ctx.push()  // 交给刘松  LocalStack() 对象, 把ctx对象添加到local中 
d 空调: Local  : '__storage__' = {1234:[ctx(request,session)]}



视图函数:
	@app.route('/index')
	def index():
    	ctx = _request_ctx_stack.top
		print(ctx) # 执行top的时候取出ctx RquestContext对象,里面 拿出
         print(ctx.request) #  拿出请求的所有数据 Request()
         print(ctx.request.environ)
```



![1553312273816](assets/1553312273816.png)



![1553313225205](assets/1553313225205.png)

SQLAlchemy:	

```js
ORM 框架: 对象关系映射, 

          表  --- ----  类

	  列   ------- 字段

	  类对象 ------ 记录

	 约束的实例化对象----约束关系

	作用: 帮助我们使用类和对象快速实现数据库的操作



数据库:
	- 原生
        - Mysqldb
        - pymysql
    - ORM 框架()
    	- SQLAlchemy	
```

```js
- 创建数据表:
# 1. 导入官宣基础模型
from sqlalchemy.ext.declarative import declarative_base

# 2. 实例化官宣模型, -Base  ORM 模型
Base = declarative_base()  
class User(Base):
	__tablename__ = 'user'
	from sqlalchemy import Column, Integer, String
    id = Column(Inter, primary_key=True, authincrement=True)
	name = Column(String(32),index=True)

# 3.去连接数据库  创建数据引擎
from sqlalchemy import crate_engine

# 创建数据库
engine = create_engine("mysql+pymysql://root:DragonFire@127.0.0.1:3306/dragon?charset=utf8")



# Base 自动检索所有继承Base的ORM 对象 并且创建所有的数据表


Base.metadata.create_all(engine)

```

```js
# 和django 的 orm 不一样,需要创建数据库连接:
from sqlalchemy.orm import sessionmaker
 # 创建数据表操作对象 sessionmaker
DB_session = sessionmaker(engine)
db_session = DB_session()	


# 增加:
单条增加:  db_session.add(对象)
多条增加:  db_session.add_all([对象1, 对象2])

# 查询:
db_session.query(Users).all()
db_session.query(Users).filter(Users.id>4)  # 返回的是一个列表

# 删除
db_session.query(Users).filter(Users.id>4).delete()

# 修改
db_session.query(Users).filter(Users.id>4).update({Users.id:19})
session.query(Users).filter(Users.id == 4).update({'name':Users.name+"DSB"},synchronize_session=False)
17 # 数据库中 增 改 删 都是操作,也就是说执行以上三种操作的时候一定要commit
18 db_session.commit()
19 db_session.close()
```



​	