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

