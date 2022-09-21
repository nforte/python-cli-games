#coord.py

def parseCol(s:str):

    if s.isnumeric():
        return (True, int(s))

    return (False, 0)

def validCoord(x, x_max, y=1, y_max=1):
    return 0 < x <= x_max or 0 < y < y_max
