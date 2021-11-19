//repeat your words
package main

import (
    "fmt"
    "strings"
)

func main() {
    var origS string = "Hi there! "
    var newS string

    newS = strings.Repeat(origS, 300)
    fmt.Printf("The new repeated string is: %s\n", newS)
}