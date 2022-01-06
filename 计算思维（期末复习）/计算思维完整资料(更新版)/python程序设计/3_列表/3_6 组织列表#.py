#3_6 组织列表 

# 1 使用sort()方法对列表进行永久性排序

#（1）英文字母组成的字符串元素默认按照字母序排列
 
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#（2）英文字母组成的字符串元素也可以通过设置参数按照字母序的反序排列

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# 2 使用函数sorted()对列表进行临时排序

print()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))  #函数sorted()调用后会得到一个排序后的列表cars的复制版本
                     #并没有真正修改列表cars的顺序

print("\nHere is the original list again:")
print(cars)

# 3 调用reverse()方法按照列表元素的顺序反序排列

print()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()  #该方法是按照列表元素的反序排列，而不是按照字母序的反序
print(cars)

# 4 使用len()函数求列表长度（元素个数）

print()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

#函数与方法本质上是一回事，只不过调用方式不同而已

#方法的调用方式为“变量名.方法名(参数列表)”

#函数的调用方式为“函数名(参数列表)”




