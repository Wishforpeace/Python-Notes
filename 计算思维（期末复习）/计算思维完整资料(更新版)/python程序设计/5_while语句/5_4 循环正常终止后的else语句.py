#5_4 循环正常终止后的else语句

# 如果循环不是通过break语句（或continue语句）终止，则称该循环是正常终止

# 循环语句（for或while循环）后面若有一个else语句，当循环正常终止时，else后面缩进的语句组会执行

# 如果循环是通过break语句（或continue语句）终止，则else后面缩进的语句组不会执行

# 例程1
for i in range(6):
    if i > 3:
        print(i)
else:
    print('hello world')

#本例中循环里面没有break语句，所以循环必定是正常终止，所以上面的代码与下面的代码功能相同

for i in range(6):
    if i > 3:
        print(i)

print('hello world')


# 例程2
i=0
while i<6:
    if i>3:
        print(i)
        break
    i+=1
else:
    print('hello world')

# 本例中循环不可能正常终止，break语句肯定会被执行，所以else后面缩进的语句不会被执行


# 例程3
n=int(input('输入正整数n='))

for i in range(1,n+1):
    if i > 3:
        print(i)
        break
else:
    print('hello world')

# 本例中循环是否能正常终止，取决于输入的n的值，输入值为1,2,3时正常终止，else后面缩进的语句会被执行

# 输入值不小于4时,break语句会执行终止循环，此时else后面缩进的语句不会被执行

# 需要注意地是，如果因为一开始循环条件就不满足而导致循环没有执行，也被当做是循环的正常终止处理


# 例程4
i=2
while i<2:
    print(i)
    i+=1
else:
    print('hello world')

# 本例中循环条件一开始就不成立，所以循环不会被执行，这种情况按照程序正常终止处理，

# 所以else后面缩进的语句会被执行





















