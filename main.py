from random import sample
from print_board import PrintBoard


BASE = 3
SIDE = BASE * BASE


def main():
    board = generate_board()
    # for i in board:
    #     print(i)
    b = PrintBoard(board)
    b.print_board()


# 產生數獨題目
def generate_board():
    rbase = range(BASE)
    rows = get_list(rbase)
    # print(rows)
    cols = get_list(rbase)
    # print(cols)
    nums = shuffle(range(1, SIDE+1))
    board = get_board(rows, cols, nums)
    # print(board)
    return board


# 產生隨機不重複數字的 list
def shuffle(s):
    return sample(s,len(s))


# 產生 0 ~ 8 位置不重複的 list
def get_list(rbase):
    temp = []
    for r in shuffle(rbase):
        for g in shuffle(rbase):
            temp.append(g*BASE + r)
    return temp


# 透過 rows 和 cols 給定之數值，指定新的位置
def pattern(r,c): 
    return (BASE*(r%BASE)+r//BASE+c)%SIDE


def get_board(rows, cols, nums):
    temp_row = []
    for r in rows:
        temp_col = []
        for c in cols:
            temp_col.append(nums[pattern(r, c)])
        temp_row.append(temp_col)
    return temp_row


if __name__ == "__main__":
    main()



