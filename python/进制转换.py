# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 16:22:13 2021

@author: cristiano


value = float(input('请输入长度: '))
unit = input('请输入单位: ')
if unit == 'in' or unit == '英寸':
    print('%f英寸 = %f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 = %f英寸' % (value, value / 2.54))
else:
    print('请输入有效的单位')   
"""

value=float(input("请输入长度:"))
uint=input("请输入单位:")
if uint=='in' or uint =='英寸':
    print("%f英寸 = %f厘米"%(value,value*2.54))
elif uint=='cm' or uint =='厘米':
    print("%f厘米 = %f英寸"%(value,value/2.54))
else:
    print("请输入有效单位")
    
    