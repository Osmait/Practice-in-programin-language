package codesignal

func FirstDuplicate(a []int) int {
	dup := make(map[int]int)

	for i, v := range a {
		if _, ok := dup[v]; ok {
			return v
		}
		dup[v] = i
	}
	return -1
}
