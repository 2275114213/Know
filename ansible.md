代码发布系统

#### 前戏

```js
ansible: 批量在远程主机上执行命令
openpyxl: 批量操作excel
// 目前比较流行
puppet 是用ruby写的,
ansible
slatstack 
```

#### ansible

##### - 安装

```js
1. 安装epel
wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
2. 安装ansible
yum install -y ansible
```

```js
ansible 通过ssh来连接并控制被控节点
ssh 的认证方式
    - 密码连接
    - 秘钥连接
		1.生成ssh的秘钥对: ssh-keygen  
         2.复制公钥到远程主机: ssh-copy-id 192.168.13.133
		 	通过 ssh 192.168.13.133 直接连接 
        	 exit 退出
```

##### - 检测机器是否在线

```js
# 系统自带的ping 走的是 ICMP 的协议
ping 192.168.13.133
- ansible 提供了ping 模块
# 查看ansible 的命令格式
ansible -h 
// 结果
ansible <host-pattern> [options]
-a   模块的参数
-C   检查
-f   用来做高并发
--list-hosts   列出主机列表
-m   模块名称
--syntax-check 语法检查
-k 输入密码
# 查看某一个机器
ansible 192.168.13.133 -m ping

# 查看某两个机器是否在线
ansible 192.168.13.133,192.168.13.143 -m ping
# 查看所有机器
ansible all -m ping

# 查看ansible 生产的文件
rpm -ql ansible| more  // 分页显示

#  查看组里面有哪两台机器
ansible web --list-hosts

ansible host文件
This is the default ansible 'hosts' file.
It should live in /etc/ansible/hosts
 - Comments begin with the '#' character # 用#来表示注释
 - Blank lines are ignored # 空白行被忽略
 - Groups of hosts are delimited by [header] elements # 主机组 需要在【】下面
 - You can enter hostnames or ip addresses #可以写主机名或者ip地址
- A hostname/ip can be a member of multiple groups # 一台主机可以在多个组里面
www[001:006].example.com #表示从www001到www006的机器

// 单个ip 配置
192.168.13.133
192.168.13.143
192.168.13.152
// 组
[web]
192.168.13.133
192.168.13.143
[db]
192.168.13.143
192.168.3.152
[cache]
192.168.13.152



- 总结
host-pattern 的 格式
1. 单个主机  ansible 192.168.13.133 -m ping
2. 全部主机  ansible all -m ping
3. 多个主机  ansible 192.168.13.133,192.168.13.143 -m ping
4. 单个组   ansible web -m ping
5. 多个组  
	 -  交集   ansible 'web:&db' -m ping
     -  并集  ansible web,db -m ping
     		ansible 'web:db' -m ping
     - 差集  ‘web：！db’  在web 里面但是不在db 里面    
```

```js
查看模块的帮助信息
ansible-doc
ansible-doc -s shell(模块名)
// 结果
 ansible-doc [-l|-F|-s] [options] [-t <plugin type> ] [plugin]
 什么都不加 # 直接显示全部的信息
 -j  #以json的方式返回ansible的所有模块
 -l, --list#列出所有的ansible的模块
 -s   #以片段式显示ansible的帮助信息
```

#### 命令相关模块

##### yum 

```js
status: latest,present,installd  安装
         removed,absent  卸载
 ansible all -m yum -a "state=present name=tree"
```



##### command

```js
ansible web -a 'ls /'   列出根目录下的所有文件
ansible web -a 'pwd'    展示当前工作目录
ansible web -a 'chdir=/tmp pwd' 切换目录执行命令,使用场景是编译安装时使用
ansible web -a 'creates=/tmp pwd' 如果tmp目录存在就不执行,如果不存在就执行
ansible web -a 'removes=/tmp pwd' #用来判断tmp目录是否存在，存在就执行操作

# 这个并不存在管控机与被管控机上的文件判断的是组里面的文件
```

##### shell

```js
shell 执行得被控机 上的文件
为什么要有shell 因为 command 不支持特殊字符 <> | ! ; $ &
# 在web 组里面创建用户
ansible web -a 'useradd alex'
# 怎么查看用户创建成功没有
	1. tail -1 /etc/passwd
	2. tail -1 /etc/shadow
	3. id yuan
    
    // 设置密码
    在 192.168.13.133 窗口
    passwd yuan  这个需要交互,但是ansible 不支持交互,
    echo '123' | passwd --stdin alex  # 一步设置密码
    在 192.168.13.103 登录一下
    ssh alex@192.168.13.133
#  批量创建密码
ansible web -m shell -a 'echo "1234" |passwd --stdin yuan'

# 执行远程文件方式一
ansible 192.168.13.133 -m shell -a 'bash a.sh'
// a.sh
	#!bin/bash
     mkdir /data 
# 方式二 这种执行方式需要权限
chmod  +x a.sh  # 添加权限
ansible 192.168.13.133 -m shell -a '/root/a.sh'

# 远程执行python 脚本
ansible 192.168.107.131 -m shell -a '/root/a.py' 
```



