# Creación de un diccionario
from collections import OrderedDict
from collections import defaultdict
my_dict = {"nombre": "Juan", "edad": 30, "ciudad": "Ejemplo"}

# Acceder a un valor por clave
name = my_dict["nombre"]
# Resultado: "Juan"

# Añadir un nuevo par clave-valor
my_dict["ocupacion"] = "Programador"

# Actualizar el valor de una clave
my_dict["edad"] = 31

# Eliminar un par clave-valor
del my_dict["ciudad"]

# Verificar si una clave existe en el diccionario
if "nombre" in my_dict:
    pass
    # Hacer algo

    # Obtener todas las claves
keys = my_dict.keys()
# Resultado: ["nombre", "edad", "ocupacion"]

# Obtener todos los valores
values = my_dict.values()
# Resultado: ["Juan", 31, "Programador"]

# Obtener pares clave-valor como tuplas
items = my_dict.items()
# Resultado: [("nombre", "Juan"), ("edad", 31), ("ocupacion", "Programador")]

# Copiar un diccionario
new_dict = my_dict.copy()

# Limpiar un diccionario
my_dict.clear()

# Recorrido de un diccionario
for key, value in my_dict.items():
    pass
    # Hacer algo con la clave y el valor

    # Usar dict comprehension para crear un nuevo diccionario
squared_dict = {x: x**2 for x in range(5)}
# Resultado: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Usar get para acceder a un valor por clave de forma segura
value = my_dict.get("nombre", "No encontrado")
# Resultado: "Juan"

# Usar setdefault para asignar un valor a una clave si no existe
my_dict.setdefault("direccion", "Desconocida")

# Eliminar y obtener un elemento por clave
value = my_dict.pop("nombre")
# Resultado: "Juan"

# Eliminar el último elemento agregado al diccionario
last_item = my_dict.popitem()
# Resultado: un par clave-valor (último par añadido)

# Usar defaultdict para definir un valor predeterminado para claves que no existen
my_default_dict = defaultdict(int)  # Valor predeterminado para enteros

# Usar OrderedDict para mantener el orden de las claves
ordered_dict = OrderedDict()
my_dict = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Ejemplo'}
# my_function(**my_dict)
my_list = [1, 2, 3, 4, 5]
a, b, *rest = my_list
