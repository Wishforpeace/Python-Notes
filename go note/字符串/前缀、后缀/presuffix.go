package main
import(
	"fmt"
	"strings"
)
func main(){
	var str string = "This my kingdom"
	fmt.Printf("T/F Dose the string \"%s\"have prefix %s?",str,"Th")
	fmt.Printf("%t\n",strings.HasPrefix(str,"Th"))
	fmt.Printf("T/F Dose the string \"%s\"have suffix %s?",str,"dom")
	fmt.Printf("%t\n",strings.HasSuffix(str,"dom"))
}