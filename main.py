from resolver.achille import main
from resolver.caillou import arbre_cailloux
from resolver.fleche import fleche
fin = False
while not fin :
    a_repondu = False
    while (a_repondu == False) :
        try :
            choix = int (input ("Choisiser 1 pour Achille.py 2 pour arbre_cailloux.py 3 pour Fleche.py ou 4 pour arreter le programe: "))
            if choix <= 3 and choix >= 1:
                a_repondu = True
            elif choix == 4 :
                fin = True
                a_repondu = True
        except :
            print ("mauvaise saisie")

    if choix == 1:
        main()

    if choix == 2 :
        arbre_cailloux()

    if choix == 3:
        fleche ()
