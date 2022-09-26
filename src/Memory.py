#Memory.py

from classes.game import Game
from classes.board import Board
from classes.piece import Card
from classes.player import Player

import random

from utils import coord, my_os
from utils.errors import InvalidCoordinate, InvalidChoice, OutOfBounds

CARD_FACES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

GAME_NAME = 'The Memory Game'

#Size Rules: GRID_WIDTH*GRID_LENGTH <= 72 and GRID_WIDTH*GRID_LENGTH must be even
GRID_WIDTH = 5 #9 standard large
GRID_LENGTH = 4 #8 standard large
MAX_PLAYERS = 6

class Memory(Game):
    def __init__(self):
        super().__init__(GAME_NAME)
        self.grid = Board(GRID_WIDTH, GRID_LENGTH, True, True)

    def initGrid(self): # TODO:
        size = GRID_WIDTH*GRID_LENGTH//2
        card_pool = list(CARD_FACES[:size])
        card_pool.extend(card_pool.copy())
        random.shuffle(card_pool)

        for y in range(self.grid.height):
            for x in range(self.grid.width):
                card = Card(card_pool.pop())
                self.grid.place(card, x, y)

    def initGame(self):
        self.initGrid()
        super().initGame()

    def initPlayers(self):
        num_players = input("How many people are playing? ")

        while True:
            if num_players.isnumeric() and 2 <= int(num_players) <= MAX_PLAYERS:
                num_players = int(num_players)
                break
            num_players = input("Try again. Please enter 2 to 6 players: ")

        for count in range(0, num_players): #skip player[0]
            name = input("Please enter Player {}'s name: ".format(str(count+1)))
            self.setPlayer(Player(name))

    def render(self):
        my_os.clear()
        offset = (4*self.grid.width - len(self.name))//2 #offset based on Board
        print("\n    " + " "*offset + self.name)

        self.grid.print()
        print()

    #================ Game Mechanics ===============
    def setIfLose(self):
        pass
    def setIfTie(self):
        pass
    def setIfWin(self):
        pass

    def setIfEnd(self):
        for row in self.grid:
            for cell in row:
                if cell:
                    return #grid is not empty, so do nothing

        #all end conditions are the same, so ignore the other set functions
        self.setEndGame()
        most_cards = 0
        for player in self.players:
            most_cards = max(player.getNumItems(), most_cards)

        winners = []
        for player in self.players: #iter through players again to get ties
            if player.getNumItems() == most_cards:
                winners.append(player)

        if len(winners) > 1:
            self.setTiePlayers(*winners)
        else:
            self.setWinner(*winners)

    def handleTurn(self):
        player = self.getCurrentPlayer()
        print("{}'s turn!".format(player))

        ask = "Please flip a card: "
        first_card, x1, y1 = self.chooseCard(ask)
        first_card.flip()

        self.render()
        print("{} flipped card {}".format(player, first_card))

        ask = "Please flip another card: "
        second_card, x2, y2 = self.chooseCard(ask)
        second_card.flip()

        self.render()

        if first_card == second_card:
            input("Cards match! Press Enter to pick up cards.")
            player.give(first_card, second_card)

            #remove from board
            self.grid.remove(x1, y1)
            self.grid.remove(x2, y2)

        else: #put face down
            input("Cards don't match. Press Enter to continue.")
            first_card.flip()
            second_card.flip()

        self.render()
        self.setIfEnd()

        if first_card != second_card:
            self.endTurn()

    def isValidChoice(self, x, y):
        #is not empty and is not face up
        return not coord.isEmptyCoord(self.grid, x, y) and self.grid[y][x].isDown()


    def chooseCard(self, ask):
        while True:
            try:
                response = input(ask)
                success, x, y = coord.parseXY(response)

                if not success:
                    raise InvalidCoordinate
                elif not coord.isValidCoord(x, self.grid.width, y, self.grid.width):
                    raise OutOfBounds
                elif not self.isValidChoice(x, y):
                    raise InvalidChoice
                break

            except InvalidCoordinate:
                ask = "Invalid coordinate. Please try again with cell code (Ex. 'A1'): "
            except OutOfBounds:
                ask = "Out of bounds. Please try again: "
            except InvalidChoice:
                ask = "Can't choose that. Please choose a different card: "

        card = self.grid[y][x]
        return [card, x, y]

def main():
    game = Memory()
    game.play()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        my_os.goodbye()

    my_os.goodbye()
