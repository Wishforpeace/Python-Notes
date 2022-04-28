# 使用 Golang 写爬虫经验总结

# 模拟登录

模拟登录最重要的是保存 cookies 的状态，例如在填写验证码的页面，服务器会传给客户端一个 sessionID 保存在 cookies 中，客户端在提交用户账户和验证码等信息时，需要连同这个 cookies 一起提交，否则服务器就无法判断两次请求是否为同一个客户端，从而导致验证码验证失败。
在 Golang 中可以使用 `CookieJar` 管理 cookies，在创建 `http.Client` 的对象时，传入一个非空的 CookieJar 对象即可。设置了之后，Golang 在收到服务器的响应之后，会自动把响应头中的 cookies 信息保存到 CookieJar 中，在下次发起请求时，自动从 CookieJar 中取出 cookies 信息放到请求头中。

```go
// &cookiejar.Options{PublicSuffixList: publicsuffix.List}，这是为了可以根据域名安全地设置cookies
cookieJar, err := cookiejar.New(&cookiejar.Options{PublicSuffixList: publicsuffix.List})
if err != nil {
   panic(err)
}
client = http.Client{Jar: cookieJar, Timeout: time.Second * 3}
```

# POST 提交

GET 提交方式很简单，直接拼接字符串就行了。POST 提交需要一个可读的（`io.Reader`）请求体 `body`，body 中是形如 `a=b&c=d` 格式的查询字符串（字节切片）。可以借助 `url.Values` 方便的生成查询字符串，它本质是一个 `map[string][]string`，提供了 `Set`，`Add` 等方法，让操作这个 map 更简单。

```go
params := url.Values{}
// 添加参数
params.Add("memberAccount", "xxx")
// 添加sha1后的参数
params.Add("memberUmm", fmt.Sprintf("%x", sha1.Sum([]byte("xxxx"))))
params.Add("check", captcha)
params.Add("rememberMe", "on")
// 1.必须设置正确的Content-Type，否则服务器无法正确识别参数
// 2.params.Encode()生成查询字符串，然后用string.NewReader包裹这个字符串使其可读
res, err := client.Post("https://www.example.com/login.json", "application/x-www-form-urlencoded", strings.NewReader(params.Encode()))
if err != nil {
   return "", err
}
// 记得关闭
defer res.Body.Close()
```

# 上传文件

上传文件需要借助 `multipart.Writer` 向请求体中写入相应的数据，使用 `multipart.NewWriter` 生成这样的一个写入器，它接收一个 `io.Writer` 作参数，这个参数即我们的表单体 `body`，`body` 除了需要可写，还要可读（让 httpClient 读取参数发送到服务器），并且它是流式的，所以选用 `bytes.Buffer`，一个可读写大小可变的字节流缓冲器。

```go
body := new(bytes.Buffer)
// 创建body的写入器
mulWriter := multipart.NewWriter(body)
```

## 写入普通字段

```go
// 直接调用writeField方法即可，参数1是参数名，参数2是参数值
err := mulWriter.WriteField("user_name", "xxx")
if err != nil {
    return "", err
}
```

## 写入文件字段

要写入文件，需要先调用 `CreateFormFile` 创建一个文件内容写入器，再通过写入器写入文件的内容

```go
// 创建文件写入器，并指明文件参数名和参数值
fileWriter, err := mulWriter.CreateFormFile("upload", filepath.Base(filename))
if err != nil {
    return "", err
}
// 打开需要上传的文件
file, err := os.Open(filename)
if err != nil {
    return "", err
}
defer file.Close()
// 复制文件内容到写入器
_, err = io.Copy(fileWriter, file)
if err != nil {
    return "", err
}
// 记得关闭，让缓冲区的内容写入body中
err = mulWriter.Close()
if err != nil {
   return "", err
}
res, err := client.Post("http://v1-http-api.jsdama.com/api.php?mod=php&act=upload", mulWriter.FormDataContentType(), body)
```

上面例子的最后一行，必须使用 `FormDataContentType()` 方法获取正确的 Content-Type，而不能自己写 `multipart/form-data`，这是因为 `boundary` 是随机生成的，这个必须由 Golang 告诉我们正确的值。`boundary` 即表单体中分隔每个参数的一个标志位，如下图：

![使用 Golang 写爬虫经验总结](https://cdn.learnku.com/uploads/images/201908/08/34745/dP825LrUvR.png!large)

# 使用 Fiddler 调试程序

使用 Fiddler 抓包可以让我们方便的看到程序提交到服务器的数据格式，使得调试和修改程序更加简单。Fiddler 相当于一个正向代理服务器，启动后，它会把 IE 的代理服务器设置为 http://127.0.0.1:8888 ，即 Fiddler 默认的代理地址，这样所有浏览器的请求都会先通过 Fiddler，再由 Fiddler 转发出去，实现抓包。
但是上面的机制只对系统的浏览器有效，要对其他程序也生效，需要单独的设置程序的代理。
Golang 设置代理比较简单，只需要增加一个环境变量设置即可，可以修改系统的环境变量，也可以通过代码动态添加。

```go
// 设置httpClient的代理
os.Setenv("HTTP_PROXY", "http://127.0.0.1:8888")
```

## 解决 HTTPS 解密失败的问题

如果 Fiddler 出现无法解密 HTTPS 请求，看不到原始请求数据的情况，可以尝试重新安装 Fiddler 的根证书来解决。具体操作：

1. 打开 Fiddler，依次点击菜单 Tools->Options，打开设置对话框，点击选中 "HTTPS" 面板

![使用 Golang 写爬虫经验总结](https://cdn.learnku.com/uploads/images/201908/08/34745/eF0GrRLATV.png!large)

1. 取消 “Decrypt HTTPS traffic” 的选中状态，点击 “Actions” 按钮，点击 “Reset All Certificates”，之后会弹出确认框问你是否要删除当前的证书并创建新的证书，一路允许即可

![使用 Golang 写爬虫经验总结](https://cdn.learnku.com/uploads/images/201908/08/34745/74iw26Ee4c.png!large)