# ============================================================
# Exercice 1 : Les chats
# ============================================================

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Étape 1 : Créer trois objets chat
cat1 = Cat("Minou", 3)
cat2 = Cat("Tigrou", 7)
cat3 = Cat("Luna", 5)

# Étape 2 : Trouver le chat le plus vieux
def find_oldest_cat(cat1, cat2, cat3):
    oldest = cat1
    if cat2.age > oldest.age:
        oldest = cat2
    if cat3.age > oldest.age:
        oldest = cat3
    return oldest

# Étape 3 : Afficher les infos
oldest = find_oldest_cat(cat1, cat2, cat3)
print(f"Le chat le plus âgé est {oldest.name}, et a {oldest.age} ans.")


# ============================================================
# Exercice 2 : Les chiens
# ============================================================

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} fait ouaf !")

    def jump(self):
        print(f"{self.name} saute {self.height * 2} cm de haut !")

# Étape 2 : Créer les objets
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Bella", 35)

# Étape 3 : Afficher les infos et appeler les méthodes
print(f"Nom : {davids_dog.name}, Taille : {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()

print(f"Nom : {sarahs_dog.name}, Taille : {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()

# Étape 4 : Comparer la taille
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} est le plus grand chien.")
elif sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name} est le plus grand chien.")
else:
    print("Les deux chiens ont la même taille.")


# ============================================================
# Exercice 3 : La chanson
# ============================================================

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# Test
stairway = Song([
    "There's a lady who's sure",
    "all that glitters is gold",
    "and she's buying a stairway to heaven"
])
stairway.sing_me_a_song()


# ============================================================
# Exercice 4 : Le zoo
# ============================================================

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, *args):          # BONUS : *args accepte plusieurs animaux
        for new_animal in args:
            if new_animal not in self.animals:
                self.animals.append(new_animal)

    def get_animals(self):
        print(f"Animaux dans {self.zoo_name} : {self.animals}")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        self.animals.sort()
        grouped = {}
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in grouped:
                grouped[first_letter] = []
            grouped[first_letter].append(animal)
        return grouped

    def get_groups(self):
        groups = self.sort_animals()
        for letter, animals in groups.items():
            print(f"{letter}: {animals}")


# Étape 2 : Créer le zoo
brooklyn_safari = Zoo("Brooklyn Safari")

# Étape 3 : Tester les méthodes
brooklyn_safari.add_animal("Giraffe", "Bear", "Baboon")  # BONUS : plusieurs à la fois
brooklyn_safari.add_animal("Lion")
brooklyn_safari.add_animal("Zebra")
brooklyn_safari.add_animal("Cat")
brooklyn_safari.add_animal("Cougar")
brooklyn_safari.get_animals()

brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()

brooklyn_safari.get_groups()