# Go 教程：从零实现 JWT 认证

> 身份验证使应用程序知道向应用程序发送请求的人是谁。JSON Web 令牌（JWT）是一种允许身份验证的方法，而无需在系统本身实际存储任何有关用户的任何信息（与基于会话的身份验证相反 ）。

## JWT格式

假设我们有一个名为的用户 user1，他们尝试登录到应用程序或网站。一旦成功，他们将收到一个看起来像这样的令牌：

```html
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVzZXIxIiwiZXhwIjoxNTQ3OTc0MDgyfQ.2Ye5_w1z3zpD4dSGdRp3s98ZipCNQqmsHRB9vioOx54``

```

**这是一个 JWT，由三部分组成（以分隔.）：**

1.第一部分是标题 header（`eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9`）。标头指定信息，例如用于生成签名的算法（第三部分）。这部分是标准的，并且对于使用相同算法的任何 JWT 都是相同的。
2.第二部分是有效负载 payload （`eyJ1c2VybmFtZSI6InVzZXIxIiwiZXhwIjoxNTQ3OTc0MDgyfQ`），其中包含特定于应用程序的信息（在我们的示例中，这是用户名），以及有关令牌的到期和有效性的信息。
3.第三部分是签名（`2Ye5_w1z3zpD4dSGdRp3s98ZipCNQqmsHRB9vioOx54`）。它是通过组合和散列前两个部分以及一个秘密密钥来生成的。

标题 header 和有效负载 payload 未加密。它们只是 base64 编码的。这意味着任何人都可以通过解码来查看其内容。

