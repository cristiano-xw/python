#!/usr/bin/env python
# coding: utf-8

# ## 类
# 
#     简单的说，类是对象的蓝图和模板，而对象是类的实例。这个解释虽然有点像用概念在解释概念，但是从这句话我们至少可以看出，类是抽象的概念，而对象是具体的东西。在面向对象编程的世界中，一切皆为对象，对象都有属性和行为，每个对象都是独一无二的，而且对象一定属于某个类（型）。当我们把一大堆拥有共同特征的对象的静态特征（属性）和动态特征（行为）都抽取出来后，就可以定义出一个叫做“类”的东西。
# 
# 
# ### 定义一个类
# 
# 首先，我们来学习怎么定义一个类

# In[ ]:


class Student(object):
    
    school = 'scu';#类变量
    # __init__是一个特殊方法用于在创建对象时进行初始化操作,可以理解为C++ 中的构造函数
    def __init__(self, name, age):  
        self.name = name
        self.age = age  
        
    def welcome(self): #self指代对象   
        print('welcome to RC!')
    
    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))


# 类定义与函数定义 (def 语句) 一样必须被执行才会起作用。
# 
# ### 创建和使用对象
# 
# 定义完之后要做的就是**实例化**这个类，也就是生成一个**对象**。

# In[ ]:


# 创建一个对象
Stu = Student('jyb',21)

# 属性引用
print(Stu.name)
print(Stu.school)

# 调用方法
Stu.welcome() 

# 简化方法
wel = Stu.welcome

wel()

Stu.study('python')


# 上述代码我们创建了一个对象，同时打印了他的其中两个属性，其中school是一个类属型，也就是所有对象共享的。
# 
# 值得注意的是，上述代码中方法的使用，我们明明在类的定义中定义函数时函数中传入了形参self，那么为什么我们在调用的时候却不会报错呢？
# 
# self在定义类时代表的是实例本身，也就是调用这个方法的时候默认会将该对象传入函数中。
# 
# **所以Stu.welcome()就相当于Student.welcome(Stu)**
# 
# 这里需要补充的是，写在类中的函数，我们通常称之为（对象的）方法，就是C++中我们的成员函数。
# 
# ### 访问可见性问题
# 
# 熟悉其他编程语言的大伙可能这时候会产生一个很关键的问题，我们的name和age属性究竟是什么访问权限呢？
# 
# public？private？protected？
# 
# 实际上，python中只有两种访问权限，public和private，默认的都是public
# 
# 那么如何定义一个私有变量呢？
# 
# 请注意：**那种仅限从一个对象内部访问的“私有”实例变量在 Python 中并不存在。**
# 
# 但我们有一种方法可以对此实现有限的支持。

# In[ ]:


class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作,可以理解为C++ 中的构造函数
    def __init__(self, name, age):
        self.name = name
        self.__age = age
        
    def welcome(self):
        print('welcome to RC!')
    
    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))
        
Stu = Student('jyb',21)

# print(Stu.__age)

print(Stu._Student__age)


# 可以看到，我们通常可以在变量前加__来声明为私有变量，但是这只是一种改名机制。
# 
#任何形式为 __spam 的标识符（至少带有两个前缀下划线，至多一个后缀下划线）
#的文本将被替换为 _classname__spam，其中 classname 为去除了前缀下划线的当前类名称。 
#这种改写不考虑标识符的句法位置，只要它出现在类定义内部就会进行。 
# 
# ### 静态方法
# 
# 静态方法不受限于对象的创建，没有对象也可以调用
# 

# In[ ]:


class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作,可以理解为C++ 中的构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @staticmethod
    def welcome():
        print('welcome to RC!')
    
    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

Student.welcome()

Stu = Student('jyb',21)

Stu.welcome()


# 实际的应用如下：
# ``` python
# if Triangle.is_valid(a, b, c):
#     t = Triangle(a, b, c)
# ```
# 
# ### 继承和多态
# 
#     刚才我们提到了，可以在已有类的基础上创建新类，这其中的一种做法就是让一个类从另一个类那里将属性和方法直接继承下来，从而减少重复代码的编写。提供继承信息的我们称之为父类，也叫超类或基类；得到继承信息的我们称之为子类，也叫派生类或衍生类。子类除了继承父类提供的属性和方法，还可以定义自己特有的属性和方法，所以子类比父类拥有的更多的能力，在实际开发中，我们经常会用子类对象去替换掉一个父类对象，这是面向对象编程中一个常见的行为，对应的原则称之为里氏替换原则。下面我们先看一个继承的例子。
#     

