# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 16:16:57 2021

@author: cristiano
"""

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))    