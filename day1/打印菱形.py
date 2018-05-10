#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: davetan
@license: Apache Licence
@contact: curetxy@163.com
@site: 
@software: PyCharm
@file: 打印菱形.py
@time: 2018-05-09-20:12
"""

'''类描述'''

for i in range(-3,4):
	if i<0:
		pre = -i
	else:
		pre = i
	print(' '*pre + '*'*(7-pre*2))