from resolver.Achille import paradox_achille_tortue
from resolver.ArbreCailloux import arbre_cailloux
from resolver.Fleche import fleche
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
        arbre_cailloux()

    if choix == 3:
        fleche ()