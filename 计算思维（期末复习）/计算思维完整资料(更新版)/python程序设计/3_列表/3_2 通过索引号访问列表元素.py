#3_2 通过索引号访问列表元素

#列表是一个复合数据类型，如下所示的列表bicycles，它有4个字符串类型的元素

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#列表中的每一个元素实际上是一个变量，列表则是多个变量组成的变量的集合

#每个列表元素可以通过“列表名[索引号]”的方式表示

#列表元素的索引号通常用非负整数表示，第1个元素的索引号为0，其余依次递增

#列表bicycles的4个元素分别表示为bicycles[0]、bicycles[1]、bicycles[2]、bicycles[3]

print('\n正序输出列表元素')
print(bicycles[0])  #输出列表中的第1个元素
print(bicycles[1])  #输出列表中的第2个元素
print(bicycles[2])  #输出列表中的第3个元素
print(bicycles[3])  #输出列表中的第4个元素

#列表元素的索引号也可以用负整数表示，最后一个元素的索引号是-1,倒序往前依次递减

print('\n倒序输出列表元素')
print(bicycles[-1])  #输出列表中的倒数第1个元素
print(bicycles[-2])  #输出列表中的倒数第2个元素
print(bicycles[-3])  #输出列表中的倒数第3个元素
print(bicycles[-4])  #输出列表中的倒数第4个元素
















