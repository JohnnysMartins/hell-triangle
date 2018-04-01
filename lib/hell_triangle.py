class HellTriangle:

    def __init__(self, triangle):
        self.__triangle = triangle
        self.__value_max = 0

    def total_sum(self):
        if self.__is_triangle_valid():
            self.__total_calculates()
            return self.__value_max
        return None

    def __total_calculates(self):
        while len(self.__triangle) > 1:
            last_row = self.__triangle.pop()
            last_but_one_row = self.__triangle.pop()
            value = [max(last_row[index], last_row[index + 1]) + number for index, number in
                     enumerate(last_but_one_row)]
            self.__triangle.append(value)
        self.__value_max = self.__triangle[0][0]

    def __is_triangle_valid(self):
        if not self.__triangle or not isinstance(self.__triangle, list):
            return False
        return self.__is_row_valid()

    def __is_row_valid(self):
        for index, row in enumerate(self.__triangle):
            if not isinstance(row, list) or not len(row) == index + 1:
                return False
            if not self.__is_item_valid(row):
                return False
        return True

    def __is_item_valid(self, row):
        if not all(isinstance(item, int) for item in row):
            return False
        return True
