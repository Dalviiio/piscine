import random 

nombre_aleatoire = random.randint(1, 100)
print (nombre_aleatoire)
tentative = 0
nbr= 0
valeur=int (input ("Trouver le chiffre"))

while nombre_aleatoire != nbr:
    nbr = int (input("Devinez"))
    if nbr < nombre_aleatoire :
        print ("le nombre est plus petit que",valeur)

    elif nbr > nombre_aleatoire :
        print ("le nombre est plus grand que",valeur)

    else:
        print ("Trouver c'était",valeur)