##### script

```js
执行的是控制机上文件,也就是本地文件
ansible web -m script -a '/root/m.sh' # 执行本地的文件，执行管控机上的文件
ansible web -m script -a 'removes=/root/m.sh /root/m.sh' # 用来判断被管控机上是不是存在文件，如果存在，存在就执行，不存在就不执行
ansible web -m script -a 'creates=/root/a.sh /root/m.sh' #用来判断被管控机上是不是存在文件，如果存在，就不执行

```

#### 文件相关模块

##### template

```js
backup 备份，以时间戳结尾
dest 目的地址,远程节点上的绝对路径
group 文件的属组,设置远程节点上template文件所属用户组
mode 	设置远程节点上的template文件权限。类似Linux中chmod的用法
owner 	设置远程节点上的template文件所属用户
src 本地Jinjia2模版的template文件位置
# jinjia2 文件后名 j2


那么在执行这个Playbook前，对应的那个template文件（俗称模版），将在本地保持{{ admin_username }}及{{ admin_password }}的状态。在Ansible调用template模版执行的时候，这里将由Jinjia2从”tomcat-servers”读取对应的值，然后替换掉模版里的变量，然后把这个替换变量值后的文件拷贝到远程节点。

vim 快捷键: 末行模式 /bind 按n切换下一个结果
复制: 数字 yy
粘贴: p
删除光标后面的内容: $  +d 
# 安装redis,并修改redis 可以远程访问的ip
ip 对应每个主机的ip,所以需要模板渲染
```



##### copy

```js
backup 备份，以时间戳结尾
dest 目的地址
group 文件的属组
mode 文件的权限 r 4 w 2 x 1
owner 文件的属主
src 源文件
content  直接把文字输入到远程的文件中
# 通过md5码来判断是否需要复制
ansible db -m copy -a 'src=/root/m.sh dest=/tmp/a.sh' #复制本地文件的到远程主机
ansible db -m copy -a 'src=/root/m.sh dest=/tmp/a.sh mode=755' #修改文件的权限
 ansible web -m copy -a 'src=/root/m.sh dest=/tmp/a.sh mode=755 owner=alex' 修改文件的属主

// 拷贝目录 
 ansible web -m copy -a 'src=/etc/init.d dest=/tmp/ mode=755 owner=alex' # 复制本地目录到远程主机，如果改变文件的属性，则文件夹内的文件也会被改变
 
 // 拷贝目录下的文件内容
 ansible web -m copy -a 'src=/etc/init.d/ dest=/tmp/ mode=755 owner=alex' # 复制本地目录内的所有文件到远程主机
 ansible web -m copy -a "content='大弦嘈嘈如急雨，小弦切切如私语\n' dest=/tmp/b.txt" # 直接将文本内容注入到远程主机的文件中
```

##### file

```js
inode 硬盘的地址
id 获取到的是内存的地址
ln -s a.py b.py 创建软连接  a.py 是源文件
ln  a.py c.py 创建硬链接
当 源文件变化时，软连接和硬链接文件都会跟着变化
ansible db -m file -a 'path=/lzmly2  state=directory' #在远程机器上创建文件夹
ansible db -m file -a 'path=/root/q.txt  state=touch' #用来在远程机器上创建文件
ansible db -m file -a 'path=/tmp/f src=/etc/fstab state=link' #创建软连接src是源地址，path是目标地址
ansible db -m file -a 'path=/tmp/f state=absent' #用来删除文件或者文件夹
```

##### fetch

```js
本地获取被控制机上的目标文件
dest 目的地址  控制机上的文件地址
src 源地址 被控制机上的文件地址

ansible web -m fetch -a 'src=/var/log/cron dest=/tmp' # 下载被控节点的文件，每台机器创建一个文件夹，并保留原来的目录结构
```

#### 软件相关模块

##### yum

