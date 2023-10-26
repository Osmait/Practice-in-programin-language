class MiClase:
    class_variable = 0  # Variable de clase

    def __init__(self, value):
        self.instance_variable = value  # Variable de instancia

    @classmethod
    def class_method(cls, x, y):
        """Un método de clase."""
        print(f"Método de clase llamado con {x} y {y}")
        cls.class_variable += 1  # Acceder a la variable de clase

    @classmethod
    def create_instance(cls, value):
        """Crear una instancia de la clase usando un método de clase."""
        instance = cls(value)  # Crear una instancia de la clase
        return instance

    @staticmethod
    def static_method(a, b):
        """Un método estático."""
        print(f"Método estático llamado con {a} y {b}")


# Uso de los métodos de clase
MiClase.class_method(1, 2)  # Llamada al método de clase
# Crear una instancia usando un método de clase
obj = MiClase.create_instance(10)


MiClase.static_method(5, 6)  # Llamada al método estático


class MiNuevaClase:
    def __init__(self, valor):
        self.valor = valor

    # Métodos para representación
    def __str__(self):
        return f"MiNuevaClase con valor {self.valor}"

    def __repr__(self):
        return f"MiNuevaClase({self.valor})"

    # Métodos para operadores aritméticos
    def __add__(self, other):
        return MiNuevaClase(self.valor + other.valor)

    def __sub__(self, other):
        return MiNuevaClase(self.valor - other.valor)

    # Métodos para operadores de comparación
    def __eq__(self, other):
        return self.valor == other.valor

    def __lt__(self, other):
        return self.valor < other.valor

    # Otros métodos especiales
    def __len__(self):
        return len(self.valor)

    def __getitem__(self, index):
        return self.valor[index]

    def __setitem__(self, index, valor):
        self.valor[index] = valor

    def __delitem__(self, index):
        del self.valor[index]

    def __call__(self):
        return "Llamado como función"


# Crear instancias
obj1 = MiNuevaClase(42)
obj2 = MiNuevaClase(10)

# Métodos de representación
print(str(obj1))  # Llama a __str__
print(repr(obj1))  # Llama a __repr__

# Métodos para operadores aritméticos
result = obj1 + obj2  # Llama a __add__
result = obj1 - obj2  # Llama a __sub__

# Métodos para operadores de comparación
print(obj1 == obj2)  # Llama a __eq__
print(obj1 < obj2)  # Llama a __lt__

# Otros métodos especiales
print(len(obj1))  # Llama a __len__
print(obj1[1])  # Llama a __getitem__
obj1[1] = 20  # Llama a __setitem__
del obj1[1]  # Llama a __delitem__

# Llamar a una instancia como función
print(obj1())  # Llama a __call__
