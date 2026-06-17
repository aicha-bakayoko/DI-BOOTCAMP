#Challenge
class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type=None, count=1, **kwargs):
        # Ajout classique : add_animal('cow', 5)
        if animal_type is not None:
            if animal_type in self.animals:
                self.animals[animal_type] += count
            else:
                self.animals[animal_type] = count

        # BONUS Étape 8 : add_animal(cow=5, sheep=2, goat=12)
        for animal, qty in kwargs.items():
            if animal in self.animals:
                self.animals[animal] += qty
            else:
                self.animals[animal] = qty

    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            info += f"{animal} : {count}\n"
        info += "\n    E-I-E-I-0!"
        return info

    # BONUS Étape 6 : liste triée des types d'animaux
    def get_animal_types(self):
        return sorted(self.animals.keys())

    # BONUS Étape 7 : description courte
    def get_short_info(self):
        animal_types = self.get_animal_types()

        # Ajoute un 's' si le nombre > 1
        animals_named = [
            animal + "s" if self.animals[animal] > 1 else animal
            for animal in animal_types
        ]

        # Formate la liste : "cows, goats and sheep"
        if len(animals_named) == 1:
            animals_str = animals_named[0]
        else:
            animals_str = ", ".join(animals_named[:-1]) + " and " + animals_named[-1]

        return f"{self.name}'s farm has {animals_str}."


# ── Tests ────────────────────────────────────────────────────

macdonald = Farm("McDonald")

# Ajouts classiques
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())
print()

# BONUS : ajout via **kwargs
macdonald.add_animal(chicken=3, duck=1)
print(macdonald.get_short_info())
print(macdonald.get_animal_types())