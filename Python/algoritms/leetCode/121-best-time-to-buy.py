def maxProfit(prices: list[int]) -> int:
    res = 0
    lowest = prices[0]
    for price in prices:
        if price < lowest:
            lowest = price
        res = max(res, price - lowest)
    return res


print(maxProfit([7, 1, 5, 3, 6, 4]))
