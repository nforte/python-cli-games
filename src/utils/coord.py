#coord.py

def parseCol(s:str):

    if s.isnumeric():
        return (True, int(s)-1) # -1 to shift to 0-indexed

    return (False, 0)

def parseXY(s:str):
    if not s:
        return(False, 0, 0)
        
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    for i in range(len(s)):
        if not s[i].isalpha():
            break

    x_str = s[:i]
    y_str = s[i:]

    #Super giant boards not supported (columns > 26*25)
    if len(x_str) < 1 or len(x_str) > 2 or not y_str.isnumeric():
        return (False, 0, 0)

    y = int(y_str) - 1
    x = alpha.find(x_str[0].lower())

    if len(x_str) == 2:
        if x_str[1] == 'a':
            return (False, 0, 0)
        x += 26*(alpha.find(x_str[1].lower()))

    return(True, x, y)

def isValidCoord(x, x_max, y=0, y_max=1):
    return 0 <= x < x_max and 0 <= y < y_max

def isEmptyCoord(board, x, y):
    return not board[y][x]

def countUpDown(board, col, piece):
    res, count = 0, 0
    for i in range(board.height):
        count = count + 1 if board[i][col] == piece else 0
        res = max(res, count)

    return res

def countLeftRight(board, row, piece):
    res, count = 0, 0
    for i in range(board.width):
        count = count + 1 if board[row][i] == piece else 0
        res = max(res, count)

    return res

def countTopLeftDiag(board, x, y, piece):
    '''Count all pieces in same diagonal containing (x,y), from top left to bottom right'''
    res, count = 0, 0

    shift = min(x, board.height-y-1)
    x, y = x-shift, y+shift
    while x < board.width and y >= 0:
        count = count + 1 if board[y][x] == piece else 0
        res = max(res, count)

        x += 1
        y -= 1

    return res

def countBottomLeftDiag(board, x, y, piece):
    '''Count all pieces in same diagonal containing (x,y), from bottom left to top right'''
    res, count = 0, 0

    shift = min(x, y)
    x, y = x-shift, y-shift
    while x < board.width and y < board.height:
        count = count + 1 if board[y][x] == piece else 0
        res = max(res, count)

        x += 1
        y += 1

    return res
