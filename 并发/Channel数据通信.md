# Channel数据通信

```go
package main

import (
	"fmt"
	"sync"
)

var Wg sync.WaitGroup

func Man(ch chan string, food string) {
	ch <- food
	fmt.Printf("投食了：%s\n", food)
	Wg.Done()
}
func Cat(ch chan string) {
	food, ok := <-ch
	if ok {
		fmt.Printf("吃了：%s\n", food)
	} else {
		fmt.Println("该投食了")
	}

	Wg.Done()
}

func main() {
	Wg.Add(2)
	ch := make(chan string)
	food := "猫粮"
	defer close(ch)
	go Man(ch, food)
	go Cat(ch)

	Wg.Wait()
}

```

