

function rotateMatriz(a: number[][]): number[][] {
  a.reverse()
  for (let i = 0; i < a.length; i++) {
    for (let j = 0; j < i; j++) {
      [a[i][j], a[j][i]] = [a[j][i], a[i][j]]
    }
  }
  return a
}
const a = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

console.log(rotateMatriz(a))
