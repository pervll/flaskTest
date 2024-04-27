MOVE={  'b':[(-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
            (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8),
            (1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(6,6),(7,7),
            (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8)],
        'k':[(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(1,1),(-1,1),(1,-1)],
        'n':[(1,2),(-1,2),(-1,-2),(1,-2),(2,1),(2,-1),(-2,1),(-2,-1)],
        'p':[(0,1)],
        'pS1':[(0,2)],
        'q':[(-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
            (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8),
            (1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(6,6),(7,7),
            (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8)
             (0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
             (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
             (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
             (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0)],
        'r':[(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
             (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
             (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),(0,-8),
             (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),(-8,0),]
        }
def move(BOARD,movement): # movement格式规范{sx,sy:出发格坐标 x,y:格变化}
    sx=movement['sx']
    sy=movement['sy']
    x=movement['x']
    y=movement['y']
    if (x,y) in MOVE[BOARD[sx][sy]]:
        if BOARD[sx][sy].lower()=='b' or BOARD[sx][sy].lower()=='q' or BOARD[sx][sy].lower()=='r':
            i=MOVE[BOARD[sx][sy]].index((x,y))-abs(x)+1
            for j in range(i,i+abs(x)-1):
                if BOARD[sx+MOVE[BOARD[sx][sy]][j][0],sy+MOVE[BOARD[sx][sy]][j][1]]==None:
                    continue
                return (False,BOARD)
            if BOARD[sx+x][sy+y]!=None:
                isWhite1=(ord('A')<=ord(BOARD[sx][sy])<=ord('Z'))
                isWhite2=(ord('A')<=ord(BOARD[sx+x][sy+y])<=ord('Z'))
                if isWhite1^isWhite2:
                    BOARD[sx+x][sy+y]=BOARD[sx][sy]
                    BOARD[sx][sy]=None
                    return (True,BOARD)
            else:
                BOARD[sx+x][sy+y]=BOARD[sx][sy]
                BOARD[sx][sy]=None
                return (True,BOARD)
            
        if BOARD[sx][sy].lower()=='k' or BOARD[sx][sy].lower()=='n' or BOARD[sx][sy].lower()=='p':
            if not(isWhite1^isWhite2):
                BOARD[sx+x][sy+y]=BOARD[sx][sy]
                BOARD[sx][sy]=None
                return (True,BOARD)
    return (False,BOARD)