import json

from difficulty import difficulty


class Initialize:
    wood = 0
    iron = 0
    people = 0
    houses = 0
    food = 0
    satisfaction = 0
    levels = [0, 0, 0]

    def __init__(self, wood, iron, people, houses, food, satisfaction, levels):
        self.wood = wood
        self.iron = iron
        self.people = people
        self.houses = houses
        self.food = food
        self.satisfaction = satisfaction
        self.levels = levels
# initialise la partie selon le scénario choisi
    def initialize(id):
        file = open("Scenario.json")
        data = json.load(file)
        for txt in data['scenario']:
            if txt['id'] == id:
                wood = txt['game']['wood']
                iron = txt['game']['iron']
                people = txt['game']['people']
                houses = txt['game']['houses']
                food = txt['game']['food']
                satisfaction = txt['game']['satisfaction']
                levels = [txt['game']['levels']['wood'], txt['game']['levels']['iron'], txt['game']['levels']['food']]
        game = Initialize(wood, iron, people, houses, food, satisfaction, levels)
# récup le multiplicateur selon la difficulté choisi
        dif = difficulty()
#appel la fonction qui débute la partie avec en parametre l'objet game et le multiplicateur de la difficulté
        #debutgame(game,dif)
        file.close()
