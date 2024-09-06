import pygame
import time

pygame.init()
LARGEUR_FENETRE = 800
HAUTEUR_FENETRE = 200


BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
NOIR = (0, 0, 0)

POSITION_ACHILLE=0.0
POSITION_TORTUE=10.0
VITESSE_ACHILLE=2.0
VITESSE_TORTUE=1.0
TEMPS = 0

def calcul_paradox():

    global POSITION_ACHILLE, POSITION_TORTUE, TEMPS
    
    TEMPS = (POSITION_TORTUE - POSITION_ACHILLE) / VITESSE_ACHILLE

    POSITION_ACHILLE = POSITION_TORTUE

    POSITION_TORTUE += TEMPS * VITESSE_TORTUE


    
def affichage_terminal():
    for i in range(1000):
        calcul_paradox()
        print(i+1, " TEMPS ", TEMPS)
        print(" achille ", POSITION_ACHILLE)
        print(" tortue ", POSITION_TORTUE)

        if POSITION_TORTUE == POSITION_ACHILLE:
            break

def affichage_graphique():
    running = True
    fenetre = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
    pygame.display.set_caption("Paradoxe d'Achille et de la tortue")
    for i in range(1000):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        fenetre.fill(NOIR)
        pygame.draw.circle(fenetre, ROUGE, (int(POSITION_ACHILLE * 40), HAUTEUR_FENETRE // 2), 10)
        pygame.draw.circle(fenetre, VERT, (int(POSITION_TORTUE * 40), HAUTEUR_FENETRE // 2), 10)

        calcul_paradox()

        pygame.display.flip()
        time.sleep(0.75)
        if POSITION_TORTUE == POSITION_ACHILLE:
            break

        if not running:
            break

    pygame.quit()

def choisir_affichage():
    a_repondu = False
    while a_repondu == False:

        choix = int(input("1 pour affichage en terminal, 2 pour affichage en interface graphique: "))
        if choix == 1:
            affichage_terminal()
            a_repondu = True
        elif choix == 2:
            affichage_graphique()
            a_repondu = True
        else :
            print ("mauvaise saisie")

if __name__ == "__main__": 
    choisir_affichage()