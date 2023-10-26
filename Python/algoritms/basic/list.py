from functools import reduce
# Crear una lista
my_list = [1, 2, 3, 4, 5]

# Añadir elementos a la lista
my_list.append(6)  # Agregar un elemento al final
my_list.insert(0, 0)  # Insertar un elemento en una posición específica

# Extender la lista con otra lista
another_list = [7, 8, 9]
my_list.extend(another_list)  # Agregar elementos de otra lista

# Acceder a elementos de la lista
first_element = my_list[0]  # Acceder al primer elemento
last_element = my_list[-1]  # Acceder al último elemento

# Eliminar elementos de la lista
my_list.remove(3)  # Eliminar un elemento específico
popped_element = my_list.pop()  # Eliminar y devolver el último elemento
del my_list[2]  # Eliminar un elemento por índice

# Encontrar el índice de un elemento
index_of_4 = my_list.index(4)  # Encuentra el índice del valor 4

# Contar elementos
count_5 = my_list.count(5)  # Contar cuántas veces aparece el valor 5

# Ordenar la lista
my_list.sort()  # Ordenar la lista en su lugar
sorted_list = sorted(my_list)  # Crear una nueva lista ordenada

# Invertir la lista
my_list.reverse()  # Invertir la lista en su lugar
reversed_list = list(reversed(my_list))  # Crear una nueva lista invertida

# Copiar la lista
copy_list = my_list.copy()  # Copiar la lista

# Limpiar la lista
my_list.clear()  # Eliminar todos los elementos de la lista

# Slicing (rebanado) de la lista
subset = my_list[1:4]  # Obtener una porción de la lista

# List comprehension (comprensión de lista)
# Crear una nueva lista con valores al cuadrado
squared = [x**2 for x in my_list]

# Filtrar elementos de la lista
filtered_list = [x for x in my_list if x % 2 == 0]  # Filtrar números pares

# Concatenar listas
combined_list = my_list + another_list  # Concatenar dos listas

# Encontrar la longitud de la lista
length = len(my_list)  # Devuelve la cantidad de elementos en la lista

# Ejemplo de lista
numbers = [1, 2, 3, 4, 5]

# Map: Aplicar una función a cada elemento de la lista
squared = list(map(lambda x: x**2, numbers))
# Resultado: [1, 4, 9, 16, 25]

# Filter: Filtrar elementos de la lista
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# Resultado: [2, 4]

# Reduce: Aplicar una función acumulativa a la lista para reducirla a un solo valor
product = reduce(lambda x, y: x * y, numbers)
# Resultado: 120 (1 * 2 * 3 * 4 * 5)

# all: Comprobar si todos los elementos de la lista cumplen una condición
all_even = all(x % 2 == 0 for x in numbers)
# Resultado: False (no todos los números son pares)

# any: Comprobar si al menos un elemento de la lista cumple una condición
any_odd = any(x % 2 != 0 for x in numbers)
# Resultado: True (al menos un número es impar)

# sorted: Ordenar la lista
sorted_numbers = sorted(numbers)
# Resultado: [1, 2, 3, 4, 5]

# max: Encontrar el valor máximo en la lista
maximum = max(numbers)
# Resultado: 5

# min: Encontrar el valor mínimo en la lista
minimum = min(numbers)
# Resultado: 1
