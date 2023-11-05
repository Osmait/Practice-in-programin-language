package leetcode

func MergeSortArray(num1, num2 []int, m, n int) {
	p1 := m - 1
	p2 := n - 1
	p := m + n - 1

	for p1 >= 0 && p2 >= 0 {
		if num1[p1] > num2[p2] {
			num1[p] = num1[p1]
			p1--
		} else {
			num1[p] = num2[p2]
			p2--
		}
		p--

	}
	copy(num1[:p2+1], num2[:p2+1])
}
