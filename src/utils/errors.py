# errors.py

class Error(Exception):
    """Base class for game errors"""
    pass

class InvalidCoordinate(Error):
    """Raised when input value doesn't parse into board coordinates"""
    pass

class InvalidPiecePlacement(Error):
    """Raised when piece cannot be moved or placed at input value"""
    pass

class OutOfBounds(Error):
    """Raised when input is not within bounds of board"""
    pass

class InvalidChar(Error):
    pass

class InvalidGuess(Error):
    pass
