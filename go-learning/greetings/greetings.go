package main

import "fmt"
import "os"

func Hello(name string) string {
	return fmt.Sprintf("Hello, %s!", name)
}

func main() {

	var args []string = os.Args[1:]

	if len(args) > 0 {
		var name string = args[0]
		fmt.Println(Hello(name))
		return
	} else if len(args) == 0 {
		fmt.Println("Hello, World!")
		return
	} else {
		// This case should never happen, but it's here for completeness.
		fmt.Println("Usage: go run greetings.go [name]")
		return
	}
}
