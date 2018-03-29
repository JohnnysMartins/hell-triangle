import unittest
from lib.hell_triangle import HellTriangle


class HellTriangleTest(unittest.TestCase):

    def test_triangle_isNone(self):
        triangle = HellTriangle([])
        self.assertIsNone(triangle.total_sum())


if __name__ == '__main__':
    unittest.main()
