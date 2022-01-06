#3_8 避免缩进错误

#for语句使用时常犯的错误除了忘记后面的':'外，还容易忘记缩进循环体语句

magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    
print(magician)  #没有缩进程序运行时，系统不会将这条语句作为循环体语句处理
                 #for语句后面因为没有发现循环体语句而报错

#当循环体有多条语句时，部分属于循环体的语句因为忘记缩进，程序虽然可以运行，但会导致运行结果错误

magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    
    print(magician.title() + ", that was a great trick!")  #这条语句循环执行
    
print("I can't wait to see your next trick, " + magician.title() + ".\n")

#还有一点需要强调地是，普通语句不能缩进，否则也会报错

message = "Hello Python world!"
    print(message)  #此处的print语句不应该缩进

#循环体之后执行的语句如果缩进，运行时不会报错，但是也会影响正常的运行结果

magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    
    print(magician.title() + ", that was a great trick!")
    
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
    
    print("Thank you everyone, that was a great magic show!")  #这条语句应该在循环后执行









