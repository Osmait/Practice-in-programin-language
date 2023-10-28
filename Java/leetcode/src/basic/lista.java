import java.util.ArrayList;
import java.util.List;

public class ListExamples {
  public static void main(String[] args) {
    // Creación de una lista
    List<String> myList = new ArrayList<>();

    // Agregar elementos a una lista
    myList.add("Manzana");
    myList.add("Banana");
    myList.add("Cereza");

    // Obtener la longitud de la lista
    int size = myList.size();

    // Acceder a elementos individuales
    String firstElement = myList.get(0);

    // Eliminar elementos de una lista
    myList.remove("Banana");

    // Iterar sobre una lista
    for (String item : myList) {
      System.out.println("Elemento: " + item);
    }
  }
}
