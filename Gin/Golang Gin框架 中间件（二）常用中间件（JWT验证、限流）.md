# Golang Gin框架 中间件（二）常用中间件（JWT验证、限流）

 小小小丶叶子  423 阅读 1 点赞



## 一、JWT验证中间件

### 1.对比 `cookie`、`session`、`token`、`jwt`

#### 因为HTTP是无状态协议，无法证明切换了网页无法证明“你还是你”，所以为了能够保存一些状态或者信息，有了这些方案：

- #### `cookie`

> 由服务器生成，发送给浏览器，浏览器以键值对的方式保存下来，下次发送请求的时候带上cookie保存的信息传给客服务器。

> 缺点：每个域名下可使用数量少，大小也有限制。

- #### `session`

> 由服务器生成，服务器保存主体信息，会发送一个sessionid给客户端cookie保存，下次发送请求时带上sessionid传给服务端，服务端根据sessionid和主体信息进行对比验证。

> 缺点：
>
> - cookie+session在跨域场景很麻烦；
> - 如果是分布式部署，需要做多机共享session机制；
> - 基于cookie的机制容易被CSRF；
> - 查询session信息可能会有数据库查询操作，带来性能问题。

- #### `token`

> 由用户发送用户名密码给服务端，服务端验证，成功之后就返回一个token给客户端，之后的请求都带上token信息，服务端也每次都验证是否有效，一般token会保存在数据库中。

> 缺点：客户端每次携带token，保存的内容太多，而且可能涉及到查数据库的操作。

- #### `JWT`

> 和token有点类似，在服务端加入了一个secret密钥，由用户发送用户名密码给服务端，服务端验证，成功之后就生成三个部分`header`,`payload`,`signature`组成的jwt token给客户端，之后的请求都带上 jwt token，服务端通过secret密钥进行验证。

> 缺点：无法中途废弃

### 2.Golang JWT验证

#### 2.1. 使用的jwt第三方库

```golang
github.com/dgrijalva/jwt-go
复制代码
```

#### 2.2. 生成jwt token

```golang
type MyClaims struct {
   Username string `json:"username"`
   jwt.StandardClaims
}

const TokenExpireDuration = time.Hour * 24 //设置过期时间

var Secret = []byte("secret") //密码自行设定

func GenToken(username string) (string, error) {
   // 创建一个我们自己的声明
   c := MyClaims{
      username, // 自定义字段
      jwt.StandardClaims{
         ExpiresAt: time.Now().Add(TokenExpireDuration).Unix(), // 过期时间
         Issuer:    "superxon",                                 // 签发人
      },
   }
   // 使用指定的签名方法创建签名对象
   token := jwt.NewWithClaims(jwt.SigningMethodHS256, c)
   // 使用指定的secret签名并获得完整的编码后的字符串token
   return token.SignedString(Secret)
}
复制代码
```

#### 2.3. 验证用户密码并把生成的jwt token返回给客户端保存

```golang
type Profile struct {
   Username    string `db:"username"`
   Password    string `db:"password"`
}
复制代码
func AuthLoginHandler(c *gin.Context) {
   // 用户发送用户名和密码过来
   var user User.Profile
   err := c.ShouldBindJSON(&user)
   if err != nil {
      c.JSON(http.StatusBadRequest, gin.H{
         "code": 2001,
         "msg":  "无效的参数",
      })
      return
   }
   // 校验用户名和密码是否正确
   _, err := getProfile(user.Username)
   if err != nil {
       c.JSON(http.StatusNotFound, gin.H{
          "code": 2003,
          "msg":  "用户不存在",
       })
       return
   }

   tokenString, _ := Middlewares.GenToken(user.Username)
   c.JSON(http.StatusOK, gin.H{
       "code":     2000,
       "msg":      "success",
       "Token":    tokenString,
       "username": profile.Username,
   })
}
复制代码
```

#### 2.4. 接收请求（Headers中放入`authorization`=jwt token） JWT验证的中间件

