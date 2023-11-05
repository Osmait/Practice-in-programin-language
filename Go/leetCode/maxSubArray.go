package leetcode

func MaxSubArray(nums []int) int {
	max := nums[0]
	curr := nums[0]

	for i := 1; i < len(nums); i++ {
		curr = Max(nums[i], curr+nums[i])
		max = Max(max, curr)

	}
	return max
}

func Max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
