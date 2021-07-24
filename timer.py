import schedule, time
import datetime

import actions
from choiceEndDay import choiceEndDay


def startTime(game):
    # lancement du chrono
    date = datetime.datetime(int(game['date'].split("-")[2]), int(game['date'].split("-")[1]), int(game['date'].split("-")[0]))
    print(date.date())


def test():
    print("test")


def timer(game):
    startTime(game)


def action():
    actions.checkActions()
