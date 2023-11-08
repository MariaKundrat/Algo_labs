import unittest
from main import max_hamsters


class TestMaxHamsters(unittest.TestCase):

    def test_case_1(self):
        s = 7
        c = 3
        hamsters = [[1, 2], [2, 2], [3, 1]]
        self.assertEqual(max_hamsters(s, c, hamsters), 2)

    def test_case_2(self):
        s = 19
        c = 4
        hamsters = [[5, 0], [2, 2], [1, 4], [5, 1]]
        self.assertEqual(max_hamsters(s, c, hamsters), 3)

    def test_case_3(self):
        s = 2
        c = 2
        hamsters = [[1, 50000], [1, 60000]]
        self.assertEqual(max_hamsters(s, c, hamsters), 1)

    def test_none_case(self):
        s = 0
        c = 10
        hamsters = [[1, 1]] * 10
        self.assertEqual(max_hamsters(s, c, hamsters), 0)


if __name__ == '__main__':
    unittest.main()
