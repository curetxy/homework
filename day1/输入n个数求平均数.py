#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: davetan
@license: Apache Licence
@contact: curetxy@163.com
@site: 
@software: PyCharm
@file: 输入n个数求平均数.py
@time: 2018-05-09-08:09
"""

'''类描述'''


sum_count = 0
count = 0
while  True:
	a = input("请输入数字 q退出>>")
	if a =="q":
		break
	sum_count +=int(a)
	count +=1
	print(sum_count/count)