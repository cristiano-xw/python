
import random #取随机数

answer = random.randint(1, 100)   
counter = 0 
while True:
    counter += 1
    number = int(input('请输入: '))
    if counter <=4:   
        if number < answer:
            print('大一点')
        if number > answer:
            print('小一点')
        if number == answer:
            print('恭喜你猜对了!')
            break
    if counter >= 5:
        print("傻瓜猜错了")
        break;
        
print('你总共猜了%d次' % counter)




