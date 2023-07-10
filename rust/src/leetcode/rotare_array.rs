pub fn rotare_array(nums: &mut [i32], k: i32) {
    let len = nums.len() as i32;
    let k = k % len;
    reverse(nums, 0, len - 1);
    reverse(nums, 0, k - 1);
    reverse(nums, k, len - 1);
}

fn reverse(nums: &mut [i32], mut start: i32, mut end: i32) {
    while start < end {
        nums.swap(start as usize, end as usize);
        start += 1;
        end -= 1;
    }
}
