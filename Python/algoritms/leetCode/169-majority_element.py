import unittest


def majorityElement(nums: list[int]) -> int:
    nums_dic = {}
    num_max = {"max": 0, "key": 0}
    for i in nums:
        nums_dic.setdefault(i, 0)
        if i in nums_dic:
            nums_dic[i] += 1

    for k, v in nums_dic.items():
        if v > num_max["max"]:
            num_max["max"] = v
            num_max["key"] = k
    return num_max["key"]


def majorityElement2(nums: list[int]) -> int:
    res, count = 0, 0

    for n in nums:
        if count == 0:
            res = n
        count += (1 if n == res else -1)
    return res


def majorityElement3(nums: list[int]) -> int:
    count = {}
    res, maxCount = 0, 0

    for n in nums:
        count[n] = 1 + count.get(n, 0)
        res = n if count[n] > maxCount else res
        maxCount = max(count[n], maxCount)
    return res


class TestMajorityElement(unittest.TestCase):

    def TestMajorityElement1(self):
        n = majorityElement([3, 3, 4, 4, 3])
        self.assertEqual(n, 3)

    def TestMajorityElement2(self):
        n = majorityElement2([2, 2, 3])
        self.assertEqual(n, 2)

    def TestMajorityElement3(self):
        n = majorityElement3([1, 1, 4])
        self.assertEqual(n, 1)


if __name__ == "__main__":
    unittest.main()
