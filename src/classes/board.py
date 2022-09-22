#Board.py

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
        return [[piece for piece in range(self.width)] for _ in range(self.height)]

    def print(self):
        '''
        Prints out board
        Args:
            Boolean x_label: if x should be labelled
            Boolean y_label: if y should be labelled
        '''
        x_label, y_label = self.x_label, self.y_label

        bar = '   ' + '+–—–'*self.width + '+\n'
        graph = bar #bottom row
        last_row = ''

        #===== Create rows =====
        for i in range(self.height):
            new_row = ''
            num = i + 1

            row_label = '   '
            if y_label:
                row_label = ' ' + str(num) if num > 9 else '  ' + str(num)

            new_row += row_label + '|'

            #==== Append cells to row =====
            for j in range(self.width):
                if not self.board[i][j]:
                    new_row += '   |'
                else:
                    new_row += ' ' + str(self.board[i][j]) + ' |'

            #prepend new_rows so that (0,0) is in the bottom left corner
            graph = bar + new_row + '\n' + graph

        #===== Print table if there's no bottom labelling =====
        if not x_label:
            print(graph)
            return

        #===== Create label for bottom =====
        last_row = '  '
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        loop = 0 #for handling large boards
        for i in range(self.width):

            if not y_label: #only bottom is labelled, so use numbers
                tag = '  ' if i < 9 else ' '
                tag += str(i+1)
            else:
                loop += 1 if i > 0 and i%26 == 0 else 0
                mini_i = i%26

                tag = '  ' if loop == 0 else ' '
                tag += alpha[mini_i] if loop == 0 else alpha[mini_i] + alpha[loop].lower()

            last_row += tag + ' '

        print(graph, last_row)

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
