#test.py

from classes.board import Board
from classes.piece import Piece
from classes.player import Player

import ConnectFour

from utils import coord
from sys import argv

def test_board():
    piece = Piece('X')

    test = Board(8,8,True)
    test.print()

    tictac = Board(3,3)
    tictac.print()

    giant = Board(28,20,True,True)
    giant.print()

    tictac.place(piece, 1, 0)
    tictac.place(piece, 2, 0)
    tictac.print()
    tictac.remove(2,0)
    tictac.print()
    tictac.copyBoard()

def test_ConnectFour():
    def testTie():
        if game.checkTie():
            print("Tie (game board filled)")
        else:
            print("Not a tie")

    p1 = Player("Dog", "X")
    p2 = Player("Cat", "O")
    game = ConnectFour.ConnectFour(p1, p2)
    game.play()
    game.clearBoard()

    piece = Piece("X")
    game.placePiece(piece, '1')
    game.placePiece(piece, '1')
    game.placePiece(piece, '1')
    game.placePiece(piece, '3')
    game.placePiece(piece, '1')
    game.printBoard()
    won, winner = game.checkWin()
    print("Dog should win", won, winner)


    print("Testing Tie:")
    testTie()

    for i in range(game.board.width):
        for _ in range(game.board.height):
            game.placePiece(piece, str(i))

    game.printBoard()
    testTie()

def test_coord():
    tests = ["a1","aa1","aaa1","ab2"]
    for test in tests:
        print(test)
        parsed = coord.parseXY(test)
        print(parsed[0],parsed[1],parsed[2])


if __name__ == '__main__':
    print("testing board (mainly print)")
    test_board()
    print("testing ConnectFour")
    #test_ConnectFour()
    test_coord()
