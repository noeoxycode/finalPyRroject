# va lire et récupérer les données d'une sauvegarde
import json

from game import setValues


def loadGame(id):

    game = {}
    file = open("Save.json")
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
    dif = 3
    setValues(game, dif)
    file.close()