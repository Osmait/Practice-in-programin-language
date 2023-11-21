import unittest


def remove_element(nums: list[int], val: int) -> int:
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


class Test(unittest.TestCase):
    def test_remove_element(self) -> None:
        nums = [3, 2, 2, 3]
        val = 3
        k = remove_element(nums, val)
        print(nums)
        expect = 2
        expectedNums = [2, 2]
        self.assertEqual(k, expect)

        for i in range(k):
            self.assertEqual(nums[i], expectedNums[i])


if __name__ == "__main__":
    unittest.main()
