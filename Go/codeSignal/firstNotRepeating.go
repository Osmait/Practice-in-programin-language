package codesignal

func FirstNotRepeating(s string) string {
	a := map[rune]int{}
	for _, c := range s {
		a[c] += 1
	}

	for _, c := range s {
		i := a[c]
		if i < 2 {
			return string(c)
		}
	}
	return "_"
}
