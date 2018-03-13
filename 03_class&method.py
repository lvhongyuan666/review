'''
面向对象的理解
以对象为单位，对象各自完成任务
'''
"""
类：定义了某些事物应该是什么样，也就是说事物具有哪些行为和属性
它是一种抽象的定义，并不是某个具体的事物

对象：某一个具体存在的事物，
类就是创建对象的模板
对象包含两个部分
①属性：用于记录和对象相关的数据 eg：姓名、年龄、肤色
②方法：用于实现和对象的相关操作 eg: 吃饭、睡觉、唱歌等

类的构成：类名、类的属性、类的方法
"""

"""
魔法方法：python中以双下划线开头，以双下划线结尾的方法，都是魔法方法

__init__()方法，初始化方法，在创建一个对象时默认被调用，不需要手动调用
作用：初始化方法，用来完成一些默认值的设定
当创建一个对象后，python解释器会默认调用__init__()方法

__del__()方法：析构方法 当删除一个对象时，python解释器会，默认调用的方法


"""

class Animal(object):

    # 初始化方法，创建完对象后会自动被调用
    def __init__(self, name):
        print("__init__方法被调用")
        self.__name = name


    #  析构方法，当对象被删除时，会自动被调用
    def __del__(self):
        print("__del__方法被调用")
        print('%s对象马上被干掉了' %self.__name)

# # 创建对象
# dog = Animal('哈巴狗')
#
# # 删除对象
# del dog
'''
__str__()和__repr__()方法
当使用print输出对象的时候，只要定义了这个方法，那么就会打印从这个方法返回的数据
'''
class Person(object):

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return '%s 是个美丽的girl'%self.name

    def __repr__(self):
        return '%s 是个漂亮的girl'%self.name

p = Person('吕小小')

print(p)
print(p)
