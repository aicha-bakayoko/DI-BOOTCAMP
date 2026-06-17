from ast import Call
from tokenize import String
import random

# ============================================================
# Exercise 1
# ============================================================

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dictionary = dict(zip(keys, values))
print(dictionary)


# ============================================================
# Exercise 2
# ============================================================

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

def calculate_ticket_cost(family):
    total_cost = 0
    print("=== Cinema Ticket Prices ===\n")
    for name, age in family.items():
        if age < 3:
            cost = 0
            print(f"{name.capitalize():<10} ({age} years) → Free")
        elif 3 <= age <= 12:
            cost = 10
            print(f"{name.capitalize():<10} ({age} years) → ${cost}")
        else:
            cost = 15
            print(f"{name.capitalize():<10} ({age} years) → ${cost}")
        total_cost += cost
    print("-" * 40)
    print(f"Total cost for the family: ${total_cost}")
    return total_cost


# ============================================================
# Exercise 3
# ============================================================

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": ["blue"],
        "Spain": ["red"],
        "US": ["pink", "green"]
    }
}

brand["number_stores"] = 2
print(f"Zara's clients: {', '.join(brand['type_of_clothes'])}")
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
del brand["creation_date"]
print(f"Last competitor: {brand['international_competitors'][-1]}")
print(f"Major colors in the US: {brand['major_color']['US']}")
print(f"Number of keys: {len(brand)}")
print(f"Keys: {list(brand.keys())}")

more_on_zara = {"creation_date": 1975, "number_stores": 7000}
brand.update(more_on_zara)
print(f"\nMerged dictionary: {brand}")


# ============================================================
# Exercise 4
# ============================================================

def describe_city(city, country="Unknown"):
    """
    Describe a city and its country.
    Parameters:
        city (str): name of the city
        country (str): name of the country (default: "Unknown")
    """
    print(f"{city} is in {country}.")


# ============================================================
# Exercise 5
# ============================================================

def compare_number(user_number):
    """
    Generate a random number and compare it to the user's number.
    Parameters: user_number (int): number provided by the user (1-100)
    """
    random_number = random.randint(1, 100)
    if user_number == random_number:
        print("Success!")
    else:
        print(f"Fail! Your number: {user_number}, Random number: {random_number}")


# ============================================================
# Exercise 6
# ============================================================

def make_shirt(size="large", text="I love Python"):
    """
    Describe a shirt's size and message.
    Parameters:
        size (str): size of the shirt (default: "large")
        text (str): message on the shirt (default: "I love Python")
    """
    print(f"The size of the shirt is {size} and the text is: {text}.")


# ============================================================
# Exercise 7
# ============================================================

def get_random_temp():
    """
    Generate a random floating-point temperature between -10 and 40.
    Returns: float: random temperature in Celsius
    """
    return random.uniform(-10, 40)

def main():
    """
    Get a random temperature and provide advice based on the range.
    """
    temperature = get_random_temp()
    print(f"The temperature right now is {temperature:.1f} degrees Celsius.")
    if temperature < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif temperature < 16:
        print("Quite chilly! Don't forget your coat.")
    elif temperature < 24:
        print("Nice weather.")
    elif temperature < 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It's really hot! Stay cool.")


# ============================================================
# Exercise 8
# ============================================================

def pizza_order():
    """
    Ask the user for pizza toppings and calculate the total price.
    Base price: $10. Each topping adds $2.50.
    """
    BASE_PRICE = 10
    TOPPING_PRICE = 2.5
    toppings = []

    while True:
        topping = input("Add a topping (or 'quit' to finish): ")
        if topping.lower() == 'quit':
            break
        toppings.append(topping)
        print(f"Adding {topping} to your pizza.")

    print(f"\nYour toppings: {', '.join(toppings)}")
    total_price = BASE_PRICE + len(toppings) * TOPPING_PRICE
    print(f"Total price: ${total_price}")


# ============================================================
if __name__ == "__main__":
    print("\n--- Exercise 1 ---")
    print(dictionary)

    print("\n--- Exercise 2 ---")
    calculate_ticket_cost(family)

    print("\n--- Exercise 3 ---")
    manipulate_brand(brand)

    print("\n--- Exercise 4 ---")
    describe_city("Reykjavik", "Iceland")
    describe_city("Paris")
    describe_city("Abidjan")

    print("\n--- Exercise 5 ---")
    compare_number(50)

    print("\n--- Exercise 6 ---")
    make_shirt()
    make_shirt("medium")
    make_shirt("small", "Long live Ivory Coast!")
    make_shirt(size="XL", text="Hello Abidjan!")

    print("\n--- Exercise 7 ---")
    main()

    print("\n--- Exercise 8 ---")
    pizza_order()