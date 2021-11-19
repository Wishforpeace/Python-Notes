## switch结构

```go
switch var1{
    case val1:
	case val2:
    default:
}
```

**这种形式可以非常优雅地进行条件判断**：****

```go
switch result := calculate(); {
    case result < 0:
        ...
    case result > 0:
        ...
    default:
        // 0
}
```

**在下面这个代码片段中，变量 a 和 b 被平行初始化，然后作为判断条件：**

```go
switch a, b := x[i], y[j]; {
    case a < b: t = -1
    case a == b: t = 0
    case a > b: t = 1
}
```

