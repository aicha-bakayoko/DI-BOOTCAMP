"""
game.py
Contient la classe Game pour jouer à Pierre-Feuille-Ciseaux contre l'ordinateur.
"""

import random


class Game:

    ITEMS = ["rock", "paper", "scissors"]

    def get_user_item(self):
        """Demande à l'utilisateur de choisir rock/paper/scissors avec validation."""
        while True:
            choix = input("Choisissez (rock / paper / scissors) : ").strip().lower()
            if choix in self.ITEMS:
                return choix
            print(f"❌ Choix invalide. Veuillez entrer 'rock', 'paper' ou 'scissors'.")

    def get_computer_item(self):
        """Sélectionne aléatoirement un élément pour l'ordinateur."""
        return random.choice(self.ITEMS)

    def get_game_result(self, user_item, computer_item):
        """
        Détermine le résultat de la partie.
        Retourne : 'win', 'draw', ou 'loss'
        """
        if user_item == computer_item:
            return "draw"

        winning_combos = {
            "rock": "scissors",
            "scissors": "paper",
            "paper": "rock",
        }

        if winning_combos[user_item] == computer_item:
            return "win"
        else:
            return "loss"

    def play(self):
        """
        Joue une partie complète :
        - Récupère le choix de l'utilisateur
        - Génère le choix de l'ordinateur
        - Détermine et affiche le résultat
        Retourne : 'win', 'draw' ou 'loss'
        """
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        # Affichage du résultat
        if result == "win":
            message = f"🏆 Vous avez choisi {user_item}. L'ordinateur a choisi {computer_item}. Vous avez gagné !"
        elif result == "draw":
            message = f"🤝 Vous avez choisi {user_item}. L'ordinateur a choisi {computer_item}. Match nul !"
        else:
            message = f"😞 Vous avez choisi {user_item}. L'ordinateur a choisi {computer_item}. Vous avez perdu."

        print(message)
        return result
