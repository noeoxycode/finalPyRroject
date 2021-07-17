import json
from random import choice

from game import game


def endGame():
    print("Game over")


# renvoie un event
def getEvent():
    # recuperation de l'event puis return
    file = open("Events.json")
    data = json.load(file)
    events = data['events']
    idMax = max(events, key=lambda ev: ev['id'])
    random = choice(range(0, idMax['id'], 1))
    event = events[random - 1]
    return event


# check si la partie est finie
def checkEndGame():
    if game.satisfaction <= 0:
        return 1
    else:
        return 0


# application de l'event sur l'objet game
def applyEvent(event):
    for i in range(len(event['effects'])):
        argsMat = event['effects'][i].split()
        if argsMat[1] == "bois":
            game['wood'] += int(event['effects'][i].split()[0])
        elif argsMat[1] == "fer":
            game['iron'] += int(event['effects'][i].split()[0])
        elif argsMat[1] == "nourriture":
            game['food'] += int(event['effects'][i].split()[0])
        elif argsMat[1] == "population":
            game['people'] += int(event['effects'][i].split()[0])
        elif argsMat[1] == "habitation":
            game['houses'] += int(event['effects'][i].split()[0])
        elif argsMat[1] == "satisfaction":
            game['satisfaction'] += int(event['effects'][i].split()[0])
        elif argsMat[1] == "level":
            if argsMat[2] == "nourriture":
                game['levels']['food'] += int(event['effects'][i].split()[0])
            elif argsMat[2] == "bois":
                game['levels']['wood'] += int(event['effects'][i].split()[0])
            elif argsMat[2] == "fer":
                game['levels']['iron'] += int(event['effects'][i].split()[0])

    return 0


# check si il est temps de fournir un event,si oui on getEvent puis applyEvent
def checkEvent():
    cptWithoutEvent = 0
    if cptWithoutEvent == game.cptWithoutEvent:
        newEvent = getEvent()
        applyEvent(newEvent)


# check si la partie et finie, si elle ne l'est pas, lance checkEvent
def checkActions():
    if checkEndGame() == 0:
        checkEvent()
    else:
        endGame()
