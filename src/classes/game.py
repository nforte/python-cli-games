#game.py

from abc import ABC, abstractmethod

from classes.board import Board

from utils import my_os

class Game(ABC):

    def __init__(self, name, b_width, b_height, x_label=False, y_label=False):
        self.board = Board(b_width, b_height, x_label, y_label)
        self.players = []
        self.turn = 0
        self.name = name

        #stacks
        self.prev_move = []
        self.prev_state = []

        self.end_game = False
        self.winner = None

    def getCurrentTurn(self):
        return self.players[self.turn]

    def getPrevMove(self):
        assert(not self.prev_move, "Must have previous move.")
        return (self.prev_move[-1][0], self.prev_move[-1][1])

    def setPlayers(self, players):
        '''Set players'''
        self.players = players

    def setPrev(self, new_move):
        '''Adds prev state and prev move to instance's stack'''
        self.prev_state.append(self.board.copyBoard())
        self.prev_move.append(new_move)

    #================ Changing Game State =======================

    def reset(self):
        '''Resets the game but keeps same players'''
        self.board.clear()
        self.turn = 0
        self.prev_move = []
        self.prev_state = []

        self.end_game = False
        self.winner = None

    def undoTurn(self):
        '''Moves game state back one turn'''
        if not self.prev_move:
            return

        self.board = self.prev_state.pop()
        self.prev_move.pop()

        self.turn = self.turn - 1 if self.turn > 0 else len(self.players) - 1

    #================= Printing Methods ==========================
    def printBoard(self):
        '''Print board simply'''
        self.board.print()

    def render(self):
        '''Clears cli and redraws title card and game board.'''
        my_os.clear()

        offset = (4*self.board.width - len(self.name))//2
        print("\n    " + " "*offset + self.name)

        self.board.print()
        print()

    #================= Generic Game Phases/Wrappers ==============
    def checkEnd(self):
        '''Check for end of game'''
        self.checkWin()
        self.checkTie()

    def doTurns(self):
        '''
        Wrapper for taking turns. Advances to next player's turn after
            each turn.
        '''
        while not self.end_game:
            self.handleTurn()

            #end turn
            self.checkEnd()
            self.turn = self.turn + 1 if self.turn < len(self.players) - 1 else 0

    def handleEnd(self):
        '''Handles the print statements for the game's ending'''
        s = ''
        names = [self.winner] if self.winner else self.players

        if len(names) == 1:
            s = names[0]
        elif len(names) == 2:
            s = names[0] + " and " + names[1]
        else:
            s = ', '.join(names[:-1]) + ", and " + names[-1]

        if self.winner:
            print("Congratulations! {} won!".format(s))
        else:
            print("End of game! {} have tied!".format(s))

    def play(self):
        '''Wrapper for playing the game'''
        self.render()
        self.initPlayers()

        assert(not self.players, "Game must have at least one player.")

        while not self.end_game:
            self.render()
            print("Players: {}".format(", ".join(map(str, self.players))))
            self.doTurns()
            self.handleEnd()

            print()
            ans = input("Would you like to play again?\n[y/n]: ")
            if ans.lower() == 'y' or ans.lower() == 'yes':
                self.reset()

        print("\nThanks for playing! Have a nice day!")

    #================= Game Mechanics =============================
    @abstractmethod
    def checkWin(self):
        '''Check for win'''
        pass

    @abstractmethod
    def checkTie(self):
        '''Check for tie'''
        pass

    @abstractmethod
    def initPlayers(self):
        '''Initializes players'''
        pass

    @abstractmethod
    def handleTurn(self):
        '''For handling a game's turn rules'''
        pass
