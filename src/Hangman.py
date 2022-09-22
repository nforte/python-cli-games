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

        self.executioner = Player("Mr. Secret", "AI")

        self.prev_state = []

    def reset(self):
        super().reset()
        self.secret = ''
        self.revealed = []
        self.guessed = set()
        self.wrong_guesses = 0

        self.prev_state = []

    def printGallows(self):
        head, body, legs = '', '', ''
        n = self.wrong_guesses

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
                 '   |   | ',
                 '   |'+ head,
                 '   |'+ body,
                 '   |'+ legs,
                 '  _|_____',
                 ' /_______\\\n'])

        print("\n","\n".join(draw))

    def render(self):
        my_os.clear()
        print("\n  {}".format(self.name))
        self.printGallows()

    def setSecret(self):
        #TODO: if exe is AI, randomly set secret word
        print("Guessers, close your eyes.")
        response = input("Executioner, please enter a secret word: ")

        while not response.isalpha():
            response = input("Try again. Only use letters: ")

        self.secret = response
        self.revealed = [None for letter in self.secret]

    def setup(self):
        print("Let's play Hangman!!!\n")
        self.initPlayers()
        self.setSecret()
        self.render()

    def setIfWin(self):
        for ele in self.revealed:
            if not ele:
                return

        self.winner = self.players

    def setIfTie(self):
        pass

    def setIfLost(self):
        if self.wrong_guesses < self.num_guesses:
            return

        if not self.executioner.isAI():
            self.winner = self.executioner
        else:
            self.loser = self.players

        self.end_game = True

    def initPlayers(self):
        num_players = input("How many people are playing? ")

        while True:
            if num_players.isnumeric() and 1 < int(num_players) < MAX_PLAYERS:
                num_players = int(num_players)
                break
            num_players = input("Try again. Please enter 2 or more: ")

        #TODO: Add AI
        exe_name = input("Who is choosing the secret word? ")
        self.executioner = Player(exe_name)
        start = 1

        for count in range(start, num_players):
            name = input("Who is Player {}? ".format(str(count+1)))
            new_p = Player(name)
            self.addPlayer(new_p)

    def handleTurn(self):
        player = self.getCurrentPlayer()
        print("{}'s turn to guess!".format(player))

        ask = ("Enter guess: ")
        while True:
            try:
                char = input(ask)

                if not char.isalpha() or len(char) > 1:
                    raise InvalidChar
                elif char.lower() in self.guessed:
                    raise InvalidGuess
                break

            except InvalidChar:
                ask = "Invalid input. Please input a single letter: "
            except InvalidGuess:
                ask = "Already guessed. Please guess another: "

        self.guess(char)

    def guess(self, char):
        self.guessed.add(char)

        char = char.lower()
        player = self.getCurrentPlayer()

        found = False
        for i, letter in enumerate(self.secret):
            if letter == char:
                self.revealed[i] = letter
                found = True

        if not found:
            self.wrong_guesses += 1

        self.render()

        print("{} guessed \"{}\"".format(player, char.upper()))
        if found:
            print("{} guessed correctly!".format(player))

def main():
    game = Hangman()
    game.play()

if __name__ == '__main__':
    main()
