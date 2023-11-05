import unittest
def removeDuplicate(nums:list[int]):
    i = 0
    while i < len(nums) -1:
        if nums[i] == nums[i+1]:
            del nums[i]
        else:
            i+=1
    return len(nums)






class TestRemoveDuplicate(unittest.TestCase):

    def Test_remove_sort(self):
        nums = [1,1,2,2]
        k = removeDuplicate(nums)
        self.assertEqual(k == 2)
        expected = [1,2]
        for i in range(len(nums)):
            self.assertEqual(nums[i],expected[i])


if __name__ == "__main__":
    unittest.main()