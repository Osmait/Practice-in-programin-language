package leetCode;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class Fetch {

  public String get() {
    try {
      // URL de la API que deseas consultar
      URL url = new URL("https://dummyjson.com/products");

      // Abrir conexión
      HttpURLConnection connection = (HttpURLConnection) url.openConnection();
      connection.setRequestMethod("GET");

      // Leer la respuesta de la API
      BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
      String line;
      StringBuilder response = new StringBuilder();
      while ((line = reader.readLine()) != null) {
        response.append(line);
      }
      reader.close();

      // Cerrar la conexión
      connection.disconnect();
      return response.toString();

    } catch (Exception e) {

      throw new RuntimeException(e);
    }

  }

}
