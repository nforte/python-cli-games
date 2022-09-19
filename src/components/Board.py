#Board.py
from Piece import Piece

class Board:

    def __init__(self, width, height):
        self.board = [[None for _ in range(width)] for _ in range(height)]
        self.width = width
        self.height = height

    def display(self, x_label=False, y_label=False):
        bar = '   ' + '+-—-'*self.width + '+\n'
        graph = bar #first row
        last_row = ''

        #===== Create rows =====
        for i in range(self.height):
            num = self.height - i
            row_label = '   '
            if y_label:
                row_label = ' ' + str(num) if num > 9 else '  ' + str(num)

            graph = graph + row_label + '|'

            for j in range(self.width):
                if not self.board[i][j]:
                    graph += '   |'
                else:
                    graph += ' ' + str(self.board[i][j]) + ' |'

            graph += '\n' + bar

        #===== Print table if there's no bottom labelling =====
        if not x_label:
            print(graph)
            return

        #===== Create label for bottom =====
        last_row = '  '
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        loop = -1 #for handling large boards
        for i in range(self.width):
            tag = ''

            if not y_label: #only bottom is labelled, so use numbers
                tag = '  ' if i < 9 else ' '
                tag += str(i+1) + ' '
            else:
                loop += 1 if i > 0 and i%26 == 0 else 0
                mini_i = i%26

                tag += '  ' if loop < 0 else ' '
                tag += alpha[mini_i] if loop < 0 else alpha[mini_i] + alpha[loop].lower()
                tag += ' '

            last_row += tag

        print(graph, last_row)

    def place(self, piece, x, y):
        '''
        Returns:
            Piece: replaced piece
        '''
        old_piece = self.board[y][x]
        self.board[y][x] = piece
        return old_piece

if __name__ == '__main__':
    test = Board(8,8)
    test.display()
    test.display(True)
    test.display(True, True)

    tictac = Board(3,3)
    tictac.display(True, True)

    giant = Board(28,20)
    piece = Piece('X')
    giant.display(True, True)
    giant.place(piece, 1, 1)
    giant.display(True)
