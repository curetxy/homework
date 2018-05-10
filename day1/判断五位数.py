#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: davetan
@license: Apache Licence
@contact: curetxy@163.com
@site: 
@software: PyCharm
@file: 判断五位数.py
@time: 2018-05-08-18:51
"""

#给定一个不超过5位数的正整数，判断其有几位数

str_num = input("请输入一个正整数")

num = int(str_num)
if (10000 <= num < 99999):
	print("5位数")
elif (1000 <= num < 10000):
	print("4位数")
elif (100 <= num < 1000):
	print("3位数")
elif (10 <= num < 100):
	print("2位数")
else:
	print('个位数')