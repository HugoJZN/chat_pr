
import os 
import math
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

#Programme principale 

# Vérification du contenu du dossier 'cleaned'


contenue_dossier = os.listdir("./cleaned/")


# Si le dossier 'cleaned' est vide, nettoyage des fichiers de 'speechees' et création de fichiers dans 'cleaned'

if not(contenue_dossier): # Mettre les fichier de speech convertie dans cleaned
    #Parcour les differents fichiers de speechees
    for i in files_names:
        with open("./speeches/{}".format(i), "r") as fichier:
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
        nouveau_fichier = open("./cleaned/{}".format(i), "a")
        nouveau_fichier.write(text_cleaned)
        nouveau_fichier.close()


# Calcul du score TF-IDF pour les fichiers nettoyés

Score_TF_IDF_CLEANED = (TF_IDF("cleaned"))
#print(Score_TF_IDF_CLEANED)


# Calcul de la somme des scores TF-IDF pour chaque mot

liste_mot_non_important = []
dico_moyenne = {}
for i in Score_TF_IDF_CLEANED.items():
    nb = 0
    for values in i[1]:
        nb += values
    dico_moyenne[i[0]] = nb   # 

# Tri des mots par leur score moyen TF-IDF

dico_mot_im_trie = dict(sorted(dico_moyenne.items(), key=lambda item: item[1]))

# Récupération du dictionnaire general des mots dans le dossier 'cleaned'

dico_general = dico_global_dossier("./cleaned")[0]
contenue = dico_global_dossier("./cleaned") [1]


# Affichage 

#Affichage de la liste des noms des présidents

print(extract_president_names(files_names))

# 2 Afficher le(s) mot(s) ayant le score TF-IDF le plus élevé

def TF_IDF_eleve():
    list_mot = list(dico_mot_im_trie)
    return ("le mot ayant le score TF-IDF le plus élevé est ", list_mot[-1])
#print(TF_IDF_eleve)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

