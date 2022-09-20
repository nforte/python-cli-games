#main.py
from games import *

if __name__ == '__main__':
    print('\nWhich game would you like to play?\n')

    for x in range(1, len(GAMES)+1):
        print('  {}. {}'.format(x, GAMES[x]))

    choice = input('\nPlease select a number: ')
    if ( not choice.isnumeric()
         or int(choice) > len(GAMES)
         or int(choice) <= 0):
         print('"{}" is not a valid choice'.format(choice))

    else:
        print('Playing {}'.format(GAMES[int(choice)]))
        locals()[GAMES[int(choice)]].main('Player 1', 'Player 2')

    print('Quitting...')
