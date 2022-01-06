#3_12 复制列表 

#切片中冒号':'前后的参数如果都缺省，则表示其默认为整个列表

my_foods = ['pizza', 'falafel', 'carrot cake']

print(my_foods[:])  #输出的切片信息和列表my_foods中的元素完全相同

#但是my_foods[:]仅仅是与列表my_foods中保存的元素信息相同，两者依然不是同一个列表

friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')  #我的食物列表里添加卡诺里
friend_foods.append('ice cream')  #朋友的食物列表里添加冰激凌

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#如果不使用切片，而是列表之间直接赋值看看会出现什么情况？

my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods

my_foods.append('cannoli')  #我的食物列表里添加卡诺里

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

friend_foods.append('ice cream')  #朋友的食物列表里添加冰激凌

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#最后总结一下，列表的复制有两种方式：

#（1）列表变量之间的直接赋值：列表1=列表2
#     这种情况下列表1与列表2实际上是同一个列表
#     对其中一个实施的修改、添加、删除操作也会实施到另一个列表上

#（2）通过列表切片给另一个列表变量赋值：列表1=列表2[a:b]
#     这种情况下列表1与列表2是两个不同的列表
#     对其中一个实施的修改、添加、删除操作不会影响到另一个列表




