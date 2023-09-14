


finish = False # 游戏是否结束
flagNum =1     #当前下棋者标记
flagch = ""    #当前下棋者棋子
x = 0          #当前棋子的横坐标
y = 0          #当前棋子的纵坐标


#棋盘初始化

def init_checkerboard():
    print('\033[1;40;42m ------------- 简易五子棋游戏（控制台版）------------- \033[0m')
    checkerboard = []
    for i in range(10):
        checkerboard.append([])
        for j in range(10):
            checkerboard[i].append("-")
    return checkerboard

def print_checkerboard(checkerboard):
    print('\033[1;30;46m ------------------------------------------ \033[0m')
    print('\033[1;30;46m    1   2   3   4   5   6   7   8   9   10   ')
    for i in range(len(checkerboard)):
        print( chr(i+ ord("A")) + "  ", end=' ')
        for j in range(len(checkerboard[i])):
            print(checkerboard[i][j] + "  ", end=' ')
        print()
    print(' ------------------------------------------ \033[0m')

if __name__ == '__main__' :
    c = init_checkerboard()
    print_checkerboard(c)
