#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: davetan
@license: Apache Licence
@contact: curetxy@163.com
@site: 
@software: PyCharm
@file: 九九乘法表.py
@time: 2018-05-09-00:09
"""

'''类描述'''

for i in range(1, 10):
    #[1-9]
    for j in range(1, i+1):
        print('{}x{}={}'.format(j, i, i*j), end="\t")
        # print('{}dddd{}={}'.format(i,j,j))
    print("\n")


print("---------\n\n")

for i in range(1, 10):
    #[1-9]
    for j in range(i, 10):
        print('{}x{}={}'.format(j, i, i*j), end="\t")
        # print('{}dddd{}={}'.format(i,j,j))
    print("\n")

