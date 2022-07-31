import speech_recognition as sr
# import win32api
import pyautogui as p
p.FAILSAFE = False
import chess
from coor import getAllCoordinates
import pyttsx3
import fens as f
import get_move as g



def getMoveByVoice(engine, r, color):
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        engine.say("Please tell your move...")
        engine.runAndWait()
        # convert speech to text
        audio_data = r.record(source, duration=5)
        text = r.recognize_google(audio_data)
        text = transformText(text, color)
        print(text)
    return text

def transformText(text, color):
    text = text.replace(" ", "")
    if color == "w":
        text = text[:1].upper() + text[-2:].lower()
    else:
        text = text.lower()
    # print(text)
    return text

def flip(board):
    b = list(str(board.__str__()))
    b.reverse()
    for i in b:
        print(i, end="")
    print("\n")

def termination(board, color):
    if color == "white":
        board.turn = chess.WHITE
    else:
        board.turn = chess.BLACK
    if board.is_checkmate():
        print("Checkmate for " + color)
        exit()
    elif board.is_stalemate():
        print("Stalemate")
        exit()
    elif board.is_insufficient_material():
        print("Neither side had sufficient winning material")
        exit()

def castle(board, move, myDict):
    if move[0].lower() + move[-2:].lower() == "kg1":
        if board.has_kingside_castling_rights:
            if board.piece_at(chess.F1) == None and \
                board.piece_at(chess.G1) == None:
                    board.push(chess.Move.from_uci("e1g1"))
                    p.moveTo(myDict['e1'][0], myDict['e1'][1])
                    p.mouseDown(button='left')
                    p.moveTo(myDict['g1'][0], myDict['g1'][1])
                    p.mouseUp()

                    #clicking on the console
                    p.moveTo(1506, 836)
                    p.mouseDown(button='left')
                    p.mouseUp()
                    return 1
    elif move[0].lower() + move[-2:].lower() == "kc1":
        if board.has_queenside_castling_rights:  #is_castling(move)
            if board.piece_at(chess.D1) == None and \
                board.piece_at(chess.C1) == None and \
                board.piece_at(chess.B1) == None:
                    board.push(chess.Move.from_uci("e1c1"))
                    p.moveTo(myDict['e1'][0], myDict['e1'][1])
                    p.mouseDown(button='left')
                    p.moveTo(myDict['c1'][0], myDict['c1'][1])
                    p.mouseUp()

                    #clicking on the console
                    p.moveTo(1506, 836)
                    p.mouseDown(button='left')
                    p.mouseUp()
                    return 1
    return 0

def promote():
    promote = str(input("Promote to ?"))
    pr = promote[0]
    print(pr)
    move = chess.Move.from_uci(f"{i}{t[-2:]}{pr}")
    if pr == "q":
        coorpr = myDict[t[-2]+"8"]
        print(coorpr)
    if pr == "n":
        coorpr = myDict[t[-2]+"7"]
    if pr == "r":
        coorpr = myDict[t[-2]+"6"]
    if pr == "b":
        coorpr = myDict[t[-2]+"5"]
    return move, coorpr

r = sr.Recognizer()
engine = pyttsx3.init()

newVoiceRate = 23
engine.setProperty('rate',newVoiceRate)

width = f.getDimensions()[0]
width = int(width/2)
height = f.getDimensions()[1]
currentPos = f.getFen(width, height)
# print(currentPos)
myDict = getAllCoordinates("ss.png")

if myDict == None:
    exit()

a = chess.Board(currentPos)

pieceExtractDict = {
    "P": 0, 
    "N": 1,
    "B": 2,
    "Q": 3,
    "K": 4,
    "R": 5,
    "p": 6,
    "n": 7,
    "b": 8,
    "q": 9,
    "k": 10,
    "r": 11
}

color = str(input("What color r u playing? (w/b) "))

# s = "rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR w KQkq - 0 1"
#Initial Print
if color == "b":
    flip(a)
else:
    print(a, end = "\n")

coorpr = 0
while True:
        termination(a, "white")
        termination(a, "black")
        t = str(input("\nEnter move= "))
        # t = getMoveByVoice(engine, r, color)
        if len(t) <=1:
            print('Invalid Move1')
            continue

        castle1 = castle(a, t, myDict)
        
        if castle1 == 0:
            # t = getMoveByVoice(engine, r, color)
            # as knight is a special case (knight and night) for voiec input
            if t[:2] == "kn":
                t = "n" + t[2:]
            t = transformText(t, color)
            p_c = t[:1]

            try:
                ls = g.getPos(currentPos)[pieceExtractDict[p_c]]
                # print(ls)
            except:
                print("Invalid Move2")
                continue

            c = 0

            # try:
            for i in ls:

                # moving the pieces
                l = list(pieceExtractDict.keys())

                if p_c in l[:6]:
                    a.turn = chess.WHITE
                elif p_c in l[6:]:
                    a.turn = chess.BLACK
                else:
                    print("Invalid Move3")
                    continue
                
                if t[-1] == "8" and t[0] == "p":
                    coorpr = promote()
                    move = coorpr[0]
                else:
                    move = chess.Move.from_uci(f"{i}{t[-2:]}")

                # print(move in a.legal_moves)
                # print(a.legal_moves)
                if move in a.legal_moves:
                    c=1
                    a.push(move)
                    # print(i, t[1:])
                    p.moveTo(myDict[i][0], myDict[i][1])
                    p.mouseDown(button='left')
                    p.moveTo(myDict[t[1:]][0], myDict[t[1:]][1])
                    p.mouseUp()


                    if t[-1] == "8" and t[0] == "p":
                        p.moveTo(coorpr[1][0], coorpr[1][1])
                        p.mouseDown(button='left')
                        # print(myDict[t[1:]][0], " ", myDict[t[1:]][1])
                        p.mouseUp()

                    #clicking on the console
                    p.moveTo(1506, 836)
                    p.mouseDown(button='left')
                    p.mouseUp()
                    currentPos = str(a.fen())
                    engine.say("Done")
                    engine.runAndWait()

                    if t[-1] == "8":
                        break
                else:
                    continue
            # except Exception as e:
            #     print(e)
            #     continue
            #     else:
            #         continue
            if c == 0:
                print("Invalid Move5")
                continue
                
        # # later board print
        # if color == "b":
        #     flip(a)
        # else:
        #     print(a, end = "\n")
            


        # current position set to previous position
        while True:
            prevPos = currentPos
            currentPos = f.getFen(width, height)
            c = g.getMove(prevPos, currentPos)
            # print(c)
            if c!=None:
                if color != "w":
                    flip(chess.Board(currentPos))
                else:
                    print(chess.Board(currentPos), end = "\n")
                print(c)
                engine.say(c)
                engine.runAndWait()
                break
            else:
                print("Waiting for Opponent's Move")
    # except:
    #     engine.say("Please say again")
    #     engine.runAndWait()
