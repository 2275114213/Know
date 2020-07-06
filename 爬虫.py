# - 为什么原生的scrapy不能实现分布式?
'''
- 调度器不能被共享
- 管道也无法被共享
'''
# - scrapy-redis 组件的作用
'''
 - 提供了可以被共享的调度器和管道
'''
# - 分布式经典流程
'''
- 为什么原生的scrapy不能实现分布式?
    - 调度器不能被共享
    - 管道无法被共享

- scrapy-redis组件的作用是什么?
    - 提供了可以被共享的调度器和管道

- 分布式爬虫实现流程
1.环境安装:pip install scrapy-redis
2.创建工程
3.创建爬虫文件:RedisCrawlSpider  RedisSpider
    - scrapy genspider -t crawl xxx www.xxx.com
4.对爬虫文件中的相关属性进行修改:
    - 导报:from scrapy_redis.spiders import RedisCrawlSpider
    - 将当前爬虫文件的父类设置成RedisCrawlSpider
    - 将起始url列表替换成redis_key = 'xxx'(调度器队列的名称)
5.在配置文件中进行配置:
    - 使用组件中封装好的可以被共享的管道类:
        ITEM_PIPELINES = {
            'scrapy_redis.pipelines.RedisPipeline': 400
            }
    - 配置调度器(使用组件中封装好的可以被共享的调度器)
        # 增加了一个去重容器类的配置, 作用使用Redis的set集合来存储请求的指纹数据, 从而实现请求去重的持久化
        DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
        # 使用scrapy-redis组件自己的调度器
        SCHEDULER = "scrapy_redis.scheduler.Scheduler"
        # 配置调度器是否要持久化, 也就是当爬虫结束了, 要不要清空Redis中请求队列和去重指纹的set。如果是True, 就表示要持久化存储, 就不清空数据, 否则清空数据
        SCHEDULER_PERSIST = True

     - 指定存储数据的redis:
        REDIS_HOST = 'redis服务的ip地址'
        REDIS_PORT = 6379

     - 配置redis数据库的配置文件
        - 取消保护模式:protected-mode no
        - bind绑定: #bind 127.0.0.1

     - 启动redis

6.执行分布式程序
    scrapy runspider xxx.py

7.向调度器队列中仍入一个起始url:
    在redis-cli中执行:lpush 队列名 起始url
    
'''










'''
spider.py : 发送请求,请求对象的封装
        - 产生一个或一批url
        - 封装成请求对象, 传递给引擎
引擎将请求对象传递给调度器, (调度器里面有队列, 里面存的就是请求对象, 调度器可以去重将重复的请求对象过滤出去,放到队列里面)

调度器将请求对象调度出来, 然后交给引擎,引擎交给下载器, 下载器去互联网下载


互联网封装成response 给下载器,下载器给引擎, 引擎给spider解析(parse(response)),


解析完了之后给item , item 给引擎然后引擎给管道,持久化等
                作用
spider.py: - 产生一个或一批url
           - 封装成请求对象, 传递给引擎
调度器 :从队列中调度请求,进行数据下载,可以去重

下载器: 进行下载

管道:进行持久化

引擎作用: 用来处理整个系统的数据流, 触发事务
'''