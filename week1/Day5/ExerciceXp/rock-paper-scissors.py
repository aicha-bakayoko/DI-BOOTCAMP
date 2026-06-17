"""
rock-paper-scissors.py
Fichier principal : menu, gestion des parties et affichage du récapitulatif.
"""

from game import Game


def get_user_menu_choice():
    """
    Affiche le menu et retourne le choix de l'utilisateur (sans boucle).
    Choix possibles : '1' (jouer), '2' (scores), 'q' (quitter).
    """
    print("\n" + "=" * 35)
    print("   🪨📄✂️  PIERRE - FEUILLE - CISEAUX")
    print("=" * 35)
    print("  1. Jouer une nouvelle partie")
    print("  2. Afficher les scores")
    print("  q. Quitter")
    print("=" * 35)

    choix = input("Votre choix : ").strip().lower()
    return choix


def print_results(results):
    """
    Affiche le récapitulatif de toutes les parties jouées.
    Paramètre : results — dict au format {win: int, loss: int, draw: int}
    """
    total = results["win"] + results["loss"] + results["draw"]

    print("\n" + "=" * 35)
    print("        📊 RÉCAPITULATIF")
    print("=" * 35)
    print(f"  Parties jouées : {total}")
    print(f"  🏆 Victoires   : {results['win']}")
    print(f"  😞 Défaites    : {results['loss']}")
    print(f"  🤝 Matchs nuls : {results['draw']}")
    print("=" * 35)
    print("  Merci d'avoir joué ! À bientôt 👋")
    print("=" * 35)


def main():
    """
    Fonction principale :
    - Affiche le menu en boucle
    - Gère les parties et le suivi des scores
    - Affiche le récapitulatif à la sortie
    """
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choix = get_user_menu_choice()

        if choix == "1":
            game = Game()
            result = game.play()
            results[result] += 1

        elif choix == "2":
            print_results(results)

        elif choix in ("q", "x"):
            print_results(results)
            break

        else:
            print("❌ Choix invalide. Entrez 1, 2 ou q.")


if __name__ == "__main__":
    main()
