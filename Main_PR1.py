
import os 
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

# Vérification du contenu du dossier 'cleaned'


contenue_dossier = os.listdir("./cleaned/")


# Si le dossier 'cleaned' est vide, nettoyage des fichiers de 'speechees' et création de fichiers dans 'cleaned'

if len(contenue_dossier) <= 8: # Mettre les fichier de speech convertie dans cleaned
    #Parcour les differents fichiers de speechees
    for i in files_names:
        with open("./speeches/{}".format(i), "r") as fichier:
            texte = fichier.read()
        # Nettoyage des textes en convertissant en minuscules et supprimant la ponctuation
        # Création de nouveaux fichiers dans le dossier 'cleaned' avec le texte nettoyé
        text_cleaned = "" 
        for a in range(len(texte)):
            if ord(texte[a]) >= 65 and ord(texte[a]) <= 90:
                text_cleaned += chr(ord(texte[a]) + 32)
            if (ord(texte[a]) >= 21 and ord(texte[a]) <=47) or (ord(texte[a]) >=58 and ord(texte[a])<= 64) or (texte[a])=="\n" :
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

#print(extract_president_names(files_names))



def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# 1 Afficher la liste des mots les moins importants dans le corpus de documents. Un mot est dit non important, si son TD-IDF = 0 dans tous les fichiers

#Je veux les n mots les moins importants 

def n_mot_moins_important(n):
    if n < 0:
        return None
    else:
        liste_mot_moins_im_n = [] 
        i = 0
        for mot_p in dico_mot_im_trie.keys():
            liste_mot_moins_im_n.append(mot_p)
            if i == n-1:
                return ("la liste des n mots les moins importants dans le corpus de documents sont: ",(liste_mot_moins_im_n))
            i += 1

    
# 2 Afficher le(s) mot(s) ayant le score TF-IDF le plus élevé

def TF_IDF_eleve():
    list_mot = list(dico_mot_im_trie)
    return ("le mot ayant le score TF-IDF le plus élevé est ", list_mot[-1])
#print(TF_IDF_eleve)

# 3 Afficher le(s) mot(s) le(s) plus répété(s) par le président Chirac

def word_chirac():
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
        with open ("./cleaned/{}".format(i), 'r') as fichier:
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

def one_president_climt():
    dico_climat_eco = {}

    for i in files_names:
        with open("./cleaned/{}".format(i), 'r') as fichier:
            contenu = fichier.read()
            texte_mot_cleaned = contenu.split()
            nom_president = (i[11:-4])
            for index in range(len(texte_mot_cleaned)):
                if texte_mot_cleaned[index] == "climat" or texte_mot_cleaned[index] == "écologie":
                    if not nom_president in dico_climat_eco.keys():
                        dico_climat_eco[nom_president] = index
    return ("Le premier président à parler du climat et/ou de l’écologie est", min_dico_valeur(dico_climat_eco))

#print(one_president_climt())

# 6. Hormis les mots dits « non importants », quel(s) est(sont) le(s) mot(s) que tous les présidents ont évoqués.

def mots_evoque_pr():
    mots_evoque = []
    for score in Score_TF_IDF_CLEANED:
        if min_tab(Score_TF_IDF_CLEANED[score]) != 0:
            if somme(Score_TF_IDF_CLEANED[score]) >= 10:
                mots_evoque.append(score)
    return ("le(s) mot(s) que tous les présidents ont évoqués sont:",mots_evoque)

#print(mots_evoque_pr())





# Partie 2 du projet

# 1. Tokenisation de la Question :
def tokenisation_question(question):

    #On va d'abord mettre tous les termes de la question en minuscules

    question_minuscule = ''

    #On fait une boucle pour vérifier chaque caractère de la question
    for lettre in question:
        #S'il est en majuscule, on le rajoute à la chaine de caractère après l'avoir passé en minuscule
        if 65 <= ord(lettre) <= 90:
            question_minuscule += chr(ord(lettre)+32)
        

        #Sinon, on le rajoute telle quel
        else:
            question_minuscule += lettre

    #On va maintenant enlever la ponctuation de la question
    question_clean = ''

    #On parcourt chaque caractère de la question
    for caractere in question_minuscule:

        #Si c'est une ponctuation on le remplace par un espace
        
        if ((21 <=ord(caractere) <= 47) or (58 <= ord(caractere) <= 64) or (91<=ord(caractere)<=96) or (123<=ord(caractere)<=126) or (caractere) == "\n"):
            question_clean += ' '
    
        #Sinon, on le rajoute le caractere sans modification

        else:
            question_clean += caractere

    #On utilise la fonction split pour séparer tous les mots de la question et les mettre dans une liste
    mot_question = question_clean.split()

    return mot_question


