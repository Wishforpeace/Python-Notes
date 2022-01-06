#4_6 if-elif-else语句

#if-elif-else语句的形式为

#if 条件表达式1:
#    语句组1

#elif 条件表达式2:
#    语句组2

#elif 条件表达式3:
#    语句组3

#...

#elif 条件表达式n:
#    语句组n

#else:
#    语句组(n+1)

#关于if-else语句的说明如下：

#（1）如果条件表达式1的值为True时，执行后面缩进的语句组1
#     然后从else后面的第一条没有缩进的语句开始继续执行随后的语句    
#     如果条件表达式1的值为False时，再看条件表达式2的值

#（2）如果条件表达式2的值为True时，执行后面缩进的语句组2
#     然后从else后面的第一条没有缩进的语句开始继续执行随后的语句
#     如果条件表达式2的值为False时，再看条件表达式3的值，并以此类推
      
#（3）如果条件表达式1到条件表达式n的值都为Flase时，执行else后面缩进的语句组(n+1)
#     然后从else后面的第一条没有缩进的语句开始继续执行随后的语句

#（4）有时else以及其后缩进的语句组(n+1)可以缺省，这种情况下
#     如果条件表达式1到条件表达式n的值都为Flase时
#     从最后一个elif语句后面的第一条没有缩进的语句开始继续执行随后的语句

#例程1 按照年龄收费，4岁以下免费，满4不满18岁收费5美元，满18岁及以上收费10美元。
#      对于一个赋值为正整数表示年龄的变量，输出其应收费用情况      

age=input("请输入一个表示年龄的正整数age=")  #分别输入2,12,20
age=int(age)

if age < 4:
    print("Your admission cost is $0.")

elif age < 18:  #age>=4 and age<18
    print("Your admission cost is $5.")

else:  #age>=18
    print("Your admission cost is $10.")

#可以将上面的程序稍作修改 

age=int(input("请输入一个表示年龄的正整数age="))  #分别输入2,12,20

if age < 4:
    price = 0

elif age < 18:  #age>=4 and age<18
    price = 5

else:  #age>=18
    price = 10
print("Your admission cost is $" + str(price) + ".")

#例程2 按照年龄收费，4岁以下免费，满4不满18岁收费5美元，满18岁不满65岁收费10美元，满65岁及以上收费5美元。
#      对于一个赋值为正整数表示年龄的变量，输出其应收费用情况

age=input("请输入一个表示年龄的正整数age=")  #分别输入2,12,20,70
age=int(age)

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $" + str(price) + ".")














