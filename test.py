def getEvent():
    #recuperation de l'event puis return
    file = open("Event.json")
    data = json.load(file)
    idMax = max(data['id'])
    random = range(0, idMax, 1)
    print(random)
    #return event
