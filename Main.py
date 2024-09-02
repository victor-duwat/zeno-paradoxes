from Achille import paradox_achille_tortue
from arbre_cailloux import caillou_arbres
from Fleche import flecche
fin = False
while not fin :
    reponse = False
    while (reponse == False) :
        try :
            choix = int (input ("Choisiser 1 pour Achille.py 2 pour arbre_cailloux.py 3 pour Fleche.py ou 4 pour arreter le programe: "))
            if choix <= 3 and choix >= 1:
                reponse = True
            elif choix == 4 :
                fin = True
                reponse = True
        except :
            print ("mauvaise saisie")

    if choix == 1:
        paradox_achille_tortue()

    if choix == 2 :
        caillou_arbres()

    if choix == 3:
        flecche ()