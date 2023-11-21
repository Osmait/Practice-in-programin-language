import ctypes

# Cargar la biblioteca compartida
# Cambia el nombre según tu sistema
mi_programa = ctypes.CDLL("./libmi_programa.so")

# Llamar a la función C
resultado = mi_programa.sumar(3, 4)

# Imprimir el resultado
print("Resultado desde C:", resultado)
