king_color = {'w':'K','b':'k'}
opp_cap_color = {'w':False,'b':True}

def check(board,color):
    king = king_color[color]
    opp_cap = opp_cap_color[color]
    for i in range(1,9):
        for j in range(1,9):
            if board[i][j]==king:
                kingpos=(i,j)
    for i in range(1,9):
        for j in range(1,9):
            cur_piece = board[i][j]
            if cur_piece == None:
                continue
            if cur_piece.isupper() == opp_cap:
                movement = [i,j,kingpos[0],kingpos[1]]
                if move(board,movement)[0] == True:
                    return True
    return False

def checkmate(board,color):
    if check(board,color) == False:
        return False
    for i in range(1,9):
        for j in range(1,9):
            cur_piece = board[i][j]
            if cur_piece == None: 
                continue
            for k in range(1,9):
                for l in range(1,9):
                    movement=[i,j,k,l]
                    if move(board,movement)[0] == True and check(move(board,movement)[1],color) == False:
                        return False
    return True
    
    
    
    
                