# 2. Recherche des mots de la question dans le Corpus :

def mot_question_et_document(question):
    #On crée une liste vide pour y stocker les mots présents à la fois dans la question et dans le document
    mot_question_documents = []

    #On appelle la fonction tokenisation pour avoir les mots présent dans la question
    mot_question = tokenisation_question(question)

    #Pour chaque mot de la question on vérifie s'il est dans le corpus et si oui on l'ajoute dans la liste
    for mot in mot_question:
        if mot in Score_TF_IDF_CLEANED.keys():
            mot_question_documents.append(mot)
    return mot_question_documents

#print(mot_question_et_document("chaine, climat, politique, président, politique, nature"))


# 3. Calcul du vecteur TF-IDF pour les termes de la question :


def TF_IDF_question(question):
    #Crée un dico vide pour y stocker le vecteur TF_IDF de la question
    vecteur_TF_IDF_question = {}

    #Appel une focntion qui va donner l'ensemble des mots de la questions
    #Et une qui va donner l'ensemble des mots de chaque fichier ainsi que la valeur de son IDF
    mots_questions = tokenisation_question(question)
    mots_repertoire = IDF("cleaned")
    # On appel la fonction qui donne les mots présent dans la quetion et dans le document
    mot_question_documents = mot_question_et_document(question)

    #On fait une boucle pour calculer le vecteur TF_IDF de chaque mots pour chaque fichier
    for mots in mots_repertoire.keys():

        #On vérifie si le mot est présent à la fois dans la question et dans le texte
        if mots in mot_question_documents:
            #On fait un boucle pour calculer le nombre d'occurences du mot dans la question
            occ_mot = 0
            for mot in mots_questions:
                if mots == mot:
                    occ_mot += 1
            #On calcul le score TF du mot
            score_TF = occ_mot/len(mots_questions)
        #Si oui on calcul sa valeur et on l'ajoute au dico des vecteurs
            vecteur_TF_IDF_question[mots] = score_TF * mots_repertoire[mots]

        #Sinon sa valeur est égal à zéro
        else:
            vecteur_TF_IDF_question[mots] = 0

    #On renvoit le dico
    return vecteur_TF_IDF_question



# 4.) Calcul vectorielle

def produit_scalaire(A, B):
    somme = 0
    for i in A:
        somme = somme + (A[i] * B[i])
    return somme 

def norme_vecteur(A):
    somme = 0
    for i in A:
        somme = somme + (A[i])**2
    somme = (somme)**(1/2)
    return somme

def similarite_cosinus(A, B):
    produit_scalaire_ab = produit_scalaire(A, B)
    norme_a = norme_vecteur(A)
    norme_b = norme_vecteur(B)
    res = (produit_scalaire_ab/(norme_a+norme_b))
    return res

def transforme_dico(dico):
    # Créer le nouveau dictionnaire transformé
    transformed_dico = {}
    for i, fichier_name in enumerate(files_names):
        values = [dico[key][i] for key in dico]
        transformed_dico[fichier_name] = {key: value for key, value in zip(dico.keys(), values)}

    return transformed_dico


# 5. Calcul du document le plus pertinent 


# Exercice 5:  
def calcul_document_plus_pertinent(question):
    TD_IDF_tous_fichier = transforme_dico(Score_TF_IDF_CLEANED)
    TF_IDF_question1 = TF_IDF_question(question)
    dico_similarite = {}
    for i in TD_IDF_tous_fichier:
            similarite = similarite_cosinus(TD_IDF_tous_fichier[i], TF_IDF_question1)
            dico_similarite[i] = similarite
    max = 0
    for i in dico_similarite:
        if max < dico_similarite[i]:
            max = dico_similarite[i]
            indice_max = i
    return indice_max


# 6. Génération d’une réponse

