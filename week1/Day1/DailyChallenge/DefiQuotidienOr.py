#Défi
#Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
#Display a little cake as seen below:
  #     ___iiiii___
 #     |:H:a:p:p:y:|
 #   __|___________|__
 #  |^^^^^^^^^^^^^^^^^|
 #  |:B:i:r:t:h:d:a:y:|
 #  |                 |
 #  ~~~~~~~~~~~~~~~~~~~


birthdate=input("Entrer votre date de naissance (format : DD/MM/YYYY) :   "  )
age=2026-int(birthdate[-4:])
print("  ___iiiii___")
print("  |:H:a:p:p:y:|")    
print(" __|___________|__")
print(" |^^^^^^^^^^^^^^^^^|")       
print(" |:B:i:r:t:h:d:a:y:|")
print(" |                 |")
print(" ~~~~~~~~~~~~~~~~~~~")
print(f"Vous avez {age} ans !")

