# coding=utf-8
from celery import Celery

# 创建celery应用对象
app = Celery('tasks',  # 模块名
             backend='redis://127.0.0.1:6379/1',
             broker='redis://127.0.0.1:6379/0')

# 表示，下面的任务由app这个对象来进行管理
@app.task
def my_task(a,b):
    print ('任务函数正在执行')
    return a+b