# In[ ]:


class Student():
    
    school = 'scu';
    # __init__是一个特殊方法用于在创建对象时进行初始化操作,可以理解为C++ 中的构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def study(self):
        print('%s正在学习高等数学.' % (self.name))
        
class Student_CS(Student):#继承
    def __init__(self,name,age,course):
        # super()代表调用父类          
        super().__init__(name,age)
        self.course = course
    
    def study(self):
        print('%s正在学习%s.' % (self.name,self.course))
    
    def review(self):
        print('%s正在复习高等数学.' % (self.name))
        
Stu = Student('jyb',21)

Stu_CS = Student_CS('hxk',21,'操作系统')

Stu.study()

Stu_CS.study()

Stu_CS.review()


#     子类在继承了父类的方法后，可以对父类已有的方法给出新的实现版本，这个动作称之为方法重写（override）。通过方法重写我们可以让父类的同一个行为在子类中拥有不同的实现版本，当我们调用这个经过子类重写的方法时，不同的子类对象会表现出不同的行为，这个就是多态（poly-morphism）。

# In[ ]:


class LeNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Sequential
        (
            nn.Conv2d(1, 6, 5), # in_channels, out_channels, kernel_size
            nn.Sigmoid(),
            nn.MaxPool2d(2, 2), # kernel_size, stride
            nn.Conv2d(6, 16, 5),
            nn.Sigmoid(),
            nn.MaxPool2d(2, 2)
        )
        self.fc = nn.Sequential
        (
            nn.Linear(16*4*4, 120),
            nn.Sigmoid(),
            nn.Linear(120, 84),
            nn.Sigmoid(),
            nn.Linear(84, 10)
        )


# ### 装饰器
# 
# #### 闭包
# 
# python的闭包从表现形式上可以定义为：如果在一个内部函数里，对在外部作用域的变量进行引用，
#并且外部函数将此内部函数作为返回值，那么这个内部函数就是闭包

# In[ ]:
def addx(x):
    def adder(y):
        return x+y #对外部作用域变量引用
    return adder  

c = addx(8) 

print(c(10))


# 上面的代码中adder就是一个闭包
# |
# 开始时调用先执行addx（8）对x进行赋值，赋值为8，然后调用C=adder(10),y=10返回值就是18
# 
# 使用闭包可以简化程序，比如我们要定义直线y=kx+b

# In[ ]:


def line_conf(a,b):
    def line(x):
        return ax+b
    return line
line_a = line_conf(1,2)


# #### 装饰器的概念和使用
# 比如通过闭包来计算时间

# In[ ]:


import time

def timer(func):
    def deco():
        start = time.time()
        func()#运行
        stop = time.time()
        print(stop-start)#运行时间
    return deco 

def test():
    time.sleep(2) 
    print("测试程序")

test = timer(test)
test()


# 这时每计算一个函数的时间，我们都要定义一个test = timer(test)
# 这时就引入了装饰器

# In[ ]:


import time
   
def timer(func):
    def deco():  
        start = time.time()
        func()
        stop = time.time()
        print(stop-start)
    return deco

@timer
def test():
    time.sleep(2)
    print("测试程序")

test() 


# In[ ]:


@csrf_exempt
@require_POST
def compute(request):
    code = request.POST.get('code')
    result = run_code(code)
    return JsonResponse(data={'result':result})


