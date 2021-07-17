import time

game = {
    "wood": 0,
    "iron": 0,
    "food": 0,
    "people": 0,
    "houses": 0,
    "dateTime": 0,
    "satisfaction": 0,
    "levels": {
        "wood": 0,
        "iron": 0,
        "food": 0
    }
}


def gameInit():
    time.time()


def setValues(content, dif):
    game['wood'] = content['wood'] * dif
    game['iron'] = content['iron'] * dif
    game['satisfaction'] = content['satisfaction'] * dif
    game['food'] = content['food'] * dif
    game['houses'] = content['houses'] * dif
    game['people'] = content['people'] * dif
    game['levels']['wood'] = content['levels']['wood'] * dif
    game['levels']['iron'] = content['levels']['iron'] * dif
    game['levels']['food'] = content['levels']['food'] * dif

    print(game)
