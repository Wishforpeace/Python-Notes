# `sync`的使用

+ `sync.WaitGroup`
+ `chan`

## 1、介绍

sync:synchronization 同步这个词的缩写，所以也叫同步包

WaitGroup：同步等待组。内部有一个计数器，从0开始，不能为负数

## 2、使用

+ Add(delta int):设置计数器

+ Done():会把计数器-1
+ Wait():会阻塞代码的运行，直到计数器的值减为0，为0终止

示例：

```go
package main

import (
	"fmt"
	"sync"
	"time"
)

var wg sync.WaitGroup

func Hi2() {
	fmt.Println("执行Hi2")
	wg.Done()
}

func Hi1() {
	fmt.Println("执行Hi1")
	wg.Done()
}
func main() {
	start_time := time.Now()
	wg.Add(2)
	go Hi1()
	go Hi2()
	wg.Wait()
	end_time := time.Now()
	fmt.Println(end_time.Sub(start_time))
}

```

