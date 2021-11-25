# Golang爬虫简明教程

## 爬取HTML源码

### net/http包

#### http包提供了HTTP客户端和服务端的实现。

##### Get、Head、Post和PostForm函数发出HTTP/ HTTPS请求。

```go
resp, err := http.Get("http://example.com/")
...
resp, err := http.Post("http://example.com/upload", "image/jpeg", &buf)
...
resp, err := http.PostForm("http://example.com/form",
	url.Values{"key": {"Value"}, "id": {"123"}})
```

##### 程序使用完必须关闭回复主体

```go
resp, err := http.Get("http://example.com/")
if err! = nil{
    //handle error
}
defer resp.Body.Close()
body, err := ioutil.ReadAll(res.Body)
```

##### 要管理HTTP客户端的头域、重定向策略和其他设置，创建一个Client：

```go
client := &http.Client{
	CheckRedirect: redirectPolicyFunc,
}
resp, err := client.Get("http://example.com")
// ...
req, err := http.NewRequest("GET", "http://example.com", nil)
// ...
req.Header.Add("If-None-Match", `W/"wyzzy"`)
resp, err := client.Do(req)
// ...
```

##### 要管理代理、TLS、keep-alive、压缩和其他设置，创建一个Transport：

```go
tr := &http.Transfer{
    TLSClientConfig:  &tls.Config{RootGAs: pool},
    DisableCompression: true,
}
client := &http.Client{Transport: tr}
resp, err := client.Get("http://example.com")
```

##### Client和Transport类型都可以安全的被多个go程同时使用。处于效率考虑，应该一次建立、尽量重用。

##### ListenAndServe使用指定的监听地址和处理器启动一个HTTP服务端。处理器参数通常是nil，这表示采用包变量DefaultServeMux作为处理器。Handle和HandleFunc函数可以向DefaultServeMux添加处理器。

```go
http.Handle("/foo",fooHandler)
http.HandleFunc("/bar",func(w http.ResponseWriter,r *http.Request){
    fmt.Fprint(w,"hello,%q",html.EscapeString(r.URL.Path))
})
log.Fatal(http.ListenAndServe(":8080",nil))
```

##### 要管理服务器的行为，可以自定义Server

```go
s := &http.Serve{
    Addr:                   ":8080",
    Handler:                myhandler,
    ReadTimeout:            10* time.Second,
    WriteTimeout:			10* time.Second,
    MaxHeaderBytes:         1<<20,
}
log.Fatal(s.ListenAndServe())
```

