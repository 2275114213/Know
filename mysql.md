####  数据库概述

1. 什么是数据库

```js
数据库即存放数据的仓库,只不过这个仓库是在计算机存储设备上,而且数据是按照一定的格式存放的,# 数据库是长期存放计算机内的,有组织,可共享的数据即可
数据库中的数据按照一定的数据模型组织,描述和存储,具有较小的冗余度,较高的数据独立性和易扩展性,并可为各种用户共享
```

2. 数据库管理系统

```js
如何科学地组织和存储数据,如何高效获取和维护数据成了关键,这就用到了一个系统软件 -- 数据库管理系统

如MySQL, Oracle, SQLite, Access, MS SQL Server
mysql 主要用于大型门户,例如搜狗,新浪等,它主要的优势就是开放源代码,因为开放源代码这个数据库是免费的, 他现在是甲骨文公司的产品

oracle 主要用于银行, 铁路, 飞机场等,该数据库功能强大,软件费用高,也是甲骨文公司的产品.

sql server 是微软公司的产品,主要用于大中型企业, 如联想, 方正等
```

#### MySql 安装和基本管理

1. 应用环境

```js
Linux 作为操作系统,Apache 或 Nginx 作为 Web 服务器,MySQL 作为数据库,PHP/Perl/Python 作为服务器端脚本解释器,由于 则是个软件都是免费或来函源码软件,因此使用这种方式不用花一分钱就可以建立起一个稳定.免费的网站系统,
称为:"LAMP" 或 "LNMP" 组合
```

2. mysql 是什么

```js
总结: mysql 就是一个基于socket编写的C/S 架构软件
```

3. 数据库管理软件分类

```js
分两类:
	关系型: 如sqllite, db2, oracle, access, sql server, MySQL
	非关系型:mongodb, redis, memcache
总结两句话:
	关系型数据库需要有表结构
    非关系型数据库 是 key-value 存储结构的,没有表结构
RDBMS 即关系数据库管理系统的特点:
	1. 数据以表格的形式 出现
    2. 每行为各种记录名称对应的数据域
    3. 每列为记录名称所对应的数据域
    4. 许多的行和列组成一张表单
    5. 若干的表单组成dataase
```

##### mysql 的介绍安装, 启动

```js
下载地址:  https://dev.mysql.com/downloads/mysql/
2. 解压
3.添加环境变量
4.初始化   mysqld --initialize-insercure
5.启动mysql服务
	mysqld # 启动mysql服务
6.启动mysql客户端并连接 mysql 服务端(新开一个cmd窗口)
	mysql -u root -p  # 连接mysql 服务端
7.上一步解决了一些问题,但不够彻底,因为在执行[mysqld] 启动 MySQL 服务器时,当前终端会被hang住,name座椅下设置即可解决此问题,即将MYSQL 服务制作成windows 服务
	注意：--install前，必须用mysql启动命令的绝对路径
    # 制作MySQL的Windows服务，在终端执行此命令：
    "c:\mysql-5.6.40-winx64\bin\mysqld" --install
    # 移除MySQL的Windows服务，在终端执行此命令：
    "c:\mysql-5.6.40-winx64\bin\mysqld" --remove
    注册成服务之后，以后再启动和关闭MySQL服务时，仅需执行如下命令：
    # 启动MySQL服务
    net start mysql
    # 关闭MySQL服务
    net stop mysql
```

```js
# 查看进程号
tasklist |findstr  mysql
# 杀死进程
taskkill /F /PID  进程号
```

##### Mysql破解密码

跳过授权方式，直接登录！！

0.以管理员身份打开cmd

