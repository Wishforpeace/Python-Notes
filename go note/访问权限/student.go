package main
package person
import(
	"fmt"
)
func main(){
	s := new(person.Student)
	s.SetName("Shirdon")
	fmt.Println(s.GetName())
}