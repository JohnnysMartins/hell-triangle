import unittest
from bin.hell_triangle import HellTriangle


class HellTriangleTest(unittest.TestCase):

    def test_upper(self):
        triangle = HellTriangle([])
        self.assertIsNone(triangle.total_sum())


if __name__ == '__main__':
    print("Hell triangle test")
    unittest.main()
