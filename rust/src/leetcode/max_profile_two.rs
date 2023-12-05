fn max_profit(prices: Vec<i32>) -> i32 {
    let mut max_profit = 0;
    for i in 1..prices.len() {
        if prices[i] > prices[i - 1] {
            max_profit += prices[i] - prices[i - 1]
        }
    }
    return max_profit;
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_max_profit() {
        let prices: Vec<i32> = vec![7, 1, 5, 3, 6, 4];
        let expected = 7;
        assert_eq!(max_profit(prices), expected)
    }
}
