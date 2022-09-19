#ConnectFour.py

from .components.Board import Board
from .components.Piece import Piece

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

    def place(self, column, piece):
        '''
        Places piece in column

        Args:
            int column
            int piece
        Return:
            return False if failed
        '''



    def play(self):
        print('Starting ConnectFour')
        self.render()



def main(player1, player2):
    game = ConnectFour(player1, player2)
    game.play()

if __name__ == '__main__':
    #player1 = input("What is first player's name? ")
    #player2 = input("What is second player's name? ")

    main('Player 1', 'Player 2')
