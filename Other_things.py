"""
def TF():
    return None

#Fonction servant à afficher le(s) mot(s) ayant le score TD-IDF le plus élevé dans un texte
def TF_ELEVE(texte):
    dico_max = {}
    dico = TF(texte)
    liste_count = list(dico.values())
    maxx = max(liste_count)
    for i in dico.keys():
        if dico[i] == maxx:
            dico_max[i] = dico[i]
    return dico_max

with open("/Users/hugojuzyna/ProjetL1/cleaned/Nomination_Chirac1.txt", "r") as fichier1:
    texte1 = fichier1.read()
with open("/Users/hugojuzyna/ProjetL1/cleaned/Nomination_Chirac2.txt", "r") as fichier2:
    texte2 = fichier2.read()
with open("/Users/hugojuzyna/ProjetL1/cleaned/Nomination_Giscard dEstaing.txt", "r") as fichier3:
    texte3 = fichier3.read()
with open("/Users/hugojuzyna/ProjetL1/cleaned/Nomination_Hollande.txt", "r") as fichier4:
    texte4 = fichier4.read()
with open("/Users/hugojuzyna/ProjetL1/cleaned/Nomination_Macron.txt", "r") as fichier5:
    texte5 = fichier5.read()
with open("/Users/hugojuzyna/ProjetL1/cleaned/Nomination_Mitterrand1.txt", "r") as fichier6:
    texte6 = fichier6.read()
with open("/Users/hugojuzyna/ProjetL1/cleaned/Nomination_Mitterrand2.txt", "r") as fichier7:
    texte7 = fichier7.read()
with open("/Users/hugojuzyna/ProjetL1/cleaned/Nomination_Sarkozy.txt", "r") as fichier8:
    texte8 = fichier8.read()




def a(chaine):
    s_n = []
    for i in chaine:
        s_n.append(i)
    x = tuple(s_n)
    return (s_n, x)

print(a("34,67,12"))













def a(chaine):
    s_n = []
    for i in chaine:
        s_n.append(i)
    x = tuple(s_n)
    return (s_n, x)

print(a("34,67,12"))


def exo4(chaine):






    return 0






import os 
import math

def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

# Variable importante 

# Call of the function
directory = "/Users/hugojuzyna/ProjetL1/speeches" # changer le chemin pour acceder au fichier
files_names = list_of_files(directory, ".txt")
#print(files_names) 

# Dictionnaire des noms des presidents 
dico_prenom = {
    'Chirac': 'Jacques',
    'Mitterrand': 'François',
    'Sarkozy': 'Nicolas',
    'Hollande': 'François',
    'Macron': 'Emmanuel',
    'Giscard dEstaing': 'Valéry'
}

#Fonctions importante

# Focntion qui detruit les doublons 
def destruct_doublon_nb(var):
    L = []
    for i in range(len(var)):
        a = (var[i][-1])
        if chr(57) >= a and a >= chr(48) :
            var[i] = var[i][:-1]
    for i in var:
        if not(i in L): 
            L.append(i)
    return L


#Extraire les noms des présidents à partir des noms des fichiers texte fournis ; 
def extract_president_names(file):
    liste = []
    pr_names = []  # Utilisez un ensemble pour éviter les doublons
    # on fait une première boucle pour mettre dans une liste tous les présidents avec leurs numéros
    # permettant d'enlever leurs type et + 
    for i in files_names:
        pr_names.append(i[11:-4])

    pr_names = destruct_doublon_nb(pr_names)
    #print(pr_names)
    return pr_names

#fonction TD-IDF et autres

# compte le nombre d'occurences d'un mot dans un texte sans ponctuation
def count_word(texte, word): 
    count = 0
    word_1 = ""
    for i in range(len(texte)):
        if texte[i] == " ":
            if word == word_1:
                count += 1 
            word_1 = ""
        else:
            word_1 += texte[i]
    return count


#Fonction servant à renvoyer le TD-IDF
def TF(texte): 
    liste_word = []
    word_index = {}
    word_1 = ""
    for i in range(len(texte)):
        if texte[i] == " " and word_1 != " ":
            if not(word_1 in liste_word):
                liste_word.append(word_1)
            word_1 = ""
        else:
            word_1 += texte[i]
    for i in liste_word:
        n = count_word(texte, i)
        word_index[i] = n
    return word_index

#Fonction servant à afficher le(s) mot(s) ayant le score TD-IDF le plus élevé dans un texte
def TF_ELEVE(dico):
    dico_max = {}
    liste_count = list(dico.values())
    maxx = max(liste_count)
    for i in dico.keys():
        if dico[i] == maxx:
            dico_max[i] = dico[i]
    return dico_max


# fonction servant à creer un dictionnaire generale en fonction du repertoire et à renvoyer la longueur du contenue
def dico_global_dossier(repertoire):
    f_texte = list_of_files(repertoire, ".txt")
    dico_global_mot = {}
    contenue_texte = ""
    for i in f_texte:
        with open("/Users/hugojuzyna/ProjetL1/cleaned/{}".format(i), "r") as fichier1:
            texte1 = fichier1.read()
            contenue_texte += texte1 + " " 
    dico_global_mot = TF(contenue_texte)
    return dico_global_mot, len(contenue_texte)

# fonction servant à creer un dictionnaire generale 
def dico_global_president(president):
    f_texte = list_of_files("/Users/hugojuzyna/ProjetL1/cleaned", "txt")
    dico_global_mot = {}
    contenue_texte = ""
    for i in f_texte:
        if president in i:
            with open("/Users/hugojuzyna/ProjetL1/cleaned/{}".format(i), "r") as fichier1:
                texte1 = fichier1.read()
                contenue_texte += texte1 + " " 
    dico_global_mot = TF(contenue_texte)
    return dico_global_mot

def IDF(repertoire):
    dico_IDF = dico_global_dossier(repertoire) [0]
    contenue_texte = dico_global_dossier(repertoire)[1]
    for i in list(dico_IDF.keys()):
        dico_IDF[i] = math.log10((len(contenue_texte) / dico_IDF[i]) + 1)
    return dico_IDF

def TF_IDF(repertoire):
    matrice_TF_IDF = {}
    dico_TF = TF(dico_global_dossier(repertoire)[0])
    dico_IDF = IDF(repertoire)
    for i in list(dico_IDF.keys()):
        matrice_TF_IDF[i] = dico_IDF[i] * dico_TF[i]
    return matrice_TF_IDF


#Programme principale 


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

            # AVec TF mais prend trop de temps à lancer
            # dico_TF = TF(texte1)
            # if not(mot in dico_TF.keys()):
            #     dico_TF[mot] = 0
            
            contenue_mot = texte1.split()
            score_tf = 0
            if mot in contenue_mot:
                for i in contenue_mot:
                    if i == mot:
                        score_tf += 1
                        
            score_tf_idf.append(score_tf * dico_IDF[mot])
        dico_TF_IDF[mot] = score_tf_idf
    return dico_TF_IDF


# Mettre les fichier de speech convertie dans cleaned

#Parcour les differents fichiers de speechees
for i in files_names:
    with open("/Users/hugojuzyna/ProjetL1/speeches/{}".format(i), "r") as fichier:
        texte = fichier.read()
#corriger saut de ligne
#Conversion des textes en miniscule et ajout dans un fichier du dossier cleaned
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
    nouveau_fichier = open("/Users/hugojuzyna/ProjetL1/cleaned/{}".format(i), "a")
    nouveau_fichier.write(text_cleaned)
    nouveau_fichier.close()


# Ouverture des fichiers de cleaned



# Affichage 

#dico_general = dico_global_dossier("/Users/hugojuzyna/ProjetL1/cleaned")

#Affichage de la liste des noms des présidents
print(extract_president_names(files_names))



# 1 Afficher la liste des mots les moins importants dans le corpus de documents. Un mot est dit non important, si son TD-IDF = 0 dans tous les fichiers



# 2 Afficher le(s) mot(s) ayant le score TD-IDF le plus élevé


# 3 Afficher le(s) mot(s) le(s) plus répété(s) par le président Chirac
dico_chirac = dico_global_president("Chirac")

print("Le mot le plus repete par le president Chirac dans le premier texte est",TF_ELEVE(dico_chirac))
print(TF_IDF("/Users/hugojuzyna/ProjetL1/cleaned"))

# 4. Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois



# 5. Indiquer le premier président à parler du climat et/ou de l’écologie

# 6. Hormis les mots dits « non importants », quel(s) est(sont) le(s) mot(s) que tous les présidents ont évoqués.
"""


"""
for mot in Score_TF_IDF_CLEANED.keys():
    
    if max_tab(Score_TF_IDF_CLEANED[mot]) == 0:
        liste_mot_non_important.append(mot)
print("la liste des mots les moins importants dans le corpus de documents sont", liste_mot_non_important)
"""

def max_tab(tab):
    if len(tab) <= 0:
        return None, None  # Retourne None si le tableau est vide
    else:
        valeur_max = tab[0]
        for i in range(1, len(tab)):
            if tab[i] > valeur_max:
                valeur_max = tab[i]
        return valeur_max
