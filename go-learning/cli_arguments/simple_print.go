package main 

import "fmt"
import "os"

func main() {
	var args []string = os.Args[1:]

	for _, arg := range args {
		fmt.Println(arg)
	}
}