```js
- 1. rpm  和 yum 的区别
	 rpm : redhat package manager
     yum : 可以解决依赖关系
     	 - linux  yum操作:
			1. 查看yum 包: yum list install
             2. 安装: yum install 包名
             3. 卸载: yum remove 包名
             4. 查看包组信息  yum grouplist
             5. 安装包组	yum groupinstall
 -2. yum 源配置
 /etc/yum.repos.d/CentOS-Base.repo
 epel 源  里面有redis ,nginx 等
 	- 配置文件 /etc/yum.repos.d/epel.repo
[epel]
name=Extra Packages for Enterprise Linux 7 - $basearch #名字
baseurl=http://mirrors.aliyun.com/epel/7/$basearch  #rpm源的地址,可以写http,https,ftp,Samba,file:
failovermethod=priority
enabled=1 # 是否开启,1代表开启,0表示关闭
gpgcheck=0  #是否校验签名,1代表校验,0表示校验
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
-3. ansible 提供的yum 模块
	- 查看yum 模块的参数
    	ansible-doc -s yum
        // 结果
       disablerepo # 禁用源
       enablerepo # 启用源
       name # 包名
       state 
       	- install present installed latest
        - remove  absent removed
     -  yum 练习
     	# 安装wget
     	ansible web -m yum -a 'name=wget'
	   
		# 安装python2-pip 
        // 因为pip 来自epel 源, 所以需要把epel 源文件传到各个主机上  ansible all -m copy -a 'src=/etc/yum.repos.d/epel.repo dest=/etc/yum.repos.d/epel.repo'
        ansible web -m yum -a 'name=python2-pip'
         
		#  卸载                                                   ansible web -m yum -a 'name=wget state=absent' 		
        # 安装包组
        ansible web -m yum -a 'name=@Development Tools'
```



#### 其他模块

##### setup

```js
- 自动从远程主机获取可用于playbook 中的变量
命令: ansible web -m setup
	 # 查看指定的
	 ansible web -m setup -a 'filter="ansible_all_ipv4_addresses"'
结果:
ansible_all_ipv4_addresses: ipv4的所有地址
ansible_all_ipv6_addresses: ipv6的所有地址
ansible_date_time: 获取控制节点的时间
ansible_default_ipv4: 默认的ipv4地址
ansible_distribution: 系统
ansible_distribution_major_version: 系统的大版本
ansible_distribution_version: 系统的版本号
ansible_domain: 系统所在域
ansible_env: 系统的环境变量
ansible_hostname: 系统的主机名
ansible_fqdn: 系统的全名
ansible_machine: 系统的架构
ansible_memory_mb: 系统的内存信息
ansible_os_family: 系统的家族
ansible_pkg_mgr: 系统的包管理工具
ansible_processor_cores: 系统的cpu的核数  // 每颗cpu 的 核数
ansible_processor_count: 系统的cpu的颗数
ansible_processor_vcpus: 系统的cpu的总个数=cpu的颗数*cpu的核数
ansible_python: 系统上的python
```



##### pip

```js
- pip install 安装包
- pip freeze > a.txt
- pip install -r a.txt  安装文件中的包
pip list 查看所有的以pip 安装成功的包

- ansible pip 操作
ansible web -m pip -a 'name=flask' 
```

##### service

```js
  - 一般操作
	# 查看进程 
        ps -ef|grep nginx
    # 查看端口信息
        ss -tnlp
    # 启动nginx
        centos7: systemctl start nginx 
        centos6: service nginx start
    # 开机自启动nginx
        centos7: systemctl enabled nginx 
        centos6: chkconfig nginx on
 - 参数
	name 服务名
    state 
    	- started
		- stoped
		- restart
		- reload
 - ansiable 操作
  	# 启动nginx
  	ansible web -m service -a 'name=nginx state=start'
	# 关闭nginx
    ansible web -m service -a 'name=nginx state=stopped' 
```



##### 计划任务cron

```js
- 一般操作
	*   *   *   *   *
    分  时   日  月  周
    0 */2 *  * *  job  每隔两个小时
    0 12,13 * * * job 12点和13点
    0 12-17 * * * job 12点到17点
    0 12-17/2 * * 1,3,6,0 周1,周3,周6,周7 12点到17点每隔两个小时 
    # 编辑计划任务  
    	crontab -e 
	# 查看计划任务
    	crontab -l 
	# 删除计划任务
    	crontab -r

- ansible cron 模块 参数
	day 天
    disabled  禁用
    hour  小时
    job 任务
    minute 分钟
    mouth 月
    name 任务名字
    weekday 周
	# 创建一个计划任务
    ansible db -m cron -a 'minute=26 job="touch /tmp/xzmly.txt"  name=touchfile'

	#删除一个任务
    ansible db -m cron -a 'name=touchfile state=absent'
	
/tmp/xzmly.txt" name=touchfile disabled=yes'  # 禁用计划任务,以#表示禁用
# 计时任务的参数查看在 /etc/crontab

# 存放计时任务的文件:
	/var/spool/cron
```

