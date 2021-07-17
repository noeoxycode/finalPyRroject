import json


# permet de choisir le scénario que le joueur veut
from initialize import initialize


def newGame():
    i = 1;
    print("Choisissez un scénario: ")
    file = open("Scenario.json")
    data = json.load(file)
    for txt in data['scenario']:
        print(i, txt['name'])
        i += 1

    file.close()
    id = int(input())
    initialize(id)
