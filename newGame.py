import json

from initialize import Initialize


def newGame():
    i = 1;
    print("Choisissez un scénario: ")
    file = open("Scenario.json")
    data = json.load(file)
    for txt in data['scenario']:
        print(i,txt['name'])
        i +=1

    file.close()
    id = int(input())
    Initialize.initialize(id)


