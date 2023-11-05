package codesignal

func RotateMatriz(a [][]int) [][]int {
	reverseRow(a)
	for i := 0; i < len(a); i++ {
		for j := 0; j < i; j++ {
			a[i][j], a[j][i] = a[j][i], a[i][j]
		}
	}
	return a
}

func reverseRow(row [][]int) {
	i, j := 0, len(row)-1
	for i < j {
		row[i], row[j] = row[j], row[i]
		i++
		j--
	}
}
