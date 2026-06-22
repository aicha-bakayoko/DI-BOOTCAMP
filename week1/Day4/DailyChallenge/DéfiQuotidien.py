# ============================================================
# Daily Challenge: Gestionnaire de Stock (Inventory)
# ============================================================

class InsufficientStockError(Exception):
    """Exception personnalisée levée quand le stock est insuffisant."""
    pass


class Inventory:
    def __init__(self, products=None, low_stock_threshold=5):
        """
        Initialise l'inventaire.
        Parameters:
            products (dict): dictionnaire {nom: quantité} (par défaut: None → dict vide)
            low_stock_threshold (int): seuil de stock faible (par défaut: 5)
        """
        if products is None:
            self.products = {}
        else:
            self.products = products
        self.low_stock_threshold = low_stock_threshold

    def add_product(self, name, quantity):
        """Ajoute une quantité à un produit (le crée s'il n'existe pas)."""
        if name in self.products:
            self.products[name] += quantity
        else:
            self.products[name] = quantity
        return self

    def remove_product(self, name, quantity):
        """
        Retire une quantité d'un produit.
        Raises: InsufficientStockError si le stock disponible est insuffisant.
        """
        available = self.products.get(name, 0)
        if quantity > available:
            raise InsufficientStockError(
                f"Stock insuffisant pour '{name}' : {available} disponibles, {quantity} demandées"
            )
        self.products[name] -= quantity
        return self

    def get_low_stock_items(self):
        """Retourne la liste des noms de produits sous le seuil de stock faible."""
        return [name for name, qty in self.products.items() if qty < self.low_stock_threshold]

    def __str__(self):
        """Affiche chaque produit et sa quantité, un par ligne."""
        return "\n".join(f"{name}: {qty}" for name, qty in self.products.items())


# ============================================================
# Tests
# ============================================================

inv = Inventory()
inv.add_product("Pomme", 10).add_product("Banane", 3).add_product("Pomme", 5)

print(str(inv))
# Pomme: 15
# Banane: 3

print(inv.get_low_stock_items())
# ['Banane']

inv.remove_product("Pomme", 4)
print(str(inv))
# Pomme: 11
# Banane: 3

try:
    inv.remove_product("Banane", 100)
except InsufficientStockError as e:
    print(e)
# Stock insuffisant pour 'Banane' : 3 disponibles, 100 demandées