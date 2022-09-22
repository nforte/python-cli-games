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

    def checkWin(self):
        '''Checks for win and adjusts game state if win is found'''
        x, y = self.getPrevMove()
        piece = self.board[y][x]

        res = 0
        #==== Check for 4 in a row up and down====
        count = 0
        for i in range(y+1): #only need to check below piece
            count = count + 1 if self.board[i][x] == piece else 0
            res = max(res, count)

        #==== Check left and right ====
        count = 0
        for i in range(BOARD_WIDTH): #for simplicity, just scan whole row
            count = count + 1 if self.board[y][i] == piece else 0
            res = max(res, count)

        #==== Check top to bottom diag ====
        shift = min(x, BOARD_HEIGHT-y-1)
        i, j = x-shift, y+shift
        count = 0
        while i < BOARD_WIDTH and j >= 0:
            count = count + 1 if self.board[j][i] == piece else 0
            res = max(res, count)

            i += 1
            j -= 1

        #==== Check bottom to top diag ====
        shift = min(x, y)
        i, j = x-shift, y-shift
        count = 0
        while i < BOARD_WIDTH and j < BOARD_HEIGHT:
            count = count + 1 if self.board[j][i] == piece else 0
            res = max(res, count)

            i += 1
            j += 1

        if res >= 4:
            self.end_game = True
            self.winner = self.players[self.turn]

    def checkTie(self):
        '''Checks for tie (whether board is full) and adjusts end_game state'''
        for column in range(BOARD_WIDTH):
            if not self.board[BOARD_HEIGHT-1][column]: #found empty, not tie
                return

        self.end_game = True

    def handleTurn(self):
        player = self.getCurrentTurn()
        print("{}'s turn! ({})".format(player, player.color))
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
        col -= 1 # -1 to convert col str to 0-based index

        for bottom in range(0, self.board.height):
            if not self.board[bottom][col]:

                self.setPrev([col, bottom])
                self.board.place(piece, col, bottom)

                return True

        return False

def main():
    game = ConnectFour()
    game.play()

if __name__ == '__main__':
    main()
