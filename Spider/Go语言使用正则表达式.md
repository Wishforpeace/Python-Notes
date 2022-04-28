# Go语言使用正则表达式 

1. **解析、编译正则表达式。**使用`regexp.MustCompile()`函数

   `func MustCompile(str string) *Regexp`

   函数的主要作用是将正则表达式中，奇形怪状的符号（如`.`、`*`、`?`、`\`、`[]`、`...`)转换成Go语言能够识别的格式，并将其存成结构体格式，方便编译器编译

   **参数**：正则表达式字串。建议使用反引号。

   **返回值**：编译后的结构体。解析失败时会产生`panic`错误。

2. 根据解析好的规则(结构体形式),从指定字符串中提取需要的信息。使用`FindAllStringSubmatch()`函数

   `func(re *Regexp)FindAllStringSubmatch(s string,n int)[][]string`

   参数**1**：待解析的字符串；

   参数**2**：匹配的次数。通常传-1，表示匹配所有。

   **返回值**：返回成功匹配的`[][]string`。

   说明：

   ```
   [
   	[string1 string2]
   	[string1 string2]
   	[string1 string2]
   ]
   string1:表示，带有匹配参考项的字符串
   string2:表示，不含有匹配参考项的字符串
   ```

   

   ​	**注意：**要使用前面`regexp.MustCompile()`函数调用的返回值，来调 用此函数

   **示例**：

   ```go
   package main
   
   import (
   	"fmt"
   	"regexp"
   )
   
   func main() {
   	str1 := "abc a7c mfc cat 8ca azc cba aMc"
   	//	1.解析编译正则表达式
   	//ret := regexp.MustCompile(`a.c`) // 可以不用检查出错情况
   	//ret := regexp.MustCompile(`a[0-9]c`) 	// 中间是数字
   	//ret := regexp.MustCompile(`a\dc`) // 中间是数字
   	ret1 := regexp.MustCompile(`a[0-9A-Z]c`)
   	//
   	// 2.提取需要信息
   	alls := ret1.FindAllStringSubmatch(str1, -1)
   	fmt.Println("alls: ", alls)
   
   	str2 := "3.14 123.123 .68 hah 1.0 abc 7. ab.3 66.6 123"
   	// 解析、编译正则表达式
   	//ret2 := regexp.MustCompile(`[0-9]+\.[0-9]+`)
   	ret2 := regexp.MustCompile(`\d+\.\d+`)
   	// 提取需要的信息
   	alls2 := ret2.FindAllStringSubmatch(str2, -1)
   	fmt.Println("alls2 : ", alls2)
   }
   ```

   

