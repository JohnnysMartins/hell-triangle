import unittest
from lib.hell_triangle import HellTriangle


class HellTriangleTest(unittest.TestCase):

    def test_triangle_is_not_none(self):
        triangle = HellTriangle([])
        self.assertIsNotNone(triangle)

    def test_total_sum_is_none(self):
        triangle = HellTriangle([])
        self.assertIsNone(triangle.total_sum())

    def test_triangle_with_letter(self):
        triangle = HellTriangle([[1], [2, 'b']])
        self.assertIsNone(triangle.total_sum())

    def test_triangle_total_sum(self):
        triangle = HellTriangle([[1], [3, 7]])
        self.assertEqual(8, triangle.total_sum())

    def test_triangle_total_sum(self):
        triangle = HellTriangle([[1], [3, 7], [9, 7, 1]])
        self.assertEqual(15, triangle.total_sum())


if __name__ == '__main__':
    unittest.main()
