class HellTriangle:

    def __init__(self, triangle):
        self.__triangle = triangle

    def total_sum(self):
        if self.__is_triangle_valid():
            return self.__total_calculates()
        return None

    def __total_calculates(self):
        total = 0
        for row in self.__triangle:
            for item in row:
                total += item
        return total

    def __is_triangle_valid(self):
        if not self.__triangle or not isinstance(self.__triangle, list):
            return False
        return self.__is_row_valid()

    def __is_row_valid(self):
        for row in self.__triangle:
            if not row or not isinstance(row, list):
                return False
            for item in row:
                if not item or not isinstance(item, int):
                    return False
        return True
