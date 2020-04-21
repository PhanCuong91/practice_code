"""
N-Queens Problem: Given a chess board having  cells,
we need to place  queens in such a way that no queen is attacked by any other queen.
A queen can attack horizontally, vertically and diagonally.
"""


class NQueens:

    def __init__(self, N):
        self.N = N
        self.matrix = []
        self.pos = []
        self.set_zero()

    @staticmethod
    def set_matrix(n):
        matrix = []
        sub_max = []
        for r in range(n):
            sub_max.append(0)
        for c in range(n):
            matrix.append([0, 0, 0, 0])
        return [[0] * n for i in range(n)]

    def set_zero(self):
        self.matrix = NQueens.set_matrix(self.N)

    def fill_matrix(self, row, col, value):
        # fill row
        for i in range(col + 1, self.N):
            self.matrix[row][i] = value
        for i in range(0, col):
            self.matrix[row][i] = value
        # fill column
        for i in range(row + 1, self.N):
            self.matrix[i][col] = value
        for i in range(0, row):
            self.matrix[i][col] = value
        # # fill diagonal
        c = col
        r = row
        while c + 1 < self.N and r + 1 < self.N:
            self.matrix[r + 1][c + 1] = value
            c += 1
            r += 1
            print(f"{r} and {c}")
        c = col
        r = row
        while c + 1 < self.N and r - 1 >= 0:
            self.matrix[r - 1][c + 1] = value
            c += 1
            r -= 1
            print(f"{r} and {c}")
        c = col
        r = row
        while c - 1 >= 0 and r - 1 >= 0:
            self.matrix[r - 1][c - 1] = value
            c -= 1
            r -= 1
            print(f"{r} and {c}")
        c = col
        r = row
        while c - 1 >= 0 and r + 1 < self.N:
            self.matrix[r + 1][c - 1] = value
            c -= 1
            r += 1
            print(f"{r} and {c}")

    def remove_value(self, value):
        for r in range(self.N):
            for c in range(self.N):
                if self.matrix[r][c] == value:
                    self.matrix[r][c] = 0

    def solve(self):
        # this method shall choose the first of matrix as 1 queen 's position. then search other position
        # from second cell of matrix by increase column and row.
        r = c = 0
        while (r < self.N) and (r >= 0):
            while (c < self.N) and (c >= 0):
                # find queen position
                if self.is_valid_pos([r, c]):
                    self.pos.append([r, c])
                c += 1
            # if reach last position of matrix (r = N-1, c = N), then check N queen is reached or not
            if r == self.N - 1 and c == self.N:
                # and cannot find N queen once , then it has two cases:
                # first one: if queen (n-m)th is at the last position of matrix,
                # then remove position of queen (n-m)th and (n-m-1)th
                # and search new queen (n-m-1)th 's position which start from old one's position plus one(with m < n-1).
                # second one: if queen (n-m)th is not at the last position of matrix
                # then remove position of queen (n-m)th
                # and search new queen (n-m)th 's position which start from old one's position plus one (with m < n-1).
                if len(self.pos) < self.N:
                    # first one: if queen (n-m)th is at the last position of matrix,
                    if self.pos[len(self.pos) - 1] == [self.N - 1, self.N - 1]:
                        # then remove position of queen (n-m)th
                        self.pos.pop(len(self.pos) - 1)
                    if len(self.pos) == 0:
                        return False
                    # first one: remove position of queen (n-m-1)th
                    # search new queen (n-m-1)th 's position which start from old one's position plus one
                    # (with m < n-1).
                    # second one: if queen (n-m)th is not at the last position of matrix
                    # then remove position of queen (n-m)th
                    # and search new queen (n-m)th 's position which start from old one's position plus one
                    # (with m < n-1).
                    c = self.pos[len(self.pos) - 1][1] + 1
                    r = self.pos[len(self.pos) - 1][0]
                    self.pos.pop(len(self.pos) - 1)
                    if c == self.N:
                        r += 1
                        c = 0
                else:
                    return True
            # if not reach last position of matrix (r = N-1, c = N), increase r and set c to 0
            else:
                r += 1
                c = 0

    def solve_1(self, r, c):
        while (c < self.N) and (c >= 0):
            # find queen position
            if self.is_valid_pos([r, c]):
                self.pos.append([r, c])
            c += 1
            # if reach last position of matrix (r = N-1, c = N), then check N queen is reached or not
        if r == self.N - 1 and c == self.N:
            # and cannot find N queen once , then it has two cases:
            # first one: if queen (n-m)th is at the last position of matrix,
            # then remove position of queen (n-m)th and (n-m-1)th
            # and search new queen (n-m-1)th 's position which start from old one's position plus one(with m < n-1).
            # second one: if queen (n-m)th is not at the last position of matrix
            # then remove position of queen (n-m)th
            # and search new queen (n-m)th 's position which start from old one's position plus one (with m < n-1).
            if len(self.pos) < self.N:
                # first one: if queen (n-m)th is at the last position of matrix,
                if self.pos[len(self.pos) - 1] == [self.N - 1, self.N - 1]:
                    # then remove position of queen (n-m)th
                    self.pos.pop(len(self.pos) - 1)
                if len(self.pos) == 0:
                    return False
                # first one: remove position of queen (n-m-1)th
                # search new queen (n-m-1)th 's position which start from old one's position plus one
                # (with m < n-1).
                # second one: if queen (n-m)th is not at the last position of matrix
                # then remove position of queen (n-m)th
                # and search new queen (n-m)th 's position which start from old one's position plus one
                # (with m < n-1).
                c = self.pos[len(self.pos) - 1][1] + 1
                r = self.pos[len(self.pos) - 1][0]
                self.pos.pop(len(self.pos) - 1)
                if c == self.N:
                    r += 1
                    c = 0
                self.solve_1(r, c)
            else:
                return True
            # if not reach last position of matrix (r = N-1, c = N), increase r and set c to 0
        else:
            r += 1
            c = 0
            self.solve_1(r, c)

    def recursive_solution(self, r, c):
        # base case
        if self.pos == self.N:
            return True
            # if column is out of matrix, then increase row and reset column

        # find queen in matrix
        while c < self.N:
            # if column is equal N, then increase row and reset column
            if c == self.N:
                r += 1
                c = 0
                # cannot find queen in matrix
                if r == self.N:
                    return False
            # check current cell is valid position for queen or not
            if self.is_valid_pos([r, c]):
                # save position
                self.pos.append([r, c])
                # find next queen 's position
                if self.recursive_solution(r, c+1):
                    return True
                # cannot find next queen position, then remove current position
                self.pos.pop()
            # increase column
            c += 1
        pass

    # copy from https://www.geeksforgeeks.org/python-program-for-n-queen-problem-backtracking-3/
    def solveNQUtil(self, col):
        # base case: If all queens are placed
        # then return true
        if col >= self.N:
            return True

        # Consider this column and try placing
        # this queen in all rows one by one
        for i in range(self.N):

            if self.is_valid_pos([i, col]):
                # Place this queen in board[i][col]
                self.matrix[i][col] = 1
                self.pos.append([i, col])

                # recur to place rest of the queens
                if self.solveNQUtil( col + 1):
                    return True

                # If placing queen in board[i][col
                # doesn't lead to a solution, then
                # queen from board[i][col]
                self.matrix[i][col] = 0
                self.pos.pop()

        # if the queen can not be placed in any row in
        # this colum col  then return false
        return False

    def is_valid_pos(self, pos):
        if len(self.pos) == 0:
            return True
        if pos[0] >= self.N and pos[1] >= self.N:
            return "the position is not in matrix"

        else:
            for i in self.pos:
                if pos[0] == i[0] or pos[1] == i[1]:
                    return False
                elif abs(pos[0] - i[0]) == abs(pos[1] - i[1]):
                    return False
        return True


if __name__ == "__main__":
    queens = NQueens(4)
    for n in range(3, 8):
        queens = NQueens(n)
        queens.solve()
        print(queens.pos)
        queens.solve_1(0, 0)
        print(queens.pos)
        queens.solveNQUtil(0)
        print(queens.pos)
        queens.recursive_solution(0, 0)
        print(queens.pos)

