import gameStarter


def dayAction(game):
    print("Voulez vous effectuer des actions en attendant le prochain évènement ?")
    print("(1 = oui, 2 = non)")
    val = ""
    while val != 1 or val != 2:
        val = int(input())
    if val == 1:
        inGameMenu(game)
    else:
        gameStarter.gameInit()

def inGameMenu(game):
    print("Quelle action voulez-vous effectuer ?")
    print("1 : Voir la disposition actuelle de vos ouvriers")
    print("2 : Retirer x ouvrier(s) d'une zone de production")
    print("3 : Assigner un ouvrier libre à une tache")
    print("4 : Voir les ressources à disposition et la production horaire")
    val = int(input())
    menuChoice(val, game)


def menuChoice(value,game):
    if value == 1 : displayOrganisation(game)
    elif value == 2 : removeWorker(game)
    elif value == 3 : putWorkerOnWork(game)
    elif value == 4 : ressourcesView(game)
    else : print("Erreur de saisie, veuillez reessayer")
    inGameMenu(game)

#affiche le nombre de workers par poste de travail
#exemple : wood : 12 iron : 5 food : 2 inactive : 6
def displayOrganisation(game):
    i = 0
    while i != 1:
        print("inactifs", game['worker']['inactive'])
        print("wood", game['worker']['active']['wood'])
        print("iron", game['worker']['active']['iron'])
        print("food", game['worker']['active']['food'])
        print("Taper 1 pour revenir au menu")
        i = int(input())
        gameStarter.gameInit()



#retirer un worker d'un poste de travail le rendant inactif
def removeWorker(game):
    i = 0
    while i != 4:
        print("1 retirer des ouvriers partie chercher du bois")
        print("2 retirer des ouvriers partie à l'usine")
        print("3 retirer des ouvriers partie faire de la nourriture")
        print("4 Retour")
        i = int(input())
        if i == 1:
            if game['worker']['active']['wood'] == 0 :
                print("Vous n'avez pas d'ouvrier sur ce poste de travail\n")
            else :
                print("Vous avez", game['worker']['active']['wood'], "de personnes partie chercher du bois")
                print("Combien de personne voulez vous déplacer ?")
                j = int(input())
                if j <= game['worker']['active']['wood']:
                    game['worker']['active']['wood']= game['worker']['active']['wood'] - j
                    game['worker']['inactive'] = game['worker']['inactive'] + j
                else:
                    print("Vous n'avez pas assez de personnes inactives")
        elif i == 2:
            if game['worker']['active']['wood'] == 0 :
                print("Vous n'avez pas d'ouvrier sur ce poste de travail\n")
            else :
                print("Vous avez", game['worker']['active']['iron'], "de personnes partie à l'usine")
                print("Combien de personne voulez vous déplacer ?")
                j = int(input())
                if j <= game['worker']['active']['iron']:
                    game['worker']['active']['iron'] = game['worker']['active']['iron'] - j
                    game['worker']['inactive'] = game['worker']['inactive'] + j

                else:
                    print("Vous n'avez pas assez de personnes inactives")
        elif i == 3:
            if game['worker']['active']['wood'] == 0 :
                print("Vous n'avez pas d'ouvrier sur ce poste de travail\n")
            else :
                print("Vous avez", game['worker']['active']['food'], "de personnes partie faire de la nourriture")
                print("Combien de personne voulez vous déplacer ?")
                j = int(input())
                if j <= game['worker']['active']['food']:
                    game['worker']['active']['food'] = game['worker']['active']['food'] - j
                    game['worker']['inactive'] = game['worker']['inactive'] + j
                else:
                    print("Vous n'avez pas assez de personnes inactives")
        elif i == 4:
            gameStarter.gameInit()

        else:
            print("Mettre un nombre entre 1 et 4")

#prend x workers inactifs pour les placer sur le poste de travail souhaité
def putWorkerOnWork(game):
    i = 0
    while i != 4:
        print("1 ajouter des ouvriers chercher du bois")
        print("2 ajouter des ouvriers à l'usine")
        print("3 ajouter des ouvriers faire de la nourriture")
        print("4 Retour")
        i = int(input())
        if i == 1:
            print("Vous avez", game['worker']['inactive'],"de personnes inactifs")
            print("Combien de personne voulez vous déplacer ?")
            j = int(input())
            if j <= game['worker']['inactive']:
                game['worker']['inactive'] = game['worker']['inactive']-j
                game['worker']['active']['wood'] = game['worker']['active']['wood'] + j
                print("Vous avez déplacer",j,"ouvriers pour aller chercher du bois\n")
            else:
                print("Vous n'avez pas assez de personnes inactives")
        elif i == 2:
            print("Vous avez", game['worker']['inactive'],"de personnes inactifs")
            print("Combien de personne voulez vous déplacer ?")
            j = int(input())
            if j <= game['worker']['inactive']:
                game['worker']['inactive'] = game['worker']['inactive'] - j
                game['worker']['active']['iron'] = game['worker']['active']['iron'] + j
                print("Vous avez déplacer", j, "ouvriers à l'usine\n")
            else:
                print("Vous n'avez pas assez de personnes inactives")
        elif i == 3:
            print("Vous avez", game['worker']['inactive'],"de personnes inactifs")
            print("Combien de personne voulez vous déplacer ?")
            j = int(input())
            if j <= game['worker']['inactive']:
                game['worker']['inactive'] = game['worker']['inactive'] - j
                game['worker']['active']['food'] = game['worker']['active']['food'] + j
                print("Vous avez déplacer", j, "ouvriers pour aller faire de la nourriture\n")
            else:
                print("Vous n'avez pas assez de personnes inactives")
        elif i == 4:
            gameStarter.gameInit()

        else:
            print("Mettre un nombre entre 1 et 4")

#affiche l'ensemble des ressources à disposition du joueur ainsi que sa production horaire par ressource
#exemple : wood : 200 12wood/h
def ressourcesView(game):
    i = 0
    while i != 1:
        print("wood: ", game["wood"], " production: ", game['worker']['active']['wood'], "/3h")
        print("iron: ", game["iron"], " production: ", game['worker']['active']['iron'], "/3h")
        print("food: ", game["food"], " production: ", game['worker']['active']['food'], "/3h")
        print("Taper 1 pour revenir au menu")
        i = int(input())
        gameStarter.gameInit()
