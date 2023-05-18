package main

import (
	"fmt"

	leetcode "github.com/osmait/algoritms/leetCode"
)

const (
	API = "https://jsonplaceholder.typicode.com/todos/1"
)

func main() {
	s := "egg"
	t := "add"

	fmt.Println(leetcode.IsISomorphic(s, t))

	// inicio2 := time.Now()
	// concurrent.Check2("https://www.google.com", "https://jsonplaceholder.typicode.com/todos/1", "https://jsonplaceholder.typicode.com/todos/2")
	// final2 := time.Since(inicio2)
	// fmt.Printf("Tiempo normal %v\n", final2)
	// endpoint := []string{"//www.google.com", "https://jsonplaceholder.typicode.com/todos/1", "https://jsonplaceholder.typicode.com/todos/2"}
	// c := make(chan string, len(endpoint))
	// inicio := time.Now()
	// concurrent.Check(c, endpoint...)
	// final := time.Since(inicio)

	// for i := 0; i < len(endpoint); i++ {
	// 	t := <-c
	// 	if t == "err" {
	// 		fmt.Println("Error")

	// 	} else {

	// 		fmt.Println(t)
	// 	}
	// }
	// defer close(c)
	// fmt.Printf("Tiempo Concurrente %v\n", final)

}
