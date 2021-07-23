import json
import sched
import time
import datetime

import actions


def startTime(game):
    # lancement du chrono
    date = datetime.datetime(int(game['date'].split("-")[2]), int(game['date'].split("-")[1]), int(game['date'].split("-")[0]))
    print(date.date())

    s = sched.scheduler(time.time, time.sleep)
    s.enter(10, 1, actions.checkActions())
    s.run()


# def getDate():
    # file = json.open("Scenario.json")


def timer(game):
    startTime(game)


def action():
    actions.checkActions()
