import unittest
def array_rotare(nums:list[int],k:int)-> None:
    n = len(nums)
    k = k % n  # Ajustar k si es mayor que la longitud de la lista
    reverse(nums, 0, n - 1)  # Invertir toda la lista
    reverse(nums, 0, k - 1)  # Invertir los primeros k elementos
    reverse(nums, k, n - 1)  # Invertir el resto de elementos


def reverse(nums, start, end) -> None:
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


class TestRotareArray(unittest.TestCase):

    def test_rotate(self):
        nums = [1,2]
        k= 3
        array_rotare(nums,k)
        self.assertEqual(nums,[2,1])

if __name__ == "__main__":
    unittest.main()