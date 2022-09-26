#Gomoku.py
#aka Five in a Row

from classes.boardgame import BoardGame

from classes.board import GoBoard
from classes.player import Player
from classes.piece import Piece

from utils import coord, my_os
from utils.errors import InvalidCoordinate, InvalidPiecePlacement, OutOfBounds


BOARD_SIZE = 15
GAME_NAME = "Gomoku"

class Gomoku(BoardGame):
    def __init__(self):
        board = GoBoard(BOARD_SIZE)
        super().__init__(GAME_NAME, board)

    def initPlayers(self):
        player1 = Player(input("What is first player's name? ").capitalize(), '@')
        player2 = Player(input("What is second player's name? ").capitalize(), 'O')

        self.setPlayers([player1, player2])

    def setIfWin(self):
        '''Checks for win and adjusts game state if win is found'''
        if not self.prev_move:
            return

        x, y = self.getPrevMove()
        piece = self.board[y][x]

        count = max(coord.countUpDown(self.board, x, piece),
                    coord.countLeftRight(self.board, y, piece),
                    coord.countTopLeftDiag(self.board, x, y, piece),
                    coord.countBottomLeftDiag(self.board, x, y, piece))

        if count >= 5:
            self.end_game = True
            self.winner = self.getCurrentPlayer()

    def setIfTie(self):
        for row in self.board:
            for ele in row:
                if not ele:
                    return
        self.end_game = True

    def setIfLose(self):
        pass

    def render(self):
        my_os.clear()
        offset = (2*self.board.width - len(self.name))//2
        print("\n    " + " "*offset + self.name)

        self.printBoard()
        print()

    def handleTurn(self):
        player = self.getCurrentPlayer()
        print("{}'s turn! ({})".format(player, player.color))
        piece = Piece(player.color)

        ask = "Please select a coordinate to place piece: "
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
                elif not coord.isValidCoord(x, self.board.width, y, self.board.height):
                    raise OutOfBounds
                elif not self.isValidPlay(x, y):
                    raise InvalidPiecePlacement
                break

            except InvalidCoordinate:
                ask = "Invalid column name. Please enter column number: "
            except OutOfBounds:
                ask = "Out of bounds. Please try again: "
            except InvalidPiecePlacement:
                ask = "Spot is not empty. Please enter a different coordinate: "

        self.placePiece(piece, x, y)
        self.render()
        print("{} placed {} at {}.".format(player, piece, response.upper()))

        self.setIfEnd()
        self.endTurn()

    def placePiece(self, piece, x, y):
        self.setPrevState([x, y])
        self.board.place(piece, x ,y)

    def isValidPlay(self, x, y):
        return not self.board[y][x]

def main():
    game = Gomoku()
    game.play()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        my_os.goodbye()

    my_os.goodbye()
