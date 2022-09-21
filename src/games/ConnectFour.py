#ConnectFour.py

from games.classes.board import Board
from games.classes.piece import Piece
from games.classes.player import Player

from utils.errors import InvalidCoordinate, InvalidPiecePlacement, OutOfBounds
from utils import coord, my_os

#let's just assume all connect four games are this size:
BOARD_WIDTH=7
BOARD_HEIGHT=6
GAME_NAME="Connect Four"

class ConnectFour:
    last_placed = []
    previous_state = [] #temp for future undo handling

    def __init__(self, player1, player2):
        #temp values for objects not yet defined
        self.board = Board(BOARD_WIDTH,BOARD_HEIGHT, x_label=True) #temp
        self.player1 = player1
        self.player2 = player2
        self.turn = player1

    def render(self):
        #my_os.clear()
        title_offset = (4*BOARD_WIDTH - len(GAME_NAME))//2 #if someone adjusts game size
        print("\n   " + " "*title_offset + GAME_NAME)
        self.board.print()

    def checkWin(self):
        '''
        Check for win

        Returns:
            Boolean: whether placed piece causes the player to win
        '''
        return (False, self.turn)

    def checkTie(self):
        '''
        Check for tie (whether board is full)

        Returns:
            Boolean: tie or not
        '''
        for column in range(BOARD_WIDTH):
            if not self.board[BOARD_HEIGHT-1][column]: #found empty, not tie
                return False

        return True

    def placePiece(self, piece, col):
        '''
        Places piece in column

        Args:
            string column
            Piece piece
        Return:
            return False if failed
        '''
        col_num = int(col) - 1 # -1 to convert col str to 0-based index

        for bottom in range(0, self.board.height):
            if not self.board[bottom][col_num]:
                self.board.place(piece, col_num, bottom)
                self.last_placed = [col_num, bottom]
                return True
        return False

    def handleTurn(self):
        player = self.turn
        print("{}'s turn!".format(player))
        piece = Piece(player.color)

        ask = "Please select a column to place piece: "
        while True:
            try:
                response = input(ask)
                success, column = coord.parseCol(response)

                if not success:
                    raise InvalidCoordinate
                elif not coord.validCoord(column, BOARD_WIDTH):
                    raise OutOfBounds

                #try to place piece, raise exception if failed
                elif not self.placePiece(piece, column):
                    raise InvalidPiecePlacement
                break

            except InvalidCoordinate:
                ask = "Invalid column name. Please enter column number: "
            except OutOfBounds:
                ask = "Out of bounds column. Please try again: "
            except InvalidPiecePlacement:
                ask = "Column is full. Please enter a different column: "

        self.render()
        print("Placed {} at {}. Ending {}'s turn.".format(piece, response, player))

        #ending turn
        self.turn = self.player2 if self.turn is self.player1 else self.player1

    def play(self):
        print('Starting ConnectFour')
        self.render()
        self.handleTurn()
        self.handleTurn()


def main(player1, player2):
    game = ConnectFour(player1, player2)
    game.play()
