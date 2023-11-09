fn bubble_sort<T: Ord>(list: &mut [T]) {
    if list.is_empty() {
        return;
    }
    let len = list.len();
    for _ in 0..len {
        for j in 0..len - 1 {
            if list[j] > list[j + 1] {
                list.swap(j, j + 1)
            }
        }
    }
}

#[cfg(test)]
mod test {

    use super::*;
    #[test]
    fn bubble_sort_test() {
        let mut list = [1, 3, 2, 5, 4];
        let expected = [1, 2, 3, 4, 5];
        bubble_sort(&mut list);
        assert_eq!(list, expected)
    }
}
