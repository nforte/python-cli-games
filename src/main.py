#main.py
from games import *
from utils.my_os import clear

if __name__ == '__main__':
    clear()

    print('\nWhich game would you like to play?\n')

    for x in range(1, len(GAMES)+1):
        print('  {}. {}'.format(x, GAMES[x]))

    choice = input('\nPlease select a number: ')
    if ( not choice.isnumeric()
         or int(choice) > len(GAMES)
         or int(choice) <= 0):
         print('"{}" is not a valid choice'.format(choice))

    else:
        clear()
        print('Playing {}'.format(GAMES[int(choice)]))
        locals()[GAMES[int(choice)]].main()

    print('Quitting...')
