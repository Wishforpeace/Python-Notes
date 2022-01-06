#4_4 简单if语句

#简单if语句的形式为

#if 条件表达式:
#    语句

#关于简单if语句的说明如下：

#（1）条件表达式是取值为布尔值的关系表达式或逻辑表达式，有时也可以是算术表达式

#（2）条件表达式值为True时执行后面缩进的所有语句，否则跳过后面缩进的所有语句，
#     从后面的第一条没有缩进的语句开始继续执行随后的语句

#（3）条件表达式后面的冒号':'不能少

#例程1

age = 19
if age >= 18:
    print("You are old enough to vote!")

#例程2
    
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

#例程3
    
age = 19  #将age的值改为17再运行一遍
if age >= 18:
    print("You are old enough to vote!")
print("Have you registered to vote yet?")

#例程4 输出两个变量中较大那个的值

a=input("请输入一个整数a=")
a=int(a)

b=input("请输入一个整数b=")
b=int(b)

c=a  #c记录a和b中较大者，初值为a的值
if a<b:  
    c=b  #条件a<b成立时，用两者中较大的b给c赋值，此行比起前面的行缩进2格
print(c)  #输出c的值



#例程5 按照年龄收费，4岁以下免费，满4不满18岁收费5美元，满18岁及以上收费10美元。
#      对于一个赋值为正整数表示年龄的变量，输出其应收费用情况

age=input("请输入一个表示年龄的正整数age=")  #分别输入2,12,20
age=int(age)

if age<4:
    print("Your admission cost is $0.")

if age>=4 and age<18:  
    print("Your admission cost is $5.")

if age>=18:
    print("Your admission cost is $10.")
    









