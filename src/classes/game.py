#game.py

from abc import ABC, abstractmethod

class Game(ABC):

    def __init__(self, name):
        self.players = []
        self.turn = 0
        self.name = name

        self.end_game = False
        self.winner = []
        self.loser = []

    def initGame(self):
        self.render()
        self.initPlayers()

        assert self.players, "Game must have at least one player."

    @abstractmethod
    def initPlayers(self):
        '''Initializes players'''
        pass

    #=============== Setters and Getters ======================
    def getCurrentPlayer(self):
        return self.players[self.turn]

    def reset(self, reset_players=False):
        '''Resets the game but keeps same players'''
        self.turn = 0
        self.end_game = False
        self.winner = []
        self.loser = []

        if reset_players:
            self.players = []
            self.render()
            self.initPlayers()

    def setEndGame(self):
        self.end_game = True

    def setLoser(self, *losers):
        for loser in losers:
            self.loser.append(loser)

    def setWinner(self, *winners):
        for winner in winners:
            self.winner.append(winner)

    def setPlayer(self, *players):
        '''Set players'''
        for player in players:
            self.players.append(player)

    def setIfEnd(self):
        '''Check for end of game and set the game to end if conditions are met'''
        self.setIfWin()
        self.setIfTie()
        self.setIfLose()

    #=================== Printing Methods ========================
    def printEnd(self):
        '''Prints generic end statements for the game's ending'''
        s = ''

        if self.winner:
            names = self.winner
        elif self.loser:
            names = self.loser
        else:
            names = self.players

        if len(names) == 1:
            s = str(names[0])
        elif len(names) == 2:
            s = str(names[0]) + " and " + str(names[1])
        else:
            s = ', '.join(map(str, names[:-1])) + ", and " + str(names[-1])

        print()
        if self.winner:
            print("Good game, everyone! {} won!".format(s))
        elif self.loser: #no winners (everyone lost or AI won)
            print("{} lost. Better luck next time.".format(s))
        else:
            print("{} tied! Good game, everyone!".format(s))

    @abstractmethod
    def render(self):
        pass

    #============= Generic Game Phases/Wrappers ==================
    def endTurn(self):
        self.turn = self.turn + 1 if self.turn < len(self.players) - 1 else 0

    def endWrapper(self):
        reset_players = False
        self.printEnd()

        print()
        ask = "Would you like to play again?\n[y/n]: "

        while True:
            ans = input(ask)
            if ans.lower() == 'y' or ans.lower() == 'yes':

                #initPlayers if response is y/yes
                ans = input("\nPlay with different players?\n[y/n]: ")
                reset_players = (ans =='y' or ans.lower() == 'yes')

                self.reset(reset_players)

            elif ans.lower() != 'n' and ans.lower() != 'no':
                ask = 'Invalid input. Please input "yes" or "no": '
                continue #keep asking until valid input

            break

    def turnWrapper(self):
        '''
        Wrapper for taking turns. Advances to next player's turn after
            each turn.
        '''
        while not self.end_game:
            self.handleTurn()

    def play(self):
        '''Wrapper for playing the game'''
        self.initGame()

        while not self.end_game:
            self.render()
            #print("Players: {}".format(", ".join(map(str, self.players))))
            self.turnWrapper()
            self.endWrapper()


    #=========== Game Mechanics Unique To Each Game =====================
    @abstractmethod
    def setIfLose(self):
        '''Check for lose'''
        pass

    @abstractmethod
    def setIfTie(self):
        '''Check for tie'''
        pass

    @abstractmethod
    def setIfWin(self):
        '''Check for win'''
        pass

    @abstractmethod
    def handleTurn(self):
        '''For handling a game's turn rules'''
        pass
