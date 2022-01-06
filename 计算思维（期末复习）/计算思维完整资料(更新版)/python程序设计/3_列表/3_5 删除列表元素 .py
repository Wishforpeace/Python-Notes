#3_5 删除列表元素 

# 1 使用del语句删除指定位置的元素

#del语句的使用方式为“del 列表名[索引号]”，索引号是被删除元素的索引号

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]  #删除元素'honda'
del motorcycles[-1]  #删除元素'suzuki'
print(motorcycles)

# 2 调用pop()方法删除列表元素

#（1）调用不带参数的pop()方法删除列表的末尾元素

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.pop()
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

#（2）调用带参数的pop()方法删除指定位置的列表元素

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)  #删除索引号为0的列表元素'honda'
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

#如果你不确定该使用del语句还是pop()方法，下面是一个简单的判断标准：

#如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用del语句；

#如果你要在删除元素后还能继续使用它，就使用pop()方法。

motorcycles = ['honda', 'yamaha', 'suzuki']

popped_motorcycle = motorcycles.pop()  #motorcycles.pop()方法调用的结果是'suzuki'
                                       #该方法调用的结果可以给变量popped_motorcycle赋值
print(motorcycles)  #最后一个列表元素已经被删除

print(popped_motorcycle)  #被删除的元素值已经被保存到变量popped_motorcycle中

# 3 调用remove()方法根据元素值删除列表元素

#（1）不知道要从列表中删除的元素所处的位置，可使用remove()方法删除知道具体值的列表元素

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

#（2）变量也可以作为remove()方法的参数调用

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)

print("\nA " + too_expensive.title() + " is too expensive for me.")

#（3）如果要删除的值可能在列表中出现多次，remove()方法只删除第一个指定的值

motorcycles = ['honda', 'ducati','yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)





