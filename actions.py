import json
import sys
import time
from random import choice

import gameStarter
from choiceEndDay import choiceEndDay

cptEvent = 0
cptApplyEvent = 0


def endGame():
    print("Vous avez perdu la partie. Merci d'avoir joué.")
    sys.exit()


# renvoie un event
def getEvent():
    # recuperation de l'event puis return
    file = open("Events.json")
    data = json.load(file)
    events = data['events']
    idMax = max(events, key=lambda ev: ev['id'])
    random = choice(range(0, idMax['id'], 1))
    event = events[random - 1]

    print(event['name'])
    print(event['description'])
    file.close()

    return event


# check si la partie est finie
def checkEndGame():
    if gameStarter.game['satisfaction'] <= 0:
        return 1
    else:
        return 0


# application de l'event sur l'objet game
def applyEvent(event):
    for i in range(len(event['effects'])):
        argsMat = event['effects'][i].split()
        if argsMat[1] == "bois":
            gameStarter.game['wood'] += int(event['effects'][i].split()[0])
        elif argsMat[1] == "fer":
            gameStarter.game['iron'] += int(event['effects'][i].split()[0])
        elif argsMat[1] == "nourriture":
            gameStarter.game['food'] += int(event['effects'][i].split()[0])
        elif argsMat[1] == "population":
            gameStarter.game['people'] += int(event['effects'][i].split()[0])
        elif argsMat[1] == "habitation":
            gameStarter.game['houses'] += int(event['effects'][i].split()[0])
        elif argsMat[1] == "satisfaction":
            gameStarter.game['satisfaction'] += int(event['effects'][i].split()[0])
        elif argsMat[1] == "level":
            if argsMat[2] == "nourriture":
                gameStarter.game['levels']['food'] += int(event['effects'][i].split()[0])
            elif argsMat[2] == "bois":
                gameStarter.game['levels']['wood'] += int(event['effects'][i].split()[0])
            elif argsMat[2] == "fer":
                gameStarter.game['levels']['iron'] += int(event['effects'][i].split()[0])


# check si il est temps de fournir un event,si oui on getEvent puis applyEvent
def checkEvent():
    if cptEvent == 0 and cptApplyEvent == 0:
        newEvent = getEvent()
        # afficher choix pour joueur
        choice = getChoices(newEvent)
        if choice == 1:
            applyEvent(newEvent)


def getChoices(event):
    i = 1
    for txt in (event['choices']):
        print(i, txt)
        i += 1
    id = int(input())
    return id


# check si la partie et finie, si elle ne l'est pas, lance checkEvent
def checkActions():
    if checkEndGame() == 0:
        checkEvent()
        choiceEndDay()
    else:
        endGame()


def getRessources():
    # ici la recup des ressources toutes les heures
    gameStarter.game['wood'] += gameStarter.game['worker']['active']['wood'] * 3
    gameStarter.game['iron'] += gameStarter.game['worker']['active']['iron'] * 3
    gameStarter.game['food'] += gameStarter.game['worker']['active']['food'] * 3
    time.sleep(40)
