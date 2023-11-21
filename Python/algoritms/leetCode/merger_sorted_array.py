import unittest


def merger_sorted_array(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    p1 = m - 1
    p2 = m - 1
    p = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    nums1[: p2 + 1] = nums2[: p2 + 1]


class Test(unittest.TestCase):
    def test_merge(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3

        test_result = [1, 2, 2, 3, 5, 6]
        merger_sorted_array(nums1, m, nums2, n)
        self.assertEqual(test_result, nums1)


if __name__ == "__main__":
    unittest.main()
