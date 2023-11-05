// Creación de una cadena
const myString = "Hola, mundo";

// Obtener la longitud de la cadena
const length = myString.length;
// Resultado: 11

// Acceder a caracteres individuales
const char = myString[0];
// Resultado: "H"

// Búsqueda de subcadenas
const indexOfWorld = myString.indexOf("mundo");
// Resultado: 7

const includesWorld = myString.includes("mundo");
// Resultado: true

// Reemplazar subcadenas
const replaced = myString.replace("mundo", "JavaScript");
// Resultado: "Hola, JavaScript"

// Concatenación de cadenas
const concatenated = myString + "!";
// Resultado: "Hola, mundo!"

// Repetición de cadenas
const repeated = myString.repeat(3);
// Resultado: "Hola, mundoHola, mundoHola, mundo"

// Conversión entre mayúsculas y minúsculas
const uppercase = myString.toUpperCase();
// Resultado: "HOLA, MUNDO"
const lowercase = myString.toLowerCase();
// Resultado: "hola, mundo"

// Eliminación de espacios en blanco al principio y al final
const trimmed = "  Cadena con espacios  ".trim();
// Resultado: "Cadena con espacios"

// División de una cadena en un array de subcadenas
const parts = myString.split(",");
// Resultado: ["Hola", " mundo"]

// Unión de un array de subcadenas en una cadena
const joined = parts.join("-");
// Resultado: "Hola- mundo"

// Extracción de una subcadena (slicing)
const substring = myString.slice(0, 4);
// Resultado: "Hola"

// Verificar si la cadena comienza o termina con una subcadena
const startsWith = myString.startsWith("Hola");
// Resultado: true
const endsWith = myString.endsWith("mundo");
// Resultado: true

// Verificar si la cadena contiene solo caracteres alfabéticos o numéricos
const isAlphaNumeric = myString.match(/^[a-zA-Z0-9]+$/) !== null;
// Resultado: false

// Contar ocurrencias de una subcadena en la cadena
const count = (myString.match(/o/g) || []).length;
// Resultado: 2
