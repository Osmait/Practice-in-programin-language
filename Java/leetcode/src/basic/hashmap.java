import java.util.HashMap;
import java.util.Map;

public class MapExamples {
  public static void main(String[] args) {
    // Creación de un mapa (HashMap)
    Map<String, Integer> myMap = new HashMap<>();

    // Agregar pares clave-valor al mapa
    myMap.put("uno", 1);
    myMap.put("dos", 2);
    myMap.put("tres", 3);

    // Obtener el valor asociado a una clave
    int value = myMap.get("uno");

    // Verificar si una clave existe en el mapa
    boolean exists = myMap.containsKey("dos");

    // Eliminar un par clave-valor del mapa
    myMap.remove("tres");

    // Iterar sobre un mapa
    for (Map.Entry<String, Integer> entry : myMap.entrySet()) {
      System.out.println("Clave: " + entry.getKey() + ", Valor: " + entry.getValue());
    }
  }
}
