#4_5 if-else语句

#if-else语句的形式为

#if 条件表达式:
#    语句组1
#else:
#    语句组2

#关于if-else语句的说明如下：

#（1）条件表达式值为True时执行后面缩进的语句组1，否则执行执行elae后面缩进的语句组2，
#     然后从else后面的第一条没有缩进的语句开始继续执行随后的语句

#（2）条件表达式后面的冒号':'与else后面的冒号':'均不能少

#例程1

age=input("请输入一个表示年龄的正整数age=")  #分别输入17,19
age=int(age)

if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")


#例程2 输出两个变量中较大那个的值

a=input("请输入一个整数a=")
a=int(a)

b=input("请输入一个整数b=")
b=int(b)

if a<b:  
    print(b)  
else:
    print(a)  










