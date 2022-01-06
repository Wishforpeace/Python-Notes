#4_7 if语句嵌套

#所谓“if语句嵌套”，就是指的if语句或else语句后面缩进的语句又是一个if语句

#例程1 按照年龄收费，4岁以下免费，满4不满18岁收费5美元，满18岁及以上收费10美元。
#      对于一个赋值为正整数表示年龄的变量，输出其应收费用情况      

age=input("请输入一个表示年龄的正整数age=")  #分别输入2,12,20
age=int(age)

if age < 4:
    print("Your admission cost is $0.")
    
else:  #age>=4
    
    if age<18:  #age>=4 and age<18
        print("Your admission cost is $5.")
        
    else:  #age>=18
        print("Your admission cost is $10.")

#上面的选择结构还可以使用下面的方式实现

age=input("请输入一个表示年龄的正整数age=")  #分别输入2,12,20
age=int(age)

if age < 18:
    
    if age < 4:  
        print("Your admission cost is $0.")
        
    else:  #age>=4 and age<18
        print("Your admission cost is $5.")
        
else:  #age>=18
    
    print("Your admission cost is $10.")
        
#上面两种if结构的嵌套方式中，外层与里层都是if-else结构，不同之处在于
#第一种实现方式中，里层if-else语句嵌套在else下面
#第二种实现方式中，里层if-else语句嵌套在if下面
    
#例程2 一个正整数按照能否被3整除或者能否被5整除可分成四种情况
#      对于一个赋值为正整数的变量，输出其属于哪一种情况

num=input("请输入一个正整数num=")  #分别输入6,10,15,17
num=int(num)

if num%3==0:
    
    if num%5==0:
        print("num能被3和5整除")
        
    else:
        print("num能被3整除,不能被5整除")

else:
    
    if num%5==0:
        print("num不能被3整除，能被5整除")
        
    else:
        print("num不能被3整除,也不能被5整除")
        






















