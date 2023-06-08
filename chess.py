class Plateau:
    def __init__(self) -> None:
        pass

class Piece(Plateau):
    def __init__(self):
        self.position = []
        self.color = 0
        self.form=''


    def move(self,pos):
        self.position=pos

class Pion(Piece):
    def __init__(self,color,x,y):
        self.basepos=[x,y]
        self.position=self.basepos
        if color == 1: self.form = '' 
        else: self.form = ''
        self.color = color
    def chckifmove(self,pos):
        possiblemoves=[[self.position[0],self.position[1]+self.color]]
        
