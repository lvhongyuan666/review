# 不定常参数的问题
def foo(x, *args):
    print(x)  # 1
    print(*args)  # 2 3 4

# foo(1,2,3,4)

def fun(*args, **kwargs):
    print(args) # (1,2)
    print(kwargs)  # {'b': 4, 'a': 3}

# fun(1,2,a = 3, b = 4)


# a = 100
# def add():
#     b = 10
#     sum = a + b
#     print(sum)
#
# add()

a = 100
def add():
    global a
    a = 200
    print(a)
#
# add()

'''
内存管理：
1、小整数对象池：[-5, 256]这些对象被提前建立好，不会被垃圾回收
在这个范围内的整数，共用同一个对象
单个字母，也共用对象

2、大整数对象池：每一个大整数，均创建一个新的对象

3、intern机制：每个单词，默认开启intern机制，共用对象


小整数[-5,256]共用对象，常驻内存
单个字符共用对象，常驻内存
单个单词，不可修改，默认开启intern机制，共用对象，引用计数为0，则销毁

'''

'''
垃圾回收：
引用计数为主，分代收集机制为辅

'''