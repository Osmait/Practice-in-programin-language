function firstNotRepeating(s: string): string {
  const arr = s.split("");
  for (let i = 0; i < arr.length; i++) {
    if (arr.indexOf(arr[i]) == arr.lastIndexOf(arr[i])) {
      return arr[i]
    }
  }
  return "_"
}


console.log(firstNotRepeating("abacabad"))
