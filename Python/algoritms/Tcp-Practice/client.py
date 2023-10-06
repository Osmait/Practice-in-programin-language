import socket

# Configuración del cliente
host = '127.0.0.1'  # Dirección IP del servidor
port = 12345       # Puerto en el que escucha el servidor

# Crear un socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor
client_socket.connect((host, port))

# Enviar un mensaje al servidor
mensaje = "Hola, servidor"
client_socket.send(mensaje.encode())

# Cerrar la conexión
client_socket.close()
