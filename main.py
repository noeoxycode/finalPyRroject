# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

import schedule, time
import gameStarter
import loadGame
from newGame import newGame


# début du programme, permet de choisir si on veut commencer une nouvelle partie ou charger une partie existante
def start():
    print("\nBonjour et bienvenue à The King of Pountos\n")
    print("1 Nouvelle partie\n2 Charger une partie\n3 Quitter")
    i = 0

    while i != 1 or i != 2:
        i = int(input())
        if i == 1:
            newGame()
            while i == 1:
                gameStarter.gameInit()
        elif i == 2:
            # lui permettra de choisir la save qu'il veut
            loadGame.loadGame()
        elif i == 3:
            # quitte le programme
            print("Merci d'avoir joué.")
            sys.exit()
        else:
            print("Mettez un nombre entre 1 et 2")

if __name__ == '__main__':
    start()


while 1:
    schedule.run_pending()
    time.sleep(10)