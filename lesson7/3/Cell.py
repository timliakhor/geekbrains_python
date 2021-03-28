class Cell:
    def __init__(self, cell_amount: int):
        self.__cell_amount = cell_amount

    def __add__(self, other):
        return self.__cell_amount + other.__cell_amount

    def __sub__(self, other):
        res = self.__cell_amount - other.__cell_amount
        if res <= 0:
            raise RuntimeError("We will die!!!!!")
        return self.__cell_amount - other.__cell_amount

    def __mul__(self, other):
        return self.__cell_amount * other.__cell_amount

    def __truediv__(self, other):
        return self.__cell_amount // other.__cell_amount

    def make_order(self, cells_in_row: int) -> str:
        int_rows: int = self.__cell_amount // cells_in_row
        remainder: int = self.__cell_amount % cells_in_row

        res = ''
        for _ in range(0, int_rows):
            res += cells_in_row * '*'
            res += '\n'
        return res + remainder * '*'

cell1: Cell = Cell(10)
cell2: Cell = Cell(5)

print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)

print(cell1.make_order(4))