pub fn name_shuffler(s: &str) -> String {
    let spl: Vec<&str> = s.split(" ").collect();

    format!("{} {}", spl[1], spl[0])
}

fn first_non_consecutive(arr: &Vec<i32>) -> Option<i32> {
    for (i, v) in arr.iter().enumerate() {
        let current = v + 1;
        if i < arr.len() - 1 {
            let next = arr[i + 1 as usize];
            if current != next {
                return Some(next);
            }
        }
    }
    None
}
#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_first_non_consecutive() {
        let expect = 6;
        let arr = vec![1, 2, 3, 4, 5, 6, 7, 8];
        let result = first_non_consecutive(&arr);
        assert_eq!(None, result)
    }

    #[test]
    fn test_name_shuffler() {
        let expectec = "burgos saul";
        let result = name_shuffler("saul burgos");
        assert_eq!(expectec, result)
    }
}
