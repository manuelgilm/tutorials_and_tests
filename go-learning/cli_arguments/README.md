# Passing arguments using cli

In this case use os package. For example. 

```go
package main

import "fmt"
import "os"

func main() {
    var args[]string = os.Args[1:]

    for _, arg := range args:
        fmt.Println(arg)
}
```



