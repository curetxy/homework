#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: davetan
@license: Apache Licence
@contact: curetxy@163.com
@site: 
@software: PyCharm
@file: 打印正方形.py
@time: 2018-05-08-22:42
"""


n = 6
for i  in range(1,n):
	if i == 1 or i == n - 1:
		print("*\t"*n)
	else:
		print('*'+'\t'*(n-1) +'*')


