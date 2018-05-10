#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: davetan
@license: Apache Licence
@contact: curetxy@163.com
@site: 
@software: PyCharm
@file: 求质数.py
@time: 2018-05-08-23:44
"""

'''类描述'''
#质数 一个大于1 且只能被自身整除的数字


L1 = []
for x in range(100, 200):
	n = 0
	for y in range(1, x + 1):
		if x % y == 0:
			n = n + 1
	if n == 2: #一个大于1 且只能被自身整除的数字，因为天生数字都可以被1和自身整除、如果还可以被更多的整除n就会大于2
		print(x)
		L1.append(x)
print(L1)
