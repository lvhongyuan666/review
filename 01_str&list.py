# -*- coding:utf-8 -*-

'''
1,字符串 （str） 不可变类型的数据

定义：用‘’或“”包裹的字符

运算： + *

使用[]提取字符
a = '123' print(a[0])  输出 1

切片 [start:end:step]
step 步长为正，则从前往后切，否则从后往前切
[:] 表示切整串
'''
#python的内置函数--字符串操作
#find rfind 查找子串在字符串中第一次出现的位置 返回下标
a = '1234512'
# print(a.find('1')) -- 0

# strip（）清除两侧字符，默认清除空格
a.lstrip('1')  # 清除字符串a左边的1

# 1.14.5.7 字符串对齐
# # 使用center()、ljust()、rjust()可以在指定长度的空间中，居中，左对齐，右对齐。
# print(a.center(20, '#') ) --> ######1234512#######  以20个#宽度居中

# 1.14.5.8 字符串大小写
# 让字符串首字母变成大写可以使用capitalize()函数,让所有的单词的开头字母变成大写，使用title()函数，让所有字母变成大写使用upper()函数，让所有单词变成小写使用lower()函数，
b = 'hello world'
# print(b.upper())
# print(b.capitalize())
# print(b.title()) -- >   Hello World


# 1.14.5.9 使用partition()函数
# 使用partition(str)函数可以将字符串分成三部分，str之前，str和str之后。
#
# 1.14.5.10 使用isalpha()和isdigit()函数
# isalpha()函数可以检测字符串是否都是字母，如果都是字母则返回True，否则返回False.
# isdigit()函数可以检测字符串是否都是数字，如果是则返回True,否则返回False.
# isalnum()函数检测字符串是否由字母和数字组成.
# isspace()函数检测字符串是否全是空格.
# 1.14.5.11 使用count()函数
# 使用count(str)可以统计字符串str出现的次数。
# print(a.count('1'))  --> 2 表示1字符在a中出现2次
'''
2、 list 合利用顺序和位置定义某中种元素，尤其是当元素的顺序和位置经常发生改变的时候
列表中的元素可以是不同类型的 li = [1,'a']
查找时元素，时间复杂度是O(n)
'''

# 使用[] 获取元素
# a = [1,2,3] a[0] --> 1


d = [6, 7, 8, 9]
# c.append('a')
# print(c)
# extend() 合并列表 相当于 c+= d
# c.extend(d)
# print(c)
# c += d
# print(c)

# insert() 在指定位置插入元素
# c.insert(0,'h')
# print(c)

# remove() 删除指定位置的元素
# del c[0]
# print(c)
# index() 查询元素的位置 -- 返回列表在元素中的位置
# print(c.index(2))
# list = ['aa', 'bb', 'cc']
# str = ','.join(list)
#
# print(str)

"""
3, 元素是由任意元素类型组成的序列，元祖一旦被定义，将无法进行增加，删除，修改操作
元祖： 暂用空间小，不可改变
只有一个元素（1，）
可以通过[]访问元祖
"""
# count()  查询元素的个数

# index()  查询元素的位置，返回角标


"""
4, 字典 可变类型  字典中元素没有顺序，通过key访问value

"""
dict = {'name':'张三', 'age': 24}
# dict['name']   --> 输出‘张三’

# 通过[]添加、或修改元素
dict['sex'] = 'm'
print(dict) # {'age': 24, 'sex': 'm', 'name': '张三'}

# del dict['sex'] 删除 对应的值和键

print(dict.keys())

