from Main_PR1 import *

def menu_general():
    clear_terminal()
    print("-" * 80)
    # On propose à l'utilisateur de choisir l'option qu'il souhaite exécuter.
    print("Que souhaitez-vous faire ?\n"
          "\n"
          "- Tapez 1 : Acceder au menu de la partie 1 où plusieurs fonctionnalités sont proposés.\n"
          "\n"
          "- Tapez 2 : Acceder au menu chatbot d'interaction avec l'IA.")
    choice1 = input("Choix :")

    clear_terminal()
    print("-" * 80)
    # Selon le choix de l'utilisateur, on appelle le menu appropriée.
    if choice1 == "1":
        menu_part1()
    elif choice1 == "2":
        menu_part2()
        return

    # Si l'utilisateur entre une option incorrecte, on lui propose de réessayer.
    else:
        re3 = input("Option invalide. Voulez-vous réessayer ?\n"
                   "- Tapez 1 pour Oui\n"
                   "- Tapez 2 pour Non\n")
        if re3 == "1":
            menu_general()
        else:
            print("Au revoir.")
            return


# On définit une fonction qui a pour rôle de présenter un menu, servant de lien entre différentes fonctions.
def menu_part1():
    clear_terminal()
    print("-"*80)
    # On propose à l'utilisateur de choisir l'option qu'il souhaite exécuter.
    print("Que souhaitez-vous faire ?\n"
          "- Tapez 1 : Obtenir les mots moins importants des fichiers.\n"
          "- Tapez 2 : Afficher les mots avec les TF-IDF les plus élevés.\n"
          "- Tapez 3 : Trouver les mots les plus fréquemment utilisés par le président Chirac.\n"
          "- Tapez 4 : Obtenir le nom des présidents parlant le plus souvent de la Nation.\n"
          "- Tapez 5 : Savoir quel président a été le premier à parler de l'écologie.\n"
          "- Tapez esc : Quitter le menu.")
    choice2 = input("Choix : ")


    clear_terminal()
    print("-"*80)

    # Selon le choix de l'utilisateur, on appelle la fonction appropriée.
    if choice2 == "1":
        n = int(input("indiquez le nombre de valeurs que vous voulez du nombre de mot non importants dans le repertoire: "))
        print(n_mot_moins_important(n))
    elif choice2 == "2":
        print(TF_IDF_eleve())
    elif choice2 == "3":
        print(word_chirac())
    elif choice2 == "4":
        print(pr_nation())
    elif choice2 == "5":
        print(one_president_climt())
    elif choice2.upper() == "\x1b":
        print("Au revoir")
        return
    
 

    # Si l'utilisateur entre une option incorrecte, on lui propose de réessayer.
    else:
        re = input("Option invalide. Voulez-vous réessayer ?\n"
                   "- Tapez 1 pour Oui\n"
                   "- Tapez 2 pour Non\n")
        if re == "1":
            menu_part1()
        else:
            print("Au revoir.")
            return

    # On propose à l'utilisateur d'essayer une autre option.
    re1 = input("Voulez-vous essayer une autre option ?\n"
                   "- Tapez 1 pour Oui\n"
                   "- Tapez 2 pour Non\n"
                   "- Tapez 3 pour retourner au menu principal\n")
    if re1 == "1":
        menu_part1()
    elif re1 == "3":
        menu_general()
    else:
        print("Au revoir")
        return



# On définit une fonction qui a pour rôle de présenter un deuxième menu afin d'appeler la fonctionde la partie 2
def menu_part2():
    clear_terminal()
    print("-" * 80)
    # On propose à l'utilisateur de poser une question.
    print("A quelle question voulez-vous que je réponde ? :\n")
    question = input("Question :")

    clear_terminal()
    print("-" * 80)
    # On fait appel aux fonctions qui permettent de répondre à la question.
    document = calcul_document_plus_pertinent(question)
    reponse_affinee = generer_reponse(question, document)
    # On affiche le résultat.
    print("Question :", question, "\n")
    print("Réponse affinée :", reponse_affinee, "\n")

    # On propose à l'utilisateur de poser une autre question.
    re2 = input("Voulez-vous poser une autre question ?\n"
                "- Tapez 1 pour Oui\n"
                "- Tapez 2 pour retourner au menu principal\n")
    if re2 == "1":
        menu_part2()
    else:
        menu_general()
        return


# On appelle la fonction menu pour démarrer le programme.
menu_general()
