# Author-Github: vvvlntno
# Date: 20.02.2023
# BLACKPIECELIST = ["♔","♕","♖","♗","♘","♙"]
# WHITEPIECELIST = ["♚","♛","♜","♝","♞","♟"]
ctable = [["","A","B","C","D","E","F","G","H"],[1,"","","","","","",""],[2,"","","","","","",""],[3,"","","","","","",""],[4,"","","","","","",""],[5,"","","","","","",""],[6,"","","","","","",""],[7,"","","","","","",""],[8,"","","","","","",""]]

# Imports

from tabulate import tabulate


# Classes

class Figure:
    def __init__(self, piece: str, x: str, y: int):
        self.piece = piece
        self.x = x
        self.y = y
    
    def changeX(self, x):
        self.x = x
    
    def changeY(self, y):
        self.y = y
    
    def getPiece(self):
        return self.piece
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y


# Functions

def convertLettertoNum(letter: str) -> int:
    if letter == "A":
        return 1
    elif letter == "B":
        return 2
    elif letter == "C":
        return 3
    elif letter == "D":
        return 4
    elif letter == "E":
        return 5
    elif letter == "F":
        return 6
    elif letter == "G":
        return 7
    elif letter == "H":
        return 8
    else:
        return 0

def convertSkintoCommand(skin: int) -> str:
    if skin == 0:
        return "grid"
    elif skin == 1:
        return "fancy_grid"
    elif skin == 2:
        return "rounded_grid"
    elif skin == 3:
        return "double_grid"
    else:
        return "plain"


def createGameboard(table, list):
    table = [["","A","B","C","D","E","F","G","H"],[1,"","","","","","","",""],[2,"","","","","","","",""],[3,"","","","","","","",""],[4,"","","","","","","",""],[5,"","","","","","","",""],[6,"","","","","","","",""],[7,"","","","","","","",""],[8,"","","","","","","",""]]
    for e in list:
        ey = e.getY()
        ex = e.getX()
        ex = convertLettertoNum(ex)
        table[int(ey)][int(ex)] = str(e.getPiece())
    return table


# Constants

BLACKKING =  "♔"
BLACKQUEEN =  "♕"
BLACKROOK =  "♖"
BLACKBISHOP =  "♗"
BLACKKNIGHT =  "♘"
BLACKPAWN =  "♙"

WHITEKING= "♚"
WHITEQUEEN= "♛"
WHITEROOK= "♜"
WHITEBISHOP= "♝"
WHITEKNIGHT= "♞"
WHITEPAWN= "♟"


BLACKY = 8
BLACKPAWNY = 7
WHITEPAWNY = 2
WHITEY = 1
SKIN = 2


# Definitions

BlackrookA = Figure(BLACKROOK, "A", BLACKY)
BlackknightB = Figure(BLACKKNIGHT, "B", BLACKY)
BlackbishopC = Figure(BLACKBISHOP, "C", BLACKY)
BlackqueenD = Figure(BLACKQUEEN, "D", BLACKY)
BlackkingE = Figure(BLACKKING, "E", BLACKY)
BlackbishopF = Figure(BLACKBISHOP, "F", BLACKY)
BlackknightG = Figure(BLACKKNIGHT, "G", BLACKY)
BlackrookH = Figure(BLACKROOK, "H", BLACKY)

BlackpawnA = Figure(BLACKPAWN, "A", BLACKPAWNY)
BlackpawnB = Figure(BLACKPAWN, "B", BLACKPAWNY)
BlackpawnC = Figure(BLACKPAWN, "C", BLACKPAWNY)
BlackpawnD = Figure(BLACKPAWN, "D", BLACKPAWNY)
BlackpawnE = Figure(BLACKPAWN, "E", BLACKPAWNY)
BlackpawnF = Figure(BLACKPAWN, "F", BLACKPAWNY)
BlackpawnG = Figure(BLACKPAWN, "G", BLACKPAWNY)
BlackpawnH = Figure(BLACKPAWN, "H", BLACKPAWNY)


WhiterookA = Figure(WHITEROOK, "A", WHITEY)
WhiteknightB = Figure(WHITEKNIGHT, "B", WHITEY)
WhitebishopC = Figure(WHITEBISHOP, "C", WHITEY)
WhitequeenD = Figure(WHITEQUEEN, "D", WHITEY)
WhitekingE = Figure(WHITEKING, "E", WHITEY)
WhitebishopF = Figure(WHITEBISHOP, "F", WHITEY)
WhiteknightG = Figure(WHITEKNIGHT, "G", WHITEY)
WhiterookH = Figure(WHITEROOK, "H", WHITEY)

WhitepawnA = Figure(WHITEPAWN, "A", WHITEPAWNY)
WhitepawnB = Figure(WHITEPAWN, "B", WHITEPAWNY)
WhitepawnC = Figure(WHITEPAWN, "C", WHITEPAWNY)
WhitepawnD = Figure(WHITEPAWN, "D", WHITEPAWNY)
WhitepawnE = Figure(WHITEPAWN, "E", WHITEPAWNY)
WhitepawnF = Figure(WHITEPAWN, "F", WHITEPAWNY)
WhitepawnG = Figure(WHITEPAWN, "G", WHITEPAWNY)
WhitepawnH = Figure(WHITEPAWN, "H", WHITEPAWNY)

FIGLIST = [BlackrookA, BlackknightB, BlackbishopC, BlackqueenD, BlackkingE, BlackbishopF, BlackknightG, BlackbishopF, BlackrookH, BlackpawnA, BlackpawnB, BlackpawnC, BlackpawnD, BlackpawnE, BlackpawnF, BlackpawnG, BlackpawnH, WhiterookA, WhiteknightB, WhitebishopC, WhitequeenD, WhitekingE, WhitebishopF, WhiteknightG, WhiterookH, WhitepawnA, WhitepawnB, WhitepawnC, WhitepawnD, WhitepawnE, WhitepawnF, WhitepawnG, WhitepawnH]



table = createGameboard(ctable, FIGLIST)


print(tabulate(table, tablefmt=convertSkintoCommand(SKIN), headers="firstrow"))