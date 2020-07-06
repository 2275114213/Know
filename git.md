```js
- 定义: git是一个用于帮助用户实现版本控制的软件
```

##### 命令

```js
git init   // 对文件夹管理初始化
git status  // 红色表示没有管控,展示状态
git add manage.py  // 对指定文件版本控制 之后变成绿色的
git add .   // 对指定文件夹下的所有文件及子目录进行版本控制  并没有真正控制起来了,准备就绪

git config --global user.email 'xx.com'
git config --global user.name 'yuan'

git commit -m  "创建第一个版本"  //相当于一个人把所有文件复制了另一个地方,在这之前先登录,原来的文件依然存在,相当于变透明,所以git status 就什么都看不见了,变透明色


# 将 index.html 里面的文件进行更改,
git status // 检测到文件发生变化, 文件变红
git add . // 将文件进行托管  
git commit -m '创建欧美功能'   // 只把修改的文件复制都另另一个地方


# 添加了欧美功能,现在项目上线了,欧美违规了,不允许有欧美的东西,在开发过程中有大量的欧美代码,不能一行一行的删除,回到开始的状态

git log 查看操作日志
git reset --hard  版本的id  // 回到某一个版本状态

# 假设疏通关系后,欧美又要上线
git log  // 这个看不见,做回滚地方的版本,默认只显示当前之前的版本

git reflog

git reset --hard f0f2e93 


# 业务上线了,要再开发一个在线直播开发过程中需要修复bug
或临时性功能到来
<body>
    <h1>东北热</h1>
    <ul>
         <li>国产</li>
         <li>日韩</li>
		<li>yuan</li>
		<li>在线直播1/2</li>
    </ul>
- 在线直播开发1/2 ,要求日韩下线
	需要进日韩删掉,然后提交,但是在线直播开发一半,不能上线
	- 1. git stash // 将当前管理目录下的所有文件,里面的红色文件,
    <h1>东北热</h1>
    <ul>
         <li>国产</li>
         <li>日韩</li>
		<li>yuan</li>
    </ul>
    - 2. 修改index.html
	删掉日韩
    git add .
    git commit -m '删除日韩'
	
	- 3. 继续开发直播功能
    git stash pop  // 恢复代码并且没有日韩
	# git stash 存储的时候里面有日韩
	# git stash pop 的时候自动检测文件是否修改了,使他们俩进行自动合并  	
	<body>
    <h1>东北热</h1>
    <ul>
         <li>国产</li>
        
		<li>yuan</li>
		<li>在线直播1/2</li>
    </ul>
- 将当前状态在 git stash, 在开发一个新的在线功能,
    <h1>东北热</h1>
    <ul>
         <li>国产</li>
        
		<li>yuan</li>
    </ul>
    添加一个<li>在线</li>
	然后 git add .
    	 git commit -m 'xxx'
	想回到在线直播, 继续开发
		git stash pop 
        
<body>
    <h1>东北热</h1>
    <ul>
        <li>国产</li>
        
		<li>yuan</li>
<<<<<<< Updated upstream
		<li>在线</li>
=======
		<li>在线直播1/2</li>
>>>>>>> Stashed changes
    </ul>
</body>

'''
git stash pop 的时候出现两种情况

假如我正在开发购物车,但是老板让我修改一下以前的页面,可能会冲突
#############  不能直接跨两个度去修改,
`
比如bug里面  小视频===>大视频  改完了,切换到master里,git merge bug ,  结果master里是大视频
切换到dev 分支 但是dev里面仍然是小视频 , 需改成小小小视频, 
切换到master 里面, git merge dev  就会冲突,
`

一种自动合并:
	
一种发生冲突:
	暂存走的文件,你又修改那一行数据了
	只能人为手动解决冲突
'''
git stash list   查看“某个地方”存储的所有记录\
git stash clear   清空“某个地方”
git stash pop 将第一个记录从“某个地方”重新拿到工作区（可能有冲突）,并删除
git stash apply     编号, 将指定编号记录从“某个地方”重新拿到工作区（可能有冲突）不删除stash
git stash drop      编号，删除指定编号的记录

```

一修改由透明色变红色,add 之后变绿色,commit 之后变化透明色

reset --hard 由透明色直接跳回最开始的透明色



由透明色变成绿色  git reset soft 版本号,让他进行准备,没有把它代到其他房间

由绿色变成红色: git reset head 文件  ,不对他进行准备

