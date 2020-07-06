Flask 智能游戏项目

```js
1. 采集数据 - 喜马拉雅
2. 点播幼教内容  儿童 古诗  国学 自然 百科
3. 家长App App 与玩具之间有
```

```js
mli  图文列表
msl  图文列表  和  轮播图
mpop  弹出框的样式
```

```js
今日内容
1. 玩具收取消息

玩具的ws
@ws_app.route("/toy/<toy_id>")
def toy(toy_id):
    user_socket = request.environ.get("wsgi.websocket")  # type: WebSocket

    if user_socket:
        user_socket_dict[toy_id] = user_socket
    print(user_socket_dict)
    while 1:
        user_msg = user_socket.receive()
        print(user_msg)  # {to_user:"toy_id",music:"asdf.mp3"}
        msg_dict = json.loads(user_msg)
        print(msg_dict.get("to_user"))
        toy_socket = user_socket_dict.get(msg_dict.get("to_user"))
        toy_socket.send(user_msg
		
def _get_msg_tixing(to_user,from_user):
	from settingd import MongoDB
	to_user_info = MongoDB.toys.find_one({"_id":to_user})
	for friend in to_user_info.get('friend_list')
		if freieng.get("frieng_id") == from_user;
			
			
		else:
			就不是好友
			
			
创建ai 文件夹 进行语音合成



get_set  里面  app
uploader
# 消息存储记录  chats

formdata 里面 f放user_id


chat  
toy.html 里面  接收未读消息,

把消息存进redis里面   ,app 端的消息是在上传完成的时候传输的时候传输的,写进redis


获取最后一条数据
# 蓝图  chat


#玩具主动发起消息
发起指令
reco_ai

后端  ai_upload


baidu.py  里面进行图灵合成
if  "发消息"  in res:
	
	
发送给通讯录的消息
点播歌曲
询问天气

# 获取聊天记录如bug
获取最后一条, 不管是自己发的指令的还是 

# 展现聊天列表






HTTP 连接 请求+响应 = 断开
	服务器不知道你是谁 - http  session -无记忆状态

http 聊天室
	长连接:
		websocket
		玉帝按电话了,并且把电话号码放在了传达室了
		服务端以及客户端节省极大的资源
		能保证数据实时性




		
		
		
		
		
		
		
app  页面展示		
		
	index 创建子页面
	mui({
	subpages:[{
	url:main.html  # 子页面html 地址 ,支持本地地址 和网络地址
	id:main.html   # 子页面标志
	styles:{
		top :   // 子页面顶部位置
		bottom:  // 子页面底部的位置
		
	}
	extras:{}  // 额外扩展参数 ,可以向子页面传递值
	}]
	})
		
	
	打开新页面
	
	mui.openWindow({
		url:player.html,
		id:player.html,
		styles:{
		},
		extras:{
		# 自定义扩展字段,可以用来处理页面间传值
		}
		createNew:false  # 是否重复创建同样id 的webview, 默认为false;不重复创建,直接显示 ,其实就是刷新
	})	
		
	注意:
		createNew   是否重新创建相同的id 的 webview(当前页面)
		
		为性能优化, 避免app 中重复创建webview, 
			createNew 参数为 true 则不重复判断,每次都创建新的webview
			createNew  参数为 false 则先查找当前App 中是否已存在同样id 的webview,若存在则直接显示,否则新创建并根据show 参数执行显示逻辑
			
		plusReady  事件仅在webview 首次创建时触发,使用mui.openWindow  方法多次打开存在的同样id 的 webview时, 是不会重复触发plusReady 事件的;因此若业务逻辑写在你plusReady  事件中,可能会出现执行结果和与预期不一致的情况
		
	
	监听自定义事件
	window.addEventListenner("send_str",function(event){
	  #  通过event.detail 可获得传过来的参数内容
	
	})
		
	触发自定义事件
	mui.fire()   方法可以触发目标窗口的自定义事件		
	mui.fire(target,event,data)
		target 需窗子的目标webview 
		event 自定义事件名称
		data  json  格式的数据
```

##### userinfo 页面注册 登录功能 自动登录功能

```js
1. 如过没登录过显示登录页面 ,可以注册
// 注册里面的gender 特殊
<div class='mui-input-row mui-radio mui-left'>
	<label>我是妈妈</label>
	<input name = "gender" type='radio' checkd  value='1'>
</div>
<div class='mui-input-row mui-radio mui-left'>
	<label>我是爸爸</label>
	<input name = "gender" type='radio' checkd  value='2'>
</div>
document.getElementById('reg_btn').addEventListener('tap',
                                                    function () {
    var gender_list = document.getElementsByName("gender");
    var gender = null;
    for (var i = 0; i < gender_list.length; i++) {
	       		if(gender_list[i].checked){
	       			gender = gender_list[i].value;
	       		}
	       } 
    
    
},"json")
2. 如果注册成功回到login 页面 进行登陆 ,登录的时候往仓库里面添加'user'
// 如果登录成功





3. 如果之前登录过,  自动登录

4. 退出登录, 
5. 登录成功之后userinfo 显示管理我的玩具 可以点击打开新的页面toy_manage
```

##### setttings

```js
import pymongo
client = pymongo.MongoClient(host = "127.0.0.1",port=27017)
// 连接的数据库
MONGO_DB = client["yuan"]
```









