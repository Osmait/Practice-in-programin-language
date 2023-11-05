fn rotate_matrix(mut a: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
    a.reverse();
    for i in 0..a.len() {
        for j in 0..i {
            (a[i][j], a[j][i]) = (a[j][i], a[i][j]);
        }
    }
    a
}
#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_matri() {
        let a: Vec<Vec<i32>> = vec![vec![1, 2, 3], vec![4, 5, 6], vec![7, 8, 9]];

        let expected: Vec<Vec<i32>> = vec![vec![7, 4, 1], vec![8, 5, 2], vec![9, 6, 3]];
        assert_eq!(expected, rotate_matrix(a))
    }
}
