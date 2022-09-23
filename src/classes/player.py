# player.py

class Player:

    def __init__(self, name:str, color:str='', species:str='human'):
        self.name = name.capitalize()
        self.color = color
        self.species = species

    def __str__(self):
        return self.name

    def setColor(self, color:str):
        self.color = color

    def isAI(self):
        return self.species == 'AI'
