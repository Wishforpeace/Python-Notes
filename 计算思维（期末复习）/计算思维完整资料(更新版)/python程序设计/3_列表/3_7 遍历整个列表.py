#3_7 遍历整个列表

#所谓遍历整个列表就是指的是依次获取每个列表元素的值，然后实施输出或修改等操作。

#对于元素数量很多列表，逐个访问其每一个元素需要大量语句，所以通常使用循环语句来操作。

#下面是通过for循环语句输出列表元素的例子，观察其运行结果

magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    
    print(magician)

#关于for循环语句使用的几点说明：

#（1）for语句后面的冒号':'不能少，程序运行时知道':'后面的语句是循环体（循环执行多遍）

#（2）for语句的格式是“for 变量名 in 列表名:”，for语句后面凡是有缩进（缩进几格不论）

#     的语句都是循环体，循环过程的执行方式为:变量magician依次获取列表magicians中的每

#     个元素的值，每取得一个值就输出来，直到输出列表的所有元素后，循环结束！

#（3）语句print(magician)必需缩进，缩进是该语句是循环体的标志，否则运行时就会出现错误！

#上面三条语句的执行过程与下面的语句执行过程完全相同

magicians = ['alice', 'david', 'carolina']

magician='alice'
print(magician)

magician='david'
print(magician)

magician='carolina'
print(magician)

#for循环只有2条语句，功能相当于上面的6条语句，由此可见循环可以极大节省语句数量

#循环体可以包含多条语句，凡是属于循环体之内的语句都要缩进

#for语句后面如果有需要在循环结束后再执行的语句，该语句前面不加缩进即可

magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    
    print(magician.title() + ", that was a great trick!")  #这条语句循环执行
    
    print("I can't wait to see your next trick, " + magician.title() + ".\n")  #这条语句循环执行

print("Thank you, everyone. That was a great magic show!")  #这条语句在循环结束后执行








