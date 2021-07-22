def inGameMenu() :
    print("Quelle action voulez-vous effectuer ?")
    print("1 : Voir la disposition actuelle de vos ouvriers")
    print("2 : Retirer x ouvrier(s) d'une zone de production")
    print("3 : Assigner un ouvrier libre à une tache")
    print("4 : Quitter")
    val = input("Entrer le chiffre correspondant à votre souhait")


def menuChoice(value):
    if value == 1 : displayOrganisation();
    elif value == 2 : removeWorker();
    elif value == 3 : putWorkerOnWork();
    else : print("Erreur de saisie, veuillez reessayer")


def displayOrganisation():


def removeWorker():

def putWorkerOnWork():