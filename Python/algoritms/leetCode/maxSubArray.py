from typing import List


def maxSubArray(nums) -> int:

    max_sum = float('-inf')
    current_sum = 0  # Initialize current_sum as 0

    for num in nums:
        current_sum += num
        max_sum = max(max_sum, current_sum)

        # If current_sum becomes negative, reset it to 0
        if current_sum < 0:
            current_sum = 0

    return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))
