from games.classes.board import Board
from games.classes.piece import Piece

from games import *

from sys import argv

def test_board():
    piece = Piece('X')

    test = Board(8,8)
    test.display(True)

    tictac = Board(3,3)
    tictac.display(True, True)

    giant = Board(28,20)
    giant.display(True, True)

    tictac.place(piece, 1, 0)
    tictac.place(piece, 2, 0)
    tictac.display(True, True)
    tictac.remove(2,0)
    tictac.display(True, True)

def test_ConnectFour():
    game = ConnectFour.ConnectFour('Player 1', 'Player 2')
    game.play()

    piece = Piece("X")
    game.place(piece, '1')
    game.place(piece, '1')
    game.place(piece, '1')
    game.place(piece, '3')
    game.render()

if __name__ == '__main__':
    print("testing board (mainly display)")
    test_board()
    print("testing ConnectFour")
    test_ConnectFour()
