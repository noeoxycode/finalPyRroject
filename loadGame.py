# va lire et récupérer les données d'une sauvegarde
import json

from gameStarter import setValues


def loadGame():
    print("Comment se nomme votre sauvegarde")
    name = ""
    while name == "":
        name = input()

    file = open(name+".json")
    data = json.load(file)

    game = {
        "wood": data['wood'],
        "iron": data['iron'],
        "food": data['food'],
        "people": data['people'],
        "houses": data['houses'],
        "date": data['date'],
        "satisfaction": data['satisfaction'],
        "levels": {
            "wood": data['levels']['wood'],
            "iron": data['levels']['iron'],
            "food": data['levels']['food']
        },
        "worker": {
            "inactive": data['worker']['inactive'],
            "active": {
                "wood": data['worker']['active']['wood'],
                "iron": data['worker']['active']['iron'],
                "food": data['worker']['active']['food']
            }
        }
    }
    print(game)
    dif = 1
    setValues(game, dif)
    file.close()