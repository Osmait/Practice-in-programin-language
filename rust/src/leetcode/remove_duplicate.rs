pub fn remove_duplicate(nums: &mut Vec<i32>) -> usize {
    let mut i: usize = 0;
    while i < nums.len() - 1 {
        if nums[i] == nums[i + 1] {
            nums.remove(i);
        } else {
            i += 1;
        }
    }

    nums.len()
}
