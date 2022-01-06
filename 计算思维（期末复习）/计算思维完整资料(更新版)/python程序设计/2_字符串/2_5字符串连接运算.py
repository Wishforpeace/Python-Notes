#2_5字符串连接运算

#所谓字符串连接就是将一个字符串连接到另一个字符串的末尾

#例如字符串"abc"连接上字符串"1234"之后得到新字符串"abc1234"

#在python中使用'+'表示字符串连接运算

first_name="ada"

last_name="lovelace"

full_name=first_name+" "+last_name  #字符串" "表示一个空格

print(full_name)  #输出字符串为"ada lovelace"

print("Hello, "+full_name.title()+"!")  #print也可以输出表达式的结果

message="Hello, "+full_name.title()+"!"

print(message)










