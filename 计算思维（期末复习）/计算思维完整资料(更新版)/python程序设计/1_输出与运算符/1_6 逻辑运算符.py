#1_6 逻辑运算符

# 逻辑运算符包括：and(与)，or(或)，not(非)

# 可以将关系表达式或算术表达式使用逻辑运算符连接起来组成逻辑表达式，其结果也是布尔值

#（1）True and True == True，True and False == False and True == False and False == False

#（2）False or False == False， True or False == False or True == True or True == True

#（3）not True == False， not False == True

# 在命令行模式下求下面表达式的计算结果

3>2 and 3==3   3<2 and 3==3   3<2 and 3!=3

3>2 or 3==3   3<2 or 3==3   3<2 or 3!=3

not 3>2   not 3<2 

# 有时关系表达式也可以和算术表达式使用逻辑运算符连接起来进行逻辑运算，

# 这种情况下对于算术运算符而言，结果为0时被当做False处理，结果非0时被当做True处理

# 在命令行模式下求下面表达式的计算结果

3+2 and 3>2   3-2 and 3<2   3==2 and 3-3

3+2 or 3<2   3-2 or 3>2   3-3 or 3==2

not 0   not 1   not 3+2  not 3-3















