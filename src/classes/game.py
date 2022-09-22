#game.py

from abc import ABC, abstractmethod

from classes.board import Board

class Game(ABC):

    def __init__(self, name):
        self.players = []
        self.turn = 0
        self.name = name

        self.end_game = False
        self.winner = None

    def getCurrentPlayer(self):
        return self.players[self.turn]

    def setPlayers(self, players):
        '''Set players'''
        self.players = players

    #================ Changing Game State =======================
    def reset(self):
        '''Resets the game but keeps same players'''
        self.turn = 0
        self.end_game = False
        self.winner = None

    #================= Printing Methods ==========================
    @abstractmethod
    def render(self):
        pass

    #================= Generic Game Phases/Wrappers ==============
    def setIfEnd(self):
        '''Check for end of game'''
        self.setIfWin()
        self.setIfTie()

    def doTurns(self):
        '''
        Wrapper for taking turns. Advances to next player's turn after
            each turn.
        '''
        while not self.end_game:
            self.handleTurn()

            #end turn
            self.setIfEnd()
            self.turn = self.turn + 1 if self.turn < len(self.players) - 1 else 0

    def handleEnd(self):
        '''Handles the print statements for the game's ending'''
        s = ''
        names = [self.winner] if self.winner else self.players

        if len(names) == 1:
            s = str(names[0])
        elif len(names) == 2:
            s = str(names[0]) + " and " + str(names[1])
        else:
            s = ', '.join(names[:-1]) + ", and " + str(names[-1])

        if self.winner:
            print("Congratulations! {} won!".format(s))
        else:
            print("End of game! {} have tied!".format(s))

    def play(self):
        '''Wrapper for playing the game'''
        self.render()
        self.initPlayers()

        assert self.players, "Game must have at least one player."

        while not self.end_game:
            self.render()
            print("Players: {}".format(", ".join(map(str, self.players))))
            self.doTurns()
            self.handleEnd()

            print()
            ans = input("Would you like to play again?\n[y/n]: ")
            if ans.lower() == 'y' or ans.lower() == 'yes':
                self.reset()

    #================= Game Mechanics =============================
    @abstractmethod
    def setIfWin(self):
        '''Check for win'''
        pass

    @abstractmethod
    def setIfTie(self):
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
