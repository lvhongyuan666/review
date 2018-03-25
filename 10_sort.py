# 打印横三竖五的星星
# a = 1
# while a <= 3:
#     b = 1
#     while b <= 5:
#         print("*", end='')
#         b += 1
#     print()
#     a += 1

# 打印竖五梯形
# c = 1
# while c <= 5:
#     d = 0
#     while d < c:
#         print('*', end='')
#         d += 1
#     print()
#     c += 1

# 九九乘法表
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print('%d * %d = %d' % (j,i,j*i), end=' ')
#         j += 1
#     print()
#     i += 1

# 输出50-100之间不能被5整除的数
# i = 50
# while i <= 150:
#     if i%5 == 0:
#         i += 1
#         continue  # 跳出后面剩余的循环语句，执行下一轮循环
#     print(i)
#     i += 1
# continue 语句：跳过当前循环的剩余语句，继续下一轮循环
# break 语句： 跳出整个循环

# 打印两个梯形合并
# i = 1
# while i <=9:
#     if i <= 5:
#         print('*'*i)
#     else:
#         print('*'*(10-i))
#     i += 1

# 单利模式

class Person(object):
    my_object = None

    def __new__(cls):
        if not cls.my_object :
            cls.my_object = object.__new__(cls)
        return cls.my_object

#
# p1 = Person()
# print(id(p1))
# p2 = Person()
# print(id(p2))

'''
菲波拉契数列
'''
def fibo(num):
    numlist=[0,1]
    for i in range(num-2):
        numlist.append(numlist[-2]+numlist[-1])
    return numlist

# if __name__ == '__main__':
#     ret = fibo(9)
#     print(ret)

def fi(n):
    num1= 0
    num2= 1
    i = 0
    while i < n:
        print(num1)
        num1,num2 = num2, num1 + num2
        i += 1

# if __name__ == '__main__':
#     fi(9)


# 冒泡排序  --- 排序，首先要传入一个需要排序的队列
# def bubble_sort(lst):
#     n = len(lst)
#
#     for i in range(n-1):  # 记录一共比较的次数
#         count = 0
#         for j in range(n-1-i): # 记录每一轮的比较
#
#             if lst[j] > lst[j + 1]:
#                 lst[j], lst[j + 1] = lst[j +1], lst[j]
#                 count += 1
#
#         if count == 0:  # 如果在一轮的比较中，没有交换位置，说明有序，直接退出
#             break

# if __name__ == '__main__':
#     l = [1, 2, 3, 5, 6, 8]
#     bubble_sort(l)
#     print(l)



# 快速排序
def quick_sort(li, start, end):

    if start >=end:  # 递归终止的条件
        return

    left = start
    right = end
    mid = li[left]

    while left < right:

        while left < right and li[right] >= mid:
            right -= 1
        li[left] = li[right]

        while left < right and li[left] <= mid:
            left += 1
        li[right] = li[left]

    li[left] = mid

    quick_sort(li,start, left-1)
    quick_sort(li, left+1, end)

# if __name__ == '__main__':
#     l = [2,6,3,9,7]
#     quick_sort(l, 0, len(l)-1)
#     print(l)
#

'''
error：maximum recursion depth exceeded in comparison
超过最大递归深度
    if start >=end:  # 递归终止的条件
        return
没有这个条件，递归就没有终止条件，就会报以下错误
python专门设置的一种机制用来防止无限递归造成Python溢出崩溃， 最大递归次数是可以重新调整的

'''

# 二分法查找元素是否在序列中

'''
此种方法只适合有序数列的查找，速度快
二分法： 找到中间的元素与要查找的元素做比较，调用递归

接收两个参数，ls item
'''
def search(ls, item):

    if len(ls) == 0:
        return False

    mid = len(ls)//2

    if ls[mid] == item:
        return True

    elif ls[mid] > item :
        return search(ls[mid+1:], item)

    else:
        return search(ls[:mid], item)



# if __name__ == '__main__':
#     ll = [1,2,3,4,5]
#     print(search(ll,6))

'''
不适用二分法查找元素，是否在列表里
一个有序列表，找出list中第一个大于item元素的下标index，无法满足则返回-1
'''
def find(ls,item):

    index = 0
    n = len(ls)

    while index < n:

        if ls[index] >= item:
            return index
        else:
            index+=1
    return -1

'''
手写一个迭代器
'''
class Mylist(object):

    def __init__(self):
        self.container = []
        self.i = 0

    def add(self,item):
        self.container.append(item)

    def __next__(self):
        # 每次调用的时候，先判断迭代器是否有元素
        if self.i < len(self.container):
            item = self.container[self.i]
            self.i += 1
            return item
        else:
            raise StopIteration

    def __iter__(self):
        return self


'''
在一个有序的数列里插入任意一个数，不改变原来的规律
'''
# li = [1,2,5,8,9]
# n = len(li)
# num = int(input('请输入数字：'))
# li.append(num)
# for i in range(n):
#
#     if num < li[i]:
#         for j in range(n, i,-1):
#             li[j] = li[j-1]
#         li[i] = num
#         break
# print(li)

#  用一行代码实现，一个列表中有下标为偶数的元素的和
ll = [1,2,3,4,5]
ret = sum([ll[i]+3 for i in range(len(ll)) if i%2 == 0])
print(ret)

# # lambda x:x%2==0,
# b = 0
# c = 2
# a = 0 if b else 1
# print(a)









