#[cfg(test)]
mod tests {

    use crate::leetcode::{
        majority_element::{majority_element, majority_element_2, majority_element_3},
        merge_sorted_array::merge_sorted_array,
        remove_duplicate::remove_duplicate,
        remove_duplicateII::remove_duplicateII,
        remove_element::remove_element,
    };

    #[test]
    fn test_merge_sorted() {
        let mut nums1 = vec![1, 2, 3, 0, 0, 0];
        let nums2 = vec![2, 5, 6];
        let m: usize = 3;
        let n: usize = 3;
        merge_sorted_array(&mut nums1, m, &nums2, n);
        let result = vec![1, 2, 2, 3, 5, 6];
        assert_eq!(result, nums1);
    }
    #[test]
    fn test_remove_element() {
        let mut nums = vec![3, 2, 2, 3];
        let val = 3;
        let k = remove_element(&mut nums, val);
        let exptect = 2;
        let expected_nums = vec![2, 2];
        assert_eq!(k, exptect);
        for i in 0..k {
            assert_eq!(nums[i as usize], expected_nums[i as usize])
        }
    }
    #[test]
    fn test_remove_duplicate() {
        let mut nums = vec![1, 1, 2, 2];
        let expect = vec![1, 2];
        let k = remove_duplicate(&mut nums);
        assert_eq!(k, 2 as usize);
        for i in 0..k {
            assert_eq!(nums[i as usize], expect[i as usize])
        }
    }
    #[test]
    fn test_remove_duplicate_ii() {
        let mut nums = vec![1, 1, 1, 2, 2, 3];
        let expect_vec = vec![1, 1, 2, 2, 3];
        let k = remove_duplicateII(&mut nums);
        assert_eq!(k, 5 as usize);
        for i in 0..k {
            assert_eq!(nums[i as usize], expect_vec[i as usize])
        }
    }
    #[test]
    fn test_majority() {
        let nums = vec![3, 3, 4, 4, 3];
        let n = majority_element(&nums);
        let k = majority_element_2(&nums);
        let p = majority_element_3(&nums);
        assert_eq!(p, 3);
        assert_eq!(k, 3);
        assert_eq!(n, 3);
    }
}
