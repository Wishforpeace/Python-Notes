#2_7数值数据与字符串数据的混合运算

age=23  #给整数型变量age赋值

print(age)  #输出23

message="Happy "+age+"rd Birthday"  #执行这条语句时会报错

#因为age是整型变量，对于整型数而言，+是加法运算

#对于字符串"Happy "和"rd Birthday"而言，+是连接运算

#所以类型不同的数据实施+运算时出现类型不匹配的错误

#上面这条语句可以改成下面的形式执行

message="Happy "+str(age)+"rd Birthday"

#函数str的功能是将变量age里面的整数值23转换为字符串'23'

#所以str(age)的调用结果是字符串类型，而不是整数类型

#上面的语句也可以改成下面的形式执行

num=str(age)  #将str(age)的调用结果给变量num赋值，所以num也是字符串类型

message="Happy "+num+"rd Birthday"

print(message)


 







