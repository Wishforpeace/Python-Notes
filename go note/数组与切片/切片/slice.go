// package main
// import "fmt"
// func sum(a[] int)(s int){
// 	s = 0
// 	for i:=0;i<len(a);i++{
// 		s += a[i]
// 	}
// 	return s

// }
// func main()  {
// 	var arr = [5]int{0,1,2,34}
// 	fmt.Println(sum(arr[:]))	
	
// }
   
//make()
package main
import "fmt"

func main() {
    var slice1 []int = make([]int, 10)
    // load the array/slice:
    for i := 0; i < len(slice1); i++ {
        slice1[i] = 5 * i
    }

    // print the slice:
    for i := 0; i < len(slice1); i++ {
        fmt.Printf("Slice at %d is %d\n", i, slice1[i])
    }
    fmt.Printf("\nThe length of slice1 is %d\n", len(slice1))
    fmt.Printf("The capacity of slice1 is %d\n", cap(slice1))
}