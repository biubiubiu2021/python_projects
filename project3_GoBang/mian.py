


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
    print('\033[1;30;46m    1   2   3   4   5   6   7   8   9   10  \033[0m')
    for i in range(len(checkerboard)):
        print( chr(i+ ord("A")) + "  ", end=' ')
        for j in range(len(checkerboard[i])):
            print(checkerboard[i][j] + "  ", end=' ')
        print()
    print(' ------------------------------------------ \033[0m')

def msg(flag):
    #print_checkerboard()
    if (flag == 1):
        print('\033[32m *棋胜利！  ***\033[0m')
    else:
        print('\033[32m o棋胜利！  ***\033[0m')

def check(x,y, checkboard): #x,y is the coordinate of the chessman
    x=int(x)
    y=int(y)
    if (y-4 >= 0):
        if (checkboard[x][y-1] == flagch
                and checkboard[x][y-2] == flagch
                and checkboard[x][y-3] == flagch
                and checkboard[x][y-4] == flagch):
            finish = True
            return finish
    if (y+4<=9):
        if (checkboard[x][y + 1] == flagch
                and checkboard[x][y + 2] == flagch
                and checkboard[x][y + 3] == flagch
                and checkboard[x][y + 4] == flagch):
            finish = True
            return finish
    if  (x-4 >= 0):
        if (checkboard[x-1][y] == flagch
                and checkboard[x-2][y] == flagch
                and checkboard[x-3][y] == flagch
                and checkboard[x-4][y] == flagch):
            finish = True
            return finish
    if  (x+4 <= 9):
        if (checkboard[x+1][y] == flagch
                and checkboard[x+2][y] == flagch
                and checkboard[x+3][y] == flagch
                and checkboard[x+4][y] == flagch):
            finish = True
            return finish

    if  (x-4 >= 0 and y -4 >=0):
        if (checkboard[x-1][y-1] == flagch
                and checkboard[x-2][y-2] == flagch
                and checkboard[x-3][y-3] == flagch
                and checkboard[x-4][y-4] == flagch):
            finish = True
            return finish

    if  (x+4 <= 9 and y -4 >=0):
        if (checkboard[x+1][y-1] == flagch
                and checkboard[x+2][y-2] == flagch
                and checkboard[x+3][y-3] == flagch
                and checkboard[x+4][y-4] == flagch):
            finish = True
            return finish

    if  (x-4 >= 0 and y +4 <=9):
        if (checkboard[x-1][y+1] == flagch
                and checkboard[x-2][y+2] == flagch
                and checkboard[x-3][y+3] == flagch
                and checkboard[x-4][y+4] == flagch):
            finish = True
            return finish

    if  (x+4 <= 0 and y +4 <=9):
        if (checkboard[x+1][y+1] == flagch
                and checkboard[x+2][y+2] == flagch
                and checkboard[x+3][y+3] == flagch
                and checkboard[x+4][y+4] == flagch):
            finish = True
            return finish


def change_player(flagNum):
    if (flagNum == 1):
        flagch = "*"
        print('\033[1;37;45 请player1 * 输入棋子坐标（例如A1）: \033[0m', end=" ")
    else:
        flagch = "o"
        print('\033[1;37;45 请player2 o 输入棋子坐标（例如A1）: \033[0m', end=" ")

    flagNum *= -1



if __name__ == '__main__' :
    c = init_checkerboard()
    print_checkerboard(c)
    msg(1)
