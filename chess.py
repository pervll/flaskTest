def fen_to_board(fen):
    fen_parts = fen.split('?')
    board_info = fen_parts[0]
    rank_info = board_info.split('/')
    board=[]
    for i in range(0,8):
        rank = []
        for j in range(0,len(rank_info[i])):
            if rank_info[i][j] == 'o':
                n = int(rank_info[i][j-1])
                j = j+1
                while n>0:
                    rank.append(None)
                    n=n-1
            elif rank_info[i][j].isdigit() == True:
                continue
            else:
                rank.append(rank_info[i][j])
        board.append(rank)
    cur_color = fen_parts[1]
    #print(board)
    board2=[]
    for i in range(0,8):
        tmp=[]
        for j in range(0,8):
            tmp.append(None)
        board2.append(tmp)

    for i in range(0,8):
        for j in range(0,8):
            board2[j][i]=board[i][j]

    ret = [board2,cur_color]

    return ret

def board_to_fen(board,color):
    board2=[]
    for i in range(0,8):
        tmp=[]
        for j in range(0,8):
            tmp.append(None)
        board2.append(tmp)

    for i in range(0,8):
        for j in range(0,8):
            board2[j][i]=board[i][j]
    board=board2
    fen=""
    for i in range(0,8):
        cnt=0
        for j in range(0,8):
            if board[i][j] != None:
                if cnt!=0:
                    fen=fen+str(cnt)+'o'
                    cnt=0
                fen=fen+board[i][j]
            else:
                cnt=cnt+1
        if cnt!=0:
            fen=fen+str(cnt)+'o'
        fen=fen+'/'
    fen=fen+'?'+color
    return fen

fen_test = "rnbqkbnr/pppppppp/8o/8o/8o/8o/PPPPPPPP/RNBQKBNR?w"

board_test = fen_to_board(fen_test)[0]

#print(board_to_fen(board_test,'w'))

        




        


    