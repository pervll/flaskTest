class Board:
    def __init__(self,pieces,next_move,white_castling,black_castling,en_passant,winboard,round):
        self.pc=pieces
        self.nm=next_move
        self.wc=white_castling
        self.bc=black_castling
        self.ep=en_passant
        self.wb=winboard
        self.rd=round
        



def generate_chess_board(fen):
    fen_parts = fen.split(' ')
    board = []
    rank = ''
    for char in fen_parts[0]:
        if char.isdigit():
            rank += '.' * int(char)
        elif char=='/':
            board.append(rank)
            rank=''
        else:
            rank += char
    board.append(rank)
    next_move=fen_parts[1]
    castling=fen_parts[2]
    white_castling=False
    black_castling=False
    if castling=='KQkq':
        white_castling=True
        black_castling=True
    elif castling=='KQ':
        white_castling=True
    elif castling=='kq':
        black_castling=True
    en_passant=fen_parts[3]
    win_board=fen_parts[4]
    round=int(fen_parts[5])
    chess_board=Board(board,next_move,white_castling,black_castling,en_passant,win_board,round)
    return chess_board

def is_check(chess_board,color):
    pieces=chess_board.pc
    if color=='black':
        for i in range(0,len(pieces)):
            for j in range(0,len(pieces)):
                if pieces[i][j]=='k':
                    posx=i
                    posy=j
                    break
        




        


    