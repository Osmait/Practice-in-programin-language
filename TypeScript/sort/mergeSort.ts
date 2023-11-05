function mergeSort(array: number[]): number[] {
  if (array.length <= 1) return array.slice();
  const midIndex = Math.floor(array.length / 2);
  const left = array.slice(0, midIndex);
  const right = array.slice(midIndex);

  return merge(mergeSort(left), mergeSort(right));
}
function merge(left: number[], right: number[]): number[] {
  const result: number[] = Array<number>(left.length + right.length);
  let curIndex = 0;
  let leftIndex = 0;
  let rightIndex = 0;

  while (leftIndex < left.length && rightIndex < right.length) {
    if (left[leftIndex] < right[rightIndex]) {
      result[curIndex++] = left[leftIndex++];
    } else {
      result[curIndex++] = right[rightIndex++];
    }
  }

  while (leftIndex < left.length) {
    result[curIndex++] = left[leftIndex++];
  }

  while (rightIndex < right.length) {
    result[curIndex++] = right[rightIndex++];
  }

  return result;
}

console.log(mergeSort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


