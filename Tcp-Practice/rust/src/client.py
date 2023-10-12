import json
import pickle
import socket

# Configuración del cliente
host = '127.0.0.1'  # Dirección IP del servidor
port = 8080      # Puerto en el que escucha el servidor

# Crear un socket TCP


class User:

    def __init__(self, nombre, edad, city):
        self.nombre = nombre
        self.edad = edad
        self.city = city


data = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Ejemploville"
}

user = User(nombre="saul", edad=13, city="santiago")

json_data = json.dumps(user.__dict__)
# Conectar al servidor
try:

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    # mensaje = input("Ingrese un mensaje (o escriba 'salir' para finalizar): ")

    # Verificar si el usuario quiere salir
    # if mensaje.lower() == 'salir':

    # Enviar el mensaje al servidor
    client_socket.send(json_data.encode())

except Exception as e:
    print(f"Error: {e}")

finally:
    client_socket.close()
