# GIN

## GIN入门

### 开始

首先创建`example.go`的文件

```
$ touch example.go
```

接下来，将如下的代码写入 `example.go` 中：

```go
package main

import "github.com/gin-gonic/gin"

func main() {
    r := gin.Default()
    r.GET("/ping", func(c *gin.Context) {
        c.JSON(200, gin.H{
            "message": "pong",
        })
    })
    r.Run() // listen and serve on 0.0.0.0:8080
}
```

### 特性

##### Gin v1 稳定的特性:

- 零分配路由。
- 仍然是最快的 http 路由器和框架。
- 完整的单元测试支持。
- 实战考验。
- API 冻结，新版本的发布不会破坏你的代码。

### Jsoniter

#### 使用 [jsoniter](https://github.com/json-iterator/go) 编译[#](https://learnku.com/docs/gin-gonic/1.7/jsoniter/11357#a37dda)

Gin 使用 `encoding/json` 作为默认的 json 包，但是你可以在编译中使用标签将其修改为 [jsoniter](https://github.com/json-iterator/go)。

```go
go build -tags=jsoniter .
```

### 部署

Gin 项目可以很方便地在以下这些云平台上部署：

#### [Qovery](https://www.qovery.com/)

Qovery 云平台提供免费的数据库、SSL 和一个全球 CDN，并支持使用 Git 自动部署。

详见 [部署你的 Gin 项目](https://docs.qovery.com/guides/tutorial/deploy-gin-with-postgresql/).

#### Render

```
Render 原生支持 Go，另外提供了 SSL 管理、数据库、平滑部署、 HTTP/2、 websocket 等支持。文档 [如何部署 Gin 项目到 Render 上](https://render.com/docs/deploy-go-gin).
```

#### **[Google App Engine](https://cloud.google.com/appengine/)**

```
GAE 有两个部署 Go 的方式。一个是标准环境，比较容易使用，但是定制起来比较不方便，并为安全提供了 [syscalls](https://github.com/gin-gonic/gin/issues/1639)。另一个是灵活的环境，可以运行各种框架和类库。

如何选择请查看文档：[ Google App Engine 的 Go 应用](https://cloud.google.com/appengine/docs/go/).
```

### 测试

#### 怎样编写 Gin 的测试用例

HTTP 测试首选 `net/http/httptest` 包。

```go
package main

import "github.com/gin-gonic/gin"

func setupRouter() *gin.Engine {
    r := gin.Default()
    r.GET("/ping", func(c *gin.Context) {
        c.String(200, "pong")
    })
    return r
}

func main() {
    r := setupRouter()
    r.Run(":8080")
}
```

上面这段代码的测试用例：

```go
package main

import (
    "net/http"
    "net/http/httptest"
    "testing"

    "github.com/stretchr/testify/assert"
)

func TestPingRoute(t *testing.T) {
    router := setupRouter()

    w := httptest.NewRecorder()
    req, _ := http.NewRequest("GET", "/ping", nil)
    router.ServeHTTP(w, req)

    assert.Equal(t, 200, w.Code)
    assert.Equal(t, "pong", w.Body.String())
}
```

