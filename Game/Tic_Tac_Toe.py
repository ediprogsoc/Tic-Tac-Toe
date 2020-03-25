#!/usr/bin/env python
# coding: utf-8

# In[3]:

# Let human player = -1 and machine player = 1


import sys

class Color:
    BOLD = "\033[1m"
    RED = "\033[31m"
    BLUE = "\033[34m"
    END = "\033[0m"

    
class Board:
    def __init__(self,board,gameType):
        self.board=board
        self.gameType = gameType
        
    def check_win(self, b, player = 0):
        lines = list(map("".join,b + list(map(list,zip(*b))) + list(map("".join,list(zip(*[[b[i][i],b[i][2-i]] for i in range(3)]))))))
        for line in lines:
            if player == 0 and (line == 'XXX' or line == 'OOO'):
                return True
            elif player == 1 and line == "OOO":
                return True
            elif player == -1 and line == "XXX":
                return True
        return False
            
    def nextMoves(self,b,player):
        possibleMoves = []
        token = 'O' if player == 1 else 'X'
        for row_idx in range(3):
            for cell_idx in range(3):
                if b[row_idx][cell_idx] == " ":
                    b_copy = [i[:] for i in b[:]]
                    b_copy[row_idx][cell_idx] = token
                    possibleMoves.append(b_copy)
        return possibleMoves


    def eval(self,b):
        if self.check_win(b,1):
            return 1
        elif self.check_win(b,-1):
            return -1
        else: return 0

    def terminal(self,b):
        return (self.check_win(b) or self.boardFull(b))

    
    def pr(self):
        X = Color.RED+"X"+Color.END
        O = Color.BLUE+"O"+Color.END
        sys.stdout.write("    1   2   3")
        sys.stdout.write("\n")
        sys.stdout.write("   " + " -  "*3)
        sys.stdout.flush()
        for row_idx in range(len(self.board)):
            sys.stdout.write("\n")
            sys.stdout.write(str(row_idx+1) + " | ")
            sys.stdout.flush()
            for item in self.board[row_idx]:
                if item=="X":
                    sys.stdout.write(X+" | ")
                    sys.stdout.flush()
                elif item=="O":
                    sys.stdout.write(O+" | ")
                    sys.stdout.flush()
                else:
                    sys.stdout.write(item+" | ")
                    sys.stdout.flush()
            sys.stdout.write("\n")
            sys.stdout.write("   " + " -  "*3)
            sys.stdout.flush()
    
    def placeX(self, ind1, ind2):
        self.board[ind1-1][ind2-1]="X"
   
    def placeO(self, ind1, ind2):
        self.board[ind1-1][ind2-1]="O"

    def boardFull(self,b):
        for row in b:
            for item in row:
                if item == " ":
                    return False
        return True

    def isEmpty(self, ind1, ind2):
        try:
            if self.board[ind1-1][ind2-1]=="X" or self.board[ind1-1][ind2-1]=="O":
                return False
            else:
                return True
        except IndexError:
            pass

    def minimax(self,b,player):
        if self.terminal(b):
            return self.eval(b)
        elif player == 1:
            return max(list(map(lambda x : self.minimax(x,-1),self.nextMoves(b,player))))
        else:
            return min(list(map(lambda x : self.minimax(x,1),self.nextMoves(b,player))))

    def alphabeta(self,b,player):
        return self.ab(b,player,-2,2)

    def ab(self,b,player,alpha,beta):
        if self.terminal(b):
            return self.eval(b)
        elif player == 1:
            return self.max_value(self.nextMoves(b,player),alpha,beta,-2)
        else:
            return self.min_value(self.nextMoves(b,player),alpha,beta,2)

    def max_value(self,moves,alpha,beta,v):
        if len(moves) == 0:
            return v
        newV = max(v,self.ab(moves[0],-1,alpha,beta))
        if newV >= beta:
            return newV
        else:
            return self.max_value(moves[1:],max(alpha,newV),beta,newV)

    def min_value(self,moves,alpha,beta,v):
        if len(moves) == 0:
            return v
        newV = min(v,self.ab(moves[0],1,alpha,beta))
        if newV <= alpha:
            return newV
        else:
            return self.min_value(moves[1:],alpha,min(beta,newV),newV)
                   
    def game(self):
        g = 'AI' if self.gameType == 1 else 'MULTIPLAYER'
        print(Color.BOLD+"-- " + g + " --"+Color.END+"\n")
        print("Press 0 to quit")
        move = 0
        self.pr()
        while move < 9:
            player = str(move%2 + 1)
            token = '(X)' if player == '1' else '(O)'
            try:
                print("\n \n"+Color.BOLD+"Player " + player + "'s Turn " + token +Color.END)
                if g == 'AI' and player == '2':
                    self.board = max(zip(list(map(lambda b : self.alphabeta(b,-1),self.nextMoves(self.board,1))),self.nextMoves(self.board,1)))[1]
                    move += 1
                             
                else:
                    ind1 = int(input("Row you want to change: "))
                    if ind1 == 0:
                        sys.exit("Successfully Quit!")
                    ind2 = int(input("Column you want to change: "))
                    if ind2 == 0:
                        sys.exit("Successfully Quit!")
                    check = self.isEmpty(ind1,ind2)
                    if (ind1<=3 and ind1>0) and (ind2<=3 and ind2>0) and check:
                        if player == '1':
                            self.placeX(ind1,ind2)
                        else:
                            self.placeO(ind1,ind2)
                        move += 1
                    else:
                        raise ValueError()
            except ValueError:
                print("Error - invalid input.")
                pass

            self.pr()
            result = self.check_win(self.board)
            if result:
                print("\n \n"+Color.BOLD+"Player " + player + " Wins!"+Color.END)
                break
            elif move==9:
                print("\n \n"+Color.BOLD+"Draw!"+Color.END)    


brd = [[" "]*3 for i in range(3)]

def main():
    print("\n\n" + Color.BOLD+"-- WELCOME TO TIC-TAC-TOE! --"+Color.END+"\n")
    print(Color.BOLD+"-- 1. SINGLE PLAYER (AI)"+Color.END+"\n")
    print(Color.BOLD+"-- 2. MULTIPLAYER (2 PERSON)"+Color.END+"\n")
    option = int(input())
    try:
        if 0 < option and option < 3:
            b = Board(brd,option)
            b.game()
        else:
            raise ValueError()
    except ValueError:
        print("Error - invalid input.")
        main()

main()

# In[ ]:


