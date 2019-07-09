# python_basealist = [1, 2, 3, 4, 6, 7, 8, 9, ]
print(alist)
# 在尾部加元素
alist.append(10)
print(alist)
# 指定位置加元素
alist.insert(1, 2)
print(alist)
 # + * 返回新列表
blist = alist + [11]
print(blist)
alist.pop()
print(alist)
# 指定位置删除
b = alist.pop(2)
print(b)
c = alist.remove(2)
print(c)
# 删除指定位置的元素
del alist[2]
print(alist)
d = alist.count(6)
print(d)
# 获取指定元素下标
alist.index(7)
print(alist.index(7))
import random
random.shuffle(alist)
print(alist)
# 不返回新列表
alist.sort(reverse=True)
# 返回新列表
sorted(alist)
print(sorted(alist))
print(alist)
blist = [1, 2, 3, 4, 5]
cList = zip(alist, blist)
print(list(cList))
# 遍历列表三种方式
for i in alist:
    print(i)
for i in range(len(alist)):
    print(i,alist[i])
for i,ele in enumerate(alist):
    print(i,ele)
# 列表推导式
vec = [[1, 2, 3], [2, 3, 4], [7, 8, 9]]
dlist = [nu for ele in vec for nu in ele]
print(dlist)
# 不断问用户想买什么,并把买的东西加入购物车用户输入q时退出并打印购物车
flas = True
blist = []
while flas:
    print("*" * 6 + "商品列表" + "*" * 6)
    alist = [["0.iphone| 6888"], ["1.三星| 3000"], ["2.小米| 2500"]]
    for i in alist:
        print(i)
    inputs =input("请输入您想购买的商品编号:")
    if inputs == '0':
        blist.append(alist[0])
        print("已将%s加入购物车" % alist[0])
    elif inputs == "1":
        blist.append(alist[1])
        print("已将%s加入购物车" % alist[1])
    elif inputs == "2":
        blist.append(alist[2])
        print("已将%s加入购物车" % alist[2])
    elif inputs == 'q':
        ip = blist.count(["0.iphone| 6888"])
        san = blist.count(["1.三星| 3000"])
        mi = blist.count(["2.小米| 2500"])
        money = 6888*ip + 3000*san + 2500*mi
        print("您购买以下商品:(iphone| 6888)*%s (三星| 3000)*%s (小米| 2500)*%s"%(ip, san, mi))
        print("您购买的商品总价:%s" % money)
        flas = False
    else:
        print("不存在该商品")

alist = ["A", "B", [1,2,3],"C", "D"]
b = alist[::]
print(b)
c = alist[::-1]
print(c)
t = alist[:1:-1]
print(t)

t = alist[1::-1]
print(t)
# 尾部追加元素
alist[len(alist):] = [9]
print(alist)
# tuple冻结列表
print(tuple(alist))
# list解冻元组
print(list(tuple(alist)))
list1 = []
alist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(alist)):
    if (9-alist[i]) in alist:
        if alist[i] > (9-alist[i]):
            a = ((9-alist[i]), alist[i])
            b = list(a)
            c = tuple(b)
            list1.append(c)
print(list1)
# 字符串切片
# 字符串全部大写 全部小写
s = "Hello word god is always busy"
alist = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
low = s.lower()
lis = []
for i in range(len(low)):
    # for j in range(len(alist)):
        if low[i] in alist:
            b = low[i]
            c = low.count(low[i])
            if b not in lis:
                lis.append(b)
                lis.append(":{} " .format(c))
print(lis)
z = ''.join(lis)
print(z)


# python猜单词游戏
li = ["apple", "mi", "red", "banana", "iphone"]
import random
time = 0
a = random.randint(0, 5)
word = li[a]
li_word = list(word)
lens = len(li_word)
# print(lens)
c = []
for j in range(lens):
    c.append('-')
# print(c)
c1 = "".join(c)
print(c1)
print(li_word)
flase = True
while flase:
    guess = input("猜一个字母")
    for i in range(len(li_word)):
        if guess == li_word[i]:
            c[i] = li_word[i]
    # print(c)
    c2 = "".join(c)
    print(c2)
    if guess not in c:
        time += 1
        print("还有%d次机会" % (5 - time))
    elif c == li_word:
        print("胜利")
        break
    elif time == 5:
        print("失败")
        flase = False
