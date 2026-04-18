package main

import "fmt"
import "net/http"
import "os"
import "sync"
import "time"

func fetchStatus(url string) {

	resp, err := http.Get(url)
	fmt.Printf("Making request to %s\n", url)
	if err != nil {
		fmt.Printf("Error fetching %s: %v\n", url, err)
		return
	}
	defer resp.Body.Close()
	fmt.Printf("Response status for %s: %s\n", url, resp.Status)
}

var args []string = os.Args[1:]

func main1() {
	var wg sync.WaitGroup

	for _, arg := range args {
		wg.Add(1)
		go func(url string) {
			defer wg.Done()
			fetchStatus(url)
		}(arg)
	}
	wg.Wait()
}

func main2() {
	for _, arg := range args {
		fetchStatus(arg)
	}
	return
}

func main() {
	if len(args) == 0 {
		fmt.Println("Usage: go run main.go [url1] [url2] ...")
		return
	}

	start := time.Now()
	main1()
	duration1 := time.Since(start)
	fmt.Printf("main1 (concurrent) execution time: %v\n", duration1)

	start = time.Now()
	main2()
	duration2 := time.Since(start)
	fmt.Printf("main2 (sequential) execution time: %v\n", duration2)
}
