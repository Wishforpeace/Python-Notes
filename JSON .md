JSON: **J**ava**S**cript **O**bject **N**otation(JavaScript 对象表示法)

JSON 是==存储和交换文本信息的语法，类似 XML。==

JSON 比 XML 更小、更快，更易解析。

# JSON 实例

```json
{
    "sites": [
    { "name":"菜鸟教程" , "url":"www.runoob.com" }, 
    { "name":"google" , "url":"www.google.com" }, 
    { "name":"微博" , "url":"www.weibo.com" }
    ]
}
```



这个 sites 对象是包含 3 个站点记录（对象）的数组。

------

## 什么是 JSON ？

- JSON 指的是 JavaScript 对象表示法（**J**ava**S**cript **O**bject **N**otation）
- JSON 是轻量级的文本数据交换格式
- JSON 独立于语言：JSON 使用 Javascript语法来描述数据对象，但是 JSON 仍然独立于语言和平台。JSON 解析器和 JSON 库支持许多不同的编程语言。 目前非常多的动态（PHP，JSP，.NET）编程语言都支持JSON。
- JSON 具有自我描述性，更易理解

------

## JSON - 转换为 JavaScript 对象

JSON 文本格式在语法上与创建 JavaScript 对象的代码相同。

由于这种相似性，无需解析器，JavaScript 程序能够使用内建的 eval() 函数，用 JSON 数据来生成原生的 JavaScript 对象。

# JSON - 简介

## 实例

```json
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
<h2>JavaScript 创建 JSON 对象</h2>
<p>
网站名称: <span id="jname"></span><br /> 
网站地址: <span id="jurl"></span><br /> 
网站 slogan: <span id="jslogan"></span><br /> 
</p>
<script>
var JSONObject= {
    "name":"菜鸟教程",
    "url":"www.runoob.com", 
    "slogan":"学的不仅是技术，更是梦想！"
};
document.getElementById("jname").innerHTML=JSONObject.name 
document.getElementById("jurl").innerHTML=JSONObject.url 
document.getElementById("jslogan").innerHTML=JSONObject.slogan
</script>
 
</body>
</html>

```

## 与 XML 相同之处

- JSON 是纯文本
- JSON 具有"自我描述性"（人类可读）
- JSON 具有层级结构（值中存在值）
- JSON 可通过 JavaScript 进行解析
- JSON 数据可使用 AJAX 进行传输

------

## 与 XML 不同之处

- 没有结束标签
- 更短
- 读写的速度更快
- 能够使用内建的 JavaScript eval() 方法进行解析
- 使用数组
- 不使用保留字

------

## 为什么使用 JSON？

对于 AJAX 应用程序来说，JSON 比 XML 更快更易使用：

#### 使用 XML

- 读取 XML 文档
- 使用 XML DOM 来循环遍历文档
- 读取值并存储在变量中

#### 使用 JSON

- 读取 JSON 字符串
- 用 eval() 处理 JSON 字符串

# JSON语法

## JSON语法规则

JSON 语法是 JavaScript 对象表示语法的子集。

- 数据在名称/值对中
- 数据由逗号分隔
- 大括号 **{}** 保存对象
- 中括号 **[]** 保存数组，数组可以包含多个对象

## JSON 名称/值对

JSON 数据的书写格式是：

```
key : value
```

名称/值对包括字段名称（在双引号中），后面写一个冒号，然后是值：

```
"name" : "菜鸟教程"
```



这很容易理解，等价于这条 JavaScript 语句：

```
name = "菜鸟教程"
```

## JSON 值

JSON 值可以是：

- 数字（整数或浮点数）
- 字符串（在双引号中）
- 逻辑值（true 或 false）
- 数组（在中括号中）
- 对象（在大括号中）
- null

| 类型       | JSON       | Go                        |
| ---------- | ---------- | ------------------------- |
| bool       | true,false | true,false                |
| string     | "a"        | string("a")               |
| 整数       | 1          | int(1),int32(1),int64(1)  |
| 浮点数     | 3.14       | float32(3.14),float(3.14) |
| 数组       | [1,2]      | [2]int{1,2},[]int{1,2}    |
| 对象Object | {"a":"b"}  | Map[string]string,struct  |
| 未知类型   | ···        | interface{}               |



## JSON 数字

JSON 数字可以是整型或者浮点型：

```
{ "age":30 }
```

## JSON 对象

JSON 对象在大括号 **{}** 中书写：

