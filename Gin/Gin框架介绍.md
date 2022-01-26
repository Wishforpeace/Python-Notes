# Gin框架介绍

下载并安装gin：

```go
go get -u github.com/gin-gonic/gin
```

第一个Gin示例：

```go
package main

import (
	"github.com/gin-gonic/gin"
)

func main() {
	//创建一个默认的路由引擎
	r := gin.Default()
	//使用GET请求方式；hello：为请求路径
	r.GET("hello", func(c *gin.Context) {
		//c.JSON;返回JSON格式的数据
		c.JSON(200, gin.H{
			"message": "hello world!",
		})

	})
	//启动http服务，默认在0.0.0.0:8080启动服务
	r.Run()
}

```



