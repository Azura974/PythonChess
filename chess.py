#this is shit don't you judge
#at least my code isn't spaghetti :)

#black pieces are on the bottom side in the test thingies. Gonna change that when I'll implement the view x)

"""
board=[['♜','♞','♝','♛','♚','♝','♞','♜'],
        ['♟','♟','♟','♟','♟','♟','♟','♟'],
        [' ',' ',' ',' ',' ',' ',' ',' ',],
        [' ',' ',' ',' ',' ',' ',' ',' ',],
        [' ',' ',' ',' ',' ',' ',' ',' ',],
        [' ',' ',' ',' ',' ',' ',' ',' ',],
        ['♙','♙','♙','♙','♙','♙','♙','♙'],
        ['♖','♘','♗','♕','♔','♗','♘','♖']]
"""

NONESTAMP = " "


class Board():
    def __init__(self) -> None:
        board = [[None for _ in range(8)] for _ in range(8)]

class Piece():
    def __init__(self,color):
        self.position = [0,0] #Actual position
        self.color = color #Black or white.
        self.stamp= None #Stamps = what is printed
        self.type = None #King, Pawn and Knight = type 1 : move only on specific spaces. Others = type 2 : move on rows/columns/diagonals.
    

# King · Queen · Rook · Bishop · Knight · Pawn 
class King(Piece): #king. well the test is shit but that "getpossiblemoves" function is working in any cases at least
    def __init__(self,color:str):
        Piece.__init__(self,color)
        if self.color == 'black': self.stamp = '♔' 
        else: self.stamp = '♚'
        self.type = 1
    
    def getpossiblemoves(self) -> list: 
        """
        Returns a list of all possible moves depending on the current position. Other pieces position does NOT count.
        """
        x,y = self.position
        possiblemoves = [[x+1, y],
                              [x-1 if x != 0 else 8, y],
                              [x, y+1],
                              [x, y-1 if y != 0 else 8],
                              [x+1, y+1],
                              [x+1, y-1 if y != 0 else 8],
                              [x-1 if x != 0 else 8, y+1],
                              [x-1 if x != 0 else 8, y-1 if y != 0 else 8]]
        return possiblemoves
    """def test(self):      #Test of self.getpossiblemoves()
        testboardmodel = [[NONESTAMP for _ in range(5)] for _ in range(5)]
        positions_tests = [[2,0]]
        for pos in positions_tests:
            bm = testboardmodel
            bm[self.position[0]][self.position[1]] = NONESTAMP
            self.position = pos
            print(self.position)
            bm[self.position[0]][self.position[1]] = self.stamp
            pmoves = self.getpossiblemoves()
            for move in pmoves:
                try:
                    bm[move[0]][move[1]] = "•"
                except IndexError:
                    continue
            for line in bm: print(line)
            print("-------")"""

"""
class Queen(Piece):
    def __init__(self):
        Piece.__init__(self)
        if self.color == 'black': self.stamp = '' 
        else: self.stamp = ''
        self.type = 2
    def getpossiblemoves(self):
        x,y = self.position
        possiblemoves = []

class Rook(Piece):
    def __init__(self):
        Piece.__init__(self)
        if self.color == 'black': self.stamp = '' 
        else: self.stamp = ''
        self.type = 2
    def getpossiblemoves(self):
        x,y = self.position
        possiblemoves = []

class Bishop(Piece):
    def __init__(self):
        Piece.__init__(self)
        if self.color == 'black': self.stamp = '' 
        else: self.stamp = ''
        self.type = 2
    def getpossiblemoves(self):
        x,y = self.position
        possiblemoves = []
"""
class Pawn(Piece):
    def __init__(self,color:str):
        Piece.__init__(self,color)
        if self.color == 'black': self.stamp = '♙' 
        else: self.stamp = '♟'
        self.type = 1
    def getpossiblemoves(self):
        x,y = self.position
        possiblemoves = [[x+1,y] if self.color == 'white' else [x-1,y]]
        return possiblemoves
    
    """def test(self):      #Test of self.getpossiblemoves()
        testboardmodel = [[NONESTAMP for _ in range(5)] for _ in range(5)]
        positions_tests = [[2,0]]
        for pos in positions_tests:
            bm = testboardmodel
            bm[self.position[0]][self.position[1]] = NONESTAMP
            self.position = pos
            print(self.position, self.color)
            bm[self.position[0]][self.position[1]] = self.stamp
            pmoves = self.getpossiblemoves()
            for move in pmoves:
                try:
                    bm[move[0]][move[1]] = "•"
                except IndexError:
                    continue
            for line in bm: print(line)
            print("-------")"""
"""
class Knight(Piece):
    def __init__(self):
        Piece.__init__(self)
        if self.color == 'black': self.stamp = '' 
        else: self.stamp = ''
        self.type = 1
    def getpossiblemoves(self):
        x,y = self.position
        possiblemoves = []

"""