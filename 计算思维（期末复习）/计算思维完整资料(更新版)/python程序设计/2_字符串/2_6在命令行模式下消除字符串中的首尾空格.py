#2_6在命令行模式下消除字符串中的首尾空格

#在命令行（终端）模式下运行以下语句

favorite_language=' python '  #字符串开头与末尾各有一个空格

favorite_language  #询问变量favorite_language的值，回车后系统会输出其值
                   #输出的值由单引号括起来

print(favorite_language)  #输出的信息中不包括单引号

#命令行（终端）模式下键入变量方法调用的语句，回车后系统会输出方法调用的结果

favorite_language.lstrip()  #方法lstrip()的作用是去掉字符串变量中开头的空格
                            #询问变量favorite_language调用lstrip()方法后的结果
                            #回车后会输出favorite_language.lstrip()的调用结果

favorite_language.rstrip()  #方法rstrip()的作用是去掉字符串变量中末尾的空格
                            #询问变量favorite_language调用rstrip()方法后的结果
                            #回车后会输出favorite_language.rstrip()的调用结果

favorite_language.strip()  #方法strip()的作用是去掉字符串变量中开头和末尾的空格
                           #询问变量favorite_language调用strip()方法后的结果
                           #回车后会输出favorite_language.strip()的调用结果

favorite_language  #询问变量favorite_language的值，发现其值没有发生变化

#方法lstrip()与rstrip()以及strip()的调用结果仅仅是输出去掉相应空格后的变量的值

#并没有实际修改变量的值，想要修改变量的值，还需要将调用结果赋值给变量

#观察以下几条语句在命令行（终端）模式下的运行结果

favorite_language=favorite_language.lstrip()

favorite_language

favorite_language=favorite_language.rstrip()

favorite_language

favorite_language=' python '

favorite_language

favorite_language=favorite_language.strip()

favorite_language

#程序中出现的变量方法调用的语句，如favorite_language.strip()以及前面例子中的name.title()等

#如果没有结合print语句使用，将不会输出任何结果












