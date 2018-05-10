#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: davetan
@license: Apache Licence
@contact: curetxy@163.com
@site: 
@software: PyCharm
@file: 求100以内的素数.py
@time: 2018-05-09-11:36
"""

'''质数表的质数又称素数。指整数在一个大于1的自然数中,除了1和此整数自身外,没法被其他自然数整除的数'''

L1 = list()
for i in range(1,100):
	sum_count = 0
	for j in range(1,i+1):
		if i % j == 0:  #判断可以整除
			sum_count +=1
	if sum_count == 2:
		L1.append(i)
print(L1)