fn binary_search(list: &[i32], item: i32) -> i32 {
    let mut low = 0;
    let mut high = list.len() - 1;
    while low <= high {
        let mid = (low + high) / 2;

        if list[mid] == item {
            return mid as i32;
        }
        if list[mid] > item {
            high = mid - 1
        } else {
            low = mid + 1
        }
    }
    2
}
#[cfg(test)]
mod test {
    use super::*;
    #[test]
    fn search_test() {
        let list = [1, 2, 3, 4, 5, 6, 7, 8];
        let result = binary_search(&list, 5);
        assert_eq!(result, 4)
    }
}
