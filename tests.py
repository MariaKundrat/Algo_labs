import unittest

from main import zigzag_function


class TestZigzagFunction(unittest.TestCase):
    def test_3x3_matrix(self):
        matrix = [[1, 2, 6],
                  [3, 5, 7],
                  [4, 8, 9]]
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(zigzag_function(matrix), expected_result)

    def test_2x4_matrix(self):
        matrix = [[1, 2, 3, 4],
                  [5, 6, 7, 8]]
        expected_result = [1, 2, 5, 6, 3, 4, 7, 8]
        self.assertEqual(zigzag_function(matrix), expected_result)

    def test_1x1_matrix(self):
        matrix = [[1]]
        expected_result = [1]
        self.assertEqual(zigzag_function(matrix), expected_result)

    def test_zero(self):
        matrix = [[]]
        expected_result = []
        self.assertEqual(zigzag_function(matrix), expected_result)
