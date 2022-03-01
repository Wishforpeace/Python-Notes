## Gin框架：参数接收

## 1.路由参数

### 1.1Param

当注册路由格式为:`/path/:a/:b` 时，`:x`指的就是路由参数，可以直接通过`Param("x")`获取值信息。

**a.代码示例:**

```go
package main
import (
	"github.com/gin-gonic/gin" // 引入Gin框架
)
func main() {
	// 创建一个默认的路由引擎
	engine := gin.Default()
	// 注册路由
	engine.GET("/test/:name", func(context *gin.Context) {
		// 接收参数
		name := context.Param("name")
		context.JSON(200, gin.H{"msg": "success", "name": name})
	})
	engine.GET("/test/:name/:age", func(context *gin.Context) {
		// 接收参数
		name := context.Param("name")
		age := context.Param("age")
		context.JSON(200, gin.H{
			"msg": "success",
			"name": name,
			"phone":age,
		})
	})
	engine.GET("/test/:name/:age/:height", func(context *gin.Context) {
		// 接收参数
		name := context.Param("name")
		age := context.Param("age")
		height := context.Param("height")
		context.JSON(200, gin.H{
			"msg": "success",
			"name": name,
			"phone":age,
			"height":height,
		})
	})
	_ = engine.Run()
}
```

**b.请求返回:**

```go
➜ curl -X GET http://127.0.0.1:8080/test/张三
{"msg":"success","name":"张三"}
➜ curl -X GET http://127.0.0.1:8080/test/张三/18
{"msg":"success","name":"张三","phone":"18"}
➜ curl -X GET http://127.0.0.1:8080/test/张三/18/170
{"height":"170","msg":"success","name":"张三","phone":"18"}
```

## 2.`GET`参数

### 2.1接受单值

在`Gin`框架中可以通过`Query、DefaultQuery、GetQuery`来获取`Get`参数信息，而`Query、DefaultQuery`是对`GetQuery`的二次封装。

**a.代码示例:**

```go
package main
import (
	"github.com/gin-gonic/gin" // 引入Gin框架
)
func main() {
	// 创建一个默认的路由引擎
	engine := gin.Default()
	// 注册路由
	testReceiveGetParam(engine)
	_ = engine.Run()
}
func testReceiveGetParam( engine *gin.Engine)  {
	engine.GET("/receive", func(context *gin.Context) {
		// 如果不存在或为空,则返回:""
		name := context.Query("name")
		// 如果不存在或为空,则返回默认值
		age := context.DefaultQuery("age","18")
		// 直接使用GetQuery
		home, ok := context.GetQuery("home")
		context.PureJSON(200,gin.H{
			"msg":"success",
			"context.Query->name":name,
			"context.DefaultQuery->age":age,
			"context.GetQuery->home":home,
			"context.GetQuery->ok":ok,
		})
	})
}
```

**c.请求返回:**

```go
# 不传任何参数时，看接收情况
➜ curl -X GET http://127.0.0.1:8080/receive
{"context.DefaultQuery->age":"18","context.GetQuery->ok":false,"context.GetQuery->home":"","context.Query->name":"","msg":"success"}
# 传任何参数时，看接收情况
➜ curl -X GET http://127.0.0.1:8080/receive\?age\=23\&home\=北京\&name\=小明
{"context.DefaultQuery->age":"23","context.GetQuery->ok":true,"context.GetQuery->home":"北京","context.Query->name":"小明","msg":"success"}
```

### 2.2 接收数组

在`Gin`框架中可以通过`QueryArray("param[]")`和`GetQueryArray("param[]")`获取`GET`方式提交中的数组值信息，而`QueryArray`是对`GetQueryArray`二次封装， 具体使用参考下面代码:

**a.代码示例:**

```go
package main
import (
	"github.com/gin-gonic/gin" // 引入Gin框架
	"go-use/practise" // 代码示例包
)
func main() {
	// 创建一个默认的路由引擎
	engine := gin.Default()
	// 注册路由
	practise.TestReceiveGetArrayParam(engine)
	_ = engine.Run()
}
//------ go-use/practise/param_receice.go -------
// 接收数组
func TestReceiveGetArrayParam(engine *gin.Engine)  {
	engine.GET("/getArr", func(context *gin.Context) {
		// 接收GET数组：/getArr?name[]=张三&name[]=李四
		nameList := context.QueryArray("name[]")
		context.JSON(200,gin.H{
			"arr": nameList,
		})
	})
}
```

**b.请求返回:![img](https://gitee.com/QingHui/picGo-img-bed/raw/master/img/20210427161130.png)**

### 2.3 接收Map

在`Gin`框架中可以通过`QueryMap("param")`和`GetQueryMap("param")`获取`GET`方式提交中的`map`值信息，而`QueryMap`是对`GetQueryMap`二次封装,具体使用参考下面代码:

**a.代码示例:**

```go
package main
import (
	"github.com/gin-gonic/gin" // 引入Gin框架
	"go-use/practise" // 代码示例包
)

func main() {
	// 创建一个默认的路由引擎
	engine := gin.Default()
	// 注册路由
	practise.TestRecGetMapParam(engine)
	_ = engine.Run()
}
//------ go-use/practise/param_receice.go -------
// 接收map
func TestRecGetMapParam(engine *gin.Engine)  {
	engine.GET("/getMap", func(context *gin.Context) {
		//接收GET map：/getMap?score[语文]=95&score[数学]=100
		queryMap := context.QueryMap("score")
		context.JSON(200,gin.H{
			"map":queryMap,
		})
	})
}
```

**b.请求返回:**

![image-20210427164158662](https://gitee.com/QingHui/picGo-img-bed/raw/master/img/20210427164158.png)

## 3.`POST`参数

### 3.1接受单值

在`Gin`框架中可以通过`PostForm、DefaultPostForm、GetPostForm`来获取`Post`提交的参数信息，而`PostForm、DefaultPostForm`同样是对`G e t P o s t F o r m`的二次封装。

a.代码示例：

```go
package main
import(
	"github.com/gin-gonic/gin"
  "go-use/practise"
)
func main(){
  //创建默认路由引擎
  engine := gin.Default()
  //注册路由
  practise>testRecPostSinglevalue(engine)
  _ = engine.Run()
}

```



