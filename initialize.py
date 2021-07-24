import json

from difficulty import difficulty
from game import setValues


# initialise la partie selon le scénario choisi
def initialize(id):
    game = {}
    file = open("Scenario.json")
    data = json.load(file)
    for txt in data['scenario']:
        if txt['id'] == id:
            print("Vous avez choisi le scénario", txt['name'])
            print(txt['description'], "\n")
            game = {
                "wood": txt['game']['wood'],
                "iron": txt['game']['iron'],
                "food": txt['game']['food'],
                "people": txt['game']['people'],
                "houses": txt['game']['houses'],
                "date": txt['date'],
                "dateTime": 0,
                "satisfaction": txt['game']['satisfaction'],
                "levels": {
                    "wood": txt['game']['levels']['wood'],
                    "iron": txt['game']['levels']['iron'],
                    "food": txt['game']['levels']['food']
                },
                "worker": {
                    "inactive": txt['game']['worker']['inactive'],
                    "active": {
                        "wood": txt['game']['worker']['active']['wood'],
                        "iron": txt['game']['worker']['active']['iron'],
                        "food": txt['game']['worker']['active']['food']
                    }
                }
            }

    dif = difficulty()
    setValues(game, dif)
    file.close()
