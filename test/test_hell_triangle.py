import unittest
from lib.hell_triangle import HellTriangle


class HellTriangleTest(unittest.TestCase):

    def test_triangle_isNotNone(self):
        triangle = HellTriangle([])
        self.assertIsNotNone(triangle)

    def test_triangle_with_letter(self):
        triangle = HellTriangle([[1], [2, 'b']])
        self.assertIsNone(triangle.total_sum())

    def test_triangle_total_sum(self):
        triangle = HellTriangle([[1], [3, 7]])
        self.assertEqual(11, triangle.total_sum())


if __name__ == '__main__':
    unittest.main()
