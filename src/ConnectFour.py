#ConnectFour.py

from classes.game import Game
from classes.player import Player
from classes.piece import Piece

from utils.errors import InvalidCoordinate, InvalidPiecePlacement, OutOfBounds
from utils import coord, my_os

#let's just assume all connect four games are this size:
BOARD_WIDTH=7
BOARD_HEIGHT=6
GAME_NAME="Connect Four"

class ConnectFour(Game):

    def __init__(self):
        super().__init__(GAME_NAME, BOARD_WIDTH, BOARD_HEIGHT, x_label=True)

    def setIfWin(self):
        '''Checks for win and adjusts game state if win is found'''
        x, y = self.getPrevMove()
        piece = self.board[y][x]

        count = max(coord.countUpDown(self.board, x, piece),
                    coord.countLeftRight(self.board, y, piece),
                    coord.countTopLeftDiag(self.board, x, y, piece),
                    coord.countBottomLeftDiag(self.board, x, y, piece))

        if count >= 4:
            self.end_game = True
            self.winner = self.getCurrentPlayer()

    def setIfTie(self):
        '''Checks for tie (whether board is full) and adjusts end_game state'''
        for column in range(BOARD_WIDTH):
            if not self.board[BOARD_HEIGHT-1][column]: #found empty, not tie
                return

        self.end_game = True

    def handleTurn(self):
        player = self.getCurrentPlayer()
        print("{}'s turn! ({})".format(player, player.color))
        piece = Piece(player.color)

        ask = "Please select a column to place piece: "
        while True:
            try:
                response = input(ask)
                success, column = coord.parseCol(response)

                if not success:
                    raise InvalidCoordinate
                elif not coord.isValidCoord(column, BOARD_WIDTH):
                    raise OutOfBounds

                #try to place piece, raise exception if failed
                elif not self.placePiece(piece, column):
                    raise InvalidPiecePlacement
                break

            except InvalidCoordinate:
                ask = "Invalid column name. Please enter column number: "
            except OutOfBounds:
                ask = "Out of bounds. Please try again: "
            except InvalidPiecePlacement:
                ask = "Column is full. Please enter a different column: "

        self.render()
        print("{} placed {} into column {}.".format(player, piece, response))

    def initPlayers(self):
        player1 = Player(input("What is first player's name? ").capitalize(), 'X')
        player2 = Player(input("What is second player's name? ").capitalize(), 'O')

        self.setPlayers([player1, player2])

    def placePiece(self, piece, col):
        '''
        Places piece in column

        Args:
            int column
            Piece piece
        Return:
            return False if failed
        '''
        for bottom in range(0, self.board.height):
            if not self.board[bottom][col]:

                self.setPrevState([col, bottom])
                self.board.place(piece, col, bottom)

                return True

        return False

def main():
    game = ConnectFour()
    game.play()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        my_os.goodbye()

    my_os.goodbye()
