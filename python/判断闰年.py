# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 16:14:15 2021

@author: cristiano
"""
"""
year = int(input('请输入年份: '))
# 如果代码太长写成一行不便于阅读 可以使用\对代码进行折行
is_leap = (year % 4 == 0 and year % 100 != 0) or \
           year % 400 == 0
print(is_leap)
"""

year=int(input("请输入年份:"))
is_leap=(year%4==0 and year %100!=0)or\
    year%400==0
print(is_leap) 