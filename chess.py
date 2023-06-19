#this is shit don't you judge
#at least my code isn't spaghetti :)
class Plateau:
    def __init__(self) -> None:
        board=[['♜','♞','♝','♛','♚','♝','♞','♜'],
               ['♟','♟','♟','♟','♟','♟','♟','♟'],
               [' ',' ',' ',' ',' ',' ',' ',' ',],
               [' ',' ',' ',' ',' ',' ',' ',' ',],
               [' ',' ',' ',' ',' ',' ',' ',' ',],
               [' ',' ',' ',' ',' ',' ',' ',' ',],
               ['♙','♙','♙','♙','♙','♙','♙','♙'],
               ['♖','♘','♗','♕','♔','♗','♘','♖']
               ]

class Piece(Plateau):
    def __init__(self):
        self.position = []
        self.color = ' '
        self.stamp=' '


    def move(self,pos):
        self.position=pos

class Pion(Piece):
    def __init__(self,color,x,y):
        self.basepos=[x,y]
        self.position=self.basepos
        if color == 'black': self.stamp = '♟' 
        else: self.stamp = '♙'
        self.color = color
    def chckifmove(self,pos):
        possiblemoves=[[self.position[0],self.position[1]+self.color]]
        
