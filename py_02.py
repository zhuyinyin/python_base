# python_base#  循环语句
#循环控制语句
# break中止循环，并且跳出循环
# continue 中止循环跳出本次循环，执行下次循环
#  pass  空语句，
#流程：
""""
 while 条件：
    语句块（条件满足就执行，
        执行完继续判断while后面的条件判断）

"""
count = 1
sum = 0
while count <= 100:
    sum += count
    if sum > 1000:
        break
    count += 1
print(sum)
#   循环变量初始化
#   while 条件：
#   循环体
#   改版循环变量的值（使循环正常退出）
#   continue  结束本次循环继续判下一次循环
count = 1
sum = 0
while count <= 100:
    if count % 2 == 0:
        count += 1
        continue
    sum += count
    count += 1
# print(sum)
# while 条件：
#     语句块
# else:
# print()
"""
for letter in 'www.baidu.com':
    取出letter里面的数据
"""
# 读取字符串里的每一个字母
for letter in 'www.baidu.com':
    print(letter)
# range()函数 :获取一连串数字
for let in range(1,5):
    print(let)
# 嵌套循环：
""""
for num in range(10, 20):  # 迭代 10 到 20 之间的数字
   for i in range(2, num):  # 根据因子迭代
      if num % i == 0:      # 确定第一个因子
         j = num / i          # 计算第二个因子
         print('%d 是一个合数' % num)
         break           # 跳出当前循环
   else :                  # 循环的 else 部分
      print('%d是一个质数' % num)
"""
# 两个乘数=行数*列数
# 列数等于所在的行数
# 外层控制行数，内层控制列数
# 先打印行里的每一列，列打印完成，就完成一行
#
"""
for i in range(1, 10):
    for j in range(1, i+1):
        print('%d*%d=%d \t' % (j, i, i*j), end = '')
    print()
"""
#    ###*   输入等腰三角形阶乘
#    ##***  折纸上月球
#    #*****
#    *******

n = 3
for i in range(1,9 ):
    for j in range(1, i+1):
        if i % 2 == 0:
          break
        else:
            print('* ', end='')
    print()


num = 4
n = 1
while n <= num:
    num_space = num - n
    num_star = 2*n - 1
    print(' ' * num_space,end="")
    print('*'*num_star)
    n += 1
    print()

x = 1
y = int(input("请输入要计算的数:"))
if y >= 0:
    for i in range(1, y + 1):
     x = x * i
    print('%s的阶乘为%s'%(y,x))
else:
    print('%s没有阶乘'%y)


number = 0
h = 0.088
while h <= 363300000000:
    h = h*2
    number += 1
print('需要折%s次'%number)
