package codewars

import (
	"fmt"
	"math"
)

func GetSum(a int, b int) int {

	return (a+b)*int(math.Abs(float64(b-a))) + 1/2
}

func SimpleMultiplication(n int) int {
	if n%2 == 0 {
		return n * 8

	}
	return n * 9
}

func OddOrEven(array []int) string {
	var sum int
	for _, v := range array {
		sum += v
	}
	if sum%2 == 0 {
		return "even"
	} else {
		return "odd"
	}
}

func rowWeights(array []int) (int, int) {
	var sum1 int
	var sum2 int
	for i, v := range array {
		if i%2 == 0 {
			sum1 += v
		}
		sum2 += v
	}

	return sum1, sum2

}

func PredictAge(ages ...int) int {
	var sum int
	for _, v := range ages {
		sum += v * v
	}
	return int(math.Sqrt(float64(sum))) / 2
}

func GetMiddle(s string) string {
	middle := len(s) / 2
	if len(s)%2 == 0 {
		return s[middle-1 : middle+1]
	}
	return s[middle : middle+1]
}

func CalculateAge(birth int, year int) string {
	age := year - birth

	switch {
	case age == 0:
		return "You were born this very year!"
	case age > 0:
		return fmt.Sprintf("You are %d year%s old.", age, pluralS(age))
	default:
		return fmt.Sprintf("You will be born in %d year%s.", -age, pluralS(-age))
	}
}

func pluralS(n int) string {
	if n == 1 {
		return ""
	}
	return "s"
}

func Evaporator(content float64, evapPerDay int, threshold int) int {
	days := 0
	limit := content * (float64(threshold) / 100)
	for content > limit {
		content -= content * (float64(evapPerDay) / 100)
		days++
	}
	return days
}

func MaxAbsLengthDiff(a1 []string, a2 []string) int {
	if len(a1) == 0 || len(a2) == 0 {
		return -1
	}
	maxDiff := 0

	for _, x := range a1 {
		for _, y := range a2 {
			diff := int(math.Abs(float64(len(x) - len(y))))
			if diff > maxDiff {
				maxDiff = diff
			}
		}
	}
	return maxDiff
}

func CalculateYears(year int) (result [3]int) {
	if year < 1 {
		return
	} else if year == 1 {
		return [3]int{1, 15, 15}

	} else if year == 2 {
		return [3]int{2, 24, 24}
	} else {
		catYears := 24 + 4*(year-2)
		dogYears := 24 + 5*(year-2)
		return [3]int{year, catYears, dogYears}
	}

}

func hero(bullets, dragons int) bool {
	return bullets >= dragons*2
}
