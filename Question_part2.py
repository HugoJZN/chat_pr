from Main_PR1 import *


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

    text = ""
    for i in mots_questions:
        text += i + " "

    mots_repertoire = Score_idf_cleaned
    # On appel la fonction qui donne les mots présent dans la quetion et dans le document
    mot_question_documents = mot_question_et_document(question)

    #On fait une boucle pour calculer le vecteur TF_IDF de chaque mots pour chaque fichier
    for mots in mots_repertoire.keys():

        #On vérifie si le mot est présent à la fois dans la question et dans le texte
        if mots in mot_question_documents:
            score_TF = TF(text) 
        #Si oui on calcul sa valeur et on l'ajoute au dico des vecteurs
            vecteur_TF_IDF_question[mots] = (score_TF[mots] * mots_repertoire[mots]) / len(mots_questions)

        #Sinon sa valeur est égal à zéro
        else:
            vecteur_TF_IDF_question[mots] = 0

    #On renvoit le dico
    return vecteur_TF_IDF_question



# 4.) Calcul vectorielle

# Calcul le produit scalaire entre deux vecteurs et le retourne
def produit_scalaire(A, B):
    somme = 0
    for i in A:
        somme = somme + (A[i] * B[i])
    return somme 

# Calcul la norme d'un vecteur et la retourne
def norme_vecteur(A):
    somme = 0
    for i in A:
        somme = somme + (A[i])**2
    somme = sqrt(somme)
    return somme

# Calcul la similarité cosinus entre deux vecteurs et la retourne
def similarite_cosinus(A, B):
    produit_scalaire_ab = produit_scalaire(A, B)
    norme_a = norme_vecteur(A)
    norme_b = norme_vecteur(B)
    # On verifie si norme a ou b egal 0 pour ne pas provoquer d'erreur
    if norme_a == 0 or norme_b == 0:
        return 0
    res = (produit_scalaire_ab/(norme_a*norme_b))
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
    # on affecte à la variable indice_max egal la premier cle du dico similarite pour ne pas provoquer d'erreur 
    indice_max = list((dico_similarite.keys()))[0]

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
    with open( "./speeches/" + document, 'r', encoding="utf-8") as file:
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
        "Peux-tu": "Oui, bien sûr! {}",
        "Comment": "Après analyse, {}",
        "Pourquoi": "Car, {}"
    }

    # Extraire le texte brut de la réponse générée
    reponse = ph_brute
    if reponse[0] == "\n":
        rest_reponse = reponse[1:]
        reponse = rest_reponse

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
    if  ord(reponse[0]) <= 122 and ord(reponse[0]) >= 97:
        premier_caractere = chr(ord(reponse[0]) - 32)
        rest_reponse = premier_caractere + reponse[1:]
        reponse = rest_reponse

    # Ajouter un point à la fin de la réponse
    if reponse[-1] != ('.'):
        reponse += '.'

    return reponse


# 6 generer une reponse à la question posée (deuxieme partie de l'etape 6)


def dispose_score_mot_TF_IDF_du_doc(question, doc):
    l = {}
    liste_mot = tokenisation_question(question)
    liste_mot_doc = []
    liste_mot_doc_TF_IDF = []
    idx = 0

    TF_IDF_question1 = TF_IDF_question(question)


    # Permet d'obtenir la position de du corpus dans la liste des fichiers que l'on pourrait reutiliser par la suite
    
    for index in range(len(files_names)):
        if doc in files_names[index]:
            idx = index

    #Permet d'ajouter le score tf_idf de chaque mot correspondant dans une liste

    for i in liste_mot:
        if i in Score_TF_IDF_CLEANED.keys():
            if int(Score_TF_IDF_CLEANED[i][idx]) != 0:
                liste_mot_doc.append(i)
                liste_mot_doc_TF_IDF.append(Score_TF_IDF_CLEANED[i][idx]*TF_IDF_question1[i])

    
    return liste_mot_doc, liste_mot_doc_TF_IDF



def generer_reponse(question, corpus):
    # dispose le score des mots du doc pertinent dans une liste_mot et sion score Tf_idf
    liste_mot_doc, liste_mot_doc_TF_IDF = dispose_score_mot_TF_IDF_du_doc(question, corpus)

    #Permet d'obtenir la position du score max TF IDF dans la liste mot ou ajouter dans un dico pour renvoyer valeur max apres
    
    if len(liste_mot_doc) == 0:
        return ("pas de reponse trouve")

    index = 0
    for i in range(len(liste_mot_doc_TF_IDF)):
        if liste_mot_doc_TF_IDF[index] < liste_mot_doc_TF_IDF[i]:
            index = i
    
    mot = liste_mot_doc[index]

    phrase = trouver_occurrence_et_phrase(corpus, mot) # forme brute
    
    phrase_affiner = affiner_reponse(question, phrase) # forme affiner, tulisation du dictionnaire

    return phrase_affiner


def partie2():

    question = input(" Posez une question ")
    document = calcul_document_plus_pertinent(question)
    reponse_affinee = generer_reponse(question, document )

    # Afficher le résultat

    print("Question :", question)
    print("Réponse affinée :", reponse_affinee)

