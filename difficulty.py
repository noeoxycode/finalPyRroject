def difficulty():
    i = 0
    print("Choisir un niveau de dificulté:")
    print("1 facile\n2 moyen\n3 difficile")

    while i!=1 or i!=2 or i!=3:
        i = int(input())
        if i == 1:
            return 0.5
        elif i == 2:
            return 1
        elif i == 3:
            return 2
        else:
            print("Mettez 1, 2 ou 3")