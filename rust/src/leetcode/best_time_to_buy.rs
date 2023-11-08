use std::cmp;

fn max_profile(prices: &[i32]) -> i32 {
    let mut res = 0;
    let mut lowest = prices[0];
    for &price in prices {
        if price < lowest {
            lowest = price;
        }
        res = cmp::max(res, price - lowest)
    }
    res
}

#[cfg(test)]
mod test {
    use super::*;
    #[test]
    fn max_profile_test() {
        let list = vec![7, 1, 5, 3, 6, 4];
        let expected = 5;
        assert_eq!(max_profile(&list), expected)
    }
}
