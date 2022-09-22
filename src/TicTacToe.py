#TicTacToe.py
from classes.game import Game
from classes.piece import Piece
from classes.player import Player

from utils import coord, my_os
from utils.errors import InvalidCoordinate, InvalidPiecePlacement, OutOfBounds

BOARD_WIDTH = 3
GAME_NAME = "Tic-Tac-Toe"

class TicTacToe(Game):
    def __init__(self):
        super().__init__(GAME_NAME, BOARD_WIDTH, BOARD_WIDTH, True, True)


    def initPlayers(self):
        player1 = Player(input("What is first player's name? ").capitalize(), 'X')
        player2 = Player(input("What is second player's name? ").capitalize(), 'O')

        self.setPlayers([player1, player2])


    def setIfWin(self):
        x, y = self.getPrevMove()
        piece = self.board[y][x]

        count = max(coord.countUpDown(self.board, x, piece),
                    coord.countLeftRight(self.board, y, piece),
                    coord.countTopLeftDiag(self.board, x, y, piece),
                    coord.countBottomLeftDiag(self.board, x, y, piece))

        if count >= 3:
            self.end_game = True
            self.winner = self.getCurrentPlayer()


    def setIfTie(self):
        for i in range(BOARD_WIDTH):
            for j in range(BOARD_WIDTH):
                if not self.board[i][j]:
                    return

        self.end_game = True


    def handleTurn(self):
        player = self.getCurrentPlayer()
        print("{}'s turn! ({})".format(player, player.color))
        piece = Piece(player.color)

        ask = "Please select a coordinate: "

        while True:
            try:
                response = input(ask)
                success, x, y = coord.parseXY(response)

                if not success:
                    raise InvalidCoordinate
                elif not coord.isValidCoord(x, BOARD_WIDTH, y, BOARD_WIDTH):
                    raise OutOfBounds
                elif not coord.isEmptyCoord(self.board, x,y):
                    raise InvalidPiecePlacement
                break

            except InvalidCoordinate:
                ask = "Invalid coordinate. Please try again with cell code (Ex. 'A1'): "
            except OutOfBounds:
                ask = "Out of bounds. Please try again: "
            except InvalidPiecePlacement:
                ask = "Cell if full. Please enter a different cell: "

        self.placePiece(piece, x, y)

        self.render()
        print("{} placed {} into cell {}.".format(player, piece, response.capitalize()))


    def placePiece(self, piece, x, y):
        self.setPrevState([x, y])
        self.board.place(piece, x, y)


def main():
    game = TicTacToe()
    game.play()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        my_os.goodbye()

    my_os.goodbye()
