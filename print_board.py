class PrintBoard:
    def __init__(self, board):
         self.board = board

    def print_board(self):
        new_board = self.board_num()
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
                print(new_board[j])

    def board_num(self):
        b_list = []
        for i in self.board:
            b = self.num2str(i)
            b_list.append(self.line_include_num(b))
        return b_list

    def num2str(self, b):
        b_with_str = []
        for k in range(len(b)):
            b_with_str.append(str(b[k]))
        return b_with_str

    def line_include_num(self, b):
        a = "║ . │ . │ . ║ . │ . │ . ║ . │ . │ . ║".split(".")
        return a[0]+b[0]+a[1]+b[1]+a[2]+b[2]+a[3]+b[3]+a[4]+b[4]+a[5]+b[5]+a[6]+b[6]+a[7]+b[7]+a[8]+b[8]+a[9]



    
        # print_board(board)   
        # print("╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗")  # 上面外框 line1
        # print("║ . │ . │ . ║ . │ . │ . ║ . │ . │ . ║")  # 上面外框 line2 
        # print("╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")  # 中間內框 line3
        # print("╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣")  # 中框間隔 line7
        # print("╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝")  # 下面外框 line19     