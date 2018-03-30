class HellTriangle:

    def __init__(self, triangle=[]):
        self.__triangle = triangle
        self.__value_max = 0
        self.__index_last_value = 0

    def total_sum(self):
        if self.__is_triangle_valid():
            self.__total_calculates()
            return self.value_max
        return None

    def __total_calculates(self):
        list_to_sum = []
        for row in self.__triangle:
            new_list = row[self.__index_last_value: self.__index_last_value + 2]
            value = max(new_list)
            list_to_sum.append(value)
            self.__index_last_value = row.index(value)

        self.value_max = sum(list_to_sum)

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
