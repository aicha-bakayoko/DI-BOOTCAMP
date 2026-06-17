import random
from exercise2 import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        all_names = [self.name] + [dog.name for dog in args]
        print(f"{', '.join(all_names)} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs",
                      "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")

my_dog = PetDog("Fido", 2, 10)
other1 = PetDog("Buddy", 3, 12)
other2 = PetDog("Max", 4, 18)

my_dog.train()
my_dog.play(other1, other2)
my_dog.do_a_trick()