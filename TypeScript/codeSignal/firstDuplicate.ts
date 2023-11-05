function firstDuplicate(a: number[]): number {
  const dup = new Set()
  for (const v of a) {
    if (dup.has(v)) {
      return v
    }
    dup.add(v)
  }
  return -1
}



console.log(firstDuplicate([2, 1, 3, 5, 3, 2]))
