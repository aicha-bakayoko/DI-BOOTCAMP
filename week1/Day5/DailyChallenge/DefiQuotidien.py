import math
import turtle


class Circle:
    """Représente un cercle, défini soit par son rayon, soit par son diamètre."""

    def __init__(self, radius=None, diameter=None):
        if diameter is not None:
            self.diameter = diameter  # passe par le setter, qui calcule le rayon
        elif radius is not None:
            self.radius = radius
        else:
            self.radius = 1  # valeur par défaut si rien n'est fourni

    # ---------- Propriétés (radius / diameter) ----------

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Le rayon doit être positif.")
        self._radius = value

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        if value <= 0:
            raise ValueError("Le diamètre doit être positif.")
        self._radius = value / 2

    # ---------- Capacité 1 : surface ----------

    def area(self):
        return math.pi * self._radius ** 2

    # ---------- Capacité 2 : affichage ----------

    def __str__(self):
        return f"Circle with radius: {self._radius}"

    def __repr__(self):
        return f"Circle({self._radius})"

    # ---------- Capacité 3 : addition ----------

    def __add__(self, other):
        return Circle(radius=self._radius + other._radius)

    # ---------- Capacités 4 et 5 : comparaisons ----------

    def __eq__(self, other):
        return self._radius == other._radius

    def __gt__(self, other):
        return self._radius > other._radius

    def __lt__(self, other):
        return self._radius < other._radius


# ============================================================
# Bonus : dessin des cercles triés avec turtle
# ============================================================

def draw_circles(circles_list):
    """Dessine les cercles, triés du plus petit au plus grand, côte à côte."""
    screen = turtle.Screen()
    screen.title("Cercles triés")
    t = turtle.Turtle()
    t.speed(3)

    x_position = -250
    for circle in sorted(circles_list):
        t.penup()
        t.goto(x_position, 0)
        t.setheading(0)
        t.pendown()
        t.circle(circle.radius * 10)  # ×10 pour que ce soit visible à l'écran
        x_position += circle.radius * 25 + 30

    screen.exitonclick()


# ============================================================
# Tests
# ============================================================

if __name__ == "__main__":
    c1 = Circle(radius=4)
    c2 = Circle(diameter=10)   # rayon = 5.0
    c3 = Circle(radius=2)

    print(c1)                  # Circle with radius: 4
    print(c2.radius)           # 5.0
    print(c1.diameter)         # 8

    print(f"Aire de c1 : {c1.area():.2f}")   # 50.27

    c4 = c1 + c3
    print(c4)                  # Circle with radius: 6 (4 + 2)

    print(c1 == c3)             # False
    print(c1 > c3)               # True
    print(c1 < c2)               # True

    circles = [c1, c2, c3, c4]
    circles_sorted = sorted(circles)
    print([repr(c) for c in circles_sorted])
    # [Circle(2), Circle(4), Circle(5.0), Circle(6)]

    # Lance la fenêtre graphique (clique dans la fenêtre pour la fermer)
    draw_circles(circles)g   