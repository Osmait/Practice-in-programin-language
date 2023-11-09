function bubbleSort(list: number[]): number[] {
  const len = list.length
  for (let i = 0; i < len; i++) {
    for (let j = 0; j < len - 1; j++) {
      if (list[j] > list[j + 1]) {
        const temp = list[j]
        list[j] = list[j + 1]
        list[j + 1] = temp
      }
    }

  }
  return list
}


console.log(bubbleSort([1, 3, 2, 4, 5, 0]))
