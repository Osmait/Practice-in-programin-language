package leetcode

func MaxProfile(prices []int) int {
	res := 0
	lowest := prices[0]
	for price := range prices {
		if price < lowest {
			lowest = price
		}
		res = Max(res, price-lowest)
	}
	return res
}
