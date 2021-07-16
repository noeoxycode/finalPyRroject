import json
from random import choice

import game


def endGame():
    print("Game over")

#renvoie un event
def getEvent():
    #recuperation de l'event puis return
    file = open("Events.json")
    data = json.load(file)
    events = data['events']
    idMax = max(events, key=lambda ev: ev['id'])
    random = choice(range(0, idMax['id'], 1))
    event = events[random-1]
    return event


#check si la partie est finie
def checkEndGame(game):
    if game.satisfaction <= 0:
        return 1
    else :
        return 0


#application de l'event sur l'objet game
def applyEvent (game, event):
    return 0


#check si il est temps de fournir un event,si oui on getEvent puis applyEvent
def checkEvent(game):
    cptWithoutEvent = 0
    if cptWithoutEvent == game.cptWithoutEvent:
        newEvent = getEvent()
        applyEvent(game, newEvent)





#check si la partie et finie, si elle ne l'est pas, lance checkEvent
def checkActions():
    if checkEndGame(game.satisfaction) == 0:
        checkEvent()
    else :
        endGame()

