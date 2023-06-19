package sort

fun <T : Comparable<T>> mergeSort(array: Array<T>, start: Int, end: Int) {

    val temp = arrayOfNulls<Comparable<*>>(array.size) as Array<T>

    if (start < end) {
        val mid = start + (end - start) / 2
        mergeSort(array, start, mid)
        mergeSort(array, mid + 1, end)
        merge(array, temp, start, mid, end)
    }
}

fun <T : Comparable<T>> merge(array: Array<T>, temp: Array<T>, start: Int, mid: Int, end: Int) {

    System.arraycopy(array, start, temp, start, end - start + 1)

    var i = start
    var j = mid + 1
    var k = start

    while (i <= mid && j <= end) {
        if (temp[i] < temp[j]) {
            array[k++] = temp[i++]
        } else {
            array[k++] = temp[j++]
        }
    }

    while (i <= mid) {
        array[k++] = temp[i++]
    }

    while (j <= end) {
        array[k++] = temp[j++]
    }
}
