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
            game = {
                "wood": txt['game']['wood'],
                "iron": txt['game']['iron'],
                "food": txt['game']['food'],
                "people": txt['game']['people'],
                "houses": txt['game']['houses'],
                "dateTime": 0,
                "satisfaction": txt['game']['satisfaction'],
                "levels": {
                    "wood": txt['game']['levels']['wood'],
                    "iron": txt['game']['levels']['iron'],
                    "food": txt['game']['levels']['food']
                }
            }

    dif = difficulty()
    setValues(game, dif)
    file.close()
