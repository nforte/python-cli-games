#TicTacToe.py

from classes.board import Board
from classes.piece import Piece
from classes.player import Player

from utils import coord, my_os
from utils.errors import InvalidCoordinate, InvalidPiecePlacement, OutOfBounds

BOARD_WIDTH = 3
GAME_NAME = "Tic-Tac-Toe"

class TicTacToe():
    def __init__(self, player1=Player("Player 1", "X"), player2=Player("Player 2", "O"))):
        self.board = Board(BOARD_WIDTH, True, True)
        self.player1 = player1
        self.player2 = player2
        self.turn = player1

    
