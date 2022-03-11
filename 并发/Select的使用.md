# Select的使用

```go
package main

import "fmt"

func main() {
	ch := make(chan int)
	go func() {
		ch <- 3
	}()
	select {
	case num := <-ch:
		fmt.Println(num)
		fmt.Println("读取操作没问题")

	case ch <- 4:
		fmt.Println("写操作没问题")
	default:
		fmt.Println("default操作")
	}
}
```

select的特点：

+ 语句只能用于信道的读写操作；
+ select可以同时监听多个channel的写入或读取；
+ 执行select时，若只有一个case通过（不阻塞），则执行这个case块；
+ 若有多个case通过，则随机挑选一个case执行；
+ 若所有case均阻塞，且定义了default模块，则执行default模块。若未定义default模块，则select语句阻塞，直到有case被唤醒；
+ 使用break会跳出select块。



## 超时判断

```go 
package main

import (
	"fmt"
	"time"
)

func main() {
	ch := make(chan int, 5)
	for i := 0; i < 10; i++ {
		select {
		case ch <- 3:
			fmt.Printf("写入操作系统第%d\n", i+1)
		case <-time.After(time.Second * 2):
			fmt.Println("写入超时")
			break
		}

	}
}

```

