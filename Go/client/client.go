package main

import (
	"fmt"
	"net"
	"os"
)

func main() {
	serverAddr := "localhost:12312"

	conn, err := net.Dial("tcp", serverAddr)
	if err != nil {
		fmt.Println("Error connecting to server:", err.Error())
		os.Exit(1)

	}
	defer conn.Close()

	message := []byte("Hello server!")
	_, err = conn.Write(message)
	if err != nil {
		fmt.Println("Error sending data:", err.Error())
		os.Exit(1)
	}

	buffer := make([]byte, 1024)
	n, err := conn.Read(buffer)
	if err != nil {
		fmt.Println("Error receiving data:", err.Error())
		os.Exit(1)
	}

	fmt.Println("Server response:", string(buffer[:n]))
}
