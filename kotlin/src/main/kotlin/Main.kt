
import kotlinx.serialization.json.Json
import sort.mergeSort

import java.io.BufferedReader
import java.io.InputStreamReader
import java.net.HttpURLConnection
import java.net.URL





fun main(args: Array<String>) {

    val listUnOrd = arrayOf(10,5,4,6,2)
    mergeSort(listUnOrd,0,listUnOrd.size -1)
    println(listUnOrd.joinToString())
    val apiUrl = "https://dummyjson.com/products/1"

    // Hacer la petición GET
    val response = getRequest(apiUrl)
//    println(response)
    val result = Json.decodeFromString<Product>(response)


    // Imprimir la respuesta
    println(result.description)
}


fun getRequest(url: String): String {
    val apiUrl = URL(url)
    val connection = apiUrl.openConnection() as HttpURLConnection
    connection.requestMethod = "GET"

    val responseCode = connection.responseCode
    val responseBody = StringBuilder()

    if (responseCode == HttpURLConnection.HTTP_OK) {
        val reader = BufferedReader(InputStreamReader(connection.inputStream))
        var line: String? = reader.readLine()
        while (line != null) {
            responseBody.append(line)
            line = reader.readLine()
        }
        reader.close()
    } else {
        responseBody.append("Error en la petición. Código de respuesta: $responseCode")
    }

    connection.disconnect()

    return responseBody.toString()
}