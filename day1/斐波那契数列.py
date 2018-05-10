#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: davetan
@license: Apache Licence
@contact: curetxy@163.com
@site: 
@software: PyCharm
@file: 斐波那契数列.py
@time: 2018-05-09-21:02
"""

'''类描述'''

# 斐波那契数列：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

a = 0
b = 1
c = 1
max_num  = 10
while True:
	print(a)
	c = a + b
	a = b
	b = c
	# a , b=b,a+b
	# if a > max_num:
	# 	break
	if c > max_num:
		break