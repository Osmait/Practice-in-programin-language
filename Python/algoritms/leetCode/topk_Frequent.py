import unittest
def toKFrequent(nums:list[int],k:int)->list[int]:

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

class TestTopFRequent(unittest.TestCase):

    def test1(self):
        nums = [1,1,1,2,2,3]
        k =2
        excepted = [1,2]
        result = toKFrequent(nums,k)
        self.assertEqual(result,excepted)


if __name__ == "__main__":
    unittest.main()