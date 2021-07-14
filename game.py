import time


class Game:
    def __init__(self, wood, iron, satisfaction):
        self.wood = wood
        self.iron = iron
        self.satisfaction = satisfaction


game = Game(10, 10, 10)


def gameInit():
    time.time()
