"""
Défi quotidien - Cercle
Classe Circle avec méthodes dunder, propriétés et bonus Turtle
"""

import math


class Circle:

    def __init__(self, radius=None, diameter=None):
        """Initialise le cercle via rayon OU diamètre."""
        if radius is not None:
            self.__radius = radius
        elif diameter is not None:
            self.__radius = diameter / 2
        else:
            raise ValueError("Veuillez fournir un rayon ou un diamètre.")

    # ── Propriétés ──────────────────────────────────────────────

    @property
    def radius(self):
        """Retourne le rayon."""
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Le rayon ne peut pas être négatif.")
        self.__radius = value

    @property
    def diameter(self):
        """Retourne le diamètre."""
        return self.__radius * 2

    @diameter.setter
    def diameter(self, value):
        if value < 0:
            raise ValueError("Le diamètre ne peut pas être négatif.")
        self.__radius = value / 2

    # ── Méthodes ────────────────────────────────────────────────

    def area(self):
        """Calcule et retourne l'aire du cercle."""
        return round(math.pi * self.__radius ** 2, 2)

    # ── Méthodes Dunder (Magiques) ───────────────────────────────

    def __str__(self):
        """Affichage convivial du cercle."""
        return (f"Circle(radius={self.__radius}, "
                f"diameter={self.diameter}, "
                f"area={self.area()})")

    def __repr__(self):
        """Représentation officielle."""
        return f"Circle(radius={self.__radius})"

    def __add__(self, other):
        """Additionne deux cercles → nouveau cercle avec la somme des rayons."""
        return Circle(radius=self.__radius + other.radius)

    def __gt__(self, other):
        """Vérifie si ce cercle est plus grand que l'autre."""
        return self.__radius > other.radius

    def __lt__(self, other):
        """Vérifie si ce cercle est plus petit que l'autre."""
        return self.__radius < other.radius

    def __eq__(self, other):
        """Vérifie si deux cercles sont égaux."""
        return self.__radius == other.radius


# ── Bonus : dessin avec Turtle ───────────────────────────────────

def draw_circles_with_turtle(circles):
    """Dessine visuellement les cercles triés avec le module Turtle."""
    try:
        import turtle

        screen = turtle.Screen()
        screen.title("Cercles triés - Turtle 🐢")
        screen.bgcolor("white")

        t = turtle.Turtle()
        t.speed(5)
        t.hideturtle()

        sorted_circles = sorted(circles)
        x_start = -300

        for circle in sorted_circles:
            r = circle.radius
            t.penup()
            t.goto(x_start, -r)
            t.pendown()
            t.color("steelblue")
            t.circle(r)
            t.penup()
            t.goto(x_start, -r - 20)
            t.color("black")
            t.write(f"r={r}", align="center")
            x_start += r * 2 + 30

        screen.mainloop()

    except ImportError:
        print("⚠️  Module 'turtle' non disponible dans cet environnement.")


# ── Tests ────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 45)
    print("        🔵 DÉFI QUOTIDIEN - CERCLE")
    print("=" * 45)

    # Création via rayon et via diamètre
    c1 = Circle(radius=5)
    c2 = Circle(radius=3)
    c3 = Circle(diameter=16)   # rayon = 8
    c4 = Circle(radius=5)

    print("\n📋 Attributs :")
    print(c1)
    print(c2)
    print(c3)

    print("\n📐 Aires :")
    print(f"  Aire de c1 (r=5)  : {c1.area()}")
    print(f"  Aire de c2 (r=3)  : {c2.area()}")
    print(f"  Aire de c3 (r=8)  : {c3.area()}")

    print("\n➕ Addition :")
    c5 = c1 + c2
    print(f"  c1 + c2 = {c5}")

    print("\n⚖️  Comparaisons :")
    print(f"  c1 > c2 ? {c1 > c2}")      # True
    print(f"  c2 > c3 ? {c2 > c3}")      # False
    print(f"  c1 == c4 ? {c1 == c4}")    # True
    print(f"  c1 == c2 ? {c1 == c2}")    # False

    print("\n📊 Tri d'une liste de cercles :")
    circles = [c1, c2, c3, c4, Circle(radius=1), Circle(radius=10)]
    sorted_circles = sorted(circles)
    for c in sorted_circles:
        print(f"  {c}")

    # Bonus Turtle (décommenter pour l'activer)
    # draw_circles_with_turtle(circles)