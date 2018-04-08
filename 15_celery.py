# coding=utf-8

'''
celery 简介
clery是一个异步的消息队列
适用于异步处理问题，当发送邮件，上传文件，图像处理等一些较耗时的操作时，我们可以将异步执行，这样用户不用等待太久，提高用户体验

celery通过消息进行通讯 client 发出消息到队列中，broker将队列中的信息派发给worker来处理
client --- broker (任务队列） --- worker
任务的发出者   中间人           任务的处理者
'''


'''
client客户端和celery（worker）执行的是同一段代码
client --  我们的django框架程序是client 任务的发出者  --创建任务 send_mail()
broker -- 可选择RabbitMQ redis   存储任务的名字（标识）  存储send_mail
worker(celery) -- 任务的处理者  同样的send_mail（）的代码

backend -- 返回任务的执行结果   选择数据库存储结果
'''

'''
多任务进行 默认是以多进程的方式 创建2个进程  支持协程
'''