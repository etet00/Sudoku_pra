base = 3
side = base * base
board =[
    [4, 6, 7, 2, 8, 9, 5, 3, 1],
    [1, 5, 3, 4, 7, 6, 8, 2, 9],
    [2, 9, 8, 3, 5, 1, 6, 7, 4],
    [8, 2, 9, 5, 1, 3, 4, 6, 7],
    [3, 1, 5, 7, 6, 4, 9, 8, 2],
    [7, 4, 6, 8, 9, 2, 1, 5, 3],
    [9, 8, 2, 1, 3, 5, 7, 4, 6],
    [5, 3, 1, 6, 4, 7, 2, 9, 8],
    [6, 7, 4, 9, 2, 8, 3, 1, 5],
]


def num2str(b):
    b_with_str = []
    for k in range(len(b)):
        b_with_str.append(str(b[k]))
    return b_with_str


def line_include_num(b):
    a = "║ . │ . │ . ║ . │ . │ . ║ . │ . │ . ║".split(".")
    return a[0]+b[0]+a[1]+b[1]+a[2]+b[2]+a[3]+b[3]+a[4]+b[4]+a[5]+b[5]+a[6]+b[6]+a[7]+b[7]+a[8]+b[8]+a[9]

def borad_num():
    b_list = []
    for i in board:
        b = num2str(i)
        b_list.append(line_include_num(b))
    return b_list


def print_board(board):

    new_borad = borad_num(board)
    for i in range(19):
        if i == 0:
            print("╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗")  # 上面外框 line1
        elif i == 18:
            print("╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝")  # 下面外框 line19
        elif i % 2 == 0 and i != 0 and i != 6 and i != 12 and i != 18:
            print("╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")  # 中間內框 line3
        elif i == 6 or i == 12:
            print("╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣")  # 中框間隔 line7
        else:
            j = int((i - 1)/2)
            print(new_borad[j])
    
    # print("╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗")  # 上面外框 line1
    # print("║ . │ . │ . ║ . │ . │ . ║ . │ . │ . ║")  # 上面外框 line2 
    # print("╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")  # 中間內框 line3
    # print("╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣")  # 中框間隔 line7
    # print("╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝")  # 下面外框 line19

print_board(board)