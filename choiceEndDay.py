#demande après la fin d'une journée si il veut continuer ou sauvegarder
import time

import actions
from game import gameInit


def choiceEndDay():
    print("\nQue voulez vous faire ?")
    print("1 continuer\n2 Sauvegarder et quitter")
    i = 0
    while i != 1 or i != 2 :
        i = int(input())
        if i == 1:
            #game(game)
            print("Chargement...\n")
            time.sleep(60)
            gameInit()
        elif i == 2:
            #Save(game)
            print("save")
        else:
            print("Mettez 1 ou 2")