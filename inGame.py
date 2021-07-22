
def inGameMenu(game) :
    print("Quelle action voulez-vous effectuer ?")
    print("1 : Voir la disposition actuelle de vos ouvriers")
    print("2 : Retirer x ouvrier(s) d'une zone de production")
    print("3 : Assigner un ouvrier libre à une tache")
    print("4 : Quitter")
    val = int(input())
    menuChoice(val,game)


def menuChoice(value,game):
    if value == 1 : displayOrganisation();
    elif value == 2 : removeWorker();
    elif value == 3 : putWorkerOnWork(game);
    else : print("Erreur de saisie, veuillez reessayer")

#affiche le nombre de workers par poste de travail
#exemple : wood : 12 iron : 5 food : 2 inactive : 6
def displayOrganisation():
    print("yes")

#retirer un worker d'un poste de travail le rendant inactif
def removeWorker():
    print("yes")

#prend x workers inactifs pour les placer sur le poste de travail souhaité
def putWorkerOnWork(game):
    inactifs = game['people']
    nbrWood = 0
    nbrIron = 0
    nbrFood = 0
    i = 0
    while i != 4:
        print("1 ajouter des ouvriers chercher du bois")
        print("2 ajouter des ouvriers à l'usine")
        print("3 ajouter des ouvriers faire de la nourriture")
        print("4 Quitter")
        i = int(input())
        if i == 1:
            print("Vous avez", inactifs,"de personnes inactifs")
            print("Combien de personne voulez vous déplacer ?")
            j = int(input())
            if j <= inactifs:
                inactifs = inactifs-j
                nbrWood = nbrWood + j
            else:
                print("Vous n'avez pas assez de personnes inactives")
        elif i == 2:
            print("Vous avez", inactifs,"de personnes inactifs")
            print("Combien de personne voulez vous déplacer ?")
            j = int(input())
            if j <= inactifs:
                inactifs = inactifs - j
                nbrIron = nbrIron + j
            else:
                print("Vous n'avez pas assez de personnes inactives")
        elif i == 3:
            print("Vous avez", inactifs,"de personnes inactifs")
            print("Combien de personne voulez vous déplacer ?")
            j = int(input())
            if j <= inactifs:
                inactifs = inactifs - j
                nbrFood = nbrFood + j
            else:
                print("Vous n'avez pas assez de personnes inactives")
        elif i == 4:
            print("Faudrait quitter en fait")
            print(nbrWood)
            print(nbrIron)
            print(nbrFood)
        else:
            print("Mettre un nombre entre 1 et 4")