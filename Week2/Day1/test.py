import pandas as pd
data = {
    'Book Title': ['The Great Gatsby', 'To Kill a Mockingbird', '1984', 'Pride and Prejudice', 'The Catcher in the Rye'],
    'Author': ['F. Scott Fitzgerald', 'Harper Lee', 'George Orwell', 'Jane Austen', 'J.D. Salinger'],
    'Genre': ['Classic', 'Classic', 'Dystopian', 'Classic', 'Classic'],
    'Price': [10.99, 8.99, 7.99, 11.99, 9.99],
    'Copies Sold': [500, 600, 800, 300, 450]
}
#Creer la DataFrame
df=pd.DataFrame(data)
#Afficher les premières lignes
df.head()
#Obtenier un résumé statistiques automatique
df.describe()
#Obtenir un résumé
df.info()
#Trier selon Price or   Copies Sold
df.sort_values(by=['Price', 'Copies Sold'])
#Filtrer par prix ou seuil spécifique
df[(df['Genre']=='Classic' )&( df['Price']>9)]

#CLASSER LES LIVRES PAR AUEUR
df.groupby('Author')['Copies Sold'].sum()