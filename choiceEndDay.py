#demande après la fin d'une journée si il veut continuer ou sauvegarder
def choiceEndDay(game):
    print("Que voulez vous faire ?")
    print("1 continuer\n2 Sauvegarder et quitter")
    while i != 1 or i != 2 :
        i = int(input())
        if i == 1:
            #game(game)
            print("continue")
        elif i == 2:
            #Save(game)
            print("save")
        else:
            print("Mettez 1 ou 2")