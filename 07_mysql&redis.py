
# def count():
#     fs = []
#     print(fs)
#     for i in range(1,4):
#
#         def f():
#             return i*i
#         fs.append(f)
#         print(fs)
#     return fs
#
# ff = count()
#
# for f in ff:
#     # print(count())
#     print(f())

'''
使用python操作数据库的流程（步骤）
'''

'''
python操作mysql步骤
'''

# 1、引入模块
from pymysql import *
# 2、创建connecti对象--用于创建与数据库的连接
conn = connect('参数列表')

# 参数
# 参数host：连接的mysql主机，如果本机是'localhost'
# 参数port：连接的mysql主机的端口，默认是3306
# 参数database：数据库的名称
# 参数user：连接的用户名
# 参数password：连接的密码
# 参数charset：通信采用的编码方式，推荐使用utf8

# 3、创建cursor对象---用于执行sql语句
cs = conn.cursor()

# 4、执行查询，执行命令、获取数据、处理数据

# 5、关闭游标
cs.close()

# 6、关闭连接
conn.close()


'''
python操作mongo的步骤
'''
# 1、引入pymonogo
from pymongo import *
# 2、连接Monogodb
client = MonogoClient('主机ip',端口)
#3、获取仓库
db = client.仓库名称  # 直接协仓库名称
# 4、获取集合对象
col = db.集合名称


'''
python操作redis

'''
# 1、引入模块
from redis import *

# 2、创建StrictRedis对象，与redis服务器建立连接
sr = StrictRedis()

# 3、获取数据、进行数据操作

