# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import actions
from loadGame import loadGame
from newGame import newGame

# début du programme, permet de choisir si on veut commencer une nouvelle partie ou charger une partie existante
def start():
    print("\nBonjour et bienvenue à The King of Pountos\n")
    print("1 Nouvelle partie\n2 Charger une partie")
    i = 0
    while i!=1 or i!=2:
        i = int(input())
        if i == 1:
            actions.getEvent()
            #newGame()
        elif i == 2:
            loadGame()
        else:
            print("Mettez un nombre entre 1 et 2")
if __name__ == '__main__':
    start()
