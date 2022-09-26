# Piece.py

class Piece:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.color

    def __eq__(self, other):
        if other:
            return self.color == other.color
        return False #for handling None pieces

class Card:
    def __init__(self, value, suit='', backside='?'):
        self.face = value + suit
        self.backside = backside
        self.isFaceDown = True

        self.value = value
        self.suit = suit

    def __str__(self):
        if self.isFaceDown:
            return self.backside
        else:
            return self.face

    def __eq__(self, other):
        if other:
            return self.face == other.face
        return False

    def flip(self):
        self.isFaceDown = not self.isFaceDown

    def isDown(self):
        return self.isFaceDown