![img](https://images2018.cnblogs.com/blog/1364810/201806/1364810-20180609171111285-1436609180.png)

 

2.停掉mysql服务端

```
C:\WINDOWS\system32>net stop mysql
MySQL 服务正在停止.
MySQL 服务已成功停止。
```

3.执行如下命令跳过授权表

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
#跳过授权表
C:\WINDOWS\system32>mysqld --skip-grant-tables
2018-06-09 17:12:38 0 [Warning] Insecure configuration for --secure-file-priv: Current value does not restrict location of generated files. Consider setting it to a valid, non-empty path.
2018-06-09 17:12:38 0 [Note] mysqld (mysqld 5.6.40) starting as process 6052 ...4.
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 4.再次查看

![img](https://images2018.cnblogs.com/blog/1364810/201806/1364810-20180609171534207-1689558816.png)

\5. 现在可以任意的更改密码，执行如下命令

 update mysql.user set authentication_string =password('') where User='root'; 

 

6.刷新权限，执行命令

```
flush privileges;
```

![img](https://images2018.cnblogs.com/blog/1364810/201806/1364810-20180609172304314-2009414171.png)

7.退出mysql。执行命令：exit，

 

8.让用户去加载权限，以管理员身份进入cmd,查看当前mysql进程

```
`tasklist |findstr mysql  ``#查看当前mysql的进程`
```

![img](https://images2018.cnblogs.com/blog/1364810/201806/1364810-20180609172758145-1321365872.png)

 

9.杀死当前的进程，执行如下命令

```
taskkill /F /PID 6052  # 杀死当前的进程pid
```

![img](https://images2018.cnblogs.com/blog/1364810/201806/1364810-20180609173150636-88289239.png)

10.再次执行如下操作，还原

![img](https://images2018.cnblogs.com/blog/1364810/201806/1364810-20180609173421127-1672852700.png)

##### Mysql 中同一字符集编码

进入mysql客户端，执行\s

![img](https://images2018.cnblogs.com/blog/1364810/201806/1364810-20180609174037170-651670879.png)

 为了统一字符编码，请执行如下操作：

（1）my.ini文件是mysql的配置文件，

```
在C:\mysql-5.6.40-winx64文件下创建my.ini文件
```

（2）将如下代码拷贝保存。

[mysqld]
\# 设置mysql的安装目录 **后面的路径一定是安装sql的目录（自己电脑的）**
basedir=C:\mysql-5.7.22-winx64\mysql-5.7.22-winx64
\# 设置mysql数据库的数据的存放目录，必须是data
datadir=C:\mysql-5.7.22-winx64\mysql-5.7.22-winx64\data
sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES

```js
mysql端口   port=3306
```

```js
字符集
[mysqld]
character-set-server=utf8
collation-server=utf8_general_ci
[client]
default-character-set=utf8
[mysql]
default-character-set=utf8

```

（3）以管理员身份重启服务，执行如下命令 

```
C:\Windows\system32>net stop MySQL
MySQL 服务正在停止..
MySQL 服务已成功停止。

C:\Windows\system32>net start MySQL
MySQL 服务正在启动 .
MySQL 服务已经启动成功。
```

（4）在cmd中输入mysql进入mysql环境，执行\s,显示如下信息，表示成功

![img](https://images2018.cnblogs.com/blog/1364810/201806/1364810-20180609174415901-1604168853.png)

#### 基本的mysql 语句

1.操作文件夹(库)

```js
增: create database db1 charset utf8;
查: # 查看当前创建的数据库
		show create database db1;
    # 查看所有的数据库
    	show databases;
改: alter database db1 charset gbk;
删: drop database db1;
```

2.操作文件(表)

```js
use db1;  切换文件夹
select database()   # 查看当前所在的文件夹
增: create table t1(id int,name char)
查:  # 查看当前的这张表如何创建的
	show create table t1;
	# 查看所有的表
    show tables;
	# 查看表的详细信息
    desc t1;
改:
	# modify 修改的意思
    alter table t1 modify name char(6);
	# 改name 为大写的NAME
	alter table t1 change name NAME char(7);
删:
	drop table t1;
```

3.操作文件内容(记录)

```js
增:  # 插入一条记录,规定id ,name 数据
	insert t1(id,name) values(1,'mjj01'),(2,"mjj02"),(3,"mjj03")
查:
	select id from db1.t1;
	select * from db1.t1;
	select * from db1.t1;
改:
	update db1.t1 set name="yuan"
	uodate db1.t1 set name="yaun" where id =2 ;
删:
	delete from t1;  # 删除整个表中的数据,但是字段依然是在原来的基础上增长
	delete from t1 where id=2;
```

##### delete truncate delete 的区别

```js
delete(dml语句) 每次从表中删除一行,并同时将该行删除操作作为事务记录在日志中保存以便进行回滚操作,
 truncate(ddl语句) 一次性地从表中删除删除所有的数据并不计录到日志保存,会隐式提交, 不能回滚, 不会触发触发器
drop 删除整个表(结构和数据)



1、在速度上，一般来说，drop> truncate > delete。

2、在使用drop和truncate时一定要注意，虽然可以恢复，但为了减少麻烦，还是要慎重。

3、如果想删除部分数据用delete，注意带上where子句，回滚段要足够大；

   如果想删除表，当然用drop； 

   如果想保留表而将所有数据删除，如果和事务无关，用truncate即可；

   如果和事务有关，或者想触发trigger，还是用delete；

   如果是整理表内部的碎片，可以用truncate跟上reuse stroage，再重新导入/插入数据。


```



#### 库的操作

```js
1 .查看数据库 : show databases;
2 .创建数据库: create database 数据库名 charset utf8;
3 .数据库命名规则:
	可以由字母, 数字, 下滑线, @, #, $
    区分大小写
    唯一性
    不能使用关键词
    不能单独使用数字
    最长128位
```

```js
数据库的相关操作
1. 查看数据库  show databases;
2. 查看当前数据库 show create 
	mysql> show create database yuan;
+----------+---------------------------------------------------------------+
| Database | Create Database                                               |
+----------+---------------------------------------------------------------+
| yuan     | CREATE DATABASE `yuan` /*!40100 DEFAULT CHARACTER SET utf8 */ |
+----------+---------------------------------------------------------------+
1 row in set (0.00 sec)
3. 查看所在的库  select database()
4.选择数据库  use yuan;
5.删除数据库	 DROP DATABASE  数据库名
6.修改数据库  alter  database db1 charset utf8;
```

#### 表的操作

##### 1.存储引擎介绍

```js
show engines\G;  # 查看所有支持的搜索引擎
show variables like "storage_engine%"; # 查看正在使用的存储引擎
```

```js
事务:
	事务是由一个或多个sql 语句组成的一个整体;
	在事务中的操作, 要么都执行修改, 要么不执行
	只有在该事务中所有的语句都执行成功才会将修改加入到数据库中,否则回滚到上一步
```

```js
1. "Myisam"
 支持全文索引
 查询速度相对较快
 支持表锁
 	表锁: select * from tb for update;( # 锁 for update)
2. "InooDB"
 支持事务
 支持行锁,表锁
 	# 表锁: select * from tb for update
    # 行锁: select id,name from tb where id = 2 for update;
3. 'Memory' 
   Memory 存储引擎中的数据都存放在内存中,数据库重启或发生崩溃,表中的数据都将消失,他适合存储OLTP 数据库应用中临时数据的临时表,也可以作为OLAP 数据库应用中数据库的维度表,Memory 存储引擎默认使用哈希索引,而不是通常熟悉的B+ 树索引
4. BLACKHOLE
   黑洞存储引擎,可以用于主备复制中的分发主库
```

```js
指定表的类型/存储引擎
create table t1(id int) engine = innodb; # 默认不写就是innodb
```

小练习：

创建四张表，分别使用innodb,myisam,memory,blackhole存储引擎，进行插入数据测试 

```
create table t1(id int)engine=innodb;
create table t2(id int)engine=myisam;
create table t3(id int)engine=memory;
create table t4(id int)engine=blackhole;
```

查看data文件下db1数据库中的文件：

![img](https://images2018.cnblogs.com/blog/1364810/201806/1364810-20180609204213105-1699347239.png)

```
#.frm是存储数据表的框架结构

# .ibd是mysql数据文件 

#.MYD是MyISAM表的数据文件的扩展名

#.MYI是MyISAM表的索引的扩展名

#发现后两种存储引擎只有表结构，无数据

#memory，在重启mysql或者重启机器后，表内数据清空
#blackhole，往表内插入任何数据，都相当于丢入黑洞，表内永远不存记录
```

##### 2.创建表

```js
create table 表名(
字段名1 类型[(宽度) 约束条件],
字段名2 类型[(宽度) 约束条件],
字段名3 类型[(宽度) 约束条件]
);

#注意：
1. 在同一张表中，字段名是不能相同
2. 宽度和约束条件可选
3. 字段名和类型是必须的
```

```js
1.创建数据库
	create databases db2 charset utf8;
2. 使用数据库
	use db2;
3. 创建表
	create table a1(id int,name char(20)) ;
3. 插入数据
	insert into a1 values (1,"mjj",18),(2,"yaun",20)
4. 查询表结构
	desc a1;
5. 查看表的详细信息
	show create table a1\G;
####6. 复制表
(1) 创建一个新的数据库
	create databases db3 charset utf8;
(2) 使用db3
	use  db3;
#####
(3) 复制db2.a1 的表的结构和记录
	mysql> create table b1 select * from db2.a1;
	Query OK, 2 rows affected (0.03 sec)	
ps1：如果只要表结构，不要记录

#在db2数据库下新创建一个b2表，给一个where条件，条件要求不成立，条件为false，只拷贝表结构
mysql> create table b2 select * from db2.a1 where 1>5;
Query OK, 0 rows affected (0.05 sec)
Records: 0  Duplicates: 0  Warnings: 0
查看表结构：

复制代码
# 查看表结构
mysql> desc b2;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | int(11)     | YES  |     | NULL    |       |
| name  | varchar(50) | YES  |     | NULL    |       |
| age   | int(3)      | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
3 rows in set (0.02 sec)

#查看表结构中的数据，发现是空数据
mysql> select * from b2;
Empty set (0.00 sec)
ps2:还有一种做法，使用like(只拷贝表结构，不拷贝记录)

复制代码
mysql> create table b3 like db2.a1;
Query OK, 0 rows affected (0.01 sec)

mysql> desc b3;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | int(11)     | YES  |     | NULL    |       |
| name  | varchar(50) | YES  |     | NULL    |       |
| age   | int(3)      | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
3 rows in set (0.02 sec)

mysql> select * from db3.b3;
Empty set (0.00 sec)

7. 删除表
drop table 表名;

```

#### 数据类型

```js
1.数字
	整型 : tinyint    int    bigint
    		# int 类型后面的存储是显示宽度,而不是存储宽度
    小数 :  float  : 在位数比较短的情况下不精准
    	   double : 在位数比较
           decimal : 如果用小数推荐使用decimal
2.字符串
	char(10) : 简单粗暴,浪费空间,存取速度快
	varchar:  精准, 节省空间, 存取速度慢
	sql 优化: 创键表的时候,定长的类型往前放,变长的往后面放
3.时间类型
	最常用: datetime
    
    # select month(o_time) from t2;
    # select day(o_time) from t2;
    
    # 查看当前月:
    	select month(now())
    
    
4.枚举类型 与 集合类型
	enum 和 set 
    enum 单选 只能在给定的指定范围内选取一个值,如性别sex 男male/女female
	set 多选 在给定的范围内可以选择一个或者一个以上的值(爱好1,爱好2,爱好3)
mysql> create table consumer(
    -> id int,
    -> name varchar(50),
    -> sex enum('male','female','other'),
    -> level enum('vip1','vip2','vip3','vip4'),#在指定范围内，多选一
    -> fav set('play','music','read','study') #在指定范围内，多选多
    -> );
Query OK, 0 rows affected (0.03 sec)


mysql> insert into consumer values
    -> (1,'赵云','male','vip2','read,study'),
    -> (2,'赵云2','other','vip4','play');
Query OK, 2 rows affected (0.00 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> select * from consumer;
+------+---------+-------+-------+------------+
| id   | name    | sex   | level | fav        |
+------+---------+-------+-------+------------+
|    1 | 赵云    | male  | vip2  | read,study |
|    2 | 赵云2   | other | vip4  | play       |
+------+---------+-------+-------+------------+
2 rows in set (0.00 sec)

```

##### 完整性约束

```js
约束条件与数据类型的宽度一样,都是可选参数
作用: 用于保证数据的完整性 和 一致性
PRIMARY KEY (PK)     # 表示该字段为改表的主键,可以唯一的表示记录,非空()提供索引,主键最快, 
	联合主键 primary key(字段1,字段2)
FOREIGN KEY (FK)     # 标识该字段为该表的外键
NOT NULL 		     #  表示该字段的值不能为空
UNIQUE KEY (UK) 	 #  标识该字段的值是唯一的
	联合唯一:
		# unique(字段1,字段2)
        大的数据库(设置联合唯一):   姓和名字分开存
        			ip 和 端口
        
        
        
        
        
AUTO_INCREMENT 		 # 表示该字段的值 自动增长(整数类型, 而且为主键,至少唯一的或主键可以自增)
DEFAULT # 该字段设置默认值
```

```js
# 1. 是否允许为空,默认NULL, 可以设置NOT NULL ,字段不允许为空,必须赋值
```

##### 单表查询

```js
单表查询语法
select 字段1,字段2...from 表名 
					where 条件
					group by field
                      having 筛选
                      order by field 
                      limit 限制条数
###
关键字的执行优先级
from         找到表
where 		拿着where 指定的约束条件,去文件/表中取出一条条记录
group by	将取出的一条条记录分组group by,如果没有 group by ,则
		整体作为一组
having		将分组的结果进行having 过滤
# select		执行select
distinct	去重
order by	排序
limit		限制结果的显示条数
```

```js
(1) where 约束
where 子句中可以使用
1.比较运算符: > < >=  <= <> != # (<> 和 != 是一样的)
2.between 80 and 100: 值在80到100 之间
3.in (80,90,100) 值是10或20或100
4.like "xiaomagepattern"  pattern 可以是%或者_  %表示任意多字符,_表示一个字符
5. 逻辑运算符:在多个条件之间可以使用逻辑运算符  and or not

(2)group by 分组查询
# 首先明确一点:分组发生在where 之后,即分组是基于where 之后的记录而进行的
# 分组指的是:将所有记录按照某个相同字段进行归类,比如针对员工信息表的职位分组,或者按照性别进行分组等等,
# 为何要分组
	取每个部门的最高薪资
    取每个部门的员工数
    取男生数和女生人数
#########
可以按照任意字段分组,但是分组完毕之后,比如group by post,只能查看post 字段,如果向查看组内信息,需要使用聚合函数
(3) 聚合函数
max() 求最大值
min() 求最小值
avg() 求平均值
sum() 求和
count() 求总和个数
# 聚合函数聚合的是组的内容,若是没有分组,则默认一组
# 每个部门有多少员工
select post,count(1) from employee group by post;
# 每个部门的最高薪水
select post,max(salary) from emlpoyee group by post;
# 每个部门的最低薪水
select post,min(salary) from emlpoyee group by post;
# 每个部门的平均薪水
select post,avg(salary) from emlpoyee group by post;
# 每个部门的所有薪水
select post,sum(salary) from emlpoyee group by post;

(4) having 过滤
# !!!执行的优先级从高到低: where > group by > having
# 1 .Where 发生在分组之前,因而Where 中可以有任意字段,但是绝对不能使用聚合函数
# 2.having 放生在分组之后,因而Having 中可以使用分组的字段,无法直接取到其他字段,可以使用聚合函数
1. 查询各岗位内包含的员工个数小于2的岗位名、岗位内包含员工名字、个数
	select count(id),group_concat(name) from employee group by post having count(id) < 2 ;
2. 查询各岗位平均薪资大于10000的岗位名、平均工资
	select post,avg(salary) from employee group by post having avg(salary) > 10000
3. 查询各岗位平均薪资大于10000且小于20000的岗位名、平均工资
	select post,avg(salary) from employee group by post having avg(salary) < 20000 and avg(salary) >10000;
	select post,avg(salary) from employee group by post having avg(salary) between  10000 and 20000;

(5)order by  查询排序
按单列排序
	select * from employee order by age;
	select * from employee order by age ASC,
	select * from employee order by age DESC,
 按多列排序,先按照age 升序排序, 如果年纪相同,则按照id 降序
 	select * from emloyee  order by age ASC,id DESC
(6) limit 限制查询的记录数
    # 显示三条
    select * from employee order by salary DESC LIMIT 3;
	#  默认初始位置为0
	select * from employee order by salary DESC LIMIT 0,5;
	// 从第o开始,即先查出第一条,然后包含这一条找内往后查5条
	select * from employee order by salary DESC limit 5,5;
	// 从第5开始,即先查询出第六条,然后包含这一条在内往后查5条

```

#### 多表查询

```js
我认为如果如果查询结果里面有两个表里的字段,就用连接
如果只有一个表的字段可以用子查询
```

##### 多表连接查询

(1)先看第一种情况交叉连接:不适用与任何匹配条件,生成笛卡尔积(关于笛卡尔积的含义,)

```js
select * from employee,department;
+----+----------+--------+------+--------+------+--------------+
| id | name     | sex    | age  | dep_id | id   | name         |
+----+----------+--------+------+--------+------+--------------+
|  1 | egon     | male   |   18 |    200 |  200 | 技术         |
|  1 | egon     | male   |   18 |    200 |  201 | 人力资源     |
|  1 | egon     | male   |   18 |    200 |  202 | 销售         |
|  1 | egon     | male   |   18 |    200 |  203 | 运营         |
```

(2)内连接: 只连接匹配的行

```js
找两张表的公有部分,相当于利用条件从笛卡尔积结果中筛选出了匹配的结果
```

```js
mysql> select * from employee inner join department on employee.dep_id=department.id;
```

(3)外链接之左连接

```js
以左表为准,即找出所有员工信息,当然包括没有部门的员工
本质就是: 在内连接的基础上增加左边有,右边没有的结果
```

```js
mysql> select * from employee left join department on employee.dep_id=department.id;
+----+----------+--------+------+--------+------+--------------+
| id | name     | sex    | age  | dep_id | id   | name         |
+----+----------+--------+------+--------+------+--------------+
|  1 | egon     | male   |   18 |    200 |  200 | 技术         |
|  5 | nvshen   | male   |   18 |    200 |  200 | 技术         |
|  2 | alex     | female |   48 |    201 |  201 | 人力资源     |
|  3 | wupeiqi  | male   |   38 |    201 |  201 | 人力资源     |
|  4 | yuanhao  | female |   28 |    202 |  202 | 销售         |
|  6 | xiaomage | female |   18 |    204 | NULL | NULL         |
+----+----------+--------+------+--------+------+--------------+
```

(4) 外链接之右连接

```js
以右表为准,即找出所有部门信息,包括没有员工的部门
# 本质就是: 在内连接的基础上增加右边有而左边没有的结果
```

```js
mysql> select * from employee right join department on employee.dep_id=department.id;
+------+---------+--------+------+--------+------+--------------+
| id   | name    | sex    | age  | dep_id | id   | name         |
+------+---------+--------+------+--------+------+--------------+
|    1 | egon    | male   |   18 |    200 |  200 | 技术         |
|    2 | alex    | female |   48 |    201 |  201 | 人力资源     |
|    3 | wupeiqi | male   |   38 |    201 |  201 | 人力资源     |
|    4 | yuanhao | female |   28 |    202 |  202 | 销售         |
|    5 | nvshen  | male   |   18 |    200 |  200 | 技术         |
| NULL | NULL    | NULL   | NULL |   NULL |  203 | 运营         |
+------+---------+--------+------+--------+------+--------------+
```

(4)全外链接: 显示左右两个表全部记录

```js
union join
外链接 : 在内连接的基础上增加左边有右边没有的和右边有而左边没有的
# 注意: mysql 不支持全外链接 full JOIN
# 强调: mysql 可以使用这种方式间接实现全外链接
```

```js
mysql> select *from employee left join department on employee.dep_id = department.id union all select * from employee right join department  on employee.dep_id = department.id;
+------+----------+--------+------+--------+------+--------------+
| id   | name     | sex    | age  | dep_id | id   | name         |
+------+----------+--------+------+--------+------+--------------+
|    1 | egon     | male   |   18 |    200 |  200 | 技术         |
|    5 | nvshen   | male   |   18 |    200 |  200 | 技术         |
|    2 | alex     | female |   48 |    201 |  201 | 人力资源     |
|    3 | wupeiqi  | male   |   38 |    201 |  201 | 人力资源     |
|    4 | yuanhao  | female |   28 |    202 |  202 | 销售         |
|    6 | xiaomage | female |   18 |    204 | NULL | NULL         |
| NULL | NULL     | NULL   | NULL |   NULL |  203 | 运营         |
+------+----------+--------+------+--------+------+--------------+
```

##### 符合条件连接查询

```js
示例一:
	以内连接的方式查询employee 和 department 表, 并且employee 表中的age 字段值必须大于25,即找出年龄大于25岁的员工以及员工所在的部门
mysql> select * from employee  inner join department on employee.dep_id = department.id where age>25;

实例二:
	以内连接的方式查询employee和department表，并且以age字段的升序方式显示。
	mysql> select * from employee inner join department on employee.dep_id=department.id order by age;
+----+---------+--------+------+--------+------+--------------+
| id | name    | sex    | age  | dep_id | id   | name         |
+----+---------+--------+------+--------+------+--------------+
|  1 | egon    | male   |   18 |    200 |  200 | 技术         |
|  5 | nvshen  | male   |   18 |    200 |  200 | 技术         |
|  4 | yuanhao | female |   28 |    202 |  202 | 销售         |
|  3 | wupeiqi | male   |   38 |    201 |  201 | 人力资源     |
|  2 | alex    | female |   48 |    201 |  201 | 人力资源     |
+----+---------+--------+------+--------+------+--------------+
5 rows in set (0.00 sec)
```

##### 子查询

```js
(1) 子查询是将一个查询语句嵌套在另一个查询语句中
(2) 内层查询语句的查询结果,可以为外层查询语句提供查询条件
(3) 子查询中可以包括: in , not in , any, all, exist 和 not exists 等关键字
(4) 还可以包含比较运算符: = , !=, >, < 等
```

例子:

```js
(1) 带 in 关键字的子查询
# 查询平均年龄在25岁以上的部门名
	// 内连接  如果用 department.id 进行分组拿不到名字
	mysql> select department.name ,avg(age) from employee inner join department on department.id = employee.dep_id group by department.name having avg(age) >25;
+--------------+----------+
| name         | avg(age) |
+--------------+----------+
| 人力资源     |  43.0000 |
| 销售         |  28.0000 |
+--------------+----------+
    // 子查询 
	select id,name from department where id in (select department.id from department inner join employee on department.id = employee.dep_id group by department.id having avg(age)>25)
# 查看技术部门员工姓名
	mysql> select name from employee where dep_id = (select id from department where name="技术");
+--------+
| name   |
+--------+
| egon   |
| nvshen |
+--------+
# 查看不足一人的部门名

mysql> select name from department where id not in (select dep_id from employee group by dep_id )
    -> ;
+--------+
| name   |
+--------+
| 运营   |
+--------+
// 下面这个查询有错误
select name from department where id in (select dep_id from employee group by dep_id having count(1)<1 )
```

```js
(2) 带比较运算符的子查询
# 比较运算符: = , != ,>, < ,>=,<=,<>
# 查询大于所有人平均年龄的员工与年龄
	mysql> select name,age from employee where age > (select avg(age) from employee);
+---------+------+
| name    | age  |
+---------+------+
| alex    |   48 |
| wupeiqi |   38 |
+---------+------+
2 rows in set (0.03 sec)

# 查询大于部门内平均年龄的员工名与年龄
mysql> select * from employee inner join (select dep_id,avg(age) as avg from employee group by dep_id) as e on e.dep_id = employee.dep_id where age > avg;
+----+------+--------+------+--------+--------+---------+
| id | name | sex    | age  | dep_id | dep_id | avg     |
+----+------+--------+------+--------+--------+---------+
|  2 | alex | female |   48 |    201 |    201 | 43.0000 |
+----+------+--------+------+--------+--------+---------+
1 row in set (0.00 sec)
```

```js
(3)带exist 关键字的子查询
# exist 关键字代表存在,在使用Exist 关键字的时候,内层查询语句不反悔查询的记录,而是返回一个真假值.True 或False 
# 当返回True 时外层语句进行查询;当返回值位False 时,外城查询语句不进行查询
```

```js
# 查询每个部门最新入职的那位员工
select * from employee inner join
 (select depart_id,max(hire_date) as f 
from employee group by depart_id  ) as e 
 on e.depart_id = employee.depart_id and 
employee.hire_date = f;


select * from employee as t1
inner join
(select post,max(hire_date) as new_date from employee group by post) as t2
on t1.post=t2.post
where t1.hire_date=t2.new_date;
```



#### MySQL  创建用户和授权

##### 1. 权限管理

(1) 创建当前用户和密码

```js
1. 进入到mysql 数据库下
    mysql> use mysql;
    Database changed
2. 对新用户增删改查
	(1) 创建用户
	// 指定ip 192.168.13.167 的 alex 用户登录
	create user "alex"@"192.168.13.167" identified by "123"
	// 指定ip 192.168.13.%  开头的yuan 用户登录
	create user "yuan"@"192.168.13.%" identified by "yaun1234"
	// 指定任何ip的yuan 用户登录
	create user "yuan"@"%" identified by "yuan1234"
	mysql> select  user,host from user
    +---------------+----------------+
    | user          | host           |
    +---------------+----------------+
    | yaoshang      | %              |
    | alex          | 192.168.13.167 |
    | mysql.session | localhost      |
    | mysql.sys     | localhost      |
    | root          | localhost      |
    +---------------+----------------+
    (2) 删除用户
    drop user "用户名"@"IP地址"
	drop user "yuan"@"192.168.13.167"
	(3) 修改用户
    rename user "用户名"@"ip地址" to "新的用户名"@"ip地址";
	(4) 修改密码
    set password for "用户名"@"ip地址"=Password("新密码")
```

(2)给当前的用户授权

```js
(1) 查看权限
show grants for "用户名"@"IP地址"
(2) 授权yuan 用户仅对yuan.employee 文件的查询,插入权限和更新操作
grant select,update,insert on yuan.employee  to "yuan"@"%"
(3) 表示所有的权限,除了grant 这个命令这个命令是root才有的
// 授权yuan 用户对yuan 数据库empolyee表 的 所有权限
grant all privileges yuan.employee to 'yuan'@"%";
// 授权yuan 用户yuan 对 yuan数据库的所有操作
grant all privileges yuan.* to "yuan"@"%";
// 授权yuan 用户所有数据的中文件有任何操作
grant all privileges  *.* to "yuan"@"%";

# 取消权限
// 取消yuan 用户 对 db1 的 t1 文件的任意操作
revoke all on db1.t1 from "yuan"@"%";
// 


```



(3)移除当前用户

#### pymysql 模块的使用

##### pymysql  的下载和使用

```js
(1)pymysql 模块的下载
pip3 install pymysql
(2) pymysql 的使用
# 实现: 使用Python 实现 用户登录,如果用户存在则登录成功(假设该用户已在数据库中)
import pymysql
user = input("请输入用户名")
pwd = input("请输入密码")
# 1. 连接
conn = pymysql.connent(host="127.0.0.1",port=3306,user="root",password='',db="db8",charset="utf8")

# 2. 创建游标
cursor = conn.cursor()
# 注意%s 需要加引号
sql = "select * from userinfo where username='%s'  and pwd = '%s' %(user,pwd)
"
print(sql)
# 3. 执行sql 语句
cursor.execute(sql)
result = cursor.execute(sql)  # 执行sql 语句,返回sql 查询成功的记录数目
print(result)
# 关闭连接,游标和连接都需要关闭
cursor.close()
conn.close()
if result:
    print("登录成功")
else:
	print("登录失败")

```



##### execute() 之注入

##### 增删改conn.commit()

```js
commit() 方法: 在数据库里面增,删,改 的时候,必须要进行提交,否则插入的数据不生效.
import pymysql
username =  input("请输入用户名")
pwd = input("请输入密码")
# 连接
conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="",db="db8",charset="utf8")

# 创建游标
cursor=conn.cursor()

# 操作
# 增
sql = 'insert into userinfo (username,pwd) values (%s,%s)'
effect_row = cursor.execute(sql,(username,pwd))
// 同时插入多条数据
curson.exectemany(sql,[('yuan',"yuan1234"),("haha","123")])

# 删
sql = 'delete from userinfo where id = 2'
curson.execute(sql)
# 改
sql = "update userinfo set username = %s  where id = 2"
effect_row = cursor.execute(sql,username)
print(effect_row)

#########一定要commit
conn.commit()

# 关闭游标
curson.close()

# 关闭连接
conn.close()

############查
fetchone(): 获取下一行数据,第一次为行首;
fetchall(): 获取所有行数据源
fetchmany(4): 获取 4 行数据
```

##### 查: fetchone ,  fetchmany, fetchall

#### 索引

```js
1. 索引的介绍
数据库中专门用于帮助用户快速查找数据的一种数据结构,类似于字典中的目录,查找字典内容内容时可以根据目录查找到数据的存放位置,然后直接获取
2. 索引的作用
约束和加速查找
3.常见的几种索引:
- 普通索引
- 唯一索引
- 主键索引
- 联合索引(多列)
	- 联合主键索引
	- 联合唯一索引
	- 联合普通索引

无索引 : 从前往后一条一条的查询
有索引 : 创建索引的本质,就是创建额外的文件(某种格式存储,查询的时候,先去额外的文件找,定好位置,然后再去原始表中直接查询,但是创建索引越多,会对硬盘也是有损耗)

建立索引的目的:
a . 额外的文件保存特殊的数据结构
b . 查询快,但是插入, 更新, 删除依然慢
c . 创建索引之后,必须命中索引才能有效

索引的种类:
	hash类型的 索引:	 查询单条快,范围查询慢
	btree类型的索引: b+树, 层数越多,数据量指数级增长(我们就用它,因为innodb默认支持它)
```

```js
# 普通索引:
// 作用: 仅有一个加速查找
// 创建表 + 普通索引
create table userinfo(
nid int not null auto_increment primary key,
name varchar(32) not null,
email varchar(64) not null,
index ix_name(name)
);
// 标建立之后想给他加索引
// 创建索引  (真的快很多)
create index 索引的名字 on 表名(列名)
// 删除索引
drop index 索引的名字 on 表名
// 查看索引
show index from 表名\G;

# 唯一索引
// 作用: 加速查找和唯一约束(可含null)
// 创建表 + 唯一索引
create table userinfo(
    id int not null auto_increment primary key,
    name varchar(32) not null,
    email varchar(64) not null,
    unique index ix_name(name)
)
// 创建唯一索引
create unique index 索引名 on 表名(列名)
// 删除唯一索引
drop index 索引名 on 表名

# 主键索引
// 作用 : 加速查找和唯一约束(不含null)
// 创建表+主键索引
create table userinfo(
				`加上primary key 就可以`
                   id int not null auto_increment primary key,
                   name varchar(32) not null,
                   email varchar(64) not null,
                   unique  index  ix_name(name)
           )
          or
           create table userinfo(
                   id int not null auto_increment,
                   name varchar(32) not null,
                   email varchar(64) not null,
                   primary key(nid),
                   unique  index  ix_name(name)
         )
 // 创建索引
alter table 表名 add primary key(列名);
// 删除主键索引
alter table 表名 drop primary key;
// 修改数据类型
alter table 表名 modify 列名 int,drop primary key;
// 
alter table 表名 change
# 组合索引
组合索引是将n个列组合合成一个索引
应用场景:频繁的同时使用n 列来进行查询,如: where name = "alex" and email = "alex@qq.com"
// 创建索引
create index 索引名 on 表名(列名1,列名2)
```

```js
索引名词:
// 覆盖索引:在索引文件中直接获取数据
	# name 是 设置的索引, 直接从索引表里面拿出来.速度很快
 	例如: select name from userinfo where name="alex11111"
// 索引合并:把多个单列索引合并使用
	select * from userinfo where name="alex123" and id=13131;
```

```js
正确使用索引的情况:
(1) 创建索引
(2) 命中索引
(3) 正确使用索引

// 以下都是不正确使用索引的情况
# 1.使用模糊查询最好使用后置，前置会大大降低效率
- like "%xx" 可以用a% 不能用%a
	select * from userinfo where name like "%al"
- 使用函数 avg(num)  > 1
	// 查询出name 然后翻转在进行匹配
	select * from userinfo where reverse(name) = "alex123"
- or
	select * from userinfo where id = 1 or email = 'alex122@oldbody';
	# 如果使用了or 那么条件中都必须必须是索引
- 类型不一致
	如果列是字符串类型,传入条件是用引号引起来,不然
- !=
   select * from userinfo where name != "alex"
	特别的:如果是主键,则还是会走索引
-  >
   select * from userinfo where name > "alex"
   特别的:如果主键或索引是整数类型,则还是会走索引
- order by 
	select email from userinfo order by name desc;
	当根据排序时候,选择的映射如果不是索引,则不走索引
	特别的: 如果对主键排序,则还是走索引
	select * from userinfo order by nid desc;
- 组合索引最左前缀
	如果组合索引为(name,email)
	name and email -- 使用索引
     name            -- 使用索引
	email          -- 不使用索引

```

```js
最左前缀匹配:
	create index ix_name_email on userinfo(name,email);
	select * from userinfo where name="yuan";
	select * from userinfo where name='yuan' and "email"="123";
	select * from userinfo where email ="alex@oldboy"
如果使用组合索引如上, name 和 email 组合索引之后,查询
	(1) name 和 email ---使用索引
	(2) name  --- 使用索引
	(3) email --- 不合适索引
# 对于同时搜索n个条件时,组合索引的性能好于多个单列索引
### 组合索引的性能 > 索引合并的性能 ###
```

```js
索引的注意事项
(1) 避免使用select * 
(2) count(1) 或count(列) 代替count(*)
(3) 创建表时尽量使用char 代替 varchar
(4) 表的字段顺序固定长度的字段优先
(5) 组合索引代替多个单列索引(经常使用多个条件查询时)
(6) 尽量使用段索引（create index ix_title on tb(title(16));特殊的数据类型 text类型）
(7) 使用join 来代替子查询
(8) 连表的时候注意条件类型需一致
(9) 索引散列(重复少)不适用于建索引,例如:性别不合适
```



```js
1、自行创建测试数据

2、查询“生物”课程比“物理”课程成绩高的所有学生的学号。ps：针对的是自己的生物成绩比物理成绩高,再把符合条件的学生的学号查出来；

select * from (select * from score where course_id = 1) as t1 right join  (select * from score where course_id = 2) as t2 on  t1.student_id = t2.student_id  where t1.num > t2.num;

3、查询平均成绩大于60分的同学的学号和平均成绩； 

select student_id,avg(number) as avg from score group by student_id having avg>60 ; 

4、查询所有同学的学号、姓名、选课数、总成绩；

select sname,sid,c,s from student left join 
(select student_id,count(1) as c ,sum(num) as s from score group by student_id) as t1 on t1.student_id = student.sid;

5、查询姓“李”的老师的个数； # 模糊查询 用 like

select count(1) from teacher where tname like "李%";

6、查询没学过“李平”老师课的同学的学号、姓名；
`
思路:
	先查到"李平老师"教的所有课程的id
	然后查到上过李平老师的学生id
	然后学生表中筛选
`
select * from student where sid not in (select student_id from score where course_id  in (select cid from course where teacher_id = (select tid from teacher where tname="李平老师")) 
group by student_id);

7、查询学过“001”并且也学过编号“002”课程的同学的学号、姓名；

select sname,sid from student inner join (select student_id,count(1) from score where course_id in (1,2) group by student_id having count(1)>1)  as t1 on t1.student_id = student.sid 

8、查询学过“李平老师”老师所教的所有课的同学的学号、姓名；
select sname,sid from student inner join (select student_id from score where course_id in 
(select cid from course where teacher_id = (select tid from teacher where tname = "李平老师") )group by student_id having count(1)>1) as
t1 on t1.student_id = student.sid ;

9、查询课程编号“002”的成绩比课程编号“001”课程低的所有同学的学号、姓名；

select *  from (select * from score where course_id = 1)  as t1 inner join
(select * from score where course_id = 2 )  as  t2 on  t1.student_id = t2.student_id where t2.num > t1.num ;

10、查询有课程成绩小于60分的同学的学号、姓名；

11、查询没有学全所有课的同学的学号、姓名；

12、查询至少有一门课与学号为“001”的同学所学相同的同学的学号和姓名；

13、查询至少学过学号为“001”同学所选课程中任意一门课的其他同学学号和姓名；

14、查询和“002”号的同学学习的课程完全相同的其他同学学号和姓名；

15、删除学习“叶平”老师课的SC表记录；

16、向SC表中插入一些记录，这些记录要求符合以下条件：①没有上过编号“002”课程的同学学号；②插入“002”号课程的平均成绩； 

17、按平均成绩从低到高显示所有学生的“语文”、“数学”、“英语”三门的课程成绩，按如下形式显示： 学生ID,语文,数学,英语,有效课程数,有效平均分；

18、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；

19、按各科平均成绩从低到高和及格率的百分数从高到低顺序；

20、课程平均分从高到低显示（现实任课老师）；

21、查询各科成绩前三名的记录:(不考虑成绩并列情况) 

22、查询每门课程被选修的学生数；

23、查询出只选修了一门课程的全部学生的学号和姓名；

24、查询男生、女生的人数；

25、查询姓“张”的学生名单；

26、查询同名同姓学生名单，并统计同名人数；

27、查询每门课程的平均成绩，结果按平均成绩升序排列，平均成绩相同时，按课程号降序排列；

28、查询平均成绩大于85的所有学生的学号、姓名和平均成绩；

29、查询课程名称为“数学”，且分数低于60的学生姓名和分数；

30、查询课程编号为003且课程成绩在80分以上的学生的学号和姓名； 

31、求选了课程的学生人数

32、查询选修“杨艳”老师所授课程的学生中，成绩最高的学生姓名及其成绩；

33、查询各个课程及相应的选修人数；

34、查询不同课程但成绩相同的学生的学号、课程号、学生成绩；

35、查询每门课程成绩最好的前两名；

36、检索至少选修两门课程的学生学号；

37、查询全部学生都选修的课程的课程号和课程名；

38、查询没学过“叶平”老师讲授的任一门课程的学生姓名；

39、查询两门以上不及格课程的同学的学号及其平均成绩；

40、检索“004”课程分数小于60，按分数降序排列的同学学号；

41、删除“002”同学的“001”课程的成绩；


```

##### DDL DML DCL语句

```js
DDL: 数据库定义语言: 数据库,表,视图, 存储过程,例如create drop truncate
DML: 数据库操纵语言: 插入数据insert 删除delete 更新update
DCL:数据库控制语句: 例如控制用户的访问权限,GRANT,REVOKE
```



关系型数据库

```js
oracle : 收费
mysql :  版本数据库 5.7 / 8.0 /5.6

	- innodb
		- 支持事务
			crm 分配学员  勾选属于我的学员那, 把这些学员查询来, 然后把这些学员设置为我
		- 行级锁
			
		- 支持外键  # 建表
            create table 表名(
            字段名   数据类型(长度) 约束,
             uid int,
             foreign key uid references user(ui)
            on update cascade
            )
     - myisam (在mysql 5.5 以前默认是myisam )
		# 查询速度和insert的速度都很快
        - 表级锁 : 对高并发的大量修改没有优势
        - innodb 支持的都不支持
  	- memory
		断电消失
	- blackhole
		往里面写什么什么没有
		# 多级主从复制, 
```

```js
事务:
begin;
select * from  app01_book where nid = 1 for update;
update 表 set 字段=值 where 条件;
commit; # 如果我不commit 提交, 



# 只有在需要先查找, 再更新的时候 时候需要事务


```



非关系型数据库

```js
存取速度快, 但是不能进行表与表之间的关联查询
mongdb 
redis
	#  在那个项目里使用路飞:
    	客户浏览记录:  user_id
    #  为什么存在redis里面:	因为查取速度快
    

```

```js
数据类型:
    数字
    	int
        float
    字符串
    	char(4) 定长:存取快  浪费空间  提倡
        varchar(4)  变长:存取慢, 节省空间
    时间
        datetime
        timestamp
        year date time
    枚举和集合
    	enum  枚举单选
        	create table t(gender enum('male','female'))
        set 集合多选去重
        	create table t(hobby set('抽烟','喝酒'))
            
       
# 约束条件
非空 not null
默认值 default
唯一 unique
	- 联合唯一  unique(字段1,字段2)  会议时预定, 如果room_id 和 time_id
    # 班级表里面 如果校区, 时间, 
	- 唯一 int 自增 auto_increment
 主键  primary key (非空 + 唯一)  
	 
```

























