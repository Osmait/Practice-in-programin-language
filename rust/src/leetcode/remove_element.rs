pub fn remove_element(nums: &mut [i32], val: i32) -> usize {
    let mut k = 0;
    for i in 0..nums.len() {
        if nums[i] != val {
            nums[k] = nums[i];
            k += 1;
        }
    }
    k
}
