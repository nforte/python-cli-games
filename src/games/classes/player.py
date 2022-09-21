# player.py

class Player:

    def __init__(self, name:str, color:str=''):
        self.name = name
        self.color = color

    def __str__(self):
        return self.name

    def setColor(self, color:str):
        self.color = color
