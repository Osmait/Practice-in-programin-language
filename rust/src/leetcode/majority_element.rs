use std::{collections::HashMap, iter::Map};

pub fn majority_element(nums: &[i32]) -> i32 {
    let mut nums_map: HashMap<i32, i32> = HashMap::new();
    let mut nums_max = HashMap::new();
    nums_max.insert("max", 0);
    nums_max.insert("key", 0);

    for &n in nums {
        let count = nums_map.entry(n).or_insert(0);
        *count += 1;
    }
    for (k, v) in &nums_map {
        if v > nums_max.get("max").unwrap() {
            nums_max.insert("max", *v);
            nums_max.insert("key", *k);
        }
    }

    *nums_max.get("key").unwrap()
}

pub fn majority_element_2(nums: &[i32]) -> i32 {
    let mut res = 0;
    let mut count = 0;

    for &n in nums {
        if count == 0 {
            res = n;
        }
        count += if n == res { 1 } else { -1 };
    }
    res
}

pub fn majority_element_3(nums: &[i32]) -> i32 {
    let mut count: HashMap<i32, i32> = HashMap::new();
    let mut res = 0;
    let mut max_count = 0;

    for &n in nums {
        let entry = count.entry(n).or_insert(0);
        *entry += 1;
        if *entry > max_count {
            res = n;
            max_count = *entry;
        }
    }
    res
}
