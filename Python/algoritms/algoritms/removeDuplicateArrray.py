def removeDuplicates(nums):
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            del nums[i]
        else:
            i += 1
    return len(nums)


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

print(removeDuplicates(nums))