例如，我们可以使用此[在线工具](https://tools.sohamkamani.com/base64-decoder/) 对标题或有效负载进行解码。

它将显示为以下内容：

```
{ "alg": "HS256", "typ": "JWT" }
```

如果您使用的是 Linux 或 Mac OS，也可以在终端上执行以下语句：

```
echo eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9 | base64 -D
```

同样，有效负载的内容为：

```
{ "username": "user1", "exp": 1547974082 }
```



## JWT 签名如何工作

因此，如果任何人都可以读写 JWT 的标头和签名，那么实际上如何保证 JWT 是安全的？答案在于如何生成最后一部分（签名）。

假设你的应用程序想要向成功登录的用户 `user1 `签发 JWT。

使标头和有效负载非常简单：标头或多或少是固定的，有效负载 JSON 对象是通过设置用户 ID 和有效时间（以 Unix 毫秒为单位）来形成的。

发行令牌的应用程序还拥有一个密钥，该密钥是一个私有值，并且仅对应用程序本身是已知的。然后将标头和有效负载的 base64 表示形式与密钥组合，然后通过哈希算法计算签名值（在本例中为 `HS256`，如标头中所述）![](https://cdn.learnku.com/uploads/images/202009/18/1/xBqvamzTiw.svg)

## GO语言实现

### 创建 HTTP 服务器

```go
package main

import (
    "log"
    "net/http"
)

func main() {
    // "Signin"和"Welcome"方法是我们将要实现的处理程序
    http.HandleFunc("/signin", Signin)
    http.HandleFunc("/welcome", Welcome)
    http.HandleFunc("/refresh", Refresh)

    // 在8000端口启动服务
    log.Fatal(http.ListenAndServe(":8000", nil))
}
```

现在，我们可以定义 `Signin` 和 `Welcome` 路由。

### 处理用户登录

`/signin` 路由将获取用户凭据并登录。为简化起见，我们在代码中将用户信息存储在 map：

```go
var users = map[string]string{
    "user1": "password1",
    "user2": "password2",
}
```

因此，目前，我们的应用程序中只有两个有效用户：` user1` 和 `user2`。接下来，我们可以编写 SigninHTTP 处理程序。对于此示例，我们使用 `dgrijalva/jwt-go` 库来帮助我们创建和验证 JWT 令牌。

```go
import (
  //...
  // 导入jwt-go库
    "github.com/dgrijalva/jwt-go"
    //...
)

// 创建一个jwt使用的密钥
var jwtKey = []byte("my_secret_key")

var users = map[string]string{
    "user1": "password1",
    "user2": "password2",
}

// 创建一个结构以从请求正文中读取用户名和密码
type Credentials struct {
    Password string `json:"password"`
    Username string `json:"username"`
}

// 创建将被编码为JWT的结构。
// 我们将jwt.StandardClaims作为嵌入式类型，以提供到期时间等字段。
type Claims struct {
    Username string `json:"username"`
    jwt.StandardClaims
}

// 创建Signin处理函数。
func Signin(w http.ResponseWriter, r *http.Request) {
    var creds Credentials
    // 获取JSON正文并解码为凭据
    err := json.NewDecoder(r.Body).Decode(&creds)
    if err != nil {
        // 如果主体结构错误，则返回HTTP错误
        w.WriteHeader(http.StatusBadRequest)
        return
    }

    // 从我们的map中获取用户的密码
    expectedPassword, ok := users[creds.Username]

    // 如果设置的用户密码与我们收到的密码相同，那么我们可以继续。
    // 如果不是，则返回“未经授权”状态。
    if !ok || expectedPassword != creds.Password {
        w.WriteHeader(http.StatusUnauthorized)
        return
    }

    // 在这里声明令牌的到期时间，我们将其保留为5分钟
    expirationTime := time.Now().Add(5 * time.Minute)
    // 创建JWT声明，其中包括用户名和有效时间
    claims := &Claims{
        Username: creds.Username,
        StandardClaims: jwt.StandardClaims{
            // In JWT, the expiry time is expressed as unix milliseconds
            ExpiresAt: expirationTime.Unix(),
        },
    }

    // 使用用于签名的算法和令牌
    token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
    // 创建JWT字符串
    tokenString, err := token.SignedString(jwtKey)
    if err != nil {
        // 如果创建JWT时出错，则返回内部服务器错误
        w.WriteHeader(http.StatusInternalServerError)
        return
    }

    // 最后，我们将客户端cookie token设置为刚刚生成的JWT
    // 我们还设置了与令牌本身相同的cookie到期时间
    http.SetCookie(w, &http.Cookie{
        Name:    "token",
        Value:   tokenString,
        Expires: expirationTime,
    })
}
```

如果用户使用正确的凭据登录，则此处理程序将使用 JWT 值在客户端设置 cookie。一旦在客户端上设置了 cookie，此后它将与每个请求一起发送。现在，我们可以编写 Welcome 方法来处理用户特定的信息。

### 处理认证后的路由

现在，所有已登录的客户端都使用 cookie 存储用户信息，我们可以将其用于：

- 验证后续用户请求
- 获取有关发出请求的用户的信息

让我们编写 `Welcome` 处理方法来做到这一点：

```go
func Welcome(w http.ResponseWriter, r *http.Request) {
    // 我们可以从每个请求的Cookie中获取会话令牌
    c, err := r.Cookie("token")
    if err != nil {
        if err == http.ErrNoCookie {
            // 如果未设置cookie，则返回未授权状态
            w.WriteHeader(http.StatusUnauthorized)
            return
        }
        // 对于其他类型的错误，返回错误的请求状态。
        w.WriteHeader(http.StatusBadRequest)
        return
    }

    // 从Cookie获取JWT字符串
    tknStr := c.Value

    // 初始化`Claims`实例
    claims := &Claims{}

    // 解析JWT字符串并将结果存储在`claims`中。
    // 请注意，我们也在此方法中传递了密钥。 
    // 如果令牌无效（如果令牌已根据我们设置的登录到期时间过期）或者签名不匹配,此方法会返回错误.
    tkn, err := jwt.ParseWithClaims(tknStr, claims, func(token *jwt.Token) (interface{}, error) {
        return jwtKey, nil
    })
    if err != nil {
        if err == jwt.ErrSignatureInvalid {
            w.WriteHeader(http.StatusUnauthorized)
            return
        }
        w.WriteHeader(http.StatusBadRequest)
        return
    }
    if !tkn.Valid {
        w.WriteHeader(http.StatusUnauthorized)
        return
    }

    // 最后，将欢迎消息以及令牌中的用户名返回给用户
    w.Write([]byte(fmt.Sprintf("Welcome %s!", claims.Username)))
}
```

### 续签令牌

在此示例中，我们将有效期设置为五分钟。如果令牌过期，我们不希望用户每五分钟登录一次。为了解决这个问题，我们将创建另一个 /refresh 路由，该路由使用先前的令牌仍然有效，并返回更新到期时间的新令牌。

> 为了最大程度地减少对 JWT 的滥用，通常将到期时间保持在几分钟左右。通常，客户端应用程序将在后台刷新令牌。

```go
func Refresh(w http.ResponseWriter, r *http.Request) {
    // (BEGIN) 此处的代码与`Welcome`路由的第一部分相同
    c, err := r.Cookie("token")
    if err != nil {
        if err == http.ErrNoCookie {
            w.WriteHeader(http.StatusUnauthorized)
            return
        }
        w.WriteHeader(http.StatusBadRequest)
        return
    }
    tknStr := c.Value
    claims := &Claims{}
    tkn, err := jwt.ParseWithClaims(tknStr, claims, func(token *jwt.Token) (interface{}, error) {
        return jwtKey, nil
    })
    if err != nil {
        if err == jwt.ErrSignatureInvalid {
            w.WriteHeader(http.StatusUnauthorized)
            return
        }
        w.WriteHeader(http.StatusBadRequest)
        return
    }
    if !tkn.Valid {
        w.WriteHeader(http.StatusUnauthorized)
        return
    }
    // (END)  此处的代码与`Welcome`路由的第一部分相同

    // 我们确保在足够的时间之前不会发行新令牌。
    // 在这种情况下，仅当旧令牌在30秒到期时才发行新令牌。  
    // 否则，返回错误的请求状态。
    if time.Unix(claims.ExpiresAt, 0).Sub(time.Now()) > 30*time.Second {
        w.WriteHeader(http.StatusBadRequest)
        return
    }

    // 现在，为当前用户创建一个新令牌，并延长其到期时间
    expirationTime := time.Now().Add(5 * time.Minute)
    claims.ExpiresAt = expirationTime.Unix()
    token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
    tokenString, err := token.SignedString(jwtKey)
    if err != nil {
        w.WriteHeader(http.StatusInternalServerError)
        return
    }

    // 查看用户新的`token` cookie
    http.SetCookie(w, &http.Cookie{
        Name:    "token",
        Value:   tokenString,
        Expires: expirationTime,
    })
}
```

