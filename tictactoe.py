import re

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
        setattr(self,userinp,turn) #set value
        return [True, ""]

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

def inputsequence(turn: str, bf: Board):
    bf.printgameboard()
    userinput = input(f"\n{turn}: Where do you want to place it?")
    validated = bf.checkinputandsetvalue(userinput, turn)
    while not validated[0]:
        print(f"\n{turn}: {validated[1]}")
        userinput = input(f"{turn}: Where do you want to place it?")
        validated = bf.checkinputandsetvalue(userinput, turn)

def gamesquence():
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

def main():
    gamesquence()

if __name__=="__main__":
    main()
