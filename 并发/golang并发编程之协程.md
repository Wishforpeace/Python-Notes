# golang并发编程之协程

Golang中的并发事函数相互独立运行的能力。Goroutines是并发运行的函数。Golang提供了Goroutines作为并发处理操作的一种方式。

创造一个协程非常简单，就是在任务函数前加go关键字：

```go
go task()
```

##  实例1

```go
package main

import (
	"fmt"
	"time"
)

func showMsg(msg string) {
	for i := 0; i < 5; i++ {
		fmt.Printf("msg:%v\n", msg)
		time.Sleep(time.Millisecond * 100)
	}
}
func main() {
	go showMsg("Java ")  //go 启动了一个协程来执行1
	go showMsg("golang") // 2
	time.Sleep(time.Millisecond * 2000)
	fmt.Println("main end ...") //3 主函数退出，程序结束
}

```

## 实例2

```go
package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"time"
)

func responseSize(url string) {
	fmt.Println("Step1:", url)
	response, err := http.Get(url)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Step3", url)
	fmt.Println("Steps3", url)
	body, err := ioutil.ReadAll(response.Body)
	if err != nil {
		log.Fatal("Step4", len(body))
	}
	fmt.Println("Step4:", len(body))
}

func main() {
	go responseSize("http://www,duoke360.com")
	go responseSize("http://baidu.com")
	go responseSize("http://jd.com")
	time.Sleep(10 * time.Second)
}


```

