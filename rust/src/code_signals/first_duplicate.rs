use std::collections::HashSet;

fn first_duplicate(a: &Vec<i32>) -> i32 {
    let mut dup: HashSet<i32> = HashSet::new();
    for i in a {
        if dup.contains(i) {
            return *i;
        }
        dup.insert(*i);
    }

    -1
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_first_duplicate() {
        let num = vec![2, 1, 3, 5, 3, 2];
        let expect = 3;
        let result = first_duplicate(&num);

        assert_eq!(expect, result);
    }
}
