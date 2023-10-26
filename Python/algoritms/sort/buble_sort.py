

from typing import Any


def bubble_sort(collection: list[Any]) -> list[Any]:
    length = len(collection)
    for i in reversed(range(length)):
        swapped = False
        for j in range(i):
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j +
                                          1] = collection[j + 1], collection[j]
        if not swapped:
            break  # Stop iteration if the collection is sorted.
    return collection


lista = [1, 4, 2, 3, 5]
print(bubble_sort(lista))
