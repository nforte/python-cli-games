#game.py

from abc import ABC, abstractmethod

class Game(ABC):

    def __init__(self, name):
        self.players = []
        self.turn = 0
        self.name = name

        self.end_game = False
        self.winner = None
        self.loser = None

    def getCurrentPlayer(self):
        return self.players[self.turn]

    def addPlayer(self, player):
        self.players.append(player)

    def setPlayers(self, players):
        '''Set players'''
        self.players = players

    def setup(self):
        self.render()
        self.initPlayers()

        assert self.players, "Game must have at least one player."

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
        self.setIfLost()

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

        if self.winner:
            names = self.winner if isinstance(self.winner, list) else [self.winner]
        elif self.loser:
            names = self.loser if isinstance(self.loser, list) else [self.loser]
        else:
            names = self.players

        if len(names) == 1:
            s = str(names[0])
        elif len(names) == 2:
            s = str(names[0]) + " and " + str(names[1])
        else:
            s = ', '.join(names[:-1]) + ", and " + str(names[-1])

        if self.winner:
            print("Congratulations! {} won!".format(s))
        elif self.loser:
            print("{} lost. Better luck next time.".format(s))
        else:
            print("End of game! {} have tied!".format(s))

    def play(self):
        '''Wrapper for playing the game'''
        self.setup()

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
    def setIfLost(self):
        '''Check for lose'''
        pass

    @abstractmethod
    def initPlayers(self):
        '''Initializes players'''
        pass

    @abstractmethod
    def handleTurn(self):
        '''For handling a game's turn rules'''
        pass
