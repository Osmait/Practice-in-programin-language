# Creación de una cadena
string = "Hola, mundo"

# Obtener la longitud de la cadena
length = len(string)
# Resultado: 11

# Acceder a caracteres individuales
char = string[0]
# Resultado: "H"

# Rebanado (slicing) de cadenas
substring = string[0:4]
# Resultado: "Hola"

# Concatenación de cadenas
concatenated = string + "!"
# Resultado: "Hola, mundo!"

# Repetición de cadenas
repeated = string * 3
# Resultado: "Hola, mundoHola, mundoHola, mundo"

# Buscar y reemplazar
replaced = string.replace("mundo", "Python")
# Resultado: "Hola, Python"

# Convertir a mayúsculas y minúsculas
uppercase = string.upper()
# Resultado: "HOLA, MUNDO"
lowercase = string.lower()
# Resultado: "hola, mundo"

# Eliminar espacios en blanco al principio y al final
stripped = "  Cadena con espacios  ".strip()
# Resultado: "Cadena con espacios"

# Dividir una cadena en una lista de subcadenas
parts = string.split(",")
# Resultado: ["Hola", " mundo"]

# Unir una lista de subcadenas en una cadena
joined = "-".join(parts)
# Resultado: "Hola- mundo"

# Buscar la posición de una subcadena
index = string.index("mundo")
# Resultado: 6

# Comprobar si una cadena comienza o termina con una subcadena
startsWith = string.startswith("Hola")
# Resultado: True
endsWith = string.endswith("mundo")
# Resultado: True

# Comprobar si la cadena contiene solo caracteres alfabéticos o numéricos
isAlphaNumeric = string.isalnum()
# Resultado: False

# Comprobar si la cadena contiene solo caracteres alfabéticos
isAlpha = string.isalpha()
# Resultado: False

# Contar ocurrencias de una subcadena en la cadena
count = string.count("o")
# Resultado: 2

# Formateo de cadenas
formatted = "Hola, {}!".format("Python")
# Resultado: "Hola, Python!"

# F-strings (cadenas formateadas)
name = "Python"
formatted = f"Hola, {name}!"
# Resultado: "Hola, Python!"

# Remover y reemplazar espacios en blanco
stripped = "  Cadena con espacios  ".strip()
replaced = "Texto con espacios".replace(" ", "-")

# Partir en líneas
lines = "Línea 1\nLínea 2".split("\n")

# Verificar si la cadena contiene una subcadena
contains = "Python" in string
# Resultado: False

# Obtener el código Unicode de un carácter
unicode = ord("A")
# Resultado: 65

# Convertir código Unicode a carácter
char = chr(65)
# Resultado: "A"
