package main

import (
	"bufio"
	"fmt"
	"io"
	"net/http"
	"os"
	"strings"
)

func main() {
	x := 0
	y := 10

	fmt.Printf("La suma es: %d\n", sum(x, y))
	fetch("https://dummyjson.com/products/1")
}

func sum(a, b int) int {
	return a + b
}

func fetch(url string) {
	response, err := http.Get(url)
	if err != nil {
		return
	}

	defer response.Body.Close()
	body, err := io.ReadAll(response.Body)
	if err != nil {
		return
	}
	fmt.Println(string(body))
}

func input() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Por favor ingresa una línea de texto: ")
	inp, err := reader.ReadString('\n')
	if err != nil {
		return
	}
	strings.TrimSpace(inp)
	fmt.Print(inp)
}
