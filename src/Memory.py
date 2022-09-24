#Memory.py

from classes.game import Game

GAME_NAME = 'The Memory Game'
GRID_WIDTH = 9
GRID_LENGTH = 8
CARD_FACES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ123456'

class Memory(Game):
    def __init__(self):
        super().__init__(GAME_NAME)
        self.grid = Board(GRID_WIDTH, GRID_LENGTH, True, True)

    def initGrid(self):
        for row in self.grid:
            for cell in row:
                pass

    def initGame(self):
        self.fillGrid()
        super().initGame()

    def initPlayers(self):
        pass

    def render(self):
        pass

    #================ Game Mechanics ===============
    def setIfLose(self):
        pass

    def setIfTie(self):
        pass

    def setIfWin(self):
        pass

    def handleTurn(self):
        pass

    def chooseCard(self):
        pass
