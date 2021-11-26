```go
package main
import(
	"bytes"
    "encoding/json"
    "fmt"
    "io/ioutil"
    "net/http"
)
//常量
const METHOD ="POST"
const CONTENT_TYPE = "application/json"
const APP_KEY ="test_report-portal"
func main(){
    //定义相关参数
    url :="http://example.com"
    token :=" "
    //构建请求参数za
    config := map[string]interface{}{}
    config["groupID"]=1020
    config["yearMonth"]="2021-03"
    fmt.Println(config)
    //JSON序列化
    configData,_ :=json.Marshal(config)
    param := bytes.NewBuffer([]byte(configData))
    //构建http请求
    client := &http.Cline{
        
    }
    req,err := http.NewRequest(METHOD,url,param)
    if err != nil{
        fmt.Prinln(err)
        return
    }
    //header
    req.Header.Add("Content-Type",CONTENT_TYPE)
    req.Header.Add("appKey",APP_KEY)
    req.Header.Add("Authorization",token)
    //发送请求
    res,err := client.Do(req)
    if err!=nil{
        fmt.Println(err)
        return
    }
    defer res.Body.Close()
    //返回结果
    body,err := ioutil.ReadAll(res.Body)
    if err!= nil{
        fmt.Println(err)
        return
    }
    fmt.Println(string(body))
}
```

