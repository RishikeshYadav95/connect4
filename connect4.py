'''
Created on April 27th 2022
@author: Rishikesh Yadav
'''

class Board(object):
    '''Connect Four: a variation of tic-tac-toe played on a rectangular board.'''

    # The constructor is always named __init__.
    def __init__(self, width = 7, height = 6):
        '''The constructor for objects of type Board.'''
        self.width = width
        self.height = height
        self.board = [['' for _ in range(self.width)] for _ in range(self.height)]

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Board that calls it (named self).'''
        string = ''
        for i in range(self.height):
            for j in range(self.width):
                if self.board[self.height -(i+1)][j] != '':
                    string = string + '|' + self.board[self.height -(i+1)][j]
                else:
                    string = string + '| '
            string = string + '|\n'
        string = string + '-'
        for i in range(self.width):
            string = string + '--'
        string = string + '\n'
        for i in range(self.width):
            string = string + ' ' + str(i)
        string = string + '\n'

        return string
        
    def __repr__(self):
        '''This method also returns a string representation for the object.'''
        return self.__str__()
    
    # Board methods
    def allowsMove(self, col):
        '''This method return True if the calling Board object can allow a move into column
        c (because there is space available). It returns False if c does not have space
        available or if it is not a valid column.'''
        if col < 0 or col >= self.width:
            return False
        else:
            for i in range(self.height):
                if self.board[i][col] == '':
                    return True
            return False

    def addMove(self, col, ox):
        '''This method adds an ox checker, where ox is a variable holding a string that is either
        "X" or "O", into column col.'''
        if self.allowsMove(col):
            for i in range(self.height):
                if self.board[i][col] == '':
                    self.board[i][col] = ox
                    break
        return
    
    def setBoard( self, moveString ):
        '''This method helps to test the Connect4 Board class.'''
        nextCh = 'X' # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X':
                nextCh = 'O'
            else:
                nextCh = 'X'
        return

    def delMove(self,col):
        '''This method removes the top checker from the column col.'''
        if col >= 0 and col < self.width:
            if self.board[self.height-1][col] != '':
                self.board[self.height-1][col] = ''
                return
            for i in range(self.height):
                if self.board[i][col] == '':
                    if i > 0:
                        self.board[i-1][col] = ''
                        return
                    elif i == 0:
                        return
                    
    def winsFor(self, ox):
        '''This method returns True if the given checker, 'X' or 'O', held in ox, has won the
        calling Board or else returns False.'''
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == ox:
                    c1 = self.checkHorizontal(i, j, ox)
                    c2 = self.checkVertical(i, j, ox)
                    c3 = self.checkLeftDiag(i, j, ox)
                    c4 = self.checkRightDiag(i, j, ox)
                    if c1 >= 4 or c2 >= 4 or c3 >= 4 or c4 >= 4:
                        return True
        return False

    def hostGame( self ):
        '''This method when called from a connect four board object, will run a loop
        allowing the user(s) to play a game.'''
        print("Lets Go!")
        print()
        nextCh = 'X'
        while True:
            print(self)
            ch = int(input(nextCh + "'s choice: "))
            if ch < 0 or ch >= self.width:
                print ("Invalid move!...Try again")
                continue
            self.addMove(ch, nextCh)
            if self.winsFor(nextCh):
                print()
                print(nextCh + " wins -- Congratulations!")
                print()
                print(self)
                return
            if nextCh == 'X':
                nextCh = 'O'
            else:
                nextCh = 'X'

    #Helper methods for winsFor method            
    def checkHorizontal(self, i, j, ox):
        '''This method checks that for the given checker ox, do we have 4 matching checkers in a
        horizontal row starting from position with coordinates (i,j)'''
        count = 0
        for h in range(j, self.width):
            if self.board[i][h] == ox:
                count += 1
            else:
                return count
        return count

    def checkVertical(self, i, j, ox):
        '''This method checks that for the given checker ox, do we have 4 matching checkers in a
        vertical column starting from position with coordinates (i,j)'''
        count = 0
        for v in range(i, self.height):
            if self.board[v][j] == ox:
                count += 1
            else:
                return count
        return count

    def checkLeftDiag(self, i, j, ox):
        '''This method checks that for the given checker ox, do we have 4 matching checkers
        diagonally on the left starting from position with coordinates (i,j)'''
        count = 0
        while i < self.height and j >= 0:
            if self.board[i][j] == ox:
                count += 1
                i += 1
                j -= 1
            else:
                return count
        return count

    def checkRightDiag(self, i, j, ox):
        '''This method checks that for the given checker ox, do we have 4 matching checkers
        diagonally on the right starting from position with coordinates (i,j)'''
        count = 0
        while i < self.height and j < self.width:
            if self.board[i][j] == ox:
                count += 1
                i += 1
                j += 1
            else:
                return count
        return count

# Start the game
while(True):
    print("Welcome to Connect 4!")
    print()
    try:
        h = int(input("Enter the desired board height (Default 6):"))
    except ValueError:
        h = 6
    try:
        w = int(input("Enter the desired board width (Default 7):"))
    except ValueError:
        w = 7
    if w < 1:
        w = 7
    if h < 1:
        h = 6
    b = Board( w, h )
    b.hostGame()
    i = input("Play again? (y/n):")
    if i == 'y':
        print()
        continue
    else:
        break
