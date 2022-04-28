# Http标准库

+ 使用`http`向客户端发送请求
+ 使用`http.Client`控制请求头部
+ 使用`httoutil`简化工作

```go
package main

import (
	"fmt"
	"net/http"
	"net/http/httputil"
)

func main() {
	request, err := http.NewRequest(
		http.MethodGet,
		"https://www.imooc.com", nil,
	)
	request.Header.Add("User-Agent", "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1")
	client := http.Client{
		CheckRedirect: func(
			req *http.Request,
			via []*http.Request) error {
			fmt.Println("Redirect", req)
			return nil
		},
	}
	//resp, err := http.Get("https://www.imooc.com")
	//resp, err := http.DefaultClient.Do(request)
	resp, err := client.Do(request)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()
	// 显示response
	s, err := httputil.DumpResponse(resp, true)
	if err != nil {
		panic(err)
	}
	fmt.Printf("%s\n", s)

}

```

