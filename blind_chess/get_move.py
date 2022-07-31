import chess

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
def subtract(lst1, lst2):
    lst3 = [value for value in lst1 if value not in lst2]
    return lst3

def getPos(fen):
    '''returns the position of pieces in a board'''
    a = chess.Board(fen)
    P = [] 
    N = []
    B = []
    Q = []
    K = []
    R = []
    F = []
    p = []
    n = []
    b = []
    q = []
    k = []
    r = []
    f = []
    for i in range(97, 104+1):
        for j in range(1, 8+1):
            s = chr(i)+str(j)
            pa = str(a.piece_at(chess.parse_square(s)))

            if pa == "P":
                P.append(s)
            elif pa == "N":
                N.append(s)
            elif pa == "B":
                B.append(s)
            elif pa == "Q":
                Q.append(s)
            elif pa == "K":
                K.append(s)
            elif pa == "R":
                R.append(s)
            elif pa == "p":
                p.append(s)
            elif pa == "n":
                n.append(s)
            elif pa == "b":
                b.append(s)
            elif pa == "q":
                q.append(s)
            elif pa == "k":
                k.append(s)
            elif pa == "r":
                r.append(s)
    F.extend([P, N, B, Q, K, R, p, n, b, q, k, r])
    return F

def getMove(prevPos, currentPos):
    PIECES = ["P", "N", "B", "Q", "K", "R", "p", "n", "b", "q", "k", "r"]
    F1 = getPos(prevPos) #d4
    F2 = getPos(currentPos) #e3
    for i in range(0, 12):
        k = intersection(F2[i], F1[i])
        j = subtract(F2[i], k)
        if j != []:
            return(str(PIECES[i])+str(j[0]))
# print(get_pos2("rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR w KQkq - 0 1", "rnbqkbnr/ppp1pppp/8/3p4/3P4/8/PPP1PPPP/RNBQKBNR w KQkq - 0 1"))
    #"rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR w KQkq - 0 1"

    #"rnbqkbnr/ppp1pppp/8/3p4/3P4/8/PPP1PPPP/RNBQKBNR w KQkq - 0 1"