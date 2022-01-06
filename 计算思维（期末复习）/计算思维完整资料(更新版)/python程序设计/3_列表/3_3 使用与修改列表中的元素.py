#3_3 使用与修改列表中的元素

#既然每个列表元素都是变量，所以前面介绍的title以及upper等方法也可以使用到列表元素上

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles)
print(bicycles[1].title())
print(bicycles[2].upper())
print(bicycles[3].lower())

message = "My first bicycle was a " + bicycles[0] + "."
print(message)

print() #不带参数的print语句输出的是一个空行

integers = [12, 18, 23, 34]  
print(integers)

message = "The first number in integers is " + integers[0] + "."  #这样赋值有什么问题？
print(message)

print()  #输出一个空行

message = "列表bicycles = " + bicycles  #这样赋值有什么问题？  
print(message)

#可以通过修改列表元素的值来修改整个列表，观察下面几条语句的运行结果

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles)

print()  #输出一个空行，起到将输出内容分隔的效果   

bicycles[1] = 'Cannondale'

bicycles[3] = 'SPECIALIZED'

print(bicycles)

print()  

print(bicycles[0].title())

print(bicycles[2].upper())

print(bicycles)  #输出时列表元素bicycles[0]和bicycles[2]的值改变了吗？为什么？

print()  

bicycles[0] = bicycles[0].title()

bicycles[2] = bicycles[2].upper()

print(bicycles)

















