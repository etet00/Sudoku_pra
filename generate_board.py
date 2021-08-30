from random import sample


class GenerateBoard:
    def __init__(self, base, side, squares):
        self.base = base
        self.side = side
        self.squares = squares

    # 產生數獨題目
    def generate_board(self):
        rbase = range(self.base)
        rows = self.get_list(rbase)
        # print(rows)
        cols = self.get_list(rbase)
        # print(cols)
        nums = self.shuffle(range(1, self.side + 1))
        board = self.get_board(rows, cols, nums)
        board = self.get_empties(board)
        # print(board)
        return board

    # 產生隨機不重複數字的 list
    def shuffle(self, s):
        return sample(s, len(s))

    # 產生 0 ~ 8 位置不重複的 list
    def get_list(self, rbase):
        temp = []
        for r in self.shuffle(rbase):
            for g in self.shuffle(rbase):
                temp.append(g*self.base + r)
        return temp

    # 透過 rows 和 cols 給定之數值，指定新的位置
    def pattern(self, r, c):
        return (self.base*(r % self.base)+r//self.base+c) % self.side

    def get_board(self, rows, cols, nums):
        temp_row = []
        for r in rows:
            temp_col = []
            for c in cols:
                temp_col.append(nums[self.pattern(r, c)])
            temp_row.append(temp_col)
        return temp_row

    # 將隨機去除 3/4 的格子
    def get_empties(self, board):
        empties = self.squares * 3//4
        for p in sample(range(self.squares), empties):
            board[p//self.side][p % self.side] = 0
        return board
