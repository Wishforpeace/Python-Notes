#5_3 通过break语句终止for循环

# for语句和while语句都可以实现循环，两者可以互相转换，所以for循环中也可以使用break语句终止循环

n=input('输入一个小于10的正整数n=')
n=int(n)

for i in range(1,10):
    
    if i==n+1:  
        break
    
    print(i)

print("循环结束后i=",i)

    


















