package main

import (
	"fmt"
	"os"
	"strconv"
	"time"

	"github.com/osmait/algoritms/concurrent"
	"github.com/osmait/algoritms/designPatterns/repository"
	leetcode "github.com/osmait/algoritms/leetCode"
	readyaml "github.com/osmait/algoritms/readYaml"
	"github.com/osmait/algoritms/sort"
)

const (
	API = "https://jsonplaceholder.typicode.com/todos/1"
)

func main() {
	fmt.Println("hello")

	args := os.Args

	fmt.Println(0)

	num, err := strconv.Atoi(args[2])
	if err != nil {
		fmt.Println(err.Error())
	}

	readyaml.ReadYAml(num)

	array := []int{10, 3, 4, 1, 5}
	result := sort.ParallelMerge(array)
	fmt.Println(result)
	repo := repository.New()
	repo.Save("saul")
	repo.Save("burgos")
	list := repo.Find()
	fmt.Println(list)
	s := "egg"
	t := "add"

	fmt.Println(leetcode.IsISomorphic(s, t))

	inicio2 := time.Now()
	concurrent.Check2("https://www.google.com", "https://jsonplaceholder.typicode.com/todos/1", "https://jsonplaceholder.typicode.com/todos/2")
	final2 := time.Since(inicio2)
	fmt.Printf("Tiempo normal %v\n", final2)
	endpoint := []string{"//www.google.com", "https://jsonplaceholder.typicode.com/todos/1", "https://jsonplaceholder.typicode.com/todos/2"}
	c := make(chan string, len(endpoint))
	inicio := time.Now()
	concurrent.Check(c, endpoint...)
	final := time.Since(inicio)

	for i := 0; i < len(endpoint); i++ {
		t := <-c
		if t == "err" {
			fmt.Println("Error")
		} else {
			fmt.Println(t)
		}
	}
	defer close(c)
	fmt.Printf("Tiempo Concurrente %v\n", final)
}
