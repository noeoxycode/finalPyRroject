import json

def save(game):
    print("Comment voulez vous nommer votre sauvegarde")
    name = ""
    while name == "":
        name = input()
    print("Sauvegarde en cours...")
    file = open(name+".json", "w")
    json.dump(game, file)
    file.close()
