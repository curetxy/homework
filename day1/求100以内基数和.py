#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: davetan
@license: Apache Licence
@contact: curetxy@163.com
@site: 
@software: PyCharm
@file: 求100以内基数和.py
@time: 2018-05-08-22:48
"""

'''类描述'''

sum = 0
for i in range(1,100,2):
	sum +=i
print(sum)

count = 100
sum_num = 0
for i in  range(count):
	if i%2 == 0:
		continue
	sum_num +=i

print(sum_num)