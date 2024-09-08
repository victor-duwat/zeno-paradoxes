import pygame
import time

pygame.init()
LARGEUR_FENETRE = 800
HAUTEUR_FENETRE = 200

BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
NOIR = (0, 0, 0)

POSITION_ACHILLE = 0.0
POSITION_TORTUE = 10.0
VITESSE_ACHILLE = 2.0
VITESSE_TORTUE = 1.0
TEMPS = 0

def calcul_paradox():
    global POSITION_ACHILLE, POSITION_TORTUE, TEMPS
    TEMPS = (POSITION_TORTUE - POSITION_ACHILLE) / VITESSE_ACHILLE
    POSITION_ACHILLE = POSITION_TORTUE
    POSITION_TORTUE += TEMPS * VITESSE_TORTUE

def affichage_terminal():
    for i in range(1000):
        calcul_paradox()
        print(i + 1, " TEMPS ", TEMPS)
        print(" achille ", POSITION_ACHILLE)
        print(" tortue ", POSITION_TORTUE)

        if POSITION_TORTUE == POSITION_ACHILLE:
            break

def affichage_graphique():
    running = True
    animation_started = False 
    fenetre = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
    pygame.display.set_caption("Paradoxe d'Achille et de la tortue")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    animation_started = True  
        fenetre.fill(NOIR)

        if animation_started:
            pygame.draw.circle(fenetre, ROUGE, (int(POSITION_ACHILLE * 40), HAUTEUR_FENETRE // 2), 10)
            pygame.draw.circle(fenetre, VERT, (int(POSITION_TORTUE * 40), HAUTEUR_FENETRE // 2), 10)
            calcul_paradox()

            if POSITION_TORTUE == POSITION_ACHILLE:
                break

            time.sleep(0.75)

        else:
            font = pygame.font.Font(None, 36)
            texte = font.render("Appuyez sur Espace pour commencer", True, BLANC)
            fenetre.blit(texte, (LARGEUR_FENETRE // 4, HAUTEUR_FENETRE // 2 - 20))

        pygame.display.flip()

    pygame.quit()

def input_choix():
    choix = int(input("1 pour affichage en terminal, 2 pour affichage en interface graphique: "))
    return choix

def lancement_affichage(choix):
    if choix == 1:
        affichage_terminal()
    elif choix == 2:
        affichage_graphique()
    else:
        input_choix()

def main():
    choix = input_choix()
    lancement_affichage(choix)

if __name__ == "__main__":
    main()
