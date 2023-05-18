package main

import (
	"fmt"
	"net"
	"os"
)

func main() {
	port := "12312"

	listener, err := net.Listen("tcp", ":"+port)
	if err != nil {
		fmt.Println("Error listening:", err.Error())
		os.Exit(1)
	}
	defer listener.Close()

	fmt.Println("Server listening on port", port)

	for {
		conn, err := listener.Accept()
		if err != nil {
			fmt.Println("Error accepting connection:", err.Error())
			continue
		}

		go handleConnection(conn)
	}
}

func handleConnection(conn net.Conn) {
	defer conn.Close()

	_, err := conn.Write([]byte("holaaaa"))
	if err != nil {
		fmt.Println("Error writing to connection:", err.Error())
		return
	}

	fmt.Println("File sent successfully")
}
