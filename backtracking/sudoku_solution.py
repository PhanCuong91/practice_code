sudoku = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

sudoku_1= [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [5, 0, 0, 9, 0, 8, 0, 0, 3],
          [0, 2, 0, 0, 7, 0, 0, 6, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 3, 0, 0, 0, 1, 0, 0],
          [0, 0, 8, 1, 0, 2, 5, 0, 0],
          [1, 0, 0, 5, 0, 4, 0, 0, 6],
          [0, 9, 5, 8, 0, 6, 4, 1, 0],
          [8, 0, 0, 0, 9, 0, 0, 0, 2]]

sudoku_2= [[4, 0, 0, 8, 0, 0, 0, 0, 0],
          [7, 6, 9, 0, 0, 0, 0, 2, 8],
          [0, 0, 8, 7, 6, 0, 3, 0, 0],
          [0, 0, 0, 3, 4, 8, 0, 1, 0],
          [0, 0, 0, 0, 7, 5, 0, 0, 6],
          [5, 0, 4, 2, 1, 0, 0, 0, 0],
          [0, 2, 0, 0, 0, 7, 0, 0, 0],
          [0, 0, 7, 0, 0, 3, 6, 8, 0],
          [0, 0, 6, 4, 0, 2, 0, 7, 9]]


class SudokuSolution:
    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.constant_cell_arr = []

    def constant_cell(self):
        for r in range(9):
            for c in range(9):
                if self.sudoku[r][c] != 0:
                    self.constant_cell_arr.append([r, c])

    def is_cell_valid(self, row, column, value):

        for c in range(9):
            # if the number was already in this row, then return False
            if c != column:
                tmp = self.sudoku[row][c]
                # print(f"column {c} and {row} value is {tmp}")
                if tmp == value:
                    return False
        for r in range(9):
            # if the number was already in this column, then return False
            if r != row:
                tmp = self.sudoku[r][column]
                # print(f"row {column} and {r} value is {tmp}")
                if tmp == value:
                    return False
        col = int(column / 3)
        ro = int(row / 3)
        # if the number was already in this sub-square, then return False
        for c in range(col*3, col*3+3):
            for r in range(ro*3, ro*3+3):
                if c != column or r != row:
                    tmp = self.sudoku[r][c]
                    # print(f"column and row {c} and {r} value is {tmp}")
                    if tmp == value:
                        return False
        return True

    def solution(self):
        decrease_col = False
        r = 0
        c = 0
        while r < 9:
            decrease_row = False
            while c < 9:
                if [r, c] not in self.constant_cell_arr:
                    # increase number if go back previous cell
                    for v in range(self.sudoku[r][c]+1, 10):
                        decrease_col = True
                        # find a valid number
                        if self.is_cell_valid(r, c, v):
                            self.sudoku[r][c] = v
                            # set to False if find a valid number
                            decrease_col = False
                            break
                # if cannot find a valid number, then reduce column
                # and set current cell to 0
                if decrease_col:
                    self.sudoku[r][c] = 0
                    c -= 1
                    # if the cell is in constant array, then reduce column
                    while c >= 0:
                        if [r, c] in self.constant_cell_arr:
                            c -= 1
                        else:
                            break
                    # if column is less than , then reduce row
                    if c < 0:
                        decrease_row = True
                        break
                else:
                    # increase column, if cell in constant array or find a valid number
                    c += 1

            if decrease_row:
                # reduce row, if row is less than 0, cannot
                r -= 1
                if r < 0:
                    return False
                # after reduce row, column should start from 8
                c = 8
                # if the cell is in constant array, then reduce column
                while c >= 0:
                    if [r, c] in self.constant_cell_arr:
                        c -= 1
                    else:
                        break
            else:
                r += 1
                c = 0
        return True


if __name__ == "__main__":
    su = SudokuSolution(sudoku_2)
    su.constant_cell()
    print(su.solution())
    print("solution result")
    for i in su.sudoku:
        print(i)
    i = 0
    for ro in range(9):
        for co in range(9):
            if su.is_cell_valid(ro, co, su.sudoku[ro][co]):
                i += 1
    if i == 81:
        print(True)