```
{key1 : value1, key2 : value2, ... keyN : valueN }
```

对象可以包含多个名称/值对：

{ "name":"菜鸟教程" , "url":"www.runoob.com" }

这一点也容易理解，与这条 JavaScript 语句等价：

name = "菜鸟教程" url = "www.runoob.com"



------

## JSON 数组

JSON 数组在中括号 **[]** 中书写：

数组可包含多个对象：

```json
[
    { key1 : value1-1 , key2:value1-2 }, 
    { key1 : value2-1 , key2:value2-2 }, 
    { key1 : value3-1 , key2:value3-2 }, 
    ...
    { keyN : valueN-1 , keyN:valueN-2 }, 
]
```

```json
{
    "sites": [
        { "name":"菜鸟教程" , "url":"www.runoob.com" }, 
        { "name":"google" , "url":"www.google.com" }, 
        { "name":"微博" , "url":"www.weibo.com" }
    ]
}
```



在上面的例子中，对象 **sites** 是包含三个对象的数组。每个对象代表一条关于某个网站（name、url）的记录。

------

## JSON 布尔值

JSON 布尔值可以是 true 或者 false：

```json
{ "flag":true }
```



------

## JSON null

JSON 可以设置 null 值：

```json
{ "runoob":null }
```



------

## JSON 使用 JavaScript 语法

因为 JSON 使用 JavaScript 语法，所以无需额外的软件就能处理 JavaScript 中的 JSON。

通过 JavaScript，您可以创建一个对象数组，并像这样进行赋值：

## 实例

```json
var sites = [
    { "name":"runoob" , "url":"www.runoob.com" }, 
    { "name":"google" , "url":"www.google.com" }, 
    { "name":"微博" , "url":"www.weibo.com" }
];
```



可以像这样访问 JavaScript 对象数组中的第一项（索引从 0 开始）：

```json
sites[0].name;
```



返回的内容是：

```json
runoob
```



可以像这样修改数据：

```json
sites[0].name="菜鸟教程";
```

## JSON 文件

- JSON 文件的文件类型是 **.json**
- JSON 文本的 MIME 类型是 **application/json**

# JSON 对象

## 对象语法

```json
{ "name":"runoob", "alexa":10000, "site":null }
```

JSON 对象使用在大括号({})中书写。

对象可以包含多个 **key/value（键/值）**对。

key 必须是字符串，value 可以是合法的 JSON 数据类型（字符串, 数字, 对象, 数组, 布尔值或 null）。

key 和 value 中使用冒号(:)分割。

每个 key/value 对使用逗号(,)分割。

## 访问对象值

你可以使用点号（.）来访问对象的值：

```json
var myObj, x;
myObj = { "name":"runoob", "alexa":10000, "site":null };
x = myObj.name;

```

你也可以使用中括号（[]）来访问对象的值：

```json
var myObj, x;
myObj = { "name":"runoob", "alexa":10000, "site":null };
x = myObj["name"];

```

## 循环对象

你可以使用 for-in 来循环对象的属性：

```json
var myObj = { "name":"runoob", "alexa":10000, "site":null };
for (x in myObj) {
    document.getElementById("demo").innerHTML += x + "<br>";
}
```

在 for-in 循环对象的属性时，使用中括号（[]）来访问属性的值：

```json
var myObj = { "name":"runoob", "alexa":10000, "site":null };
for (x in myObj) {
    document.getElementById("demo").innerHTML += myObj[x] + "<br>";
}
```

## 嵌套 JSON 对象

JSON 对象中可以包含另外一个 JSON 对象：

```json
myObj = {
    "name":"runoob",
    "alexa":10000,
    "sites": {
        "site1":"www.runoob.com",
        "site2":"m.runoob.com",
        "site3":"c.runoob.com"
    }
}
```

你可以使用点号(.)或者中括号([])来访问嵌套的 JSON 对象。

```json
x = myObj.sites.site1;
// 或者
x = myObj.sites["site1"];
```

## 修改值

你可以使用点号(.)来修改 JSON 对象的值：

```json
myObj.sites.site1 = "www.google.com";
```

你可以使用中括号([])来修改 JSON 对象的值：

```json
myObj.sites["site1"]="www.google.com";
```

## 删除对象属性

我们可以使用 **delete** 关键字来删除 JSON 对象的属性：

```json
delete myObj.sites.site1;
```

你可以使用中括号([])来删除 JSON 对象的属性：

```
delete myObj.sites["site1"]
```

