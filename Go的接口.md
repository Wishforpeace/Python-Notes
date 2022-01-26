# Go的接口

Go语言接口概念，可实现很多面向对象的特性。

接口定义了一组方法，但不包含实现的代码。==接口里不能含有变量。==

定义接口：

```
type Namer interface {
	Method1(param_list) return_type
	Method2(param_list) return_type
}
```

`Namer`是一个接口类型。

接口名字由方法名加`[e]r`后缀组成，例如`Printer`	、`Reader`、、`Writer`、`Logger`、`Converter `等等。还有一些不常用的方式（当后缀 er 不合适时），比如` Recoverable`，此时接口名以 able 结尾，或者以 I 开头（像 .NET 或 Java 中那样）。

类型（比如结构体）实现接口方法集中的方法，每一个方法的实现说明了此方法是如何作用于该类型的：即实现接口，同时方法集也构成了该类型的接口。实现了 `Namer` 接口类型的变量可以赋值给 ai （接收者值），此时方法表中的指针会指向被实现的接口方法。当然如果另一个类型（也实现了该接口）的变量被赋值给 ai，这二者（译者注：指针和方法实现）也会随之改变。





