package basic

import (
	"fmt"
	"sync"
	"time"
)

func concurrent() {
	// Creación de una goroutine
	go func() {
		fmt.Println("¡Hola desde una goroutine!")
	}()

	// Uso de canales (channels)
	ch := make(chan int)

	// Enviar datos a un canal
	go func() {
		ch <- 42
		close(ch)
	}()

	// Recibir datos de un canal
	value, ok := <-ch

	// Cerrar un canal
	close(ch)

	// Selección de canales
	select {
	case value := <-ch:
		fmt.Printf("Valor recibido: %d\n", value)
	case ch <- 100:
		fmt.Println("Valor enviado")
	default:
		fmt.Println("Ninguna comunicación en curso")
	}

	// Esperar que las goroutines finalicen con WaitGroup
	var wg sync.WaitGroup
	wg.Add(2)
	go func() {
		defer wg.Done()
		fmt.Println("Goroutine 1")
	}()
	go func() {
		defer wg.Done()
		fmt.Println("Goroutine 2")
	}()
	wg.Wait()

	// Temporización
	timer := time.NewTimer(2 * time.Second)
	<-timer.C
	fmt.Println("Temporización completada")
}
