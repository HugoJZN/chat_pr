
import os 
from math import*
from Fonctions import *



# Variable importante 

# Répertoire contenant les fichiers texte
directory = "./speeches" # changer le chemin pour acceder au fichier
files_names = list_of_files(directory, ".txt")
#print(files_names) 

# Dictionnaire des noms des présidents avec leurs prénoms associés
dico_prenom = {
    'Chirac': 'Jacques',
    'Mitterrand': 'François',
    'Sarkozy': 'Nicolas',
    'Hollande': 'François',
    'Macron': 'Emmanuel',
    'Giscard dEstaing': 'Valéry'
}

# Dictionnaire brut avec les noms des présidents et leurs dates d'élection
presidents_et_dates = {
    "Giscard dEstaing": 1974,
    "Mitterrand": 1981,
    "Chirac": 1995,
    "Sarkozy": 2007,
    "Hollande": 2012,
    "Macron": 2017
}

#Programme principale 


# on trouve le chemin pour acceder à cleaned, nouveau repertorie
directory_cleaned = "./cleaned"

os.makedirs(directory_cleaned, exist_ok=True) # fonctionne sur Mac cependant si cela ne marche sur Pycharm, 
# il faut créer un dossier vide cleaned 

# Vérification du contenu du dossier 'cleaned'
contenue_dossier = list_of_files(directory_cleaned, "txt")


# Si le dossier 'cleaned' est vide, nettoyage des fichiers de 'speechees' et création de fichiers dans 'cleaned'

if len(contenue_dossier) < 8: # Mettre les fichier de speech convertie dans cleaned
    #Parcour les differents fichiers de speechees
    for i in files_names:
        with open("./speeches/{}".format(i), "r", encoding="utf-8") as fichier:
            texte = fichier.read()
        # Nettoyage des textes en convertissant en minuscules et supprimant la ponctuation
        # Création de nouveaux fichiers dans le dossier 'cleaned' avec le texte nettoyé
        text_cleaned = " " 
        for a in range(len(texte)):
            if ord(texte[a]) >= 65 and ord(texte[a]) <= 90:
                text_cleaned += chr(ord(texte[a]) + 32)
            elif (ord(texte[a]) >= 21 and ord(texte[a]) <=47) or (ord(texte[a]) >=58 and ord(texte[a])<= 64) or (texte[a])=="\n" :
                if text_cleaned[-1] != " ":
                    text_cleaned += " "
                else:
                    text_cleaned = text_cleaned
            else:
                text_cleaned += texte[a]
        # print(texte)         Affichage des textes
        # print(text_cleaned)  Affichage des textes
        nouveau_fichier = open("./cleaned/{}".format(i), "a", encoding="utf-8")
        nouveau_fichier.write(text_cleaned)
        nouveau_fichier.close()


# Calcul du score TF-IDF pour les fichiers nettoyés
Score_idf_cleaned = IDF("cleaned")
Score_TF_IDF_CLEANED = (TF_IDF("cleaned"))

# Calcul de la somme des scores TF-IDF pour chaque mot

liste_mot_non_important = []
dico_moyenne = {}
for i in Score_TF_IDF_CLEANED.items():
    nb = 0
    for valeur in i[1]:
        nb += valeur
    dico_moyenne[i[0]] = nb   # 


# Récupération du dictionnaire general des mots dans le dossier 'cleaned'

dico_general = dico_global_dossier("./cleaned")[0]
contenue = dico_global_dossier("./cleaned") [1]


# Affichage 

#Affichage de la liste des noms des présidents

#print(extract_president_names(files_names))


# Pour afficher un terminal propre
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')



