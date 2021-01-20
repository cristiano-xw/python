import random

a = input("请出拳")
b = ["剪刀", "石头", "布"]
#定义赢的列表
win_list = [["石头", "剪刀"], ["剪刀", "布"], ["布", "石头"]]
#计算机选择出拳
mac = random.choice(b)
print("你出拳",a)
print("计算机出拳",mac)
if a in b:
    if a == mac:
        print("平局")
    elif [a,mac] in win_list:
        print("你赢了")
    else:
        print("你输了")
else:
    print("输入错误")        