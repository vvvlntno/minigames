# Author-Github: vvvlntno
# Date: 03.11.2022

import re
import random

class Board:
    def __init__(self, values: list=["-","-","-","-","-","-","-","-","-"],winner: str="") -> None:
        self.a1 = values[0]
        self.a2 = values[1]
        self.a3 = values[2]
        self.b1 = values[3]
        self.b2 = values[4]
        self.b3 = values[5]
        self.c1 = values[6]
        self.c2 = values[7]
        self.c3 = values[8]
        self.values = [self.a1,self.a2,self.a3,self.b1,self.b2,self.b3,self.c1,self.c2,self.c3]
        self.winner = winner


    def renewvaluelist(self):
        self.values = [self.a1,self.a2,self.a3,self.b1,self.b2,self.b3,self.c1,self.c2,self.c3]


    def checkforend(self) -> bool:
        for val in self.values:
            if val == "-":
                return False
        return True


    def checkforwin(self, var: str) -> bool:
        if (self.a1 == var and self.a2 == var and self.a3 == var) or (self.b1 == var and self.b2 == var and self.b3 == var) or (self.c1 == var and self.c2 == var and self.c3 == var) or (self.a1 == var and self.b1 == var and self.c1 == var) or (self.a2 == var and self.b2 == var and self.c2 == var) or (self.a3 == var and self.b3 == var and self.c3 == var) or (self.a1 == var and self.b2 == var and self.c3 == var) or (self.a3 == var and self.b2 == var and self.c1 == var):
            self.winner = var
            return True
        return False


    def __checkinputforvalidation(self, inp: str) -> bool:
        if (re.match(r"([a-c][1-3])", inp) and len(inp)==2):
            return True #matches the length and regex
        return False #does not match the regex and length


    def __checkinputforfieldusage(self, inp: str) -> bool:
        if (getattr(self, inp) == "X" or getattr(self, inp) == "O"): #get value of value of inp
            return False #is already in use
        return True #can be used


    def checkinputandsetvalue(self, userinp: str, turn: str) -> list:
        if not self.__checkinputforvalidation(userinp):
            return [False, "Please give a validate input (a-c1-3)"]
        if not self.__checkinputforfieldusage(userinp):
            return [False, "Please input a field that is not used"]
        self.setvalue(userinp, turn) #set value
        return [True, ""]


    def __checkifvarisavailable(self, var):
        if (var=="X" or var=="O"):
            return False
        return True

    def createlistofvalidelements(self):
        validoptions = []
        if(self.__checkifvarisavailable(self.a1)):
            validoptions.append("a1")
        if(self.__checkifvarisavailable(self.a2)):
            validoptions.append("a2")
        if(self.__checkifvarisavailable(self.a3)):
            validoptions.append("a3")
        if(self.__checkifvarisavailable(self.b1)):
            validoptions.append("b1")
        if(self.__checkifvarisavailable(self.b2)):
            validoptions.append("b2")
        if(self.__checkifvarisavailable(self.b3)):
            validoptions.append("b3")
        if(self.__checkifvarisavailable(self.c1)):
            validoptions.append("c1")
        if(self.__checkifvarisavailable(self.c2)):
            validoptions.append("c2")
        if(self.__checkifvarisavailable(self.c3)):
            validoptions.append("c3")
        return validoptions
    

    def setvalue(self, inp: str, turn: str):
        setattr(self,inp,turn)


    def printgameboard(self):
        print("    a   b   c")
        print(f"            ")
        print(f"1   {self.a1} | {self.b1} | {self.c1} ")
        print("   ---|---|---")
        print(f"2   {self.a2} | {self.b2} | {self.c2} ")
        print("   ---|---|---")
        print(f"3   {self.a3} | {self.b3} | {self.c3} ")


    def printwinner(self):
        print(f"{self.winner} Won, well played")

    
    def _flushdata(self):
        self.a1 = "-"
        self.a2 = "-"
        self.a3 = "-"
        self.b1 = "-"
        self.b2 = "-"
        self.b3 = "-"
        self.c1 = "-"
        self.c2 = "-"
        self.c3 = "-"
        self.values = [self.a1,self.a2,self.a3,self.b1,self.b2,self.b3,self.c1,self.c2,self.c3]
        self.winner = ""


class Bot:
    def __init__(self, indicator) -> None:
        self.indicator = indicator
    
    def getrandomchoice(self,validoptions: list) -> list:
        return random.choice(validoptions)


#bot: list of valid options (a1,a2,a3,...)
#create valid list
# for val in values if value does not have "x" or "o" then add to list

#bot class, init with indicator "x" or "o"
#give list of elements and return option

def inputsequence(turn: str, bf: Board):
    bf.printgameboard()
    userinput = input(f"\n{turn}: Where do you want to place it?")
    validated = bf.checkinputandsetvalue(userinput, turn)
    while not validated[0]:
        print(f"\n{turn}: {validated[1]}")
        userinput = input(f"{turn}: Where do you want to place it?")
        validated = bf.checkinputandsetvalue(userinput, turn)


def botsequence(turn: str, bf: Board, bt: Bot):
    botchoice = bt.getrandomchoice(bf.createlistofvalidelements())
    bf.setvalue(botchoice, turn)
    bf.printgameboard()


def gamesequence():
    B = Board()
    loop = B.checkforend()
    while not loop:
        B.renewvaluelist()
        inputsequence("X", B)
        if (B.checkforwin("X")):
            loop = True
            break

        inputsequence("O", B)
        loop = B.checkforend()
        if (B.checkforwin("O")):
            loop = True
            break
    B.printgameboard()
    B.printwinner()


def botgamesequence():
    B = Board()
    loop = B.checkforend()
    BT = Bot("O")
    while not loop:
        B.renewvaluelist()
        inputsequence("X", B)
        if (B.checkforwin("X")):
            loop = True
            break
        
        botsequence(BT.indicator, B, BT)
        loop = B.checkforend()
        if (B.checkforwin("O")):
            loop = True
            break
    B.printgameboard()
    B.printwinner()

def main():
    inp = input("Please type if you want to play with a bot (b) or with a friend (n): ")
    if(inp=="n"):
        gamesequence()
    elif(inp=="b"):
        botgamesequence()
    else:
        print("Please restart and Input 'n' or 'b'")

if __name__=="__main__":
    main()



#test
# B = Board()
# B.printgameboard()
# B.setvalue("a1", "X")

# rrlist = B.createlistofvalidelements()
# print(rrlist)
# Bot1 = Bot("O")
# botchoice = Bot1.getrandomchoice(rrlist)

# B.setvalue(botchoice, Bot1.indicator)

# B.printgameboard()

