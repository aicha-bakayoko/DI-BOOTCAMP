import random


class Game:
    """Classe représentant une partie de Pierre-Papier-Ciseaux."""

    def get_user_item(self):
        """
        Demande à l'utilisateur de choisir rock/paper/scissors.
        Continue de demander jusqu'à obtenir une entrée valide.
        Returns: str ('rock', 'paper' ou 'scissors')
        """
        valid_choices = {"r": "rock", "p": "paper", "s": "scissors"}

        while True:
            user_input = input("Select (r)ock, (p)aper, or (s)cissors: ").lower()
            if user_input in valid_choices:
                return valid_choices[user_input]
            elif user_input in valid_choices.values():
                return user_input
            else:
                print("Invalid choice. Please select rock, paper, or scissors.")

    def get_computer_item(self):
        """
        Sélectionne aléatoirement rock/paper/scissors pour l'ordinateur.
        Returns: str ('rock', 'paper' ou 'scissors')
        """
        items = ["rock", "paper", "scissors"]
        return random.choice(items)

    def get_game_result(self, user_item, computer_item):
        """
        Détermine le résultat de la partie.
        Parameters:
            user_item (str): choix de l'utilisateur
            computer_item (str): choix de l'ordinateur
        Returns: str ('win', 'draw' ou 'loss')
        """
        if user_item == computer_item:
            return "draw"

        winning_combos = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper",
        }

        if winning_combos[user_item] == computer_item:
            return "win"
        else:
            return "loss"

    def play(self):
        """
        Joue une partie complète : récupère les choix, affiche le résultat,
        et retourne le résultat.
        Returns: str ('win', 'draw' ou 'loss')
        """
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"You chose: {user_item[0]}. The computer chose: {computer_item[0]}. Result: {result}")

        return result