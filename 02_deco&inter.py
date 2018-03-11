# coding = utf-8
"""
浅copy是对一个对象的顶层拷贝，拷贝的引用，并没有拷贝内容
深copy 是对一个对象所有层次的拷贝

注意点： 对于可变类型 copy和deepcopy都是新建一个对象（id不一样）
对于不可变类型的如tuple copy是同一个对象（id和原来的一样）
deepcopy是不同的对象
"""

"""
可迭代对象：能放在for  in语句中，能够每次取出一条数据提供我们使用的对象，都是可迭代对象

具备了__iter__方法的对象，就是可迭代对象

一个实现了__iter__方法和__next__方法的对象就是迭代器
"""


class Mylist(object):  # 自定义一个迭代器
    def __init__(self):
        self.container = []
        self.i = 0

    def add(self, item):
        self.container.append(item)

    def __next__(self):
        if self.i < len(self.container):
            item = self.container[self.i]
            self.i+= 1
            return item
        else:
            raise StopIteration

    def __iter__(self):
        return self

# p = Mylist()
# p.add(1)
# p.add(2)
# p.add(3)
# for num in p:
#     print(num)

"""
迭代器的应用场景：对于大规模，有规律的，根据特定的数学计算方式现场生成，不用保存数据，节省空间 eg：菲波拉契数列
对于小规模，但用列表推导式描述不出来，通过迭代方式遍历
"""

# def fib(n):
#     num1 = 0
#     num2 = 1
#     i = 0
#     while i < n:
#         print(num1)
#         num1,num2 = num2, num1+num2
#         i += 1

# if __name__ == '__main__':
#     fib(8)
def fibo(num):
    numlist = [0, 1]
    for i in range(num-2):
        numlist.append(numlist[-2] + numlist[-1])
    return numlist

# print(fibo(8))
"""
生成器：一种特殊的迭代器
创建生成器的两种方式
①把一个列表生成的[]该成（）
②在函数中加入yield关键字，加入了yield关键字的函数不再是函数，而是生成器

"""
# 1创建生成器的两种方式 把一个列表生成的[]该成（）
l = [i*2 for i in range(5)]
g = (i*2 for i in range(5))
# l是一个列表，g是一个生成器，对于生成器，可以通过next()方法，for循环，list（）等使用
"""
yield理解：遇到yield关键字后，代码会暂停执行，使用next()方法，让生成器从断电处继续执行，
使用send()函数唤醒生成器，好处：唤醒的同时，可以像断点处传入一个附加数据
"""

def fib(n):
    num1 = 0
    num2 = 1
    i = 0
    while i < n:
        yield num1
        num1,num2 = num2, num1+num2
        i += 1

gen_obj = fib(5)
# print(gen_obj.__next__())
# print(gen_obj.__next__())
# print(gen_obj.__next__())
# print(gen_obj.__next__())
# print(gen_obj.__next__())
#
# print(gen_obj.__next__())

'''
闭包：函数里面再定义一个函数，并且内部函数用到了外部函数的变量，这个函数以及用到的变量，称为闭包

作用：提高代码复用性

闭包修改外部函数的变量，需要在内层声明 nonloal (python3的方法）
python2/3通用方法
如果外部变量是可变类型，可以直接修改，不用声明
如果不是可变类型，可以把外部变量变成可变类型，然后直接修改
'''
def outer(number):
    def inner(number_in):
        print('in inner函数，number_in is %d' %number_in)
        return number + number_in
    return inner

# ret = outer(20)
# print(ret(100))
"""
LEGB规则 locals -> enclosing function -> globals -> builtins
locals : 当前的命名空间（如：函数，模块）函数的参数也属于命名空间内部的变量
enclosing: 外部嵌套函数的，命名空间
globals: 全局变量，函数定义所在模块的命名空间
builtins: 内建模块的命令空间
"""
"""
装饰器：实际是一个闭包函数，它可以让其他方法在不需要做任何变动的情况下增加额外的功能
它经常用于切面的需求：
引入日志
函数执行时间统计
权限校验
事物处理

装饰器的可变参数：装饰器的参数与调用者传的参数不匹配

wraps()函数 因为被装饰的的函数的函数名和属性发生变化，所有使用该方法消除这样的副作用
"""
import functools
def decorator(fun):
    @functools.wraps(fun)
    def inner(*args, **kwargs):
        fun(*args, **kwargs)
    return inner