有红色变成透明色: git checkout 文件名  取消修改内容



branch

```js
# 开发小视频1/2,  然后有关部门告诉你可以上日韩了, 
<body>
    <h1>东北热</h1>
    <ul>
        <li>国产</li>
		<li>yuan</li>
		<li>在线直播</li>
    </ul>
</body>
git branch dev 拷贝当前目录的所有代码到 dev 里面去


<body>
    <h1>东北热</h1>
    <ul>
        <li>国产</li>
		<li>yuan</li>
		<li>在线直播</li>
		<li>小视频开发1/2</li>
    </ul>
</body>
git add .
git commit -m '小视频创建一半了'
# 代码只有dev 里变了, master 里面没变
git branch master

dev 里面开发
master 代码上线


切换 git checkout name 切换到某个分支
合并 g

git branch -d bug  // 删除bug分支




# 面试题:
	如果代码出现bug 如何解决
    	- 创建一个bug分支,然后进行bug处理,处理完毕后合并到master分支
		- 删除bug分支
		- 回到dev分支继续开发

# 面试题:
		你们公司如何基于git做版本控制
        	- master 分支是用来存放生产环境代码的
            - dev 分支是用来开发的
            - bug 创建临时bug分支来修复线上的bug,修复完成后合并到master,删除bug 分支

```

```js
命令总结:
     -  git init 	 初始化 
     -  git status   查看状态
     -  git log 	 查看提交记录,从当前位置往前的提
交记录
     -  git reflog  查看所有的提交记录
     -  git add 添加到缓存区
     -  git commit -m "说明" 添加到版本库 
     -  git diff 对比工作区和缓存区之间的差别
     -  git diff --cached 对比缓存区和版本库
     
     - 回滚系列:
     	-  git reset --hard 版本号 回滚到某一个版本
        //   git reset --hard 直接一步到位
       	-  git reset soft 版本号 由透明色变成绿色
        -  git reset head 文件  由绿色变成红色(从缓存区拉取内容) (//状态的改变)
        -  git checkout 文件名 取消修改(由红色变成透明色)

  - stash
        git stash 将当前开发的内容放到某个地方
        git stash pop  恢复当前的工作目录,并删除
        git stash apply 恢复当前工作目录不删除
        git stash grop 删除stash
        git stash list 查看stash 列表
	
  - branch
        git branch name 新建分支
        git branch 查看分支
        git checkout name 切换到某个目录
        git branch -d name 删除分支
        git branch -b name 创建某个分支并直接切换分支
```

#### git版本控制 之github代码托管

##### 上传github 与 下载github

```js
 - 家里面一台电脑, 公司一台电脑, 需要一个代码托管平台 github
 #  origin 是别名
 git remote add origin1 https://github.com/2275114213/learngit.git
# 将master 分支上的上传到
git push -u origin1 master

# 将dev 分支上传
git checkout dev
git push -u gitex dev

# 在公司的电脑上
git clone  https://github.com/2275114213/gitex.git

# 切换目录
cd gitex

git branch  //只有master分支

git pull origin dev 
```

##### 开发一半功能,回家继续开发

```js
- 在公司开发一半,要回家了
公司电脑 
git commit -a '开发1/3' //上传到本地
git push origin dev // 上传到github 上

回家了, 在家的电脑上 
git pull origin dev 
开发完了
git commit -a '开发完毕'
git push origin dev 
```

##### 开发一半忘记提交

```js
# 在公司开发完了, 已经commit完了, 但是没提交到github
touch 1.py
git add .
git commit -m '创建一个p1.py'
# 回到家拉取不下来,所以开发其他功能
touch 2.py
git add .
git commit -m '创建一个p2.py'
git push origin dev


# 第二天回到公司先拉代码
弹出一个框,
```

```js
git pull origin dev  // 直接将远程文件拉取到本地
分解成两步:
    git fetch dev // 去远程仓库里面把代码下下来,拉到版本库
    git merge  origin/dev ===> git rebase origin/dev
    						// 这样整洁
```

##### 多人协作,修改别人代码

```js
加入到合作者 或者 组里面
```

##### 修改网上的一个

```js
# 先fork
然后 在pull

```



tags ,版本控制

```js
git tag  : 查看tag
git -a v1.1 -m '创建1.1版本'
git push origin --tags 提交tags
#给之前提交过的大标签  git tag -a v1 md5值
```

忽略目录

git 免密钥登录

```js

```























