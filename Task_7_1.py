class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.my_list)

    def __add__(self, other):
        result_list = [[0, 0], [0, 0], [0, 0]]
        for index in range(len(self.my_list)):
            for el in range(len(self.my_list[index])):
                result_list[index][el] = self.my_list[index][el] + other.my_list[index][el]
        return '\n'.join('\t'.join(map(str, row)) for row in result_list)


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[1, 2], [3, 4], [5, 6]])
print(matrix_2)
print(matrix_1 + matrix_2)
