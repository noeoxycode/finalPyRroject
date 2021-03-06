import inGame
from inGame import inGameMenu
from datetime import datetime

import actions

game = {
    "wood": 0,
    "iron": 0,
    "food": 0,
    "people": 0,
    "date": 0,
    "houses": 0,
    "dateTime": 0,
    "satisfaction": 0,
    "levels": {
        "wood": 0,
        "iron": 0,
        "food": 0
    },
    "worker": {
        "inactive": 0,
        "active": {
            "wood": 0,
            "iron": 0,
            "food": 0
        }
    }
}


def gameInit():
    while 1:
        if datetime.now().minute % 8 == 0:
            actions.checkActions()
        else:
            inGameMenu(game)
        if datetime.now().minute % 1 == 0:
            actions.getRessources()




def setValues(content, dif):
    game['wood'] = content['wood'] * dif
    game['iron'] = content['iron'] * dif
    game['satisfaction'] = content['satisfaction'] * dif
    game['food'] = content['food'] * dif
    game['houses'] = content['houses'] * dif
    game['people'] = content['people'] * dif
    game['date'] = content['date']
    game['levels']['wood'] = content['levels']['wood'] * dif
    game['levels']['iron'] = content['levels']['iron'] * dif
    game['levels']['food'] = content['levels']['food'] * dif
    game['worker']['inactive'] = content['worker']['inactive'] * dif
    game['worker']['active']['wood'] = content['worker']['active']['wood'] * dif
    game['worker']['active']['iron'] = content['worker']['active']['iron'] * dif
    game['worker']['active']['food'] = content['worker']['active']['food'] * dif
    gameInit()

    # dayAction(game)
