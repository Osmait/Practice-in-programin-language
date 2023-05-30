package main

import (
	strategy "github.com/osmait/algoritms/designPatterns/strategy"
)

const (
	API = "https://jsonplaceholder.typicode.com/todos/1"
)

// func main() {

// s := "egg"
// t := "add"

// fmt.Println(leetcode.IsISomorphic(s, t))

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

// }

func main() {
	lfu := &strategy.Lfu{}
	cache := strategy.IniCache(lfu)
	cache.Add("a", "1")
	cache.Add("b", "2")
	cache.Add("c", "3")

	lru := &strategy.Lru{}
	cache.SetEvictionAlgo(lru)

	cache.Add("d", "4")

	fifo := &strategy.Fifo{}
	cache.SetEvictionAlgo(fifo)
	cache.Add("e", "5")

}
