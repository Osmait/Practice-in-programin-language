import unittest
def removeDuplicate(nums:list[int]):
    if len(nums) <= 2:
        return len(nums)

    k = 2

    for i in range(2, len(nums)):
        if nums[i] != nums[k - 2]:
            nums[k] = nums[i]
            k += 1

    return k






class TestRemoveDuplicate(unittest.TestCase):

    def Test_remove_sort(self):
        nums = [1,1,1,2,2,3]
        k = removeDuplicate(nums)
        self.assertEqual(k == 5)
        expected = [1,1,2,2,3]
        for i in range(len(nums)):
            self.assertEqual(nums[i],expected[i])


if __name__ == "__main__":
    unittest.main()




