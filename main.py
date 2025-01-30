import os
from datetime import datetime
from get_value import get_int_value


commande = ''

#default values
param = {'bdd': [(1,3,10),(2,1,13),(3,2,6), (3,1,8) ],
         'nages': [(1, "Brasse"), (2, "Dos"), (3, "Crawl")],
         'nageurs': [(1, "Pierre"), (2, "Paul"), (3, "Léa")]
        }


def reset(param):
    '''réinitialise la bdd'''
    param.clear()
    param['bdd'] = []
    param['nages'] = []
    param['nageurs'] = []


def get_str_from_num_in_list(num, liste):
    """Return str from num into liste"""
    for elt in liste:
        if elt[0]==num:
            return elt[1]
    #la ligne suivante ne devrait jamais être exécutée
    return "unknown"


def cmd_individu(param):
    """Ajoute un nouveau najeur"""
    prénom = input("Prénom du nouveau nageur ? ")
    id = len(param['nageurs'])+1
    param['nageurs'].append( (id,prénom ))
    print(param['nageurs'])


def cmd_nouvelle_nage(param):
    """Ajoute une nouvelle nage au logiciel"""
    nage = input("Quelle nage enregistrer ? ")
    id = len(param['nages'])+1
    param['nages'].append( (id,nage ))
    print(param['nages'])


def cmd_ajout(param):
    """Ajoute un évènement à la liste"""
    for elt in param['nageurs']:
        print(f"{elt[0]:5} : {elt[1]}")
    a = int(input("Nageur n° ? "))
    for elt in param['nages']:
        print(f"{elt[0]:5} : {elt[1]}")
    b = int(input("Nage n° ? "))
    c = int(input("combien de longueur ? "))
    param['bdd'].append((a,b,c))

    a = get_int_value(input("Nageur n° ? "))
    b = get_int_value(input("Nage n° ? "))
    c = get_int_value(input("combien de longueur ? "))


def cmd_liste(param):
    """Affiche toutes les performances des nageurs"""
    print("Prénom      |  nage   |  longueur")
    print("---------------------------------")
    for elt in param['bdd']:
        nageur = get_str_from_num_in_list(elt[0], param['nageurs'])
        nage = get_str_from_num_in_list(elt[1], param['nages'])
        print(f" {nageur:11}| {nage:8}|  {elt[2]}")


def cmd_nageur(param):
    """Affiche toutes les performances d'un nageur"""
    for elt in param['nageurs']:
        print(f"{elt[0]:5} : {elt[1]}")
    tmp = int(input("Quel numéro de nageur ? "))
    tmp = get_int_value(input("Quel numéro de nageur ? "))
    print("Performances de ", tmp)
    print("  nage   |  longueur")
    print("--------------------")
    for elt in param['bdd']:
        if elt[0]== tmp:
            nage = get_str_from_num_in_list(elt[1], param['nages'])
            print(f" {nage:8}|  {elt[2]}")


def cmd_nage(param):
    """Affiche toutes les performances suivant une nage donnée"""
    for elt in param['nages']:
        print(f"{elt[0]:5} : {elt[1]}")
    tmp = int(input("Quel numéro de nage ? "))
    tmp = get_int_value(input("Quel numéro de nage ? "))
    print("Nage ", tmp)
    print(" Nageur     |  longueur")
    print("------------------------")
    for elt in param['bdd']:
        if elt[1]== tmp:
            nageur = get_str_from_num_in_list(elt[0], param['nageurs'])
            print(f" {nageur:11}|  {elt[2]}")


def cmd_exit(param):
    tmp = input("En êtes-vous sûr ? (o)ui/(n)on ")
    tmp = get_int_value(input("En êtes-vous sûr ? (o)ui/(n)on "))
    if tmp == 'o':
        cmd_save(param, 'save.backup')
        return False
    else:
        return True


def cmd_save(param, filename = 'save.csv'):
    '''sauvegarde complète de la BDD'''
    fichier = open(filename, 'w')
    # sauvegarde des nageurs
    fichier.write('@ nageurs\n')
    for elt in param['nageurs']:
        fichier.write(str(elt[0])+','+str(elt[1])+"\n")
    # sauvegarde des nages
    fichier.write('@ nages\n')
    for elt in param['nages']:
        fichier.write(str(elt[0])+','+str(elt[1])+"\n")
    # sauvegarde des données
    fichier.write('@ bdd\n')
    for elt in param['bdd']:
        fichier.write(str(elt[0])+','+str(elt[1])+','+str(elt[2])+"\n")
    fichier.close()


def cmd_load(param, filename = 'save.csv'):
    '''chargement complet la BDD avec réinitialisation'''
    reset(param)
    key = ''
    fichier = open(filename, 'r')
    for line in fichier:
        line.strip()
        if line[-1] == '\n':
            line = line[:-1]
        if line[0]=='#':
            continue
        if line[0]=='@':
            key = line[2:]
            continue
        if key =='':
            continue
        tmp = line.split(',')
        # convertion en int de ce qui doit l'être
        if key == 'bdd':
            for i in range(len(tmp)):
                tmp[i] = int(tmp[i])
        if key == 'nages' or key == 'nageurs':
            tmp[0] = int(tmp[0])
        param[key].append(tuple(tmp))
    fichier.close()