```
解析token
// ParseToken 解析JWT
func ParseToken(tokenString string) (*MyClaims, error) {
   // 解析token
   token, err := jwt.ParseWithClaims(tokenString, &MyClaims{}, func(token *jwt.Token) (i interface{}, err error) {
      return MySecret, nil
   })
   if err != nil {
      return nil, err
   }
   if claims, ok := token.Claims.(*MyClaims); ok && token.Valid { // 校验token
      return claims, nil
   }
   return nil, errors.New("invalid token")
}
复制代码
验证中间件
// JWTAuthMiddleware 基于JWT的认证中间件--验证用户是否登录
func JWTAuthMiddleware() func(c *gin.Context) {
   return func(c *gin.Context) {
      authHeader := c.Request.Header.Get("authorization")
      if authHeader == "" {
         c.JSON(http.StatusUnauthorized, gin.H{
            "code": 2003,
            "msg":  "请求头中auth为空",
         })
         c.Abort()
         return
      }
      // 按空格分割
      parts := strings.Split(authHeader, ".")
      if len(parts) != 3 {
         c.JSON(http.StatusUnauthorized, gin.H{
            "code": 2004,
            "msg":  "请求头中auth格式有误",
         })
         c.Abort()
         return
      }
      mc, ok := ParseToken(authHeader, Secret)
      if ok == false {
         c.JSON(http.StatusUnauthorized, gin.H{
            "code": 2005,
            "msg":  "无效的Token",
         })
         c.Abort()
         return
      }
      m := mc.(jwt.MapClaims)
      // 将当前请求的username信息保存到请求的上下文c上
      c.Set("username", m["username"])
      c.Next() // 后续的处理函数可以用过c.Get("username")来获取当前请求的用户信息
   }
}
复制代码
```

#### 2.5. 可以进行测试，在路由中使用JWT中间件和不使用的区别。

## 二、 限流中间件

### 1.参考文档 [限流中间件](https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F354064637)

### 2.使用场景为防止并发量突然增高时，服务器无法承受，保证了QPS的上限值。

### 3.主要分为`漏桶`和`令牌桶`：

> 漏桶是指我们有一个一直装满了水的桶，每过固定的一段时间即向外漏一滴水。如果你接到了这滴水，那么你就可以继续服务请求，如果没有接到，那么就需要等待下一滴水。

> 令牌桶则是指匀速向桶中添加令牌，服务请求时需要从桶中获取令牌，令牌的数目可以按照需要消耗的资源进行相应的调整。如果没有令牌，可以选择等待，或者放弃。

### 4.golang第三方库

```
github.com/juju/ratelimit
```

### 5.示例代码

```golang
package main

import (
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
	"github.com/juju/ratelimit"
)

func RateLimitMiddleware(fillInterval time.Duration, cap, quantum int64) gin.HandlerFunc {
	bucket := ratelimit.NewBucketWithQuantum(fillInterval, cap, quantum)
	return func(c *gin.Context) {
		if bucket.TakeAvailable(1) < 1 {
			c.String(http.StatusForbidden, "rate limit...")
			c.Abort()
			return
		}
		c.Next()
	}
}

func main() {
	r := gin.Default()
	gin.ForceConsoleColor()
	r.Use(RateLimitMiddleware(time.Second, 100, 100)) //初始100，每秒放出100
	r.GET("/", func(c *gin.Context) {
		c.String(http.StatusOK, "golang ~")
	})
	r.Run(":8080")
}
复制代码
```

### 6.库中其它方法

- #### 默认的令牌桶，fillInterval 指每过多长时间向桶里放一个令牌，capacity 是桶的容量，超过桶容量的部分会被直接丢弃。桶初始是满的

```golang
func NewBucket(fillInterval time.Duration, capacity int64) *Bucket
复制代码
```

- #### 和普通的 NewBucket() 的区别是，每次向桶中放令牌时，是放 quantum 个令牌，而不是一个令牌。

```golang
func NewBucketWithQuantum(fillInterval time.Duration, capacity, quantum int64) *Bucket
复制代码
```

- #### 按照提供的比例，每秒钟填充令牌数。例如 capacity 是100，而 rate 是 0.1，那么每秒会填充10个令牌。

```　golang
func NewBucketWithRate(rate float64, capacity int64) *Bucket
复制代码
```