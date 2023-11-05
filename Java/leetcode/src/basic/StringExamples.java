package basic;

public class StringExamples {
  public static void main(String[] args) {
    // Creación de una cadena
    String myString = "Hola, mundo";

    // Obtener la longitud de una cadena
    int length = myString.length();

    // Acceder a caracteres individuales
    char firstChar = myString.charAt(0);

    // Búsqueda de subcadenas
    boolean containsWorld = myString.contains("mundo");

    // Reemplazar subcadenas
    String replaced = myString.replace("mundo", "Java");

    // Concatenación de cadenas
    String concatenated = myString + "!";

    // División de una cadena en un arreglo de subcadenas
    String[] parts = myString.split(", ");

    // Unión de un arreglo de subcadenas en una cadena
    String joined = String.join("-", parts);

    // Conversión entre mayúsculas y minúsculas
    String uppercased = myString.toUpperCase();
    String lowercased = myString.toLowerCase();
  }
}