#### 用户相关

##### user

```js
用户:
	管理员 root 0
	普通用户
    	系统用户 不能登录 1-999 centos7 1-499 centos6
        登录用户  可以登录 1000-65535 centos7 500-65535 centos6
 用户组:
	管理员组: root 0 
	系统用户组 1-999 centos7 1-499 centos6
    登录用户组 1000-65535 centos7 500-65535 centos6
    
 useradd 参数
 -d 指定用户的家目录
 -g 指定用户的组
 -G 指定用户的附加组
 -s 指定登录后使用的shell
 -r 创建一个系统用户
 
 useradd -r wusir  创建系统用户,从999倒序
 useradd -s /sbin/nologin yuan 创建的普通用户,从1000开始
 useradd -d /opt/yuan 指定用户家目录
 useradd -u 3000 yuan 创建用户并指定用户的uid
 userdel yuan 删除用户,但是不删除家目录
 userdel -r yuan 删除用户,并删除用户家目录

     
 - ansible  user 模块操作
	group 组
    groups 附加组
    home 家目录
    name 用户名
    password 密码
    remove 删除的时删除用户家目录
    shell 用户登陆后使用的shell
    system 创建一个系统用户
    uid 用来指定用户的id
    state 状态
 
        

    # 创建一个用户,并指定用户的id,用户的家目录,用户的附加组,用户的shell
    ansible db -m user -a 'name=yuan uid=4000 home=/opt/yuan groups=root shell=/sbin/nologin'
# 删除用户但是不删除用户的家目录
	ansible db -m user -a 'name=yuan state=absent'
# 删除用户并删除用户的家目录
	ansible db -m user -a 'name=yuan remove=yes'



```

##### group

```js
tail /etc/group  查看用户组是否创建成功
groups : 查看当前登录用户的组内成员
groups yuan : 查看yuan用户所在的组,以及组内成员
whoami : 查看当前登录的用户名
/etc/passwd 和 /etc/shadow 系统存在的所有用户
/etc/group 文件中包含所有组


groupadd yuchao 创建用户组
groupadd yuchao 删除用户组

    - ansible group
        gid 组的id
        name 组名
        system 系统组
        # 创建一个系统组
        ansible db -m group -a 'name=yuan system=yes'

        # 删除组
        ansible db -m group -a 'name=yuan state=absent'

```



#### ansible 剧本

```js
# 创建一个用户组yuan
	ansible web -m group -a 'name=yuan'
# 创建一个用户yuan
	ansible web -m user group -a 'name=yuan'
# 把/etc/fstab 文件复制到远程主机/tmp/f
	ansible web -m copy 'src=/etc/fstab dest=/tmp/f'
# 安装nginx,并启动,设置开机自启动
	ansible web -m yum 'name=nginx'
	ansible web service -a 'name=nginx enabled=yes'
```



##### ansible-playbook命令格式

```js
可以重复执行
```



```js
执行顺序: 从上往下
特性: 幂等性  不管执行多少遍,结果都是一样的

ansible-playbook [options] playbook.yml [playbook2 ...] 

-C ,--check # 检查,白跑,不执行
-f  # 用来做并发
--list-hosts  # 列出主机列表
--syntax-check # 语法检查

yaml 语法: 
	-1. :后面必须加空格
    -2. =两边不可有空格
	-3. 字典 key:value
    	列表 [] -
        
# 简单用法
- hosts: web
  tasks:
  - name: creategroup
    group: name=yuan
  - name: createuser
    user: name=yuan1


```



##### 传参

```js
- hosts: web
  tasks:
  - name: create{{user}}
	user: name{{user}}
```

```js
-1. ansible-playbook -e 'user=yuan' a.yml
-2. z在/etc/ansible/hosts 文件中
	[db]
    192.168.107.132 user=alexsb11
    192.168.107.133 user=alexsb12
-3. z在/etc/ansible/hosts 文件中
	[db:vars] # 表示组的参数
     user=yuan
-4.
- hosts: db
  vars:
  - user: alexsb14
  tasks:
  - name: create{{ user }}
    user: name={{ user}}
-5. 
- hosts: db
  tasks:
  - name: sum
    shell: echo 7+8|bc
    register: user
  - name: createuser
    user: name={{user.stdout}}
    
    
 # 传参的优先级
 -e > playbook vars >  hosts 文件 
```

