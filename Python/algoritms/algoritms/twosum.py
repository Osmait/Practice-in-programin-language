from typing import List


# def twoSum(nums: List[int], target: int) -> List[int]:

#     for i in range(0, len(nums)-1):
#         a = target - nums[i]
#         for t in range(1, len(nums)-1):
#             if nums[i] + a == target:
#                 return [i, t]
def twoSum(nums: List[int], target: int) -> List[int]:
    numMap = {     }

    for i, n in enumerate(nums):
        complement = target - n
        if complement in numMap:
            return [numMap[complement], i]
        numMap[n] = i
    return []


print(twoSum([2, 7, 11, 15], 9))
