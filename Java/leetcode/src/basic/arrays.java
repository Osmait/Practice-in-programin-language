import java.util.Arrays;

public class ArrayExamples {
  public static void main(String[] args) {
    // Creación de un arreglo
    int[] myArray = { 1, 2, 3, 4, 5 };

    // Obtener la longitud de un arreglo
    int length = myArray.length;

    // Acceder a elementos individuales
    int firstElement = myArray[0];

    // Copiar un arreglo
    int[] copyOfArray = Arrays.copyOf(myArray, myArray.length);

    // Ordenar un arreglo
    Arrays.sort(myArray);

    // Búsqueda en un arreglo ordenado
    int index = Arrays.binarySearch(myArray, 3);

    // Iterar sobre un arreglo
    for (int value : myArray) {
      System.out.println("Valor: " + value);
    }
  }
}
