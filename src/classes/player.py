# player.py

class Player:

    def __init__(self, name:str, color:str='', species:str='human'):
        self.name = name.capitalize()
        self.color = color
        self.species = species
        self.items = []

    def __str__(self):
        return self.name

    def setColor(self, color:str):
        self.color = color

    def isAI(self):
        return self.species == 'AI'

    def give(self, *items):
        for item in items:
            self.items.append(item)

    def getNumItems(self):
        return len(self.items)

    def clearItems(self):
        self.items = []
