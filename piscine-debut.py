liste = [("Pierre","Dos",10),("Paul","Brasse",13),("Léa","Crawl",6), ("Léa","Brasse",8) ]
commande = ''

def cmd_ajout(liste):
    a = input("Qui nage ? ")
    b = input("quelle nage ? ")
    c = input("combien de longueur ? ")
    liste.append((a,b,c))

def cmd_liste(liste):
    for elt in liste:
        print(f"Prénom {elt[0]}, nage {elt[1]}, longueur {elt[2]}")

def cmd_exit():
    tmp == "exit"
    isAlive = cmd_exit()
    
isAlive = True

while isAlive:
    commande = input("Que faut-il faire ? ")

    if commande == 'ajout':
        cmd_ajout(liste)
   
    if commande == 'liste':
        cmd_liste(liste)
        

    if commande =='exit':
        tmp = input ("En etes vous sur ? oui/non")
        if tmp == "o":
            isAlive = cmd_exit()
        continue

    print (f"Commande {commande} inconnue")

fichier = open('save.csv', 'w')
for elt in liste:
    fichier.write(elt[0]+','+elt[1]+','+str(elt[2])+"\n")
fichier.close()

fichier = open('save.csv', 'r')
for line in fichier:
    line.strip()
    if line[-1] == '\n':
        line = line[:-1]
    if line[0]=='#':
        continue
    tmp = line.split(',')
    liste.append(tuple(tmp))
fichier.close()