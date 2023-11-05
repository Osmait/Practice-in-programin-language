package main

import (
	"bufio"
	"fmt"
	"log"
	"net"
)

// Estructura para almacenar la información del cliente
type Client struct {
	conn     net.Conn
	nickname string
}

// Función para manejar las conexiones de los clientes
func handleConnection(conn net.Conn, clients map[string]Client) {
	// Cerrar la conexión al finalizar la función
	defer conn.Close()

	// Obtener la dirección IP y el puerto del cliente
	clientAddr := conn.RemoteAddr().String()
	log.Println("Cliente conectado:", clientAddr)

	// Crear un nuevo cliente y agregarlo al mapa de clientes
	client := Client{conn: conn}
	clients[clientAddr] = client

	// Enviar mensaje de bienvenida al cliente
	conn.Write([]byte("¡Bienvenido al chat!\n"))

	// Leer mensajes del cliente de manera continua
	scanner := bufio.NewScanner(conn)
	for scanner.Scan() {
		message := scanner.Text()

		// Si el cliente envía "/quit", cerrar la conexión y eliminarlo del mapa de clientes
		if message == "/quit" {
			log.Println("Cliente desconectado:", clientAddr)
			delete(clients, clientAddr)
			break
		}

		// Enviar el mensaje a todos los demás clientes
		for addr, otherClient := range clients {
			if addr != clientAddr {
				otherClient.conn.Write([]byte(fmt.Sprintf("[%s]: %s\n", clientAddr, message)))
			}
		}
	}

	// Manejar cualquier error de escaneo
	if err := scanner.Err(); err != nil {
		log.Println("Error al leer los datos del cliente:", err)
	}
}

func main() {
	// Mapa para almacenar los clientes conectados
	clients := map[string]Client{}

	// Establecer el puerto en el que el servidor escuchará las conexiones
	port := "8080"

	// Crear un servidor TCP en el puerto especificado
	listener, err := net.Listen("tcp", ":"+port)
	if err != nil {
		log.Fatal("Error al iniciar el servidor:", err)
	}

	log.Println("Servidor de chat iniciado en el puerto", port)

	// Cerrar el servidor al finalizar la función
	defer listener.Close()

	for {
		// Esperar y aceptar conexiones de clientes
		conn, err := listener.Accept()
		if err != nil {
			log.Println("Error al aceptar la conexión del cliente:", err)
			continue
		}

		// Manejar la conexión del cliente en una goroutine separada
		go handleConnection(conn, clients)
	}
}
