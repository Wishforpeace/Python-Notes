# golang并发编程之runtime包

runtime包里面定义了一些协程管理相关的api

## runtime.Gosched()

让出CPU时间片，重新等待安排任务

```go
package main

import (
	"fmt"
	"runtime"
)

func show(c string) {
	for i := 0; i < 2; i++ {
		fmt.Printf("msg:%v", c)
	}
}

func main() {
	go show("java") // 子协程
	// 主协程
	for i := 0; i < 2; i++ {
		runtime.Gosched() // 我有权利执行任务了，让给其他子协程来执行
		fmt.Printf("\"golang\":%v\n", "golang")
	}
	fmt.Println("end...")
}

```

## runtime.Goexit()

退出当前协程

```go
package main

import (
	"fmt"
	"runtime"
	"time"
)

func showMsg() {
	for i := 0; i < 10; i++ {
		fmt.Printf("i:%v\n", i)
		if i >= 5 {
			runtime.Goexit()
		}
	}
}

func main() {
	go showMsg()
	time.Sleep(time.Second)
}

```



## runtime.GOMAXPROCS

```go
package main

import (
	"fmt"
	"runtime"
	"time"
)

func a() {
	for i := 0; i < 10; i++ {
		fmt.Println("a:", i)
	}
}

func b() {
	for i := 0; i < 10; i++ {
		fmt.Println("b:", b)
	}
}

func main() {
	fmt.Printf("runtime.NumCPU():%v\n", runtime.NumCPU())
	go a()
	go b()
	time.Sleep(time.Second)
}

```

