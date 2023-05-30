use std::collections::HashSet;

pub fn contain_duplicate(nums: Vec<i32>) -> bool {
    let mut hash_set = HashSet::new();

    for &n in nums.iter() {
        if hash_set.contains(&n) {
            return true;
        }
        hash_set.insert(n);
    }
    false
}
