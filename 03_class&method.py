'''
理解面向对象：
一种软件开发方法，是一种思想紧急
优点：
① 将数据和业务抽象为对象，有利于程序整体结构的分析和设计，使设计思路更清晰
②事物以对象为单位，各自完成任务，减少代码耦合度

'''
'''
类：是定义了某个事物应该是什么样，具体来讲，也就是说该事物具有那些行为和属性

对象：某一个具体存在的事物
类就是创建对象的模板
类的构成：类名、类的属性、类的方法

对象包含两部分：属性和方法
属性：用于记录和对象相关的数据 eg：姓名、年龄、肤色
方法：用于实现与对象相关的操作 eg：睡觉、吃饭、唱歌
'''

'''
魔法方法： 在python中方法如果是以双下划线开头以双下划线结尾的，那么就有特殊的功能
__init__() 初始化方法，用来完成一些默认值的设定，实例创建完成后自动被调用
__str__()  如果实例对象想输入print一些内容的时候，可以在类内部增加此函数，返回一个字符串（即：输出内容）
或者  当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
__del__()  析构方法，删除实例时调用

'''

'''
保护对象数据
①以单下划线开头的，from import * 禁止导入

②以双下划线开头的属性和方法是私有属性或方法，属性私有就不能直接访问或赋值，可以使用get和set方法进行访问和赋值
目的：可以精确控制变量的读写访问权限
@property成为属性函数，可以对属性赋值时做必要的检查，并保证代码的清晰短小---升级get、set方法
'''

class Phone(object):
    def __init__(self):
        self.A = 10
        self.__B = 20

p = Phone()
print(p.A)
# 访问B失败，不能直接访问私有属性
print(p.__B)

# 添加get方法，可以访问私有属性
# class Phone(object):
#     def __init__(self):
#         self.A = 10
#         self.__B = 20
#
#     def get(self):
#         return self.__B
#
# p = Phone()
# print(p.get())

class Money(object):
    def __init__(self):
        self.__money = 0

    @property
    def money(self):
        return self.__money

    @money.settero
    def money(self, value):
        if isinstance(value,int):
            self.__money = value
        else:
            print('error:不是整形数字')

# a = Money()
# a.money = 100
# print(a.money)