class TicTacToe:
    def __init__(self,pick,sz=3):
        self.pick = pick
        self.dim_sz = sz
        self.board = self.ClearBoard()

    def ClearBoard(self):
        board = [['blur' for i in range(self.dim_sz)] for j in range(self.dim_sz)]
        # made a 3x3 by-default board
        return board
    
    def MoveRecord(self,r,c):
        if r > self.dim_sz or c > self.dim_sz:
            return "Out of Bounds"
        if self.board[r][c] != 'blur':
            return "Spot Pre-Occupied"
        self.board[r][c] = self.pick
        return True 
    
    def CheckWin(self):# 1 you won, 0 computer won, -1 tie

        #Flag syntax -> first player no. , User is Player#1 ; Check set 1 -> row and '\' diagonal & Check set 2 -> col and '/' diagonal


        for i in range(0,self.dim_sz):#Rows
            flag11 = True
            flag21 = True

            flag12 = True
            flag22 = True 
            for j in range(0,self.dim_sz):

                ch1 = self.board[i][j]
                ch2 = self.board[j][i]
                                       #Row
                if ch1 == self.pick:# if it's mine, computer didn't make it
                    flag21 = False
                elif ch1 == 'blur':#if it's blank no one made it
                    flag11 = False
                    flag21 = False
                else: flag11 = False# else i didn't make it 

                if ch2 == self.pick:#Same but for Col
                    flag22 = False
                elif ch2 == 'blur':
                    flag12 = False
                    flag22 = False
                else: flag12 = False

            if flag11 or flag12:# I won
                return 1
            if flag21 or flag22:#Computer Won
                return 0

        #Diagonals#
        flag11 = True
        flag21 = True

        flag12 = True
        flag22 = True 
        for i in range(0,self.dim_sz):

            ch1 = self.board[i][i]
            ch2 = self.board[i][self.dim_sz-1-i]

            if ch1 == self.pick:
                flag21 = False
            elif ch1 == 'blur':
                flag11 = False
                flag21 = False
            else:flag11 = False

            if ch2 == self.pick:
                flag22 = False
            elif ch2 == 'blur':
                flag12 = False
                flag22 = False
            else:flag12 = False

        if flag11 or flag12:
            return 1
        if flag21 or flag22:
            return 0

        return -1
    

    def NextMove(self):
        AvailableMoves = []# will carry all available moves
        PlayerWinSpot = []#if player (user Wins)
        CompPick = 'O'
        if self.pick == 'O':
            CompPick = 'X'
        for i in range(0,self.dim_sz):
            for j in range(0,self.dim_sz):
                if self.board[i][j] == 'blur':#BLANK
                    AvailableMoves.append( tuple(i,j) )#add it to available moves
                    self.board[i][j] = CompPick#Check if I (Computer can win)
                    temp = self.CheckWin()
                    if temp ==0:#Best Case I win!
                        return i,j;
                    elif temp == 1: #Second Best Case, he (player) didn't won
                        PlayerWinSpot.append( tuple(i,j) )
                    #Tie till now
                    self.board[i][j] = 'blur'
        
        if len(AvailableMoves) == 0:
            return tuple(-1,-1)

        c1 , c2  = self.dim_sz//2,self.dim_sz//2
        if tuple(c1,c2) in AvailableMoves:#CENTER 
            self.board[c1][c2] = CompPick
            return c1,c2
        for i in range(c1-1,-1,-1):#IN TO OUT
            gap = c1 - i
            #checking  - 4 possibilities at max
                                                     #EDGES 
            if  tuple(c1-gap,c2-gap) in AvailableMoves:
                self.board[c1-gap][c2-gap] = CompPick
                return c1-gap,c2-gap
            if  tuple(c1-gap,c2+gap) in AvailableMoves:
                self.board[c1-gap][c2+gap] = CompPick
                return c1-gap,c2+gap
            if  tuple(c1+gap,c2-gap) in AvailableMoves:
                self.board[c1+gap][c2-gap] = CompPick
                return c1+gap,c2-gap
            if  tuple(c1+gap,c2+gap) in AvailableMoves:
                self.board[c1+gap][c2+gap] = CompPick
                return c1+gap,c2+gap

            #Four Lines

            for i in range(0,gap):
                if  tuple(c1-gap,c2-gap+i) in AvailableMoves:#TOP LEFT TO TOP RIGHT
                    self.board[c1-gap][c2-gap+i] = CompPick
                    return c1-gap,c2-gap+i
                if  tuple(c1+gap,c2-gap+i) in AvailableMoves:#BOTTOM LEFT TO BOTTOM RIGHT
                    self.board[c1+gap][c2-gap+i] = CompPick
                    return c1+gap,c2-gap+i
                if  tuple(c1-gap,c2-gap) in AvailableMoves:#LEFT TOP TO LEFT BOTTOM
                    self.board[c1-gap+i][c2-gap] = CompPick
                    return c1-gap+i,c2-gap
                if  tuple(c1-gap+i,c2+gap) in AvailableMoves:#RIGHT TOP TO RIGHT BOTTOM
                    self.board[c1-gap+i][c2+gap] = CompPick
                    return c1-gap+i,c2+gap

if __name__ == "__main__":
    print("Hello!")
                    
        



        

        
