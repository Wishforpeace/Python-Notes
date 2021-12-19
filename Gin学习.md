# Gin学习

## Gin 的介绍

[Gin](https://github.com/gin-gonic/gin) 是用 Go 编写的一个 Web 应用框架，对比其它主流的同类框架，他有更好的性能和更快的路由。由于其本身只是在官方 net/http 包的基础上做的完善，所以理解和上手很平滑。如果你现在开始做一套新的Api，我十分推荐你使用它。

Gin 的性能怎么样，需要数据说话，我们来看官方给出的表格：

```
| Benchmark name                 |       (1) |             (2) |          (3) |             (4) |
| ------------------------------ | ---------:| ---------------:| ------------:| ---------------:|
| BenchmarkGin_GithubAll         | **43550** | **27364 ns/op** |   **0 B/op** | **0 allocs/op** |
| BenchmarkAce_GithubAll         |     40543 |     29670 ns/op |       0 B/op |     0 allocs/op |
| BenchmarkAero_GithubAll        |     57632 |     20648 ns/op |       0 B/op |     0 allocs/op |
| BenchmarkBear_GithubAll        |      9234 |    216179 ns/op |   86448 B/op |   943 allocs/op |
| BenchmarkBeego_GithubAll       |      7407 |    243496 ns/op |   71456 B/op |   609 allocs/op |
| BenchmarkBone_GithubAll        |       420 |   2922835 ns/op |  720160 B/op |  8620 allocs/op |
| BenchmarkChi_GithubAll         |      7620 |    238331 ns/op |   87696 B/op |   609 allocs/op |
| BenchmarkDenco_GithubAll       |     18355 |     64494 ns/op |   20224 B/op |   167 allocs/op |
| BenchmarkEcho_GithubAll        |     31251 |     38479 ns/op |       0 B/op |     0 allocs/op |
| BenchmarkGocraftWeb_GithubAll  |      4117 |    300062 ns/op |  131656 B/op |  1686 allocs/op |
| BenchmarkGoji_GithubAll        |      3274 |    416158 ns/op |   56112 B/op |   334 allocs/op |
| BenchmarkGojiv2_GithubAll      |      1402 |    870518 ns/op |  352720 B/op |  4321 allocs/op |
| BenchmarkGoJsonRest_GithubAll  |      2976 |    401507 ns/op |  134371 B/op |  2737 allocs/op |
| BenchmarkGoRestful_GithubAll   |       410 |   2913158 ns/op |  910144 B/op |  2938 allocs/op |
| BenchmarkGorillaMux_GithubAll  |       346 |   3384987 ns/op |  251650 B/op |  1994 allocs/op |
| BenchmarkGowwwRouter_GithubAll |     10000 |    143025 ns/op |   72144 B/op |   501 allocs/op |
| BenchmarkHttpRouter_GithubAll  |     55938 |     21360 ns/op |       0 B/op |     0 allocs/op |
| BenchmarkHttpTreeMux_GithubAll |     10000 |    153944 ns/op |   65856 B/op |   671 allocs/op |
| BenchmarkKocha_GithubAll       |     10000 |    106315 ns/op |   23304 B/op |   843 allocs/op |
| BenchmarkLARS_GithubAll        |     47779 |     25084 ns/op |       0 B/op |     0 allocs/op |
| BenchmarkMacaron_GithubAll     |      3266 |    371907 ns/op |  149409 B/op |  1624 allocs/op |
| BenchmarkMartini_GithubAll     |       331 |   3444706 ns/op |  226551 B/op |  2325 allocs/op |
| BenchmarkPat_GithubAll         |       273 |   4381818 ns/op | 1483152 B/op | 26963 allocs/op |
| BenchmarkPossum_GithubAll      |     10000 |    164367 ns/op |   84448 B/op |   609 allocs/op |
| BenchmarkR2router_GithubAll    |     10000 |    160220 ns/op |   77328 B/op |   979 allocs/op |
| BenchmarkRivet_GithubAll       |     14625 |     82453 ns/op |   16272 B/op |   167 allocs/op |
| BenchmarkTango_GithubAll       |      6255 |    279611 ns/op |   63826 B/op |  1618 allocs/op |
| BenchmarkTigerTonic_GithubAll  |      2008 |    687874 ns/op |  193856 B/op |  4474 allocs/op |
| BenchmarkTraffic_GithubAll     |       355 |   3478508 ns/op |  820744 B/op | 14114 allocs/op |
| BenchmarkVulcan_GithubAll      |      6885 |    193333 ns/op |   19894 B/op |   609 allocs/op |

- (1): Total Repetitions achieved in constant time, higher means more confident result
- (2): Single Repetition Duration (ns/op), lower is better
- (3): Heap Memory (B/op), lower is better
- (4): Average Allocations per Repetition (allocs/op), lower is better
```

查看更多的数据，可以查看 [Benchmarks](https://github.com/gin-gonic/gin/blob/master/BENCHMARKS.md) .

数据很亮眼，在编程体验上 Gin 也是毫不逊色。你仅仅只需要引入包、定义路由、编写 Handler ，你的应用就搭建完成了。实际上你只需要对 gin.Context 这个结构有深刻认识，就可以使用 Gin 流畅的编写代码了。

## Gin 的使用

### 安装和更新

首次安装，使用 `go get`命令获取即可。

```bash
$ go get github.com/gin-gonic/gin
```

更新就是常规的 `go get -u`。

```bash
$ go get -u github.com/gin-gonic/gin
```

> 如果你的 go 版本大于1.12, 强烈建议使用 `go mod` 管理项目依赖。

```bash
# basic usage of go mod
# cd your/project/root/folder
# init go.mod file
$ go mod init
# will be created automatically go.mod file
# go.mod is a dependency description file, like package.json with npm
$ go build
```

### 快速运行

在你的 main 包中，引入 gin 包并初始化。

```go
package main

import (
    "github.com/gin-gonic/gin"
    "net/http"
)

func main() {
    // 初始化引擎
    engine := gin.Default()
    // 注册一个路由和处理函数
    engine.Any("/", WebRoot)
    // 绑定端口，然后启动应用
    engine.Run(":9205")
}

/**
* 根请求处理函数
* 所有本次请求相关的方法都在 context 中，完美
* 输出响应 hello, world
*/
func WebRoot(context *gin.Context) {
    context.String(http.StatusOK, "hello, world")
}
```

一个最简单的应用就写好了，来运行下试试:

```bash
$ go run
[GIN-debug] Listening and serving HTTP on :9205
```

访问 [http://127.0.0.1:9205](http://127.0.0.1:9205/) ，就可以得到响应 “hello, world” 。

## 路由(Router)

### Restful Api

你可以注册路由方法有 GET, POST, PUT, PATCH, DELETE 和 OPTIONS.

使用很简单，直接调用同名的方法即可。

```go
// 省略的代码 ...

func main() {
    router := gin.Default()

    router.GET("/someGet", getting)
    router.POST("/somePost", posting)
    router.PUT("/somePut", putting)
    router.DELETE("/someDelete", deleting)
    router.PATCH("/somePatch", patching)
    router.HEAD("/someHead", head)
    router.OPTIONS("/someOptions", options)

    // 默认绑定 :8080
    router.Run()
}

// 省略的代码 ...
```

### 动态路由（参数路由）

有时候我们需要动态的路由，如 `/user/:id`，通过调用的 url 来传入不同的 id .在 Gin 中很容易处理这种路由：

```go
// 省略的代码 ...

func main() {
    router := gin.Default()

    // 注册一个动态路由
  	// 可以匹配 /user/joy
  	// 不能匹配 /user 和 /user/
    router.GET("/user/:name", func(c *gin.Context) {
        // 使用 c.Param(key) 获取 url 参数
        name := c.Param("name")
        c.String(http.StatusOK, "Hello %s", name)
    })

  	// 注册一个高级的动态路由
    // 该路由会匹配 /user/john/ 和 /user/john/send
    // 如果没有任何路由匹配到 /user/john, 那么他就会重定向到 /user/john/，从而被该方法匹配到
    router.GET("/user/:name/*action", func(c *gin.Context) {
        name := c.Param("name")
        action := c.Param("action")
        message := name + " is " + action
        c.String(http.StatusOK, message)
    })

    router.Run(":8080")
}

// 省略的代码 ...
```

### 路由组

一些情况下，我们会有统一前缀的 url 的需求，典型的如 Api 接口版本号 `/v1/something`。Gin 可以使用 Group 方法统一归类到路由组中：

```go
// 省略的代码 ...

func main() {
    router := gin.Default()

    // 定义一个组前缀
  	// /v1/login 就会匹配到这个组
    v1 := router.Group("/v1")
    {
        v1.POST("/login", loginEndpoint)
        v1.POST("/submit", submitEndpoint)
        v1.POST("/read", readEndpoint)
    }

    // 定义一个组前缀
  	// 不用花括号包起来也是可以的。上面那种只是看起来会统一一点。看你个人喜好
    v2 := router.Group("/v2")
    v2.POST("/login", loginEndpoint)
    v2.POST("/submit", submitEndpoint)
    v2.POST("/read", readEndpoint)

    router.Run(":8080")
}

// 省略的代码 ...
```

## 中间件(Middleware)

现代化的 Web 编程，中间件已经是必不可少的了。我们可以通过中间件的方式，验证 Auth 和身份鉴别，集中处理返回的数据等等。Gin 提供了 Middleware 的功能，并与路由紧紧相连。

### 单个路由中间件

单个路由使用中间件，只需要在注册路由的时候指定要执行的中间件即可。

```go
// 省略的代码 ...

func main() {
    router := gin.Default()

    // 注册一个路由，使用了 middleware1，middleware2 两个中间件
    router.GET("/someGet", middleware1, middleware2, handler)
  
    // 默认绑定 :8080
    router.Run()
}

func handler(c *gin.Context) {
    log.Println("exec handler")
}

// 省略的代码 ...
```

### 执行流程控制

用上面的实例代码，我们来看一下中间件是怎么执行的。

```go
// 省略的代码 ...

func middleware1(c *gin.Context) {
    log.Println("exec middleware1")
  
    //你可以写一些逻辑代码
  
    // 执行该中间件之后的逻辑
    c.Next()
}

// 省略的代码 ...
```

可以看出，中间件的写法和路由的 Handler 几乎是一样的，只是多调用 `c.Next()`。

正是有个`c.Next()`，我们可以在中间件中控制调用逻辑的变化，看下面的 `middleware2` 代码。

```go
// 省略的代码 ...

func middleware2(c *gin.Context) {
    log.Println("arrive at middleware2")
    // 执行该中间件之前，先跳到流程的下一个方法
    c.Next()
    // 流程中的其他逻辑已经执行完了
    log.Println("exec middleware2")
  
    //你可以写一些逻辑代码
}

// 省略的代码 ...
```

在 `middleware2`中，执行到 `c.Next()`时，Gin 会直接跳到流程的下一个方法中，等到这个方法执行完后，才会回来接着执行 `middleware2` 剩下的代码。

所以请求上面注册的路由 url `/someGet` ，请求先到达`middleware1`，然后到达 `middleware2`，但此时 `middleware2`调用了 `c.Next()`，所以 `middleware2`的代码并没有执行，而是跳到了 `handler` ，等 `handler`执行完成后，跳回到 `middleware2`，执行 `middleware2`剩下的代码。

所以我们可以在控制台上看到以下日志输出:

```bash
exec middleware1
arrive at middleware2
exec handler
exec middleware2
```

### 路由组使用中间件

路由组使用中间件和单个路由类似，只不过是要把中间件放到 `Group` 上.

```go
// 省略的代码 ...

func main() {
    router := gin.Default()

    // 定义一个组前缀, 并使用 middleware1 中间件
  	// 访问 /v2/login 就会执行 middleware1 函数
    v2 := router.Group("/v2", middleware1)
    v2.POST("/login", loginEndpoint)
    v2.POST("/submit", submitEndpoint)
    v2.POST("/read", readEndpoint)

    router.Run(":8080")
}

// 省略的代码 ...
```

## 参数

### Url 查询参数

假定一个 url 为 `/welcome?firstname=Jane&lastname=Doe`，我们想获取参数 `firstname` 的内容，可以使用`c.Query`方法。该方法始终返回一个 `string` 类型的数据。

```go
// 省略的代码 ...

func main() {
    router := gin.Default()

    // 注册路由和Handler
    // url为 /welcome?firstname=Jane&lastname=Doe
    router.GET("/welcome", func(c *gin.Context) {
        // 获取参数内容
        // 获取的所有参数内容的类型都是 string
        // 如果不存在，使用第二个当做默认内容
        firstname := c.DefaultQuery("firstname", "Guest")
        // 获取参数内容，没有则返回空字符串
        lastname := c.Query("lastname") 

        c.String(http.StatusOK, "Hello %s %s", firstname, lastname)
    })
    router.Run(":8080")
}
```

### 表单和Body参数（Multipart/Urlencoded Form）

典型的如 `POST` 提交的数据，无论是 `multipart/form-data`格式还是`application/x-www-form-urlencoded`格式，都可以使用 `c.PostForm`获取到参数。该方法始终返回一个 `string` 类型的数据。

```go
// 省略的代码 ...

func main() {
    router := gin.Default()

    router.POST("/form_post", func(c *gin.Context) {
        // 获取post过来的message内容
        // 获取的所有参数内容的类型都是 string
        message := c.PostForm("message")
        // 如果不存在，使用第二个当做默认内容
        nick := c.DefaultPostForm("nick", "anonymous")

        c.JSON(200, gin.H{
            "status":  "posted",
            "message": message,
            "nick":    nick,
        })
    })
    router.Run(":8080")
}
```

### 上传文件

Gin 对接受用户上传的文件做了友好的处理，在 Handler 中可以很简单的实现文件的接收。

要注意的是，上传文件的大小有限制，通常是 `<32MB`，你可以使用 `router.MaxMultipartMemory`更改它。

```go
// 省略的代码 ...

func main() {
    router := gin.Default()
    // 设置文件上传大小 router.MaxMultipartMemory = 8 << 20  // 8 MiB
    // 处理单一的文件上传
    router.POST("/upload", func(c *gin.Context) {
        // 拿到这个文件
        file, _ := c.FormFile("file")
        log.Println(file.Filename)
        c.String(http.StatusOK, fmt.Sprintf("'%s' uploaded!", file.Filename))
    })
  
    // 处理多个文件的上传
    router.POST("/uploads", func(c *gin.Context) {
        form, _ := c.MultipartForm()
        // 拿到集合
        files := form.File["upload[]"]
        for _, file := range files {
            log.Println(file.Filename)
        }
        c.String(http.StatusOK, fmt.Sprintf("%d files uploaded!", len(files)))
    })
    router.Run(":8080")
}
```

我们用 `curl` 工具测试一下：

```bash
# 单一文件上传
$ curl -X POST http://localhost:8080/upload \
  -F "file=@/Users/appleboy/test.zip" \
  -H "Content-Type: multipart/form-data"

# 多文件上传
$ curl -X POST http://localhost:8080/uploads \
  -F "upload[]=@/Users/appleboy/test1.zip" \
  -F "upload[]=@/Users/appleboy/test2.zip" \
  -H "Content-Type: multipart/form-data"
```

### 其他格式的数据

一些复杂的场景下，如用户直接 `POST`一段 `json`字符串到应用中，我们需要获取原始数据，这时需要用 `c.GetRawData`来获取原始字节。

```go
// 省略的代码 ...

func main() {
    router := gin.Default()

    router.POST("/post", func(c *gin.Context) {
        // 获取原始字节
        d, err := c.GetRawData()
        if err!=nil {
            log.Fatalln(err)
        }
        log.Println(string(d))
        c.String(200, "ok")
    })
    router.Run(":8080")
}
```

`curl` 请求示例：

```bash
$ curl -v -X POST \
  http://localhost:8080/post \
  -H 'content-type: application/json' \
  -d '{ "user": "manu" }'
```

## 数据绑定

Gin 提供了非常方便的数据绑定功能，可以将用户传来的参数自动跟我们定义的结构体绑定在一起。

### 绑定 Url 查询参数（Only Bind Query String）

使用 `c.ShouldBindQuery`方法，可以自动绑定 Url 查询参数到 `struct`.

```go
package main

import (
    "log"
    "github.com/gin-gonic/gin"
)

// 定义一个 Person 结构体，用来绑定 url query
type Person struct {
    Name    string `form:"name"` // 使用成员变量标签定义对应的参数名
    Address string `form:"address"`
}

func main() {
    route := gin.Default()
    route.Any("/testing", startPage)
    route.Run(":8085")
}

func startPage(c *gin.Context) {
    var person Person
    // 将 url 查询参数和person绑定在一起
    if c.ShouldBindQuery(&person) == nil {
        log.Println("====== Only Bind By Query String ======")
        log.Println(person.Name)
        log.Println(person.Address)
    }
    c.String(200, "Success")
}
```

### 绑定url查询参数和POST参数

使用 `c.ShouldBind`方法，可以将参数自动绑定到 `struct`.该方法是会检查 Url 查询字符串和 POST 的数据，而且会根据 `content-type`类型，优先匹配`JSON`或者 `XML`,之后才是 `Form`. 有关详情查阅 [这里](https://github.com/gin-gonic/gin/blob/master/binding/binding.go#L48)

```go
package main

import "log"
import "github.com/gin-gonic/gin"
import "time"

// 定义一个 Person 结构体，用来绑定数据
type Person struct {
    Name     string    `form:"name"`
    Address  string    `form:"address"`
    Birthday time.Time `form:"birthday" time_format:"2006-01-02" time_utc:"1"`
}

func main() {
    route := gin.Default()
    route.GET("/testing", startPage)
    route.Run(":8085")
}

func startPage(c *gin.Context) {
    var person Person
    // 绑定到 person
    if c.ShouldBind(&person) == nil {
        log.Println(person.Name)
        log.Println(person.Address)
        log.Println(person.Birthday)
    }

    c.String(200, "Success")
}
```

### 其他数据绑定

Gin 提供的数据绑定功能很强大，建议你仔细查阅官方文档，了解 `gin.Context`的 `Bind*`系列方法。这里就不再一一详述。

## 数据验证

永远不要相信用户任何的输入。对于获取的外来数据，我们要做的第一步就是校验和转换。对于这类基础并且常用的功能， Gin 很贴心的帮我们提供了数据校验的方法，省去我们重复判断的烦恼。

Gin 的数据验证是和数据绑定结合在一起的。只需要在数据绑定的结构体成员变量的标签添加`binding`规则即可。详细的规则查阅 [这里](https://godoc.org/gopkg.in/go-playground/validator.v8#hdr-Baked_In_Validators_and_Tags)。

来看官方给出的一段代码：

```go
// 省略的代码 ...

// 定义的 Login 结构体
// 该 struct 可以绑定在 Form 和 JSON 中
// binding:"required" 意思是必要参数。如果未提供，Bind 会返回 error
type Login struct {
    User     string `form:"user" json:"user" binding:"required"`
    Password string `form:"password" json:"password" binding:"required"`
}

func main() {
    router := gin.Default()

    // POST 到这个路由一段 JSON, 如 ({"user": "manu", "password": "123"})
    router.POST("/loginJSON", func(c *gin.Context) {
        var json Login
        // 验证数据并绑定
        if err := c.ShouldBindJSON(&json); err == nil {
            if json.User == "manu" && json.Password == "123" {
                c.JSON(http.StatusOK, gin.H{"status": "you are logged in"})
            } else {
                c.JSON(http.StatusUnauthorized, gin.H{"status": "unauthorized"})
            }
        } else {
            c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        }
    })

    // POST 到这个路由一个 Form 表单 (user=manu&password=123)
    router.POST("/loginForm", func(c *gin.Context) {
        var form Login
        // 验证数据并绑定
        if err := c.ShouldBind(&form); err == nil {
            if form.User == "manu" && form.Password == "123" {
                c.JSON(http.StatusOK, gin.H{"status": "you are logged in"})
            } else {
                c.JSON(http.StatusUnauthorized, gin.H{"status": "unauthorized"})
            }
        } else {
            c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        }
    })

    router.Run(":8080")
}
```

除了绑定验证之外，你还可以注册自定义的验证器。

我们来看这段完整的代码：

```go
package main

import (
    "net/http"
    "reflect"
    "time"
    "github.com/gin-gonic/gin"
    "github.com/gin-gonic/gin/binding"
    "gopkg.in/go-playground/validator.v8"
)

// 定义的 Booking 结构体
// 注意成员变量CheckIn的标签 binding:"required,bookabledate"
// bookabledate 即下面自定义的验证函数
// 成员变量CheckOut的标签 binding:"required,gtfield=CheckIn"
// gtfield 是一个默认规则，意思是要大于某个字段的值
type Booking struct {
    CheckIn  time.Time `form:"check_in" binding:"required,bookabledate" time_format:"2006-01-02"`
    CheckOut time.Time `form:"check_out" binding:"required,gtfield=CheckIn" time_format:"2006-01-02"`
}

// 定义一个验证方法，用来验证时间是否合法
// 验证方法返回值应该是个布尔值
func bookableDate(
    v *validator.Validate, topStruct reflect.Value, currentStructOrField reflect.Value,
    field reflect.Value, fieldType reflect.Type, fieldKind reflect.Kind, param string,
) bool {
    if date, ok := field.Interface().(time.Time); ok {
        today := time.Now()
        if today.Year() > date.Year() || today.YearDay() > date.YearDay() {
            return false
        }
    }
    return true
}

func main() {
    route := gin.Default()
    // 注册一个自定义验证方法 bookabledate
    binding.Validator.RegisterValidation("bookabledate", bookableDate)
    route.GET("/bookable", getBookable)
    route.Run(":8085")
}

func getBookable(c *gin.Context) {
    var b Booking
    // 验证数据并绑定
    if err := c.ShouldBindWith(&b, binding.Query); err == nil {
        c.JSON(http.StatusOK, gin.H{"message": "Booking dates are valid!"})
    } else {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
    }
}
```

Gin 提供的验证灰常灰常强大，可以帮我们很好的处理数据验证和省掉各种 `if else`的判断，建议各位使用 Gin 的道友一定要把这个东东吃透。

## 输出响应

Web 应用的目标之一就是输出响应。Gin 为我们提供了多种常见格式的输出，包括 `HTML`, `String`，`JSON`， `XML`， `YAML`。

### String

```go
// 省略的代码 ...

func Handler(c *gin.Context) {
    // 使用 String 方法即可
    c.String(200, "Success")
}

// 省略的代码 ...
```

### JSON、 XML、 YAML

Gin 输出这三种格式非常方便，直接使用对用方法并赋值一个结构体给它就行了。

你还可以使用`gin.H`。`gin.H` 是一个很巧妙的设计，你可以像`javascript`定义`json`一样，直接一层层写键值对，只需要在每一层加上 `gin.H`即可。看代码：

```go
// 省略的代码 ...

func main() {
    r := gin.Default()

    // gin.H 本质是 map[string]interface{}
    r.GET("/someJSON", func(c *gin.Context) {
        // 会输出头格式为 application/json; charset=UTF-8 的 json 字符串
        c.JSON(http.StatusOK, gin.H{"message": "hey", "status": http.StatusOK})
    })

    r.GET("/moreJSON", func(c *gin.Context) {
        // 直接使用结构体定义
        var msg struct {
            Name    string `json:"user"`
            Message string
            Number  int
        }
        msg.Name = "Lena"
        msg.Message = "hey"
        msg.Number = 123
        // 会输出  {"user": "Lena", "Message": "hey", "Number": 123}
        c.JSON(http.StatusOK, msg)
    })

    r.GET("/someXML", func(c *gin.Context) {
        // 会输出头格式为 text/xml; charset=UTF-8 的 xml 字符串
        c.XML(http.StatusOK, gin.H{"message": "hey", "status": http.StatusOK})
    })

    r.GET("/someYAML", func(c *gin.Context) {
        // 会输出头格式为 text/yaml; charset=UTF-8 的 yaml 字符串
        c.YAML(http.StatusOK, gin.H{"message": "hey", "status": http.StatusOK})
    })

    r.Run(":8080")
}

// 省略的代码 ...
```

### HTML

Gin 使用 Html 模板就是官方标准包`html/template`, 模板的用法没什么太多要说明的。这里给大家说一下如何在 gin 中输出 `html`。

由于 Gin 并没有强制的文件夹命名规范，所以我们必须要告诉 Gin 我们的静态资源（如图片、Css、JS 脚本等）和我们的html 模板放在了哪里，看代码：

```go
package main

import "github.com/gin-gonic/gin"

func main() {
    engine := gin.Default()
    engine.GET("/html-test", startPage)
    // 注册一个目录，gin 会把该目录当成一个静态的资源目录
    // 该目录下的资源看可以按照路径访问
    // 如 static 目录下有图片路径 index/logo.png , 你可以通过 GET /static/index/logo.png 访问到
    engine.Static("/static", "./static")
    // 注册一个路径，gin 加载模板的时候会从该目录查找
    // 参数是一个匹配字符，如 views/*/* 的意思是 模板目录有两层
    // gin 在启动时会自动把该目录的文件编译一次缓存，不用担心效率问题
    engine.LoadHTMLGlob("views/*/*")
  
    route.Run(":9205")
}

func startPage(c *gin.Context) {
    // 输出 html
    // 三个参数，200 是http状态码
    // "shop/search" 要加载的模板路径，对应目录路径 views/shop/search.html
    // gin.H{"keywords":"macbook pro"} 是模板变量
    c.HTML(200, "shop/search", gin.H{"keywords":"macbook pro"})
}
```

编译启动后访问 `/html-test`, 就可以看到编译后的模板字符串输出.

## 开发热更新

我们在开发代码时希望能够边改代码边运行看到结果，类似于 `PHP`脚本语言那样，但受限于 Go 的编译运行，自身无法实现，所以要借助一些第三方工具来解决这个问题。

我使用 Go 开发了一个文件更新通知的软件 `fileboy`，可以很好的处理这类问题。该软件已开源，有兴趣的朋友可以在 [fileboy github ](https://github.com/dengsgo/fileboy)下载使用。

`gin` 项目的 `filegirl.yaml` 配置示例如下：

```yaml
core:
    version: 1

monitor:
    includeDirs:
        - .,*

    exceptDirs:
        - .idea
        - .git
        - .vscode
        - node_modules
        - vendor

    types:
        - .go
        - .html

    events:
        - write
        - rename
        - remove
        - create
        - chmod

command:
    exec:
        - go build -o app.exe
        - ./app.exe

    delayMillSecond: 2000

notifier:
    callUrl: ""

instruction:
    - exec-when-start
    - ignore-warn
```

## 测试

测试时一款健壮的应用程序不可或缺的一部分（虽然我们都不喜欢写这玩意）。Gin 是怎么解决这个环节的呢？

呃。。。。好吧，实际上 Gin 并没有提供内置方法 （此处应有斜眼笑）.

Gin 直接推荐使用 Go 官方包 `net/http/httptest` 来测试你的应用。

> The `net/http/httptest` package is preferable way for HTTP testing.

假定有如下一段代码：

```go
// 省略的代码 ...

func setupRouter() *gin.Engine {
    r := gin.Default()
    r.GET("/ping", func(c *gin.Context) {
        // 以 200 的 http status 输出字符串 pong
        c.String(200, "pong")
    })
    return r
}

func main() {
    r := setupRouter()
    r.Run(":8080")
}
```

那么我们可以这样编写测试代码：

```go
package main

import (
    "net/http"
    "net/http/httptest"
    "testing"

    "github.com/stretchr/testify/assert" // 这是一个断言库，你也可以直接比较
)

func TestPingRoute(t *testing.T) {
    router := setupRouter()
    // 获取一个请求实例
    w := httptest.NewRecorder()
    // 构造请求
    // 参数依次是 请求方法、路由、参数
    req, _ := http.NewRequest("GET", "/ping", nil)
    // 执行
    router.ServeHTTP(w, req)
    // 断言
    assert.Equal(t, 200, w.Code)
    assert.Equal(t, "pong", w.Body.String())
    // 完了
}
```