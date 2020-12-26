from Engine import main
import time
import os

main()
choice = False
while not choice:
    restart = input ("Do you want to play again: y/N ").lower()
    if restart == "y":
        main()
        if os.name == 'nt':
          os.system('cls')
        else:
          os.system('clear')
    elif restart == "n":
        choice = True
        time.sleep(1)
