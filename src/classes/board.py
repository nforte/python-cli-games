#board.py

class Board:

    def __init__(self, width, height, x_label=False, y_label=False):
        self.board = [[None for _ in range(width)] for _ in range(height)]
        self.width = width
        self.height = height

        self.x_label = x_label
        self.y_label = y_label

    def __getitem__(self, index):
        return self.board[index]

    def copyBoard(self):
        return [[piece for piece in row] for row in self.board]

    #============= Print Help Functions ==============
    def _cellStr(self, x, y):
        item = str(self.board[y][x]) if self.board[y][x] else ' '
        return ' {} |'.format(item)

    def _colLabel(self, col_num):
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        if not self.y_label: #column labels are numbers
            space = '  ' if col_num < 9 else ' '
            return '{}{} '.format(space, col_num + 1)

        #Column labels are letters, so do the following:
        count = 0 #for handling large boards
        while col_num >= 26:
            col_num -= 26
            count += 1

        if count == 0:
            return '  {} '.format(alpha[col_num])
        else:
            return ' {}{} '.format(alpha[col_num], alpha[count].lower())

    #last row filled with labels (or blank newline)
    def _lastRow(self, left_offset=3):
        if not self.x_label:
            return '\n'

        cell_labels = []
        for col_num in range(self.width):
            cell_labels.append(self._colLabel(col_num))

        return ' '*left_offset + ''.join(cell_labels)

    def _rowLabel(self, row_num):
        num = row_num + 1
        label = '   '
        if self.y_label:
            label = ' ' + str(num) if num > 9 else '  ' + str(num)

        return label + '|'

    def _rowStr(self, row_num, end=''):
        s = []
        s.append(self._rowLabel(row_num))

        for x in range(self.width):
            s.append(self._cellStr(x, row_num))

        s.append(end)

        return ''.join(s)

    #============== Board Methods =========================
    def print(self):
        grid = []
        bar = '   ' + '+–—–'*self.width + '+'
        grid.append(bar)

        #append cell rows and bar rows
        for row_num in range(self.height-1, -1, -1): #iterate backwards so that (0,0) is at bottom
            grid.append(self._rowStr(row_num))
            grid.append(bar)

        grid.append(self._lastRow())

        print('\n'.join(grid))

    def place(self, piece, x, y):
        '''
        Place piece at (x,y)
        Returns:
            None or Piece: returns whatever was at (x,y)
        '''
        temp = self.board[y][x]
        self.board[y][x] = piece
        return temp

    def remove(self, x, y):
        '''
        Returns:
            Piece: removed piece
        '''
        return self.place(None, x, y)

    def clear(self):
        self.board = [[None for _ in range(self.width)] for _ in range(self.height)]


class GoBoard(Board):
    def __init__(self, width=19):
        width = 19 if width > 19 else width

        super().__init__(width, width, True, True)

    def _cellStr(self, x, y):
        cell = str(self.board[y][x]) if self.board[y][x] else '.'
        return ' {}'.format(cell)

    def _colLabel(self, col_num):
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return ' {}'.format(alpha[col_num])

    def print(self):
        grid = []
        border = '   +' + '——'*self.width + '—+'

        grid.append(border)

        #append cell rows and bar rows
        for row_num in range(self.width-1, -1, -1): #iterate backwards so that (0,0) is at bottom
            grid.append(self._rowStr(row_num,' |'))

        grid.append(border)
        grid.append(self._lastRow(left_offset=4))

        print('\n'.join(grid))
