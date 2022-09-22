#main.py

import ConnectFour, TicTacToe

from utils import my_os

GAMES = {1: "ConnectFour",
         2: "TicTacToe",
        }

if __name__ == '__main__':
    my_os.clear()

    print('Which game would you like to play?\n')

    for x in range(1, len(GAMES)+1):
        print('  {}. {}'.format(x, GAMES[x]))

    try:
        choice = input('\nPlease select a number: ')
        while not (choice.isnumeric() and 0 < int(choice) < len(GAMES)):
            choice = input('"{}" is not a valid choice. Try again: '.format(choice))

        my_os.clear()
        print('Playing {}'.format(GAMES[int(choice)]))
        locals()[GAMES[int(choice)]].main()

    except KeyboardInterrupt:
        my_os.goodbye()

    print('Quitting...')
