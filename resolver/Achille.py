def paradox_achille_tortue (position_achille = 0.0, position_tortue = 10.0, vitesse_achille = 2.0,  vitesse_tortue = 1.0):

    for i in range (1000):

        # Calcul du temps que met Achille à aller à la dernière position de la tortue
        temps = ( position_tortue - position_achille ) / vitesse_achille
    
        # Achille se situe donc a à la dernière position de la tortue
        position_achille = position_tortue

        # Calcul de la distance parcouru par la tortue selon sa vitesse et le temps calculé plus haut
        position_tortue = position_tortue + (temps * vitesse_tortue)

        print (i+1," temps ",temps)
        print (" achille ",position_achille)
        print (" tortue ",position_tortue)

        if position_tortue == position_achille:
            break
if __name__ == "__main__" :
    paradox_achille_tortue ()