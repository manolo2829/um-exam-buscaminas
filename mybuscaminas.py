
class Buscaminas: 
    def __init__(self, ancho, alto, bombas):
        self.ancho = ancho
        self.alto = alto
        self.bombas = bombas
        self.board = []
        self.show = []

    def test(self):
        flags = 0
        for row in range(self.ancho):
            for column in range(self.alto):
                
                if(self.board[row][column] == 'B' and self.show[row][column] == 'F'):
                    flags = flags+1
        if(flags == self.bombas):
            return True
        else:
            return False
        
    def question(self, movs):
        mov = input()
        row = input()
        col = input()

        if not mov in movs:
           raise ValueError("Error")

        row = int(row)
        col = int(col)

        return mov, row, col
    

    def play(self, mov, row, col):
        self.show[row][col] = 'F' if mov == 'flag' else self.board[row][col]


    def win(self):
        return self.test()
        
    def lose(self):
        return not self.test()

