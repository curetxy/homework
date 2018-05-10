#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: davetan
@license: Apache Licence
@contact: curetxy@163.com
@site: 
@software: PyCharm
@file: 1到5阶乘之和.py
@time: 2018-05-08-22:56
"""

'''类描述'''
# 1 + 1*2 + 1*2*3  + 1*2*3*4
# 就相当于 1 + 2 + 2*3 + 6*4
num_start = 1
sum = 0
for i in range(1, 6):
	print(i)
	# count = i
	# count *=i
	num_start = num_start * i
	sum += num_start

print(sum)

#第二种思路  每次都算出 一列值
# 1 + 1*2 + 1*2*3
sum_count = 0
mid_num = 1
for i in range(1, 6):
	for item in range(1, i + 1):
		mid_num = mid_num * item
	sum_count += mid_num
	mid_num = 1 # 每次循环完毕后初始化mid值

print('>>>---', sum_count)

'''
# 给出的数据
# n = 7
#
# 逐步计算
# 公式：n! = n x (n-1) x (n-2) x .... x 1
# 替代值
# n! = 7 x 6 x 5 x 4 x 3 x 2 x 1
# n! = 5040

'''
