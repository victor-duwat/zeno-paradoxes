import time
import os

def arbre_cailloux():
    diviseur = 2.0
    caillou = 0.0
    arbre = 8.0
    longueur_piste = 30

    for iteration in range(50):
        caillou += arbre / diviseur
        diviseur *= 2
        progression = int((caillou / arbre) * longueur_piste)

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Progrès: [{'=' * progression}{' ' * (longueur_piste - progression)}] {caillou:.5f}/8.00 unités")
        print(f"Iteration: {iteration + 1}, diviseur actuel: {diviseur // 2}")

        if caillou >= arbre - 0.001:
            print("Le caillou est infiniment proche de l'arbre, mais il ne l'atteindra jamais.")
            break

        time.sleep(0.5)

if __name__ == "__main__":
    arbre_cailloux()
