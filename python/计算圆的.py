# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 16:12:41 2021

@author: cristiano
"""

import math   

radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)