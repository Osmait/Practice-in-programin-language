package leetcode

func LongestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}
	shortest := strs[0]
	for _, str := range strs {
		if len(str) < len(shortest) {
			shortest = str
		}
	}
	for i := 0; i < len(shortest); i++ {
		c := shortest[i]
		for _, str := range strs {
			if str[i] != c {
				return shortest[:i]
			}
		}
	}
	return shortest
}
