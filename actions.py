import game


def endGame:
    print("Game over")

#renvoie un event
def getEvent():
    #recuperation de l'event puis return
    return event


#check si la partie est finie
def checkEndGame(Game game):
    if game.satisfaction <= 0:
        return 1
    else :
        return 0


#application de l'event sur l'objet game
def applyEvent (Game game, Event event):



#check si il est temps de fournir un event,si oui on getEvent puis applyEvent
def checkEvent(Game game):
    if cptWithoutEvent = game.cptWithoutEvent
        Event newEvent = getEvent()
        applyEvent(game, newEvent)





#check si la partie et finie, si elle ne l'est pas, lance checkEvent
def checkActions():
    if checkEndGame(game.satisfaction) == 0:
        checkEvent()
    else :
        endGame()

