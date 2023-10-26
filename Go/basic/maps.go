package basic

import "fmt"

func maps() {
	// Creación de un mapa
	myMap := make(map[string]int)

	// Asignar valores a claves
	myMap["uno"] = 1
	myMap["dos"] = 2

	// Acceder a valores por clave
	value := myMap["uno"]

	// Eliminar un par clave-valor
	delete(myMap, "dos")

	// Verificar si una clave existe en el mapa
	_, exists := myMap["uno"]

	// Iterar sobre un mapa
	for key, value := range myMap {
		fmt.Printf("Clave: %s, Valor: %d\n", key, value)
	}
}
