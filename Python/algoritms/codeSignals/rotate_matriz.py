import unittest


def rotate_matrix(a: list[list[int]]):

    a.reverse()
    for i in range(len(a)):
        for j in range(i):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a


class test(unittest.TestCase):
    def matrix_test(self):

        a = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        expected = [[7, 4, 1],
                    [8, 5, 2],
                    [9, 6, 3]]
        self.assertEqual(expected, rotate_matrix(a))


if __name__ == "__main__":
    unittest.main()
