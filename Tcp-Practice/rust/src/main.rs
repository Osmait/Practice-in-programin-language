use std::fs::OpenOptions;
use std::io::{Read, Write};
use std::net::{TcpListener, TcpStream};

use std::thread;

fn handle_client(mut stream: TcpStream) {
    // Leer datos de la conexión
    let mut buffer = [0; 1024];
    if let Ok(n) = stream.read(&mut buffer) {
        if n == 0 {
            return; // No se recibieron datos, cerrar la conexión.
        }

        // Convertir los datos en una cadena
        let received_message = String::from_utf8_lossy(&buffer[0..n]);

        // Imprimir el mensaje recibido
        println!("Mensaje recibido: {}", received_message);

        // Abrir el archivo en modo de "append"
        let mut file = OpenOptions::new()
            .create(true)
            .append(true)
            .open("mensaje.json")
            .expect("No se pudo abrir el archivo");

        // Escribir el mensaje en el archivo
        if let Err(e) = writeln!(file, "{}", received_message) {
            eprintln!("Error al escribir en el archivo: {}", e);
        }
    }
}

fn main() {
    // Crear un servidor TCP que escucha en localhost:8080
    let listener = TcpListener::bind("127.0.0.1:8080").expect("Error conexion");
    println!("Servidor escuchando en 127.0.0.1:8080...");

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                // Manejar cada conexión entrante en un hilo separado
                thread::spawn(|| {
                    handle_client(stream);
                });
            }
            Err(e) => {
                eprintln!("Error al aceptar la conexión: {}", e);
            }
        }
    }
}
