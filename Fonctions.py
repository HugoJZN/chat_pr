import os
import math


# Fonctions importante

def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return sorted(files_names)

# Focntion qui detruit les doublons 
def destruct_doublon_nb(list_var):
    L = []
    for i in range(len(list_var)):
        a = (list_var[i][-1])
        if chr(57) >= a and a >= chr(48) :
            list_var[i] = list_var[i][:-1]
    for i in list_var:
        if not(i in L): 
            L.append(i)
    return L


#Extraire les noms des présidents à partir des noms des fichiers texte fournis ; 
def extract_president_names(file):
    pr_names = []  # Utilisez un ensemble pour éviter les doublons
    # on fait une première boucle pour mettre dans une liste tous les présidents avec leurs numéros
    # permettant d'enlever leurs type et + 
    for i in file:
        pr_names.append(i[11:-4])

    pr_names = destruct_doublon_nb(pr_names)
    #print(pr_names)
    return pr_names

#fonction TD-IDF et autres

# compte le nombre d'occurences d'un mot dans un texte sans ponctuation
def count_word(texte, word): 
    count = 0
    list_word = texte.split()
    for i in list_word:
        if i == word:
            count += 1
    return count


#Fonction servant à renvoyer le TD-IDF
def TF(texte): 
    liste_word = []
    word_index = {}
    word_1 = ""
    for i in range(len(texte)):
        if texte[i] == " " and word_1 != " ":
            if not(word_1 in liste_word) and word_1 != '':
                liste_word.append(word_1)
            word_1 = ""
        else:
            word_1 += texte[i]
    for i in liste_word:
        n = count_word(texte, i)
        word_index[i] = n
    return word_index

# fonction servant à creer un dictionnaire generale en fonction du repertoire et à renvoyer le dico et la longueur des textes fusionnées
def dico_global_dossier(repertoire):
    f_texte = list_of_files(repertoire, ".txt")
    dico_global_mot = {}
    contenue_texte = ""
    for i in f_texte:
        with open("./cleaned/{}".format(i), "r") as fichier1:
            texte1 = fichier1.read()
            contenue_texte += texte1 + " " 
    dico_global_mot = TF(contenue_texte)
    return dico_global_mot, len(contenue_texte)

# fonction servant à creer un dictionnaire generale d'un president dans le dossier cleaned
def dico_global_president(president):
    f_texte = list_of_files("./cleaned", "txt")
    dico_global_mot = {}
    contenue_texte = ""
    for i in f_texte:
        if president in i:
            with open("./cleaned/{}".format(i), "r") as fichier1:
                texte1 = fichier1.read()
                contenue_texte += texte1 + " " 
    dico_global_mot = TF(contenue_texte)
    return dico_global_mot


#Fonction IDF
def IDF(repertoire):
    #taille_contenue_texte = dico_global_dossier(repertoire)[1]
    files_names = list_of_files(repertoire, ".txt")
    taille = len(files_names)

    # liste de mots dans tous les fichiers 
    dico = dico_global_dossier(repertoire)[0]
    liste_contenu = dico.keys()
    #remplacer liste contenue par les mots dans le dico

    # parcours la liste de mots et compte le nombre d'occurence pour ensuite calculer le score IDF
    for mot in liste_contenu:
        occurence = 0
        for i in files_names:
            with open('./{}/{}'.format(repertoire, i), 'r') as fichier_IDF :
                contenu = fichier_IDF.read()
                if mot in contenu:
                    occurence += 1
        calcul_idf = math.log10((taille / occurence) + 1)
        dico[mot] = calcul_idf
    return dico

#Fonction TF_IDF 

def TF_IDF(repertoire):
    dico_TF_IDF = {}
    dico_IDF = IDF(repertoire)
    f_texte = list_of_files("./{}".format(repertoire), "txt")
    premiere_colonnes = ["Mot"] + f_texte
    #print(premiere_colonnes)
    for mot in list(dico_IDF.keys()):
        score_tf_idf = []
        for i in f_texte:
            
            with open("./cleaned/{}".format(i), "r") as fichier1:
                texte1 = fichier1.read()
            
            contenue_mot = texte1.split()
            score_tf = 0
            if mot in contenue_mot:
                for i in contenue_mot:
                    if i == mot:
                        score_tf += 1
                        
            score_tf_idf.append(score_tf * dico_IDF[mot])
        dico_TF_IDF[mot] = score_tf_idf
    return dico_TF_IDF

def min_tab(tab):
    if len(tab) <= 0:
        return None, None  # Retourne None si le tableau est vide
    else:
        valeur_min = tab[0]
        for i in range(1, len(tab)):
            if tab[i] < valeur_min:
                valeur_min = tab[i]
        return valeur_min
    

def min_dico_valeur(dico):
    if len(dico) <= 0:
        return None  # Retourne None si le dictionnaire est vide
    else:
        valeur_min = float('inf')  # Initialiser à l'infini positif pour assurer la comparaison, c'est à dire qu'il y aura toujours une valeur superieur
        cle_min = None
        for cle, valeur in dico.items():
            if valeur < valeur_min:
                valeur_min = valeur
                cle_min = cle

        return cle_min
    

def max_dico_valeur(dico):
    if len(dico) <= 0:
        return None  # Retourne None si le dictionnaire est vide
    else:
        valeur_max = float('-inf')  # Initialiser à l'infini positif pour assurer la comparaison, c'est à dire qu'il y aura toujours une valeur superieur
        cle_max = None
        for cle, valeur in dico.items():
            if valeur > valeur_max:
                valeur_max = valeur
                cle_max = cle

        return cle_max
    

