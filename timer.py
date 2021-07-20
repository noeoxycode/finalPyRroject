import json
import sched
import time
import datetime

import actions
import game


def startTime():
    # lancement du chrono
    print(game.game['date'])
    date = datetime.datetime(2021, 7, 11)
    # print(time.time())
    s = sched.scheduler(time.time, time.sleep)
    s.enter(10, 1, actions)
    s.run()
    # chrono = threading.Timer(8, actions)
    # chrono.start()
    # print(time.hour)
    # return datetime


def getDate():
    file = json.open("Scenario.json")


def timer():
    startTime()


def actions():
    actions.checkActions()

