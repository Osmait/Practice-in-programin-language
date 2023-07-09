package leetcode

import "testing"

func TestMergeSorted(t *testing.T) {
	nums1 := []int{1, 2, 3, 0, 0, 0}
	nums2 := []int{2, 5, 6}
	m := 3
	n := 3
	MergeSortArray(nums1, nums2, m, n)
	result := []int{1, 2, 2, 3, 5, 6}

	for i := 0; i < len(nums1); i++ {
		if nums1[i] != result[i] {
			t.Errorf("Expected %v, but got %v", result, nums1)
			break
		}
	}
}
func TestRemoveElement(t *testing.T) {
	nums := []int{3, 2, 2, 3}
	val := 3
	k := RemoveElement(nums, val)
	expecte := 2
	if k != expecte {
		t.Errorf("Expected %v,but got %v", expecte, k)
	}
	for i := 0; i < k; i++ {
		if nums[i] != nums[k] {
			t.Errorf("Expected %v,but got %v", nums[k], nums[i])
		}
	}

}
func TestRemoveDuplicateII(t *testing.T) {
	nums := []int{1, 1, 1, 2, 2, 3}

	k := RemoveDuplicateII(nums)

	expecte := 5
	if k != expecte {
		t.Errorf("Expected %v,but got %v", expecte, k)
	}
	excetedArray := []int{1, 1, 2, 2, 3}
	for i := 0; i < k; i++ {
		if excetedArray[i] != nums[i] {
			t.Errorf("Expected %v,but got %v", excetedArray[i], nums[i])
		}
	}

}
