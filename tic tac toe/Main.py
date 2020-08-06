row =["-"]*9
import random as r
import time as t
r1=0
I=0
def display():
    print(f"{row[0] } | {row[1] } | { row[2]} ")
    print(f"{row[3] } | { row[4]} | { row[5]} ")
    print(f"{row[6] } | { row[7]} | { row[8]} ") 
display()
def guess():
    while(1):
        try:
            enter = int(input("Your Turn: "))
            if(enter<1 or enter>9):
                print("Enter Value Must Be In Between 1-9")
        except:
            print("Entered option must be integer")
        if(enter>0 and enter<10):
            break
    return enter
comp=[]
me=[]
main=[]
def user():
    g = guess()
    if g not in main:
        me.append(g)
        main.append(g)
        row[g-1] = "O"
        display()
    else:
        user()
   

def CompOption():
        computer = r.randint(1,9)
        if computer not in main:
            comp.append(computer)
            main.append(computer)
            row[computer-1] ="X"
            display()
        else:
            CompOption()
        

    

def mainOne():
  
    while(1):
        if(row[0] == row[1] == row[2] == "O" or row[0] == row[3] == row[6] =="O" or row[2] == row[5] == row[8] =="O" or row[3] == row[4] == row[5] == "O" or row[1] == row[4] == row[7] == "O" or row[8] == row[7] == row[6] =="O" or row[0] == row[4] == row[8] =="O" or row[2]==row[4] == row[6]=="O"):
            print("User win")
            break
        if(row[0] == row[1] == row[2] == "X" or row[0] == row[3] == row[6] =="X" or row[2] == row[5] == row[8] =="X" or row[3] == row[4] == row[5] == "X" or row[1] == row[4] == row[7] == "X" or row[8] == row[7] == row[6] =="X" or row[0] == row[4] == row[8] =="X" or row[2]==row[4] == row[6]=="X"):
            print("Computer win")
            break
        if(len(main)==9):
            break
        print("opponent turn ")
        print("opponent selecting....")
        t.sleep(1)
        CompOption()
       
        if(row[0] == row[1] == row[2] == "O" or row[0] == row[3] == row[6] =="O" or row[2] == row[5] == row[8] =="O" or row[3] == row[4] == row[5] == "O" or row[1] == row[4] == row[7] == "O" or row[8] == row[7] == row[6] =="O" or row[0] == row[4] == row[8] =="O" or row[2]==row[4] == row[6]=="O"):
            print("User win")
            break
        if(row[0] == row[1] == row[2] == "X" or row[0] == row[3] == row[6] =="X" or row[2] == row[5] == row[8] =="X" or row[3] == row[4] == row[5] == "X" or row[1] == row[4] == row[7] == "X" or row[8] == row[7] == row[6] =="X" or row[0] == row[4] == row[8] =="X" or row[2]==row[4] == row[6]=="X"):
            print("Computer win")
            break
        if(len(main)==9):
            break
        user()
        print("---------------------------------------------------------------------------------------")
mainOne()
while(1):
    ins = input("Play Again(Y/N): ")
    if(ins == "Y" or ins=="y"):
        row = ["-"]*9
        comp=[]
        me=[]
        main=[]
        mainOne()
    if(ins == "N" or ins=="n"):
        break
    else:
        print("Enter Valid Option")
    
