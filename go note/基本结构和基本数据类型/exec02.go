package main
import (
	"fmt"
	"unicode"
)
func main()  {
	var ch string 
	ch = "1000"
	fmt.Printf("%t",unicode.IsLetter(ch))
}
