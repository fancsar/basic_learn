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
# b = [i for i in a if i[1] < 50 ]
# print(b)
# print(len(a))
# def shju(a):
# b=0
# for i in [3,51,49,42,42]:
#     if i < 50:
#         b+=i
#         if b > 50:
#             print(b)
#             b=0

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
print(list)