##### mian  页面显示歌曲列表

```js
1. 页面显示歌曲列表
mli 图片在左,页面展示
<ul class="mui-table-view" id="content_list"></ul>
	# 如果后面使用plus  了 ,前面一定要 mui.PlusReady()
	(1) 向后端获取数据,页面加载就获取数据,所以写在plusReady()
		main.html  里面展示点播的列表
        <ul class="mui-table-view" id="content_list"></ul>
        mui.plusReady(function(){
            mui.post(window.serv + '/content_list',{
            },function(data){
                for(var i=0; i<data.data.length;i++){
                create_item(data.data[i]);
                }
            },'json')
        })
        function  create_item(content){
            var li = document.createElement("li");
                  li.className ="mui-table-view-cell mui-media";
                  var a = document.createElement("a");
                  //  因为是创建的
                  a.onclick = function(){
                        mui.openWindow({
                            url:"player.html",
                            id:"player.html",
                            extras:content
                        })
                  }
                  var img = document.createElement("img");
                  img.className ="mui-media-object mui-pull-left";
                  img.src = window.serv_image + content.cover;
                  var div = document.createElement("div");
                  div.className="mui-media-body";
                  div.innerText = content.title;
                  var p = document.createElement("p");
                  p.className="mui-ellipsis";
                  p.innerText=content.intro; 
                  li.appendChild(a);
                  a.appendChild(img);
                  a.appendChild(div);
                  div.appendChild(p);  
                  document.getElementById("content_list").appendChild(li);
        }

	后端
    import flask import Blueprint,jsonify
    from settings import MONGO_DB,RET
	content = Blueprint("content",__name__)
	@content.route("/content_list",methods = ["POST"])
		// 获取所有数据,但是里面的Objectid  不可以序列化,需要转化成字符串来返回json
		// 返回一个列表, 列表里面是一个一个字典
	    res=list(MONGO_DB.content.find({}))
		for index,item in   enmuerate(res):
        	// 里面每个字典  _id  需要变成字符串
        	res[index]["_id"] = str(item.get("_id"))

		RET["code"] = 0
		RET["msg"] = '查询幼教内容'
		RET["data"] = res
		return jsonify(RET)

2. 点击进去 到 player 页面, 然后可以播放,暂停,停止 并且发送给玩具
		var a = document.createElement("a");
                  //  因为是创建的
                  a.onclick = function(){
                        mui.openWindow({
                            url:"player.html",
                            id:"player.html",
                            extras:content
                        })
                  }
3. 发送给玩具  点击出现弹出框,展示所绑定的玩具

player.html 页面
<button type="button" id="pause" class="mui-btn mui-btn-yellow mui-btn-block">暂停</button>
        <button type="button" id="resume" class="mui-btn mui-btn-green mui-btn-block">继续</button>
        <button type="button" id="stop" class="mui-btn mui-btn-red mui-btn-block">停止</button>

mui.plusReady(function(){
    Sdata = plus.webview.currentWebview();
    mui.post(window.serv + "toy_list",{
        
    },function(data){},"json"
            );
    # 创建播放音频对象
    myplayer = plus.audio.createPlayer(window.serv_music + Sdata.audio)
    # 可以播放
    myplayer.play()
    
})
document.getElementById('pause').addEventListener('tap',function () {
    // 暂停事件      
    myplayer.pause();  
    })
    
    document.getElementById('resume').addEventListener('tap',function () {		
        // 继续播放事件
          myplayer.resume();  
    })
    
    document.getElementById('stop').addEventListener('tap',function () {	
        	// 停止播放事件
            myplayer.stop();
    })

function create_toy(toy) {
		var li = document.createElement("li");
		li.className = "mui-table-view-cell";
		var a = document.createElement("a");
		a.innerText = toy.toy_name;
    
    	// 将音乐发送给 玩具 基于websocket  通讯
		a.onclick = function() {
			var index = plus.webview.getWebviewById("HBuilder");
			mui.fire(index, 'send_music', {
				to_user: toy._id,
				music: Sdata.audio
			});
		}

		li.appendChild(a);
		document.getElementById("toy_list").appendChild(li);
	}


################# 一个App 里面只能有一个ws  如果新建就会覆盖前面的,所以将ws 放在index 页面 

index  页面 里对应自定义事件
document.addEventListener("send_music", function(data) {
    		// 这种激活自定义事件, 获取传过来的值是通过 data.detail
			var send_str = data.detail // {to_user:"toy123",music:Sdata.audio}
			ws.send(JSON.stringify(send_str)); 
		});


ws  后端  ws://192.168.13.198:3721/app/" + window.localStorage.getItem("user"));
from flask import Flask,request
from gevevtwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from geventwebscoket.websocket import WebSocket


ws_app = Flask(__name__)
user_scoket_dict  = {}
@ws_app.route('/app/<app_id>')
def app(app_id):
	// 获取连接的对象
	user_scoket = request.environ.get("wsgi.webscoket")
	if user_scoket:
        user_scoket_dict[app_id] = user_scoket
	// 循环接收数据
	while 1:
    	// 接收到的是序列化数据,所以需要放序列化
    	user_msg = user_scoket.receive()
		msg_dict = json.loads(user_msg)
		toy_socket = user_socket_dict.get(msg_dict.get("to_user"))
		
		


```