def get_cmd():
    '''traitement de la commande d'entrée'''
    print("\n--- Menu ---")
    print("1 -> Ajout d'une performance")
    print("2 -> Ajout d'un individu")
    print("3 -> Ajout d'une nouvelle nage")
    print("4 -> Liste toutes les performances")
    print("5 -> Liste les performances d'un nageur")
    print("6 -> Liste tous les nageurs pratiquant une nage")
    print("7 -> Sauvegarde des données")
    print("8 -> Chargement des données")
    print("0 -> Quitter le logiciel")
    # Création du Menu
    choix = input("Que souaither vous faire ? (Entrez un numero) ")
    return choix

def cmd_ajout(param):
    """Ajoute un évènement à la liste avec la date"""
    for elt in param['nageurs']:
        print(f"{elt[0]:5} : {elt[1]}")
    a = int(input("Nageur n° ? "))
    for elt in param['nages']:
        print(f"{elt[0]:5} : {elt[1]}")
    b = int(input("Nage n° ? "))
    c = int(input("Combien de longueurs ? "))
    date_input = input("Date de l'événement (YYYY-MM-DD) ? ")
    #test date
    try:
        date_obj = datetime.strptime(date_input, '%Y-%m-%d')
        date_str = date_obj.date().strftime('%Y-%m-%d')
        param['bdd'].append((a, b, c, date_str))
        print(f"Performance ajoutée le {date_str}")
    except ValueError:
        print("Date invalide. Format attendu : YYYY-MM-DD")

#affichage
def cmd_liste(param):
    print("Prénom      |  nage   |  longueur |  date")
    print("--------------------------------------------")
    for elt in param['bdd']:
        nageur = get_str_from_num_in_list(elt[0], param['nageurs'])
        nage = get_str_from_num_in_list(elt[1], param['nages'])
        print(f" {nageur:11}| {nage:8}|  {elt[2]:8}| {elt[3]}")

def cmd_nageur(param):
    """Affiche toutes les performances d'un nageur"""
    for elt in param['nageurs']:
        print(f"{elt[0]:5} : {elt[1]}")
    tmp = get_int_value()
    print(f"Performances de {tmp}")
    print(" nage   |  longueur")
    print("--------------------")

def get_int_value():
    while True:
        try:
            msg = int(input("Valeur ? "))
            return msg
        except ValueError:
            print("Indiquez valeur numérique")

def cmd_nageur(param):
    for elt in param['nageurs']:
        print(f"{elt[0]:5} : {elt[1]}")
    tmp = get_int_value()
    print(f"Performances de {tmp}")
    print(" nage   |  longueur")
    print("--------------------")
    
    longueurs = []
    
    for elt in param['bdd']:
        if elt[0] == tmp:
            nage = get_str_from_num_in_list(elt[1], param['nages'])
            print(f" {nage:8}|  {elt[2]}")
            longueurs.append(elt[2])
    
    if longueurs:
        minimum = min(longueurs)
        maximum = max(longueurs)
        moyenne = sum(longueurs) / len(longueurs)
        print(f"Minimum : {minimum}")
        print(f"Maximum : {maximum}")
        print(f"Moyenne : {moyenne:.1f}")
    else:
        print("Aucune performance enregistrée pour ce nageur.")



def get_cmd():
    '''Traitement de la commande d'entrée'''
    msg = input("Que faut-il faire ? ")
    msg = msg.lower()
    return msg

#
#   Programme principal
#
isAlive = True
if os.path.exists('save.backup'):
    cmd_load(param, 'save.backup')
while isAlive:
    commande = get_cmd()

    if commande == 'ajout':
        cmd_ajout(param)
        continue
    if commande == 'individu':
        cmd_individu(param)
        continue

    if commande == 'nouvelle nage':
        cmd_nouvelle_nage(param)
        continue

    if commande == 'liste':
        cmd_liste(param)
        continue

    if commande == 'nageur':
        cmd_nageur(param)
        continue

    if commande == 'nage':
        cmd_nage(param)
        continue

    if commande == 'save':
        cmd_save(param)
        continue

    if commande == 'load':
        cmd_load(param)
        continue

    if commande == 'exit':
        isAlive = cmd_exit(param)
        continue

    if commande == '1': 
        cmd_ajout(param)

    elif commande == '2':  
        cmd_individu(param)

    elif commande == '3':  
        cmd_nouvelle_nage(param)

    elif commande == '4':  
        cmd_liste(param)

    elif commande == '5':  
        cmd_nageur(param)

    elif commande == '6':  
        cmd_nage(param)

    elif commande == '7':  
        cmd_save(param)

    elif commande == '8':  
        cmd_load(param)

    elif commande == '0': 
        isAlive = cmd_exit(param)
        
    else:
        print(f"Commande {commande} inconnue")


    #try,exept et finally sont des mots cléfs qui font partie de structure qui permet de gerer les erreur ca permet de dire au programme quoi faire pour gerer l'erreur 