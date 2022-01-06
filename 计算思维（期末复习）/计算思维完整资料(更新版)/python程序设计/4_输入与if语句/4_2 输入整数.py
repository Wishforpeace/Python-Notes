#4_2 输入整数
   
age = input("How old are you? ")  #输入21

age = age+1

#运行上面这两条语句时，系统会报错

#因为age是字符串变量，不能做加法

#显然这个例子中，用户是想输入整数（而不是字符串）保存到变量age中

#可以在输入后调用int()函数将字符串变量age转换成整型变量，具体操作如下：

age = input("How old are you? ")  #输入21

age = int(age)

age = age+1

print('age=',age)

#也可以将input函数的调用结果作为int函数的参数，直接实现数值型变量的输入

age = int(input("How old are you? "))

#总结一下，调用input()函数只能将输入信息保存到字符串变量

#如果需要将输入的信息保存到数值型变量中，需要结合int()函数一起使用












