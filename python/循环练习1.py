b = ["剪刀", "石头", "布"]
a = 123456 #后面需要转换数据类型
while True:
	name = input("请输入您的用户名")
	if name in b:
		break
	else:
		print('您输入的用户名不存在，请重新输入')
		continue

while True:
	password = input('请输入您的密码：')
	if str(a) == password:  #将a转换为字符串
		print('进入系统')
		break
	else:
		print('您输入的密码不正确，请重新输入')
		continue
    