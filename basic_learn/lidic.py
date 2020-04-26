# -*- coding: utf-8 -*-
# @Time   :2019/11/5 22:18
'''
1、使用字典推倒是将下面字符串格式的数据，改成字典类型的数据 cook_str='BIDUPSID=D0727533D7147B7;PSTM=1530348042; BAIDUID=B1005C9BC2EB28;
sugstore=0;__cfduid=d0a13458f8ac2a;BD_UPN=12314353;ispeed_lsm=2;BDORZ=B490B5EBF6F3CD402'
'''
cook_str = 'BIDUPSID=D0727533D7147B7;PSTM=1530348042; BAIDUID=B1005C9BC2EB28; \
sugstore=0;__cfduid=d0a13458f8ac2a;BD_UPN=12314353;ispeed_lsm=2;BDORZ=B490B5EBF6F3CD402'

cook_dict = {i.split('=')[0]: i.split('=')[1] for i in cook_str.split(';')}
print(cook_dict)

'''
 2、定义一个函数实现以下功能，第一个元素是数据标识，第二个元素的数值必须大于等于50才返回，
 不够50往后累加加到最后如果不够50也直接返回，因为没有可加的数据了
例子1 ：
a = [[1,3],[2,51],[3,49],[4,42],[5,42]] #入参 
a1 = [[2,54],[4,91],[5,42]] #返回 
例子2：
 b = [[1,50],[2,5],[3,10],[4,42],[5,42],[6,10]] #入参
 b1 = [[1,50],[4,57],[6,52]] #返回
'''
a = [[1, 50], [2, 5], [3, 10], [4, 42], [5, 42], [6, 10]]


def func(a):
    count = 0
    b = []
    for i in range(len(a)):
        count += a[i][1]
        if count > 50 or a[i][1] >= 50:
            b.append([a[i][0], count])
            count = 0
        elif i + 1 == len(a):
            b.append([i + 1, count])
    return b


print(func(a))

'''
3、通过列表推导式完成下面数据类型转换
现在有以下数据， li1 = ["{'a':11,'b':2}","[11,22,33,44]"] 
需要转换为以下格式： li1 = [{'a':11,'b':2},[11,22,33,44]] 
'''
li1 = ["{'a':11,'b':2}", "[11,22,33,44]"]
li2 = [eval(i) for i in li1]
print(li2)

'''
str = """
url:www.baidu.com,mobilephone:13760246701,pwd:123456
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
"""
# 转换后数据
list = [{'url': 'www.baidu.com', 'mobilephone': '13760246701', 'pwd': '123456'},
        {'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
        {'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
        {'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
        {'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'}]
'''
str1 = """
url:www.baidu.com,mobilephone:13760246701,pwd:123456
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934531,pwd:234555
url:www.baidu.com,mobilephone:15678934541,pwd:234555
url:www.baidu.com,mobilephone:15678934561,pwd:234555
"""
list = [{j.split(':')[0]: j.split(':')[1] for j in s.split(',')} for s in str1.split('\n') if s != '']
# print(list)

'''
一、一个球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''


def fun(n):
    if n == 1:
        return 100 / 2
    else:
        return fun(n - 1) / 2


res = fun(10)
print(f'第10次反弹的高度是{res}')
'''
1 100
2 100 50 50
3.100 50 50 25 25 
4.100 50 50 25 25 12.5 12.5
'''


def fun1(n):
    if n == 1:
        return 100
    else:
        return (fun(n - 1) * 2) + fun1(n - 1)


print('第10次反弹的总路径是{}'.format(fun1(10)))


# for循环实现
def qiuhe(n):
    s = 0
    h = 100
    for i in range(n):
        s += h
        h = h / 2
        s += h
    print(s - h)


qiuhe(10)

'''
二、古典问题：有一对兔子，第三个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？（意味着生长期为2个月） （递归实现）
'''


# 1,1,2,3,5,8,13
def summ(n):
    if n == 1 or n == 2:
        return 2
    else:
        return summ(n - 1) + summ(n - 2)


print(summ(10))


# 循环实现
def sums(n):
    s = []
    for i in range(1, n + 1):
        if i == 1 or i == 2:
            s.append(2)  # 前两月时，都是固定值
        else:
            s.append(s[i - 3] + s[i - 2])  # 从第三月开始，是前两数之和
    return f'第{n}月时，兔子总数为{s[-1]}只'


print(sums(10))

'''
三、小明有100元钱 打算买100本书，A类书籍5元一本，B类书籍3元一本，C类书籍1元两本，请用程序算出小明一共有多少种买法?（面试笔试题）

A 20
B 33
C 200
'''


def goshop():
    count = 0
    for a in range(21):  # 遍历可以买A类书籍的所有本数
        for b in range(34):  # 遍历可以买B类书籍的所有本数
            c = 100 - a - b  # 剩下为C类书籍的本数
            if a * 5 + b * 3 + c * 0.5 <= 100:
                count += 1
    return f'小明一共有{count}种买法'


print(goshop())

"""冒泡排序"""
aa = [12, 4, 5, 76, 98, 32, 56]
for i in range(len(aa) - 1):
    for j in range(len(aa) - 1):
        if aa[i] > aa[i + 1]:
            aa[i], aa[i + 1] = aa[i + 1], aa[i]
print(aa)

'''
2、 请设计一个装饰器  ，可以给函数扩展登录认证的功能（提示数账号密码，然后进行校验），
多个函数同时使用这个装饰器， 调用函数的时候，只要登录成功一次，
后续的函数无需再进行登录（默认的认证账号：qwe123，密码：123456）
'''

result = 0


def login(func):
    def check():
        global result
        if result:
            func()
        else:
            username = input('用户名为：')
            password = input('密码为：')
            if username == 'qwe123' and password == '123456':
                result = 1
                func()

    return check


@login
def successlogin():
    print('成功登陆')
