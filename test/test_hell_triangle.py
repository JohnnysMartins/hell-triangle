import unittest
from lib.hell_triangle import HellTriangle


class HellTriangleTest(unittest.TestCase):

    def test_triangle_isNotNone(self):
        triangle = HellTriangle([])
        self.assertIsNotNone(triangle)

    def test_triangle_sum_isNone(self):
        triangle = HellTriangle([])
        self.assertIsNone(triangle.total_sum())

    def test_triangle_sum_isNotNone(self):
        triangle = HellTriangle([0])
        self.assertIsNotNone(triangle.total_sum())


if __name__ == '__main__':
    unittest.main()
