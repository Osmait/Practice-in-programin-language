package main

import "fmt"

func main() {
	x := 5
	y := 10

	fmt.Printf("La suma es: %d\n", sum(x, y))
}

func sum(a, b int) int {
	return a + b
}
