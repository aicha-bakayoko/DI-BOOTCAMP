#Exercise 1
#Instructions
#. Ask the user to input a month (1 to 12).
#2. Display the season of the month received:
#- Spring runs from March (3) to May (5)
#"- Summer runs from June (6) to August (8)
#- Autumn runs from September (9) to November (11)
#- Winter runs from December (12) to February (2)

from ast import If


month_number=int(input("Entrez un numéro de mois (1 à 12) :   "  ))
if month_number in [3,4,5]:
    print("C'est le printemps !")   
elif month_number in [6,7,8]:
    print("C'est l'été !")   
elif month_number in [9,10,11]:
    print("C'est l'automne !")   
else:
    print("C'est l'hiver !")   


#Exercise 2
#Instructions
#Key Python Topics:
#Loops (for)
#Range and indexing

number=20
for i in range(1,number+1):
    print(i)


#Exercise 3
#Instructions
#Write a while loop that keeps asking the user to enter their name.
#Stop the loop if the user’s input is your name.

nom="Lylda"
while True:
    nom1=input("Entrez votre nom :   "  )
    if nom1==nom:
        print("Vous , c'est le même nom!")   
        break
    else:    print("Oups, les noms sont différents, reessayez !")

#Exercises 4
#Instructions
#Using this variable:

#names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

#Ask a user for their name, if their name is in the names list print out the index of the first occurrence of the name.

#Example: if input is Cortana we should be printing the index 1

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
nom=input("Entrez votre nom :   "  )    
if nom in names:
    print(f"Votre nom est dans la liste à l'index {names.index(nom)}")   
else:    print("Oups, votre nom n'est pas dans la liste !")

#Exercises 5
#Instructions
#Ask the user for 3 numbers and print the greatest number.

#Test Data:

#Input the 1st number: 25
#Input the 2nd number: 78
#Input the 3rd number: 87

#The greatest number is: 87

nombre1=int(input("Entrez le 1er nombre :   "  ))
nombre2=int(input("Entrez le 2ème nombre :   "  ))
nombre3=int(input("Entrez le 3ème nombre :   "  ))
greatest_number=max(nombre1, nombre2, nombre3)
print(f"Le plus grand nombre est: {greatest_number}")

#Exercise 6
#Instructions
#Ask the user to input a number from 1 to 9 (including).
#   Get a random number between 1 and 9. Hint: random module.
#If the user guesses the correct number print a message that says “Winner”.
#If the user guesses the wrong number print a message that says “Better luck next time.”
#Bonus: use a loop that allows the user to keep guessing until they want to quit.
#Bonus 2: on exiting the loop, tally up and display total games won and lost.


nombre_choisi=int(input('Entrez un nombre de 1 à 9 :   '  ))
import random
nombre_aleatoire=random.randint(1,9)
if nombre_choisi == nombre_aleatoire:
    print("Winner!")
else:
    print("Better luck next time!")
    

