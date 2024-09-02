def caillou_arbres(n):
    diviseur = 2 
    caillou = 0
    arbre = 8
    compteur = 0
    for i in range (1,n):
        compteur += 1
        caillou += arbre/diviseur
        diviseur *= 2
        print(caillou)
        if caillou == 8:
            break
    print(compteur)
caillou_arbres(50)