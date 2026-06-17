# Daily Challenge 1
word = input("Enter a word: ")

letter_indices = {}

for index, character in enumerate(word):
    if character in letter_indices:
        letter_indices[character].append(index)
    else:
        letter_indices[character] = [index]

print(letter_indices)


# Daily Challenge 2
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

budget = int(wallet.replace("$", "").replace(",", ""))

basket = []

for item, price in items_purchase.items():
    clean_price = int(price.replace("$", "").replace(",", ""))
    if clean_price <= budget:
        basket.append(item)
        budget -= clean_price

if not basket:
    print("Nothing")
else:
    print(sorted(basket))