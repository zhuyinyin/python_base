# python_base# name1 = input("名字")
# name2 = int(name1)
# print(f'我叫{name1}')
# print(f'我叫{name2}')
# import random
# myGuess = random.randint(20, 25)
# print(myGuess)
# for i in range(1, 10):
#     for j in range(1, i + 1):
#
#         print(f'{i}x{j}={i*j}', end=' ')
#     print()
# a = 2 + 2j
# print(a)
# b = type(a)
# print(b)
# c = 4
# print(a + c)
#
# dict1 = {'Name': 'Runoob', 'Age': 7}
# print("dict1['Name']: ", dict1['Name'])
# 输入三个数排序输出
# x = int(input("输入第一个数："))
# y = int(input("输入第二个数："))
# z = int(input("输入第三个数："))
# if x > y:
#     x, y = y, x
# if x > z:
#     x.z = z, x
# if y > z:
#     y, z = z, y
# print(z)
# 求一个数的阶乘
# num = int(input("整数"))
# total = 1
# sum = 0
# for i in range(1, num+1):
#     total *= i
#     sum += total
# print(total, sum)
# 计算100以内能被7或者3整除但不能同时被整除的数
# j= 0
# for i in range(1,101):
#     if not( i% 7 and i% 3)and(i%7 or i%3):
#
#         j += 1
#         if j %4 :
#             print(i, end="  ")
#         else:
#             print(i)
# 一个三位数它的各个位数的三次方的和等于它
# for i in range(100, 1000):
#     if ((i//100)**3 + (i//10 % 10)**3 + (i % 10)**3) == i:
#         print(i)
# 一百以内素数（质数）
# for i in range(1, 101):
#     a = 0
#
#     for j in range(2, i):
#         if i % j == 0:
#             a = 1
#             break
#     if a == 0:
#         print(i)
# 打印*
# num = 4
# n = 1
# while n <= num:
#     num_space = num - n
#     num_star = 2*n - 1
#     print(' ' * num_space, end="")
#     print('*'*num_star)
#     n += 1
# a= 5
# for i in range(1,a):
#     print(" "*(a-i),"*"*(2*i-1))
#     # print("*"*(2*i-1))
for i in range(1,7):
    for k in range(1,7-i):
        print(" ", end=" ")
    for j in range(0,2*i-1):
        print("*", end=" ")
    print()
for i in range(1, 6):
    for k in range(0,i):
        print(" ", end=" ")
    for m in range(11-2*i):
        print("*", end=" ")
    print()

for i in range(1, 7):
    for k in range(1, 7 - i):
        print(" ", end=" ")
    for j in range(0, 2 * i - 1):
        if j == 0:
            print("*", end=" ")
        if j == (2*i-2) and not (j == 0):
            print("*", end=" ")
        if 0 < j < (2*i-2):
            print(" ", end=" ")
    print()
for i in range(1, 6):
    for k in range(0, i):
        print(" ", end=" ")
    for m in range(0, 11-2*i):
        if m == 0:
            print("*", end=" ")
        if m == (10-2*i) and not m == 0:
            print("*", end=" ")
        if 0 < m < 10-2*i:
            print(" ", end=" ")
    print()







# for i in range(1, 5):
#     print("*"*i)
# for i in range(1,5):
#     print("*"*(5-i))
