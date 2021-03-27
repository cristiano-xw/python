# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 16:44:13 2021

@author: cristiano
"""

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()  