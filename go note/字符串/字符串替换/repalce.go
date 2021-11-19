package main
import (
    "fmt"
    "strings"
)
func main()  {
	var str string = "hello,mother fucker"
	fmt.Printf("%s",strings.Replace(str,"mother fucker","sweet honey",-1))
}