# demande après la fin d'une journée si il veut continuer ou sauvegarder
import time

import gameStarter
from save import save


def choiceEndDay():
    print("\nQue voulez vous faire ?")
    print("1 continuer\n2 Sauvegarder et quitter")
    i = 0
    while i != 1 or i != 2:
        i = int(input())
        if i == 1:
            gameStarter.game['food'] -= gameStarter.game['people']
            print("Vous consommez", gameStarter.game['people'], "par jour.")
            print("Chargement...\n")
            time.sleep(60)
            gameStarter.gameInit()
        elif i == 2:
            save(gameStarter.game)
            print("save")
        else:
            print("Mettez 1 ou 2")