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
