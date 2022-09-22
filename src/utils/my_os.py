from os import system,name

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def goodbye():
    print("\n\nThanks for playing! Have a nice day!")
    exit()
