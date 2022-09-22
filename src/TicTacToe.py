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
        super()__init__(GAME_NAME, BOARD_WIDTH, BOARD_WIDTH, True, True)

def setIfWin(self):
    x, y = self.getPrevMove():
    count = max(coord.countUpDown(self.board, x),
                coord.countTopLeftDiag(self.board,x,y),
                coord.countBottomLeftDiag(self.board,x,y))

    if count >=3:
        self.end_game = True
        self.winner = self.getCurrentPlayer()

def setIfTie(self):
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_WIDTH):
            if not self.board[i][j]:
                return

    self.end_game = True

def initPlayers(self):
    player1 = Player(input("What is first player's name? ").capitalize(), 'X')
    player2 = Player(input("What is second player's name? ").capitalize(), 'O')

    self.setPlayers([player1, player2])


def handleTurn(self):
    pass

def placePiece(self, piece, x, y):
    self.board.place(piece, x, y)

def main():
    game = TicTacToe()
    game.play()
