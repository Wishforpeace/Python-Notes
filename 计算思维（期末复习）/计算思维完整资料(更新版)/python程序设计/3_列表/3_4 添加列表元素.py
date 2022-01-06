#3_4 添加列表元素

# 1 在列表末尾添加元素

#（1）调用append()方法在列表末尾添加元素

#append()方法的调用方式为“列表名.append(添加元素的值)”

#方法名append后面括号里面的信息被称为该方法调用时的参数

#该参数是要添加进列表的元素值

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')  #'ducati'是调用append()方法时使用的参数  
print(motorcycles)

message='kawasaki'
motorcycles.append(message)  #变量message是调用append()方法时使用的参数  
print(motorcycles)

#（2）从空表开始逐步调用append()方法创建列表

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# 2 调用insert()方法在列表的指定位置添加（插入）元素

#insert()方法的调用方式为“列表名.insert(索引号，添加元素的值)”

#insert()方法调用时有两个参数，第一个参数索引号，添加的元素插入到该索引号对应元素的前面

#第二个参数是添加进列表的元素值，参数之间使用逗号分隔，顺序不能颠倒

#（1）通过非负整数索引值指定插入位置

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')  #索引号为0的元素是'honda'，所以'ducati'插入到'honda'的前面
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(1, 'ducati')  #索引号为1的元素是'yamaha'，所以'ducati'插入到'yamaha'的前面
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(4, 'ducati')  #索引号为4的元素不存在，所以调用时将自动在末尾添加！
print(motorcycles)

#（2）通过负整数索引值指定插入位置

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(-1, 'ducati')  #索引号为-1的元素是'suzuki'，所以'ducati'插入到'suzuki'的前面
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(-2, 'ducati')  #索引号为-2的元素是'yamaha'，所以'ducati'插入到'yamaha'的前面
print(motorcycles)






