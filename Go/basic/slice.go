package basic

import "fmt"

func slice() {
	// Creación de una rebanada
	mySlice := []int{1, 2, 3, 4, 5}

	// Obtener la longitud de la rebanada
	length := len(mySlice)

	// Acceder a elementos individuales
	element := mySlice[0]

	// Rebanado (slicing) de rebanadas
	subset := mySlice[1:4]

	// Agregar elementos a una rebanada
	mySlice = append(mySlice, 6, 7, 8)

	// Copiar una rebanada
	copyOfSlice := make([]int, len(mySlice))
	copy(copyOfSlice, mySlice)

	// Eliminar elementos de una rebanada
	mySlice = append(mySlice[:2], mySlice[3:]...)

	// Iterar sobre una rebanada
	for index, value := range mySlice {
		fmt.Printf("Índice: %d, Valor: %d\n", index, value)
	}
}
