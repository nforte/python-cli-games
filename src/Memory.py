#Memory.py

from classes.game import Game
from classes.board import Board
from classes.piece import Card
from classes.player import Player

from utils import coord, my_os
from utils.errors import InvalidCoordinate, InvalidChoice, OutOfBounds

CARD_FACES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ123456'

GAME_NAME = 'The Memory Game'
GRID_WIDTH = 9
GRID_LENGTH = 8
MAX_PLAYERS = 6

class Memory(Game):
    def __init__(self):
        super().__init__(GAME_NAME)
        self.grid = Board(GRID_WIDTH, GRID_LENGTH, True, True)

    def initGrid(self): # TODO:
        for y in range(self.grid.height):
            for x in range(self.grid.width):
                card = Card("A") #temp for testing other stuff
                self.grid.place(card, x, y)

    def initGame(self):
        self.initGrid()
        super().initGame()

    def initPlayers(self):
        num_players = input("How many people are playing? ")

        while True:
            if num_players.isnumeric() and 1 <= int(num_players) <= MAX_PLAYERS:
                num_players = int(num_players)
                break
            num_players = input("Try again. Please enter 1 to 6 players: ")

        for count in range(0, num_players): #skip player[0]
            name = input("Please enter Player {}'s name: ".format(str(count+1)))
            self.addPlayer(Player(name))


    def render(self):
        my_os.clear()
        offset = (4*self.grid.width - len(self.name))//2 #offset based on Board
        print("\n    " + " "*offset + self.name)

        self.grid.print()
        print()

    #================ Game Mechanics ===============
    def setIfLose(self):
        pass
    def setIfTie(self): #for simplicity, game will only have multiple winners
        pass
    def setIfWin(self):
        pass

    def setIfEnd(self):
        for row in self.grid:
            for cell in row:
                if cell:
                    return #grid is not empty, so do nothing

        #all end conditions are the same, so ignore the other set functions
        self.end_game = True
        most_cards = 0
        for player in self.players:
            most_cards = max(player.getNumItems, most_cards)

        winners = []
        for player in self.players: #iter through players again to get ties
            if player.getNumItems == most_cards:
                winners.append(player)

        self.winners = winners

    def handleTurn(self):
        player = self.getCurrentPlayer()
        print("{}'s turn!".format(player))

        ask = "Please flip a card: "
        first_card, x1, y1 = self.chooseCard(ask)

        self.render()
        print("{} flipped card {}".format(player, first_card))

        ask = "Please flip another card: "
        second_card, x2, y2 = self.chooseCard(ask)
        self.render()

        if first_card == second_card:
            input("Cards match! Press any key to pick up cards.")
            player.give(first_card, second_card)

            #remove from board
            self.grid.remove(x1, y1)
            self.grid.remove(x2, y2)

            self.render()
            self.handleTurn() #don't change turns if a pair is found

        else:
            self.render()

    def isValidChoice(self, x, y):
        #is not empty and is not face up
        return not coord.isEmptyCoord(self.grid, x, y) and not self.grid[y][x].isDown


    def chooseCard(self, ask):
        while True:
            try:
                response = input(ask)
                success, x, y = coord.parseXY(response)

                if not success:
                    raise InvalidCoordinate
                elif not coord.isValidCoord(x, self.grid.width, y, self.grid.width):
                    raise OutOfBounds
                elif self.isValidChoice(x, y):
                    raise InvalidChoice
                break

            except InvalidCoordinate:
                ask = "Invalid coordinate. Please try again with cell code (Ex. 'A1'): "
            except OutOfBounds:
                ask = "Out of bounds. Please try again: "
            except InvalidChoice:
                ask = "Can't choose that. Please choose a different card: "

        card = self.grid[y][x]
        card.flip()
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
