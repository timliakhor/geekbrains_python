from typing import List


class Matrix:
    def __init__(self, matrix_values: List[List[int]]):
        for i in range(1, len(matrix_values)):
            if len(matrix_values[i]) != len(matrix_values[i - 1]):
                raise RuntimeError('Bad matrix')
        self.__matrix: List[List[int]] = matrix_values

    def __str__(self):
        s = [[str(e) for e in row] for row in self.__matrix]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        return '\n'.join(table)

    def __add__(self, other):
        if len(self.__matrix) != len(other.__matrix):
            raise RuntimeError('Bad matrix')
        elif len(self.__matrix[0]) != len(other.__matrix[0]):
            raise RuntimeError('Bad matrix')

        return Matrix([[self.__matrix[i][j] + other.__matrix[i][j] for j in range(len(self.__matrix[0]))] for i in
                       range(len(self.__matrix))])


mt1 = Matrix([
    [4, 2, 3],
    [7, 3, 4]
])

mt2 = Matrix([
    [1, 0, 1],
    [5, 2, 9]
])

print(mt1)
print('********')
print(mt2)

mt3 = mt1 + mt2
print('********')
print(mt3)
