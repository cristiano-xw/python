# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 17:06:44 2021

@author: cristiano
"""

row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='') #end取消换行
    print() 


for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for k in range(row - i - 1):
        print(' ', end='') #不会重复输出哈哈哈
    for k in range(2 * i + 1):   
        print('*', end='')
    print()
    