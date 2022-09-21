#ConnectFour.py

from classes.board import Board
from classes.piece import Piece
from classes.player import Player

from utils.errors import InvalidCoordinate, InvalidPiecePlacement, OutOfBounds
from utils import coord, my_os

#let's just assume all connect four games are this size:
BOARD_WIDTH=7
BOARD_HEIGHT=6
GAME_NAME="Connect Four"

class ConnectFour:
    last_placed = []
    previous_state = [] #temp for future undo handling

    def __init__(self, player1=Player("Player 1", "X"), player2=Player("Player 2", "O")):
        #temp values for objects not yet defined
        self.board = Board(BOARD_WIDTH,BOARD_HEIGHT, x_label=True) #temp
        self.player1 = player1
        self.player2 = player2
        self.turn = player1

    def printBoard(self):
        self.board.print()

    def clearBoard(self):
        self.board.clear()

    def setPlayers(self, p1, p2):
        self.player1 = p1
        self.player2 = p2
        self.turn = p1

    def render(self):
        my_os.clear()
        title_offset = (4*BOARD_WIDTH - len(GAME_NAME))//2 #if someone adjusts game size
        print("\n   " + " "*title_offset + GAME_NAME)
        self.board.print()
        print()

    def checkWin(self):
        '''
        Check for win

        Returns:
            Boolean: whether placed piece causes the player to win
        '''
        x, y = self.last_placed[0], self.last_placed[1]
        piece = self.board[y][x]
        winner = self.player1 if piece.color == self.player1.color else self.player2

        #==== Check for 4 in a row up and down====
        count = 0
        for i in range(y+1): #only need to check below piece
            if self.board[i][x] == piece:
                count += 1
            else:
                count = 0

            if count == 4:
                return (True, winner)
        #==== Check left and right ====
        count = 0
        for i in range(BOARD_WIDTH): #for simplicity, just scan whole row
            if self.board[y][i] == piece:
                count += 1
            else:
                count = 0

            if count == 4:
                return (True, winner)

        #==== Check top to bottom diag ====
        shift = min(x, BOARD_HEIGHT-y-1)
        i, j = x-shift, y+shift

        count = 0
        while i < BOARD_WIDTH and j >= 0:
            if self.board[j][i] == piece:
                count += 1
            else:
                count = 0

            if count == 4:
                return(True, winner)

            i += 1
            j -= 1

        #==== Check bottom to top diag ====
        shift = min(x, y)
        i, j = x-shift, y-shift

        count = 0
        while i < BOARD_WIDTH and j < BOARD_HEIGHT:
            if self.board[j][i] == piece:
                count += 1
            else:
                count = 0

            if count == 4:
                return(True, winner)

            i += 1
            j += 1

        #no 4 in a row found, so return false
        return (False, winner)

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

        #ending turn
        self.turn = self.player2 if self.turn is self.player1 else self.player1

    def play(self):
        print('Starting ConnectFour')
        self.render()

        has_winner, has_tie = False, False
        while not has_winner and not has_tie:
            self.handleTurn()
            has_winner, winner = self.checkWin()
            has_tie = self.checkTie()

        if has_winner:
            print("Congratulations! {} has won!".format(winner))
        elif has_tie:
            print("No more moves left. {} and {} have tied!".format(self.player1, self.player2))


def main():
    game = ConnectFour()
    game.render()

    player1 = Player(input("What is first player's name? ").capitalize(), 'X')
    player2 = Player(input("What is second player's name? ").capitalize(), 'O')

    game.setPlayers(player1, player2)
    game.play()

if __name__ == '__main__':
    main()
