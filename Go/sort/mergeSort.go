package sort

import (
	"sync"
)

func Mergesort(array []int) []int {
	if len(array) <= 1 {
		return array
	}

	mid := len(array) / 2

	leftHalf := array[:mid]
	rightHalf := array[mid:]

	return merge(Mergesort(leftHalf), Mergesort(rightHalf))

}

func merge(i1, i2 []int) []int {
	size := len(i1) + len(i2)
	sortedArray := make([]int, size)

	pointer1 := 0
	pointer2 := 0
	index := 0

	for pointer1 < len(i1) && pointer2 < len(i2) {
		if i1[pointer1] < i2[pointer2] {
			sortedArray[index] = i1[pointer1]
			pointer1++
			index++
		} else {
			sortedArray[index] = i2[pointer2]
			pointer2++
			index++
		}
	}
	for pointer1 < len(i1) {
		sortedArray[index] = i1[pointer1]
		pointer1++
		index++
	}

	for pointer2 < len(i2) {
		sortedArray[index] = i2[pointer2]
		pointer2++
		index++
	}
	return sortedArray
}

func Merge(items []int) []int {

	if len(items) < 2 {
		return items

	}

	var middle = len(items) / 2
	var a = Merge(items[:middle])
	var b = Merge(items[middle:])
	return merge(a, b)

}

// ParallelMerge Perform merge sort on a slice using goroutines
func ParallelMerge(items []int) []int {
	if len(items) < 2 {
		return items
	}

	if len(items) < 2048 {
		return Merge(items)
	}

	var wg sync.WaitGroup
	wg.Add(1)

	var middle = len(items) / 2
	var a []int
	go func() {
		defer wg.Done()
		a = ParallelMerge(items[:middle])
	}()
	var b = ParallelMerge(items[middle:])

	wg.Wait()
	return merge(a, b)
}
