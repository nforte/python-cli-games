#ConnectFour.py
from games.classes.board import Board
from games.classes.piece import Piece

class ConnectFour:

    def __init__(self, player1, player2):
        #temp values for objects not yet defined
        self.board = Board(7,6) #temp
        self.player1 = player1
        self.player2 = player2

    def render(self):
        self.board.display(True)

    def winCheck(self):
        '''
        Check for win

        Returns:
            Boolean: whether placed piece causes the player to win
        '''
        return False

    def place(self, piece, col):
        '''
        Places piece in column

        Args:
            string column
            Piece piece
        Return:
            return False if failed
        '''
        col_num = int(col) - 1 #user input by column name, so starts at 1 not 0

        for bottom in range(0, self.board.height):
            if not self.board.board[bottom][col_num]:
                self.board.place(piece, col_num, bottom)
                return True
        return False

    def play(self):
        print('Starting ConnectFour')
        self.render()


def main(player1, player2):
    game = ConnectFour(player1, player2)
    game.play()
