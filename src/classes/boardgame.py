#boardgame.py

from classes.game import Game
from classes.board import Board

class BoardGame(Game):

    def __init__(self, name, b_width, b_height, x_label=False, y_label=False):
        super().__init__(name)
        self.board = Board(b_width, b_height, x_label, y_label)

        #stacks
        self.prev_move = []
        self.prev_state = []

    def getPrevMove(self):
        assert self.prev_move, "Must have previous move."
        return self.prev_move[-1]

    def setPrevState(self, new_move):
        '''Adds prev state and prev move to instance's stack'''
        self.prev_state.append(self.board.copyBoard())
        self.prev_move.append(new_move)

    #================ Changing Game State =======================
    def reset():
        '''Resets game state without changing players'''
        super().reset()
        self.board.clear()
        self.prev_move = []
        self.prev_state = []

    def undoTurn(self):
        '''Moves game state back one turn'''
        if not self.prev_move:
            return

        self.board.board = self.prev_state.pop()
        self.prev_move.pop()

        self.turn = self.turn - 1 if self.turn > 0 else len(self.players) - 1

    #================= Printing Methods ==========================
    def printBoard(self):
        '''Print board simply'''
        self.board.print()

    def render(self):
        '''Clears cli and redraws title card and game board.'''
        offset = (4*self.board.width - len(self.name))//2
        print("\n    " + " "*offset + self.name)

        self.printBoard()
        print()


    '''
    #========= Parent Abstract Methods to Implement ========
    def setIfWin(self)
    def setIfTie(self)
    def initPlayers(self)
    def handleTurn(self)
    '''
