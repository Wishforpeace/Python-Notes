# golang并发编程之WaitGroup实现同步

**实例演示**

查看添加`Waitgroup`和不添加`WaitGroup`的区别

```go
package main

import (
	"fmt"
	"sync" // 同步
)

var wp sync.WaitGroup

func showMsg(i int) {
	defer wp.Done() // 延迟执行
	fmt.Printf("i:%v\n", i)
}

func main() {
	for i := 0; i < 10; i++ {
		go showMsg(i)
		wp.Add(1)
	}

	wp.Wait()
	// 主协程
	fmt.Println("end...")
}

```