# ### 进程与线程
# 
# 首先是为什么要有线程与进程？是由于IO指令与计算指令相差时间较大所以引入的。
#
#进程就是操作系统中执行的一个程序，操作系统以进程为单位分配存储空间，每个进程都有自己的地址空间、
#数据栈以及其他用于跟踪进程执行的辅助数据，操作系统管理所有进程的执行，为它们合理的分配资源。
#进程可以通过fork或spawn的方式来创建新的进程来执行其他的任务，不过新的进程也有自己独立的内存空间，
#因此必须通过进程间通信机制（IPC，Inter-Process Communication）来实现数据共享，
#具体的方式包括管道、信号、套接字、共享内存区等。
#     
#一个进程还可以拥有多个并发的执行线索，简单的说就是拥有多个可以获得CPU调度的执行单元，
#这就是所谓的线程。由于线程在同一个进程下，它们可以共享相同的上下文，因此相对于进程而言，线程间的信息共享和通信更加容易。当然在单核CPU系统中，真正的并发是不可能的，因为在某个时刻能够获得CPU的只有唯一的一个线程，多个线程共享了CPU的执行时间。使用多线程实现并发编程为程序带来的好处是不言而喻的，最主要的体现在提升程序的性能和改善用户体验，今天我们使用的软件几乎都用到了多线程技术，这一点可以利用系统自带的进程监控工具（如macOS中的“活动监视器”、Windows中的“任务管理器”）来证实，如下图所示。
# 
# 

# In[ ]:


from multiprocessing import Process#多进程
from os import getpid 
from random import randint
from time import time, sleep


def deposit(person):
    print('%s 开始存钱' % person )
    time_to_deposit = randint(5, 10)
    sleep(time_to_deposit)
    print('%s存钱完成! 耗费了%d秒' % (person, time_to_deposit))


def main():
    start = time()
    p1 = Process(target=download_task, args=('jyb', ))
    p1.start()
    p2 = Process(target=download_task, args=('hxk', ))
    p2.start()
    p1.join()
    p2.join()      
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()


# In[ ]:


from random import randint
from threading import Thread #线程
from time import time, sleep

def deposit(person):
    print('%s 开始存钱\n' % person )
    time_to_deposit = randint(5, 10)
    sleep(time_to_deposit)
    print('%s存钱完成! 耗费了%d秒' % (person, time_to_deposit))


def main():
    start = time()
    t1 = Thread(target=deposit, args=('jyb',))    
    t1.start()
    t2 = Thread(target=deposit, args=('hxk',))
    t2.start()#启动
    t1.join()   
    t2.join()
    end = time()
    print('总共耗费了%.3f秒' % (end - start))


if __name__ == '__main__':
    main()


# 上述代码中，我们使用了Thread类来创建线程对象，然后start方法启动线程，
#join方法则是用于线程之间的时序问题，比如我在A线程中调用了B线程的join方法，
#那么A线程就会阻塞在此处等待B线程运行完成后进行下一步操作。所以当我们在主程序中使用这两个方法时，
#主线程就会阻塞等待两个线程进行完成在进行下一步操作。
# 
# ### 共享数据的访问控制
# 
# 假如还是存钱问题，这时候有很多人往同一个账户里存钱，我们先看第一个程序的结果

# In[ ]:


from random import randint
from threading import Thread
from time import time, sleep

    
account = 0

def deposit(person,money):
    global account
    acc = account
    sleep(0.1)
    account = acc + money
    print('子线程%d结束 ' % person)



theadlist = []
for idx in range(10):
    thread = Thread(target = deposit,args = (idx,1))
    thread.start()
    theadlist.append(thread)

for thread in theadlist:
    thread.join()

print('主线程结束')
print('最后我们的账号余额为 %d' % account)


# In[ ]:


from random import randint
from threading import Thread,Lock
from time import time, sleep

    
account = 0

depolock = Lock()

def deposit(person,money):
    global account
    depolock.acquire()
    acc = account
    sleep(0.1)
    account = acc + money
    print('子线程%d结束 ' % person)
    depolock.release()


theadlist = []
for idx in range(10):
    thread = Thread(target = deposit,args = (idx,1))
    thread.start()
    theadlist.append(thread)

for thread in theadlist:
    thread.join()

print('主线程结束')
print('最后我们的账号余额为 %d' % account)


# In[ ]:


from random import randint
from threading import Thread,Semaphore
from time import time, sleep

    
account = 0

depolock = Semaphore(1) #信号量

def deposit(person,money):
    global account
    depolock.acquire()
    acc = account
    sleep(0.1)
    account = acc + money
    print('子线程%d结束 ' % person)
    depolock.release()  

theadlist = [] 
for idx in range(10):
    thread = Thread(target = deposit,args = (idx,1))
    thread.start()
    theadlist.append(thread)

for thread in theadlist:
    thread.join()

print('主线程结束')
print('最后我们的账号余额为 %d' % account)

