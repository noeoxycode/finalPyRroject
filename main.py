# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import schedule, time

import actions
import choiceEndDay
import game
import timer
from loadGame import loadGame
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
            # time.timer()
            # boucles toutes les 8 minutes pour déclencher un évènement
            # mettre bon ou mauvais event dans JSON
            # actions.checkActions()
            # newEvent = actions.getEvent()
            # afficher choix pour joueur
            # choice = actions.getChoices(newEvent)
            # if choice == 1:
                # actions.applyEvent(newEvent)
            while i == 1:
                game.gameInit()
        elif i == 2:
            # lui permettra de choisir la save qu'il veut
            # j = 1;
            # print("Choisissez un scénario: ")
            # file = open("Scenario.json")
            # data = json.load(file)
            # for txt in data['scenario']:
            #   print(j, txt['name'])
            #  j += 1

            # file.close()
            # id = int(input())
            # loadGame(id)
            newGame()
        else:
            print("Mettez un nombre entre 1 et 2")

if __name__ == '__main__':
    start()


while 1:
    schedule.run_pending()
    time.sleep(10)