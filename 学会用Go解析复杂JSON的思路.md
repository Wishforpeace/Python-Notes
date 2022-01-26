# 学会用Go解析复杂JSON的思路

2020-04-08阅读 4.8K0

[本文被 1 个清单收录，推荐清单Go语言实战技术分享](https://cloud.tencent.com/developer/inventory/1491)

`Go`语言自带的`encode/json`包提供了对`JSON`数据格式的编码和解码能力。之前的文章《[如何控制Go编码JSON数据格式的行为](https://mp.weixin.qq.com/s?__biz=MzUzNTY5MzU2MA==&mid=2247484156&idx=1&sn=4cd3b66a727fd9b7ab7a6a8423b5ab16&chksm=fa80d36bcdf75a7d621f3f6e722496d573758f6c2ec2ded4abd0c983c84b01edf7079ceb9656&token=1680603331&lang=zh_CN&scene=21#wechat_redirect)》已经介绍了编码`JSON`时常见的几个问题，如何使用`encode/json`来解决。解码`JSON`时`encode/json`包使用`UnMarshall`或者`Decode`方法根据开发者提供的存放解码后数据的变量的类型声明来解析`JSON`并把解码后的数据填充到`Go`变量里。所以解析`JSON`的关键其实是如何声明存放解析后数据的变量的类型。

由于`JSON`格式的自由组合的特点，对新手来说通过观察`JSON`数据的内容，声明解析后数据的类型还是挺困难的。反正我刚用`Go`开始做项目时面对[数据库](https://cloud.tencent.com/solution/database?from=10680)之前的一个复杂的`JSON`研究了一天才解析出来（也有我那会太菜的原因，被逼无奈看了两天语法，就直接开始用Go写项目了）。所以我花时间总结了一下常见的几类`JSON`数据组合模式应该如何声明解析数据的类型，以及`UnMarshal`和`Decode`两个解码函数的用法。

文章主题内容是很早以前发在思否上的一篇文章，后来授权给了Go语言中文网的站长。那会儿我还觉得公众号不适合写技术文章。回看之前那篇文章感觉有的地方文字表达的方式不太好，这跟自己对语言的熟悉程度也有关。

我们先从最简单的`JSON`数据内容开始介绍，一点点增加`JSON`数据内容的复杂度。

### **解析简单JSON**

先观察下这段`JSON`数据的组成，`name`，`created`是字符串。`id`是整型，`fruit`是一个字符串数组

```javascript
{
    "name": "Standard", 
    "fruit": [
        "Apple", 
        "Banana", 
        "Orange"
    ], 
    "id": 999, 
    "created": "2018-04-09T23:00:00Z"
}
```

那么对应的在`Go`里面解析数据的类型应该被声明为：

```javascript
type FruitBasket struct {
    Name    string    `json:"name"`
    Fruit   []string  `json:"fruit"`
    Id      int64     `json:"id"`
    Created time.Time `json:"created"`
}
```

完整的解析`JSON`的代码如下：

```javascript
package main

import (
    "fmt"
    "encoding/json"
    "time"

)

func main() {
    type FruitBasket struct {
        Name    string    `json:"name"`
        Fruit   []string  `json:"fruit"`
        Id      int64     `json:"id"`
        Created time.Time `json:"created"`
    }

    jsonData := []byte(`
    {
        "name": "Standard",
        "fruit": [
             "Apple",
            "Banana",
            "Orange"
        ],
        "id": 999,
        "created": "2018-04-09T23:00:00Z"
    }`)

    var basket FruitBasket
    err := json.Unmarshal(jsonData, &basket)
    if err != nil {
         fmt.Println(err)
    }
    fmt.Println(basket.Name, basket.Fruit, basket.Id)
    fmt.Println(basket.Created)
}
```

说明：由于`json.UnMarshal()`方法接收的是==字节切片==，所以首先需要把JSON字符串转换成字节切片`c := []byte(s)`

### **解析内嵌对象的JSON**

把上面的`fruit`键对应的值如果改成字典 变成`"fruit" : {"name":"Apple", "priceTag":"$1"}`：

```javascript
    jsonData := []byte(`
    {
        "name": "Standard",
        "fruit" : {"name": "Apple", "priceTag": "$1"},
        "def": 999,
        "created": "2018-04-09T23:00:00Z"
    }`)
```

那么`Go`语言里存放解析数据的类型应该这么声明

```javascript
type Fruit struct {
    Name string `json":name"`
    PriceTag string `json:"priceTag"`
}

type FruitBasket struct {
    Name    string    `json:"name"`
    Fruit   Fruit     `json:"fruit"`
    Id      int64     `json:"id"`
    Created time.Time `json:"created"`
}
```

### **解析内嵌对象数组的JSON**

如果上面`JSON`数据里的`Fruit`值现在变成了

```javascript
"fruit" : [
    {
        "name": "Apple",
      "priceTag": "$1"
    },
    {
        "name": "Pear",
        "priceTag": "$1.5"
    }
]
```

这种情况也简单把存放解析后数据的类型其声明做如下更改，把`Fruit`字段类型换为 `[]Fruit`即可

```javascript
type Fruit struct {
    Name string `json:"name"`
    PriceTag string `json:"priceTag"`
}

type FruitBasket struct {
    Name    string    `json:"name"`
    Fruit   []Fruit   `json:"fruit"`
    Id      int64     `json:"id"`
    Created time.Time `json:"created"`
}
```

### **解析具有动态Key的对象**

下面再做一下复杂的变化，如果把上面的对象数组变为以`Fruit`的`Id`作为==属性名的复合对象==（object of object）比如：

```javascript
"Fruit" : {
    "1": {
        "Name": "Apple",
        "PriceTag": "$1"
    },
    "2": {
        "Name": "Pear",
        "PriceTag": "$1.5"
    }
}
```

每个`Key`的名字在声明类型的时候是不知道值的，这样该怎么声明呢，答案是把`Fruit`字段的类型声明为一个`Key`为`string`类型值为`Fruit`类型的`map`

```javascript
type Fruit struct {
    Name string `json:"name"`
    PriceTag string `json:"priceTag"`
}

type FruitBasket struct {
    Name    string             `json:"name"`
    Fruit   map[string]Fruit   `json:"fruit"`
    Id      int64              `json:"id"`
    Created time.Time          `json:"created"`
}
```

可以运行下面完整的代码段试一下。

```javascript
package main

import (
    "fmt"
    "encoding/json"
    "time"

)

func main() {
    type Fruit struct {
        Name string `json:"name"`
        PriceTag string `json:"priceTag"`
    }

    type FruitBasket struct {
        Name    string             `json:"name"`
        Fruit   map[string]Fruit   `json:"fruit"`
        Id      int64              `json:"id"`
        Created time.Time          `json:"created"`
    }  
    jsonData := []byte(`
    {
        "Name": "Standard",
        "Fruit" : {
              "1": {
                    "name": "Apple",
                    "priceTag": "$1"
              },
              "2": {
                    "name": "Pear",
                    "priceTag": "$1.5"
              }
        },
        "id": 999,
        "created": "2018-04-09T23:00:00Z"
    }`)

    var basket FruitBasket
    err := json.Unmarshal(jsonData, &basket)
    if err != nil {
         fmt.Println(err)
    }
    for _, item := range basket.Fruit {
    fmt.Println(item.Name, item.PriceTag)
    }
}
```

### **解析包含任意层级的数组和对象的JSON数据**

针对包含任意层级的`JSON`数据，`encoding/json`包使用：

- `map[string]interface{}` 存储`JSON`对象
- `[]interface` 存储`JSON`数组

`json.Unmarshl` 将会把任何合法的JSON数据存储到一个interface{}类型的值，通过使用空接口类型我们可以存储任意值，但是使用这种类型作为值时需要先做一次类型断言。

```javascript
jsonData := []byte(`{"Name":"Eve","Age":6,"Parents":["Alice","Bob"]}`)

var v interface{}
json.Unmarshal(jsonData, &v)
data := v.(map[string]interface{})

for k, v := range data {
    switch v := v.(type) {
    case string:
        fmt.Println(k, v, "(string)")
    case float64:
        fmt.Println(k, v, "(float64)")
    case []interface{}:
        fmt.Println(k, "(array):")
        for i, u := range v {
            fmt.Println("    ", i, u)
        }
    default:
        fmt.Println(k, v, "(unknown)")
    }
}
```

虽然将`JSON`数据存储到空接口类型的值中可以用来解析任意结构的`JSON`数据，但是在实际应用中发现还是有不可控的地方，比如将数字字符串的值转换成了`float`类型的值，所以经常会在运行时报类型断言的错误，所以在`JSON`结构确定的情况下还是优先使用结构体类型声明，将`JSON`数据到结构体中的方式来解析`JSON`。

### **用 Decoder解析数据流**

上面都是使用的`UnMarshall`解析的`JSON`数据，如果`JSON`数据的载体是打开的文件或者`HTTP`请求体这种数据流（他们都是`io.Reader`的实现），我们不必把`JSON`数据读取出来后再去调用`encode/json`包的`UnMarshall`方法，包提供的`Decode`方法可以完成读取数据流并解析`JSON`数据最后填充变量的操作。

```javascript
// This example uses a Decoder to decode a stream of distinct JSON values.
func ExampleDecoder() {
    const jsonStream = `
    {"Name": "Ed", "Text": "Knock knock."}
    {"Name": "Sam", "Text": "Who's there?"}
    {"Name": "Ed", "Text": "Go fmt."}
    {"Name": "Sam", "Text": "Go fmt who?"}
    {"Name": "Ed", "Text": "Go fmt yourself!"}
`
    type Message struct {
        Name, Text string
    }
    dec := json.NewDecoder(strings.NewReader(jsonStream))
    for {
        var m Message
        if err := dec.Decode(&m); err == io.EOF {
            break
        } else if err != nil {
            log.Fatal(err)
        }
        fmt.Printf("%s: %s\n", m.Name, m.Text)
    }
    // Output:
    // Ed: Knock knock.
    // Sam: Who's there?
    // Ed: Go fmt.
    // Sam: Go fmt who?
    // Ed: Go fmt yourself!
}
```

写这篇文章的主要目的是和之前介绍`Go`语言如何编码`JSON`的文章搭配上，尽量让这个主题在公众号里的文章完整些，这样也更便于刚接触`Go`语言的同学的学习。