import json


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

    def initialize(id):
        file = open("Scenario.json")
        data = json.load(file)
        for txt in data['scenario']:
            if txt['id'] == id:
                wood = txt['game']['wood']
                #iron = txt['iron']
                #people = txt['people']
                #houses = txt['houses']
                #food = txt['food']
                #satisfaction = txt['satisfaction']
                # self.levels[0] = txt['']
                print(wood)

        file.close()
