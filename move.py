from check import check

MOVE={  'b':[(-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
            (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8),
            (1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(6,6),(7,7),
            (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8)],
        'k':[(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(1,1),(-1,1),(1,-1)],
        'n':[(1,2),(-1,2),(-1,-2),(1,-2),(2,1),(2,-1),(-2,1),(-2,-1)],
        'p':[(0,1),(1,1),(-1,1),(0,2),(0,-1),(1,-1),(-1,-1),(0,-2)],
        'q':[(-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7),(-8,-8),
            (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),(8,-8),
            (1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(6,6),(7,7),
            (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),(-8,8),
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
    #print (sx,sy,x,y)

    if not(0 <= sx+x < 8) or not(0 <= sy+y < 8) or not(0 <= sx < 8) or not(0 <= sy < 8):
        #print(1)
        return [False,BOARD]
    
    start=BOARD[sx][sy]
    end=BOARD[sx+x][sy+y]
    if start == None:
        #print(2)
        return [False,BOARD]
    
    if end != None and start.isupper() == end.isupper():
        #print(3)
        return [False,BOARD]
    
    if (x,y) not in MOVE[start.lower()]:
        #print(4)
        return [False,BOARD]
    
    if start.lower()=='b' or start.lower()=='q' or start.lower()=='r':
        i = MOVE[start.lower()].index((x,y)) - max(abs(x),abs(y)) + 1
        for j in range(i,i+max(abs(x),abs(y))-1):
            if BOARD[sx+MOVE[start.lower()][j][0]][sy+MOVE[start.lower()][j][1]]==None:
                continue
            #print(5)
            return [False,BOARD]
        BOARD[sx+x][sy+y] = start
        BOARD[sx][sy] = None
        return [True,BOARD]

    if start.lower() == 'n' or start.lower() == 'k':
        BOARD[sx+x][sy+y] = start
        BOARD[sx][sy] = None
        return [True,BOARD]  
    
    if start.lower() == 'p':
        if start.isupper() == False:
            if (x,y) == (0,1) and end == None:
                BOARD[sx+x][sy+y] = start
                BOARD[sx][sy] = None
                return [True,BOARD]
            elif ( (x,y)==(1,1) or (x,y)==(-1,1) ) and end != None:
                BOARD[sx+x][sy+y] = start
                BOARD[sx][sy] = None
                return [True,BOARD]
            elif (x,y)==(0,2) and sy==1:
                BOARD[sx+x][sy+y] = start
                BOARD[sx][sy] = None
                return [True,BOARD]
        if start.isupper() == True:
            if (x,y) == (0,-1) and end == None:
                BOARD[sx+x][sy+y] = start
                BOARD[sx][sy] = None
                return [True,BOARD]
            elif ( (x,y)==(1,-1) or (x,y)==(-1,-1) ) and end != None:
                BOARD[sx+x][sy+y] = start
                BOARD[sx][sy] = None
                return [True,BOARD]
            elif (x,y)==(0,-2) and sy==6:
                BOARD[sx+x][sy+y] = start
                BOARD[sx][sy] = None
                return [True,BOARD]
        
    #print(6)
    return [False,BOARD]

def move1(BOARD,movement,cp):
    if move(BOARD,movement)[0]:
        b=move(BOARD,movement)[1]
        if not check(b,cp):
            return [True,b]
    return [False,BOARD]