##### 条件判断

```js
应用场景:
	- 不同的系统
	- 不同的版本
	- 不同的环境
	- 不同的用户
# 当时3的时候执行插入'哈哈',当是4的时候执行插入'呵呵' 文件内容是覆盖原来的
[root@localhost ~]# cat a1.yml 
- hosts: web
  tasks:
  - name: createfile
    copy: content='哈哈' dest=/tmp/a.txt
    when: a=='3'
  - name: createfile
    copy: content='呵呵' dest=/tmp/a.txt
    when: a=='4' 



```

##### tags

```js
- 应用场景: 指定某一个任务执行,修改了配置文件

- hosts: web
  tasks:
  - name: installnginx
    yum: nginx
  - name: copyfile
  	copy: src=/etc/nginx/nginx.conf dest=/etc/nginx/nginx.conf
	tags: copyfile
  - name: start
  	service: name=nginx state=started

# 运行命令
ansible-playbook -t copyfile a2.yml
```

##### 循环

```js
- 应用场景: 一次性创建多个
# 创建用户yuan2,yuan3,yuan4
- hosts: web
  tasks:
  - name: createuser
    user: name={{item}}
    with_items:
    - yuan2
    - yuan3
    - yuan4
- 循环嵌套
# 创建用户yuan6,yuan7,yuan8  分别属于组 ha1,ha2,ha3
- hosts: web
  tasks:
  - name: creategroup
    group: name={{item}}
    with_items:
    - ha3   
    - ha1
    - ha2
  - name: createuser
    user: name={{item.name}} group={{item.group}}
    with_items:
       - {'name':yuan6,'group':ha1}
       - {'name':yuan7,'group':ha2}
       - {'name':yuan8,'group':ha3}
```

##### handlers

```js
- 应用场景: 修改配置文件

```



#### get_url

```js
ansible client01 -m get_url -a 'url=http://nginx.org/download/nginx-1.6.3.tar.gz dest=/tmp'
```

#### roles

```js
- 目录清晰
- 可以互相调用
[root@localhost app]# tree ansible-playbook
ansible-playbook
├── nginx.yml
└── roles
    └── web                   #这就是在nginx.yml主文件中指定的role
        ├── defaults
        │   └── main.yml
        ├── files
        │   ├── compile.sh.j2
        │   └── nginx-1.6.3.tar.gz
        ├── handlers
        │   └── main.yml
        ├── tasks
        │   ├── install.yml
        │   └── main.yml
        └── templates
            └── nginx.conf.j2
	└── db
    	 ├── tasks
            │   ├── install.yml
            │   └── main.yml
# 在要使用 ansible-playbook 目录下建 web.yml
	- hosts: web
       remote_user: root
       roles:
	   - web
在 web 目录的tasks 目录下建
	- main.yml
		内容:
			- import_tasks: install.yml
			- import_tasks: copyfile.yml
			- import_tasks: start.yml
			
	- start.yml
	- install.yml
	- copyfile.yml

运行: ansible-playbook web.yml

# 将redis.conf cp 到 /web/tempaltes  
cp /etc/redis.conf /etc/ansible/roles/templates/


# 但是有得需要触发才能执行
在 tasks 里面创建/tasks/handlers/mian.yml
main.yml
- name: restart
  service: name=redis state=restarted

在 /tasks/copyfile.yml 里面监听
- name: copyfile
  copy: src=/etc/redis.conf 
  tags: copyfile
  notify: restart

web 调用 db 里面的东西, 
    在web 的main.html 里面import_tasks 就可以了
    
    
    
  
 
```



nginx 和 uwsgi 配合配置文件的三种方式

```js
# uwsgi 是http 的时候
[uwsgi]
http = 0.0.0.0:8000
#the local unix socket file than commnuincate to Nginx
socket = /data/mysite/mysit.socket
# the base directory (full path)
chdir = /data/mysite
# Django's wsgi file
wsgi-file = mysite/wsgi.py
# maximum number of worker processes
processes = 4
#thread numbers startched in each worker process
threads = 2
# clear environment on exit
vacuum          = true
daemonize = /data/mysite/uwsgi.log
py-autoreload=1

nginx 的配置文件
location / {
        include  /data/mysite/conf/uwsgi_params;
        proxy_pass http://127.0.0.1:8000;
            root   html;
            index  index.html index.htm;
        }

```

