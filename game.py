import time

game = {
    "wood": 50,
    "iron": 20,
    "food": 100,
    "people": 150,
    "houses": 5,
    "dateTime": 0,
    "satisfaction": 15,
    "levels": {
        "wood": 1,
        "iron": 1,
        "food": 2
    }
}


class Game:
    def __init__(self, wood, iron, satisfaction):
        game['wood'] = wood
        game['iron'] = iron
        game['satisfaction'] = satisfaction


# game = Game(10, 10, 10)


def gameInit():
    time.time()
