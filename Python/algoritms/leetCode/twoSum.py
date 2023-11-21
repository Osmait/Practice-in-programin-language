def twoSum(nums: list[int], target: int) -> list[int] | None:
    prevMap = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i


print(twoSum([3, 2, 4], 6))
