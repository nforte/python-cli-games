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
        self.tie_people = []

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
        self.tie_people = []

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

    def setTiePeople(self, *players):
        for player in players:
            self.tie_people.append(player)

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
    def _strNames(self, players):
        '''Converts a list of players into a string of names'''
        if len(players) == 1:
            return str(players[0])
        elif len(players) == 2:
            return str(players[0]) + " and " + str(players[1])
        elif len(players) >= 3:
            return ', '.join(map(str, players[:-1])) + ", and " + str(players[-1])

    def printEnd(self):
        '''Prints generic end statements for the game's ending'''
        winners = self._strNames(self.winner)
        losers = self._strNames(self.loser)
        tie_people = self._strNames(self.tie_people)

        print()
        if self.winner:
            print("Good game, everyone! {} won!".format(winners))
        elif self.tie_people:
            print("{} tied! Good game, everyone!".format(tie_people))
        elif self.loser:
            print("{} lost. Better luck next time.".format(losers))

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
