use std::collections::HashMap;

pub fn two_sum(nums: Vec<i32>, target: i32) -> Option<Vec<i32>> {
    let mut map: HashMap<i32, usize> = HashMap::new();

    for (i, v) in nums.iter().enumerate() {
        let diff = target - v;

        if map.contains_key(&diff) {
            let k = map.get(&diff).unwrap();
            return Some(vec![*k as i32, i as i32]);
        }
        map.insert(*v, i);
    }
    None
}
