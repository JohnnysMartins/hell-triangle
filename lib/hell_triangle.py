class HellTriangle:

    def __init__(self, triangle):
        self.triangle = triangle

    def total_sum(self):
        if not self.triangle or not isinstance(self.triangle, list):
            return None
        return 0
