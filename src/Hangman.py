#Hangman.py

from classes.game import Game
from classes.player import Player

from utils import my_os
from utils.errors import InvalidChar, InvalidGuess

GAME_NAME = "Hangman"
NUM_GUESSES = 6
MAX_PLAYERS = 5

class Hangman(Game):
    def __init__(self):
        super().__init__(GAME_NAME)
        self.secret = ''
        self.revealed = []
        self.guessed = set()
        self.wrong_guesses = 0
        self.num_guesses = NUM_GUESSES

        self.players = []

    def initGame(self):
        self.render()
        print("Let's play Hangman!!!\n")

        self.initPlayers()
        self.setSecret()
        self.render()

    def initPlayers(self):
        num_players = input("How many people are playing? ")
        self.players = [Player("Mr. Hangman", species="AI")]

        while True:
            if num_players.isnumeric() and 1 <= int(num_players) <= MAX_PLAYERS:
                num_players = int(num_players)
                break
            num_players = input("Try again. Please enter 1 to 5 players: ")

        if num_players == 1:
            name = input("What is your name? ")
            self.addPlayer(name)
            return

        name = input("What is the word setter's name? ")
        self.players[0] = Player(name)

        for count in range(1, num_players): #skip player[0]
            name = input("What is guesser {}'s name? ".format(str(count)))
            self.addPlayer(Player(name))

    #============= Setters and Getters ===========
    def reset(self, reset_players=False):
        self.secret = ''
        self.revealed = []
        self.guessed = set()
        self.wrong_guesses = 0

        super().reset(reset_players)

        self.setSecret()

    def setSecret(self):
        self.render()

        if self.players[0].isAI():
            #TODO: change so that a random word is selected
            secret = 'Hangman is fun'
            print('{} has selected a phrase.'.format(self.players[0]))
            input('Press a key to continue.')

        else:
            print("Guessers, close your eyes.")
            secret = input("Word Setter {}, please enter a secret word or phrase: ".format(self.players[0]))

            while not all(x.isalpha() or x.isspace() for x in secret):
                secret = input("Invalid input. Only use letters or spaces: ")

        #set instance values
        self.secret = secret
        for letter in self.secret:
            if letter.isspace():
                self.revealed.append(' ')
            else:
                self.revealed.append(None)

    #============ Printing Methods ===========
    def printEnd(self):
        print("\nThe secret was: {}".format(self.secret))
        super().printEnd()

    def printGallows(self):
        head, body, legs = '', '', ''
        n = self.wrong_guesses
        revealed = self.strRevealed()

        #====head====
        if n >= 1:
            head = '   O '
        #====body====
        if 2 <= n <= 4:
            body = '   @ '
        elif n == 5:
            body = '  /@ '
        elif n >= 6:
            body = '  /@\\'
        #====legs====
        if n == 3:
            legs = '  /'
        elif n >= 4:
            legs = '  /\\'

        draw = (['  +———+ ',
                 '   |   | ' + '    ' + revealed,
                 '   |'+ head,
                 '   |'+ body,
                 '   |'+ legs,
                 '  _|_____',
                 ' /_______\\\n'])

        print("\n","\n".join(draw))
        print("Letters Guessed")
        print(' ', self.strGuessed())

    def strRevealed(self):
        converted = []
        for char in self.revealed:
            if not char:
                converted.append('_')
            else:
                converted.append('{}'.format(char))

        return ' '.join(converted)

    def strGuessed(self):
        convert = list(self.guessed)
        convert.sort()
        return ' '.join(convert)

    def render(self):
        my_os.clear()
        print("\n  {}".format(self.name))
        self.printGallows()

    #=========== Game Mechanics Unique to Hangman ============

    def setIfWin(self):
        for ele in self.revealed:
            if not ele:
                return

        self.winner = self.players[1:]
        self.end_game = True

    def setIfTie(self):
        pass

    def setIfLose(self):
        if self.wrong_guesses < self.num_guesses:
            return

        if not self.players[0].isAI():
            self.winner = self.players[0]
            self.loser = self.players[1:]
        else:
            self.loser = Player("You") #special condition in 1-player game

        self.end_game = True

    def handleTurn(self):
        player = self.getCurrentPlayer()

        if player == self.players[0]: #skip the secret word setter
            return

        print("{}'s turn to guess!".format(player))

        ask = ("Enter guess: ")
        while True:
            try:
                char = input(ask)

                if not char.isalpha() or len(char) > 1:
                    raise InvalidChar
                elif char.upper() in self.guessed:
                    raise InvalidGuess
                break

            except InvalidChar:
                ask = "Invalid input. Please input a single letter: "
            except InvalidGuess:
                ask = "Already guessed. Please guess another: "

        self.guess(char.upper())

    def guess(self, char):
        self.guessed.add(char)

        player = self.getCurrentPlayer()

        found = False
        for i, letter in enumerate(self.secret):
            if letter.casefold() == char.casefold():
                self.revealed[i] = letter
                found = True

        if not found:
            self.wrong_guesses += 1

        self.render()

        #print("\n{} guessed \"{}\"".format(player, char.upper()))

def main():
    my_os.clear()
    game = Hangman()
    game.play()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        my_os.goodbye()

    my_os.goodbye()
