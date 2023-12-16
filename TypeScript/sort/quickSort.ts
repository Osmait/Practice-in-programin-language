function qs(arr: number[], hi: number, low: number): void {
  if (low >= hi) {
    return;
  }
  const pivot = partition(arr, hi, low);
  qs(arr, pivot - 1, low);
  qs(arr, hi, pivot + 1);
}
function partition(arr: number[], hi: number, low: number): number {
  const pivot = arr[hi];
  let idx = low - 1;
  for (let i = low; i < hi; ++i) {
    if (arr[i] < pivot) {
      idx++;
      const temp = arr[i];
      arr[i] = arr[idx];
      arr[idx] = temp;
    }
  }
  idx++;
  arr[hi] = arr[idx];
  arr[idx] = pivot;
  return idx;
}
function quickSort(arr: number[]): void {
  const hi = arr.length - 1;
  const low = 0;
  qs(arr, hi, low);
}

let arr = [7, 4, 3, 2, 8];
quickSort(arr);
console.log(arr);
