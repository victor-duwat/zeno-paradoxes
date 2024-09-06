import pygame
import time


def paradox_achille_tortue(position_achille=0.0, position_tortue=10.0, vitesse_achille=2.0, vitesse_tortue=1.0, seuil=19):

    pygame.init()

    largeur_fenetre = 800
    hauteur_fenetre = 200
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Paradoxe d'Achille et de la tortue")


    blanc = (255, 255, 255)
    rouge = (255, 0, 0)
    vert = (0, 255, 0)
    noir = (0, 0, 0)

    running = True
    for i in range(1000):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        
        temps = (position_tortue - position_achille) / vitesse_achille

        position_achille = position_tortue

        position_tortue += temps * vitesse_tortue

        fenetre.fill(noir)


        pygame.draw.circle(fenetre, rouge, (int(position_achille * 40), hauteur_fenetre // 2), 10)
        pygame.draw.circle(fenetre, vert, (int(position_tortue * 40), hauteur_fenetre // 2), 10)

        pygame.display.flip()

        print(i+1, " temps ", temps)
        print(" achille ", position_achille)
        print(" tortue ", position_tortue)

        time.sleep(0.5)

        if position_tortue == position_achille:
            break

        if not running:
            break

    pygame.quit()

if __name__ == "__main__":
    paradox_achille_tortue()
