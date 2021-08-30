class SolveSudoku:
    def __init__(self, board):
        self.board = board

    def do_solve(self):
        self.solve_sudoku()
        return self.board

    def solve_sudoku(self):

        found = self.is_empty()
        if not found:
            return True
        else:
            row, col = found
       
        # self.guess_num(row, col)
        for guess_num in range(1, 10):
            if self.is_num_ok(guess_num, row, col):
                self.board[row][col] = guess_num
                if self.solve_sudoku():
                    return True

            self.board[row][col] = 0
        return False

    def is_empty(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                # (i, j)  # (row, column)
                if self.board[i][j] == 0:
                    return i, j
        return False

    # def guess_num(self, row, col):
    #     for guess in range(1, 10):
    #         if self.is_num_ok(guess, row, col):
    #             self.board[row][col] = guess
    #             if self.solve_sudoku():
    #                 return True

    #         self.board[row][col] = 0

    def is_num_ok(self, guess, row, col):
        for i in range(len(self.board[0])):  # 判斷同一列(row)是否有相同數字
            if self.board[row][i] == guess and col != i:
                return False
        for i in range(len(self.board)):     # 判斷同(column)一行是否有相同數字
            if self.board[i][col] == guess and row != i:
                return False
        
        # 判斷小九宮格內是否有相同數字
        box_row = col // 3
        box_col = row // 3
        for i in range(box_col*3, box_col*3 + 3):
            for j in range(box_row*3, box_row*3 + 3):
                if self.board[i][j] == guess and i != row and j != col:
                    return False

        return True
