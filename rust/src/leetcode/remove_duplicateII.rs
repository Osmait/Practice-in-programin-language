pub fn remove_duplicateII(nums: &mut Vec<i32>) -> usize {
    if nums.len() <= 2 {
        return nums.len();
    }

    let mut k: usize = 2;

    for i in 2..nums.len() {
        if nums[i] != nums[k - 2] {
            nums[k] = nums[i];
            k += 1;
        }
    }
    k
}