# Permet de trouver la phrase dans le texte correspondant au mot

def trouver_occurrence_et_phrase(document, mot):
    # Lire le contenu du document
    with open( "./speeches/" + document, 'r') as file:
        contenu_document = file.read()

    # Trouver la position du mot dans le contenu du document
    position_mot = -1
    for i in range(0, len(contenu_document)):
        if contenu_document[i:i+len(mot)] == mot:
            position_mot = i
            break

    # Trouver le début de la phrase
    debut_phrase = 0
    for i in range(position_mot, 0, -1):
        if contenu_document[i] == '.':
            debut_phrase = i + 1 # Commencer la phrase juste apres le mot
            break

    # Trouver la fin de la phrase
    fin_phrase = len(contenu_document)
    for i in range(position_mot, len(contenu_document)):
        if contenu_document[i] == '.':
            fin_phrase = i # finir la phrase au point
            break

    # Extraire la phrase
    phrase_contenant_mot = contenu_document[debut_phrase:fin_phrase+1]

    return phrase_contenant_mot


# 7 Affiner la reponse obtenue depuis la question 

def affiner_reponse(question, ph_brute):

    # Dictionnaire de formes de questions possibles et de modèles de réponses associés
    question_starters = {
        "Comment": "Après analyse, {}",
        "Pourquoi": "Car, {}",
        "Peux-tu": "Oui, bien sûr! {}"
    }

    # Extraire le texte brut de la réponse générée
    reponse = ph_brute.strip()

    # Trouver la forme de la question
    forme_question = None
    for debut in question_starters:
        if (debut) in question:
            forme_question = debut
            break


    # Si une forme de question correspondante est trouvée, utiliser le modèle de réponse associé
    if forme_question:
        modele_reponse = question_starters[forme_question]
        reponse = modele_reponse.format(reponse)

    # Mettre en majuscule la première lettre de la réponse
    reponse = reponse.capitalize()

    # Ajouter un point à la fin de la réponse
    if reponse[-1] != ('.'):
        reponse += '.'

    return reponse


# 6 generer une reponse à la question posée (deuxieme partie de l'etape 6)


def dispose_score_mot_TF_IDF_du_doc(question, doc):

    liste_mot = tokenisation_question(question)
    liste_mot_doc = []
    liste_mot_doc_TF_IDF = []
    idx = 0

    # Permet d'obtenir la position de du corpus dans la liste des fichiers que l'on pourrait reutiliser par la suite
    
    for index in range(len(files_names)):
        if doc in files_names[index]:
            idx = index

    #Permet d'ajouter le score tf_idf de chaque mot correspondant dans une liste

    for i in liste_mot:
        if i in Score_TF_IDF_CLEANED.keys():
            if int(Score_TF_IDF_CLEANED[i][idx]) != 0:
                liste_mot_doc.append(i)
                liste_mot_doc_TF_IDF.append(Score_TF_IDF_CLEANED[i][idx])
    
    return liste_mot_doc, liste_mot_doc_TF_IDF



def generer_reponse(question, corpus):
    # dispose le score des mots du doc pertinent dans une liste_mot et sion score Tf_idf
    liste_mot_doc, liste_mot_doc_TF_IDF = dispose_score_mot_TF_IDF_du_doc(question, corpus)

    #Permet d'obtenir la position du score max TF IDF dans la liste mot ou ajouter dans un dico pour renvoyer valeur max apres
    
    index = 0
    for i in range(len(liste_mot_doc_TF_IDF)):
        if liste_mot_doc_TF_IDF[index] < liste_mot_doc_TF_IDF[i]:
            index = i
    

    mot = liste_mot_doc[index]

    phrase = trouver_occurrence_et_phrase(corpus, mot) # forme brute
    print("Réponse brute :", phrase) # Afficher forme brute
    
    phrase_affiner = affiner_reponse(question, phrase) # forme affiner, tulisation du dictionnaire

    return phrase_affiner



# Affichage deuxieme partie du projet

# Exemple d'utilisation


question = "Peux-tu me dire comment une nation peut-elle prendre soin du climat ?"
document = calcul_document_plus_pertinent(question)
reponse_affinee = generer_reponse(question, document )


# Afficher le résultat

print("Question :", question)
print("Réponse affinée :", reponse_affinee)






