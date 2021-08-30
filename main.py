from generate_board import GenerateBoard
from print_board import PrintBoard
from solve_sudoku import SolveSudoku


BASE = 3
SIDE = BASE * BASE
SQUARES = SIDE * SIDE


def main():
    bd = GenerateBoard(BASE, SIDE, SQUARES)
    board = bd.generate_board()
    b = PrintBoard(board)
    b.print_board()
    # for i in board:
    #     print(i)

    s = SolveSudoku(board)
    solution_board = s.do_solve()

    s_b = PrintBoard(solution_board)
    s_b.print_board()


if __name__ == "__main__":
    main()



