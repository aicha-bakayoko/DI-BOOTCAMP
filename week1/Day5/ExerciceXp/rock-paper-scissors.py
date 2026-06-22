from game import Game


def get_user_menu_choice():
    """
    Affiche le menu et récupère le choix de l'utilisateur (sans boucle interne).
    Returns: str ('g' ou 'x', ou autre valeur invalide)
    """
    print("""
    Menu:
    (g) Play a new game
    (x) Show scores and exit
    """)
    choice = input(": ").lower()

    if choice not in ["g", "x"]:
        print("Invalid choice. Please select 'g' or 'x'.")

    return choice


def print_results(results):
    """
    Affiche le résumé des résultats et remercie l'utilisateur.
    Parameters:
        results (dict): {'win': int, 'loss': int, 'draw': int}
    """
    print("""
    Game Results:""")
    print(f"     You won {results.get('win', 0)} times")
    print(f"     You lost {results.get('loss', 0)} times")
    print(f"     You drew {results.get('draw', 0)} times")
    print("\n    Thank you for playing!")


def main():
    """Fonction principale : boucle le menu jusqu'à ce que l'utilisateur quitte."""
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()

        if choice == "g":
            game = Game()
            result = game.play()
            results[result] += 1
        elif choice == "x":
            print_results(results)
            break
        # Si le choix est invalide, on ne fait rien : le menu se réaffiche
        # automatiquement au prochain tour de la boucle while.


if __name__ == "__main__":
    main()