import random as r 
import time as t 

def printTTT(board):
    for a in range(len(board)):
        for b in range(len(board[0])):
            if(b<len(board)-1):
                print(f" {board[a][b]} ",end="|")
            else:
                print(f" {board[a][b]} ",end="")
        print()
        if(a<len(board)-1):
            print(" -"*(len(board)+2),)



class Planting:

    def __init__(self):
        self.board = [[" "," "," "],[" "," "," "],[" "," "," "]]
        self.check = []
        for a in range(0,len(self.board)):
            for b in range(0,len(self.board[0])):
                if(self.board[a][b] == " "):
                    self.check.append((a,b))

    def user(self):
        while(1):
            try:
                enter = int(input())
                if(0<=enter<=9):
                    row,col = (enter-1)//3,(enter-1)%3
                    if (row,col) in self.check:
                        break
                    else:
                        2/0
            except:
                print("Enter valid value")
        if (row,col) in self.check:
            self.board[row][col] = "O"
            self.check.remove((row,col))
    
    def computer(self):
        let = r.choice(self.check)
        self.board[let[0]][let[1]] = "X"
        self.check.remove(let)
    
    def checkCase(self):
        k = self.board
        if(k[0][0]==k[1][1]==k[2][2]):
            if(k[0][0]!=" "):
                return (True,k[0][0])
        if(k[2][0]==k[1][1]==k[0][2]):
            if(k[2][0]!=" "):
                return (True,k[2][0])
        for a in range(3):
            if(k[a][0]==k[a][1]==k[a][2]):
                if(k[a][0]!=" "):
                    return (True,k[1][0])
        for a in range(3):
            if(k[0][a]==k[1][a]==k[2][a]):
                if(k[0][a]!=" "):
                    return (True,k[2][1])
        return (False,0)


play =  Planting()
while(play.check):
    print("Selecting...")
    play.computer()
    t.sleep(1)
    print()
    printTTT(play.board)
    save = play.checkCase()
    if(not play.check or save[0]):
        print(f"{save[1]} won")
        break
    play.user()
    t.sleep(1)
    print()
    printTTT(play.board)
    print()
    save = play.checkCase()
    if(save[0]):
        print(f"{save[1]} won")
        break

