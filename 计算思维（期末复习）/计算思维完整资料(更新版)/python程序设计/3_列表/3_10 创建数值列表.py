#3_10 创建数值列表

# 1 使用函数range()结合list()函数可以生成一个整数列表

numbers = list(range(1,6))  #函数range(1,6)的调用结果作为list()函数的参数
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

# 2 使用函数range()结合for循环也可以生成一个整数列表

squares = []  #创建一个空列表

for value in range(1,11):  #循环时变量value接收到的值依次为1,2,3,...,9
    square = value**2  #运算符**是乘方运算
    squares.append(square)  #调用append()方法往列表中添加元素
    
print(squares)

















