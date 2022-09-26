#TicTacToe.py

from classes.boardgame import BoardGame
from classes.board import Board
from classes.piece import Piece
from classes.player import Player

from utils import coord, my_os
from utils.errors import InvalidCoordinate, InvalidPiecePlacement, OutOfBounds

BOARD_WIDTH = 3
GAME_NAME = "Tic-Tac-Toe"

class TicTacToe(BoardGame):
    def __init__(self):
        board = Board(BOARD_WIDTH, BOARD_WIDTH, True, True)
        super().__init__(GAME_NAME, board)


    def initPlayers(self):
        player1 = Player(input("What is first player's name? ").capitalize(), 'X')
        player2 = Player(input("What is second player's name? ").capitalize(), 'O')

        self.setPlayer(player1, player2)

    def render(self):
        my_os.clear()
        super().render()

    def setIfWin(self):
        if not self.prev_move:
            return
        x, y = self.getPrevMove()
        piece = self.board[y][x]

        count = max(coord.countUpDown(self.board, x, piece),
                    coord.countLeftRight(self.board, y, piece),
                    coord.countTopLeftDiag(self.board, x, y, piece),
                    coord.countBottomLeftDiag(self.board, x, y, piece))

        if count >= 3:
            self.setEndGame()
            self.setWinner(self.getCurrentPlayer())


    def setIfTie(self):
        for i in range(self.board.width):
            for j in range(self.board.width):
                if not self.board[i][j]:
                    return

        self.setEndGame()
        self.setTiePeople(self.players)

    def setIfLose(self):
        pass

    def handleTurn(self):
        player = self.getCurrentPlayer()
        print("{}'s turn! ({})".format(player, player.color))
        piece = Piece(player.color)

        ask = "Please select a coordinate: "

        while True:
            try:
                response = input(ask)
                if response.lower() == "undo":
                    self.undoTurn()
                    self.render()
                    print("Went back a turn.")

                    player = self.getCurrentPlayer()
                    print("{}'s turn! ({})".format(player, player.color))
                    piece = Piece(player.color)
                    ask = "Please select a coordinate to place piece: "
                    continue

                success, x, y = coord.parseXY(response)

                if not success:
                    raise InvalidCoordinate
                elif not coord.isValidCoord(x, self.board.width, y, self.board.width):
                    raise OutOfBounds
                elif not coord.isEmptyCoord(self.board, x,y):
                    raise InvalidPiecePlacement
                break

            except InvalidCoordinate:
                ask = "Invalid coordinate. Please try again with cell code (Ex. 'A1'): "
            except OutOfBounds:
                ask = "Out of bounds. Please try again: "
            except InvalidPiecePlacement:
                ask = "Cell is full. Please enter a different cell: "

        self.placePiece(piece, x, y)

        self.render()
        print("{} placed {} into cell {}.".format(player, piece, response.capitalize()))

        self.setIfEnd()
        self.endTurn()

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
