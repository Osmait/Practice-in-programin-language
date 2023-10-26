package basic

import "strings"

func string() {
	// Creación de una cadena
	myString := "Hola, mundo"

	// Obtener la longitud de una cadena
	length := len(myString)

	// Acceder a caracteres individuales
	char := myString[0]

	// Concatenación de cadenas
	concatenated := myString + "!"

	// Búsqueda de subcadenas
	containsWorld := strings.Contains(myString, "mundo")

	// Reemplazar subcadenas
	replaced := strings.Replace(myString, "mundo", "Go", -1)

	// División de una cadena en un arreglo de subcadenas
	parts := strings.Split(myString, ", ")

	// Unión de un arreglo de subcadenas en una cadena
	joined := strings.Join(parts, "-")

	// Conversión entre mayúsculas y minúsculas
	uppercased := strings.ToUpper(myString)
	lowercased := strings.ToLower(myString)
}
