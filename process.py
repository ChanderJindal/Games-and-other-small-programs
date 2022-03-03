import random

from matplotlib.pyplot import flag
from numpy import true_divide

class TicTacToe:
    def __init__(self,pick,sz=3):
        self.pick = pick
        self.dim_sz = sz
        self.board = self.ClearBoard()

    def ClearBoard(self):
        board = [['B' for i in range(self.dim_sz)] for j in range(self.dim_sz)]
        # made a 3x3 by-default board
        return board
    
    def MoveRecord(self,r,c):
        if r > self.dim_sz or c > self.dim_sz:
            return "Out of Bounds"
        if self.board[r][c] != 'B':
            return "Spot Pre-Occupied"
        self.board[r][c] = self.pick
    
    def CheckWin(self):# 1 you won, 0 computer won, -1 tie

        for i in range(0,self.dim_sz):#Rows
            flag1 = True
            flag2 = True
            for j in range(0,self.dim_sz):
                ch = self.board[i][j]
                if ch == self.pick:# if it's mine, computer didn't make it
                    flag2 = False
                elif ch == 'B':#if it's blank no one made it
                    flag1 = False
                    flag2 = False
                    break;
                else: flag1 = False# else i didn't make it 
            if flag1 is True:# I won
                return 1
            if flag2 is True:#Computer Won
                return 0
        
        for i in range(0,self.dim_sz):#Col
            flag1 = True
            flag2 = True
            for j in range(0,self.dim_sz):
                ch = self.board[j][i]
                if ch == self.pick:# if it's mine, computer didn't make it
                    flag2 = False
                elif ch == 'B':#if it's blank no one made it
                    flag1 = False
                    flag2 = False
                    break;
                else: flag1 = False# else i didn't make it 
            if flag1 is True:# I won
                return 1
            if flag2 is True:#Computer Won
                return 0

        #Diagonal#1
        flag1 = True
        flag2 = True
        for i in range(0,self.dim_sz):
            ch = self.board[i][i]
            if ch == self.pick:
                flag2 = False
            elif ch == 'B':
                flag1 = False
                flag2 = False
            else:flag1 = False

        if flag1 is True:
            return 1
        if flag2 is True:
            return 0

        #Diagonal#2
        flag1 = True
        flag2 = True   
        for i in range(0,self.dim_sz):
            ch = self.board[i][self.dim_sz-1-i]
            if ch == self.pick:
                flag2 = False
            elif ch == 'B':
                flag1 = False
                flag2 = False
            else:flag1 = False

        if flag1 is True:
            return 1
        if flag2 is True:
            return 0

        return -1
    

    def NextMove(self):
        


        

        
