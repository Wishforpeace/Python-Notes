#2_4输出字符串变量时的方法使用

name="aDa loveLace"  #给字符串变量name赋值

print(name)  #输出变量name的值

print(name.title())  #按照每个单词首字母大写的方式输出name

print(name.upper())  #按照每个字母都大写的方式输出name

print(name.lower())  #按照每个字母都小写的方式输出name

#上面几条语句中，以print(name.title())为例

#这条语句输出的是name.title()运行的结果

#name.title()可以理解为关于变量name的一个具有独立功能的小程序（程序模块）

#这个小程序的功能是将变量name中保存的字符串变成每个单词首字母大写的形式

#这个小程序通常被称为“方法”，方法名称为title，前面加上变量名name以及圆点（圆点运算符）

#表明该方法实施的功能是针对变量name，调用时方法名称后面的一对括号不能少

#语句name.title()可以称为“调用变量name的方法title”

#本例中还调用的变量name的upper方法与lower方法

print(name)  #上述方法的调用并没有修改变量name中的值

#如果想要修改变量name的值，需要将方法的调用结果重新赋值给变量name

#观察以下语句的输出结果

name=name.title()

print(name)

name=name.upper()

print(name)

name=name.lower()

print(name)

#title以及upper和lower方法只能由字符串类型变量调用，其它类型的变量不能调用












