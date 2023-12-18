from Main_PR1 import *


# 1 Afficher la liste des mots les moins importants dans le corpus de documents. Un mot est dit non important, si son TD-IDF = 0 dans tous les fichiers

#Je veux les n mots les moins importants 

def n_mot_moins_important():
    liste_mot_moins_im_n = [] 
    for mot_p in dico_moyenne.keys():
        if dico_moyenne[mot_p] == 0:
            liste_mot_moins_im_n.append(mot_p)
    return ("la liste des n mots les non importants dans le corpus de documents sont: ",(liste_mot_moins_im_n))

    
# 2 Afficher le(s) mot(s) ayant le score TF-IDF le plus élevé

def TF_IDF_eleve():
    return ("le mot ayant le score TF-IDF le plus élevé est ", (max_dico_valeur(dico_moyenne)))
#print(TF_IDF_eleve)

# 3 Afficher le(s) mot(s) le(s) plus répété(s) par le président Chirac

def mot_chirac():
    dico_chirac = dico_global_president("Chirac")
    mot_max = max_dico_valeur(dico_chirac)
    return ("Le mot le plus repete par le president Chirac dans le premier texte est", mot_max)

#print(word_chirac())

# 4. Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois

def pr_nation():

# On créera un liste max qui prendra pour valeur le mot avec le plus d'occurences, on l'initialise à 0
    listes_president = []
    dico_nation = {}
    for i in files_names:
        with open ("./cleaned/{}".format(i), 'r', encoding="utf-8") as fichier:
            contenu = fichier.read()
        texte_nation = contenu.split()

        nom_president = (i[11:-4])
        if nom_president[-1] >= chr(48) and nom_president[-1] <= chr(57):
            nom_president = nom_president[:-1]
        if "nation" in texte_nation:
            dico_mot = TF(contenu)
            if not(nom_president in listes_president):
                listes_president.append(nom_president)
            if (nom_president in dico_nation.keys()):
                dico_nation[nom_president] = dico_nation[nom_president] + dico_mot["nation"]
            if not(nom_president in dico_nation.keys()):
                dico_nation[nom_president] = dico_mot["nation"]
    return ("Les presidents qui ont parlé du mot « Nation » sont",  listes_president, "et celui qui l'a repete le plus de fois est :",max_dico_valeur(dico_nation) )

#print(pr_nation())

# 5. Indiquer le premier président à parler du climat et/ou de l’écologie

def un_president_climt():
    liste_president_climat = []

    for i in files_names:
        with open("./cleaned/{}".format(i), 'r', encoding="utf-8") as fichier:
            contenu = fichier.read()
            texte_mot_cleaned = contenu.split()
            nom_president = (i[11:-4])
            if ("climat" in texte_mot_cleaned) or ("écologie" in texte_mot_cleaned) or ("écologique" in texte_mot_cleaned) :
                if not nom_president in liste_president_climat:
                    liste_president_climat.append(nom_president)
    return ("Les présidents à parler du climat et/ou de l’écologie sont", (liste_president_climat))

#print(un_president_climt())
