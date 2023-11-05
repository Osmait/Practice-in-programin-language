package leetcode

func RomanToInt(s string) int {
	romanMap := map[byte]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}

	result := 0
	for i := 0; i < len(s); i++ {
		value := romanMap[s[i]]
		if i < len(s)-1 && value < romanMap[s[i+1]] {
			result -= value
		} else {
			result += value
		}
	}
	return result
}
