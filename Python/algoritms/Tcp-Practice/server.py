import socket

# Configuración del servidor
host = '127.0.0.1'  # Dirección IP del servidor
port = 12345       # Puerto en el que escuchará el servidor
filename = 'mensaje.txt'

# Crear un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar el socket al host y puerto
server_socket.bind((host, port))

# Escuchar conexiones entrantes
server_socket.listen(1)
print(f"Esperando conexiones en {host}:{port}...")

while True:
    # Aceptar una conexión entrante
    client_socket, client_address = server_socket.accept()
    print(f"Conexión entrante desde {client_address}")

# Recibir el mensaje del cliente
    data = client_socket.recv(1024).decode()
    print(f"Mensaje recibido: {data}")

    with open(filename, 'a') as file:
        file.write("\n")
        file.write(data)

# Cerrar la conexión
    client_socket.close()
