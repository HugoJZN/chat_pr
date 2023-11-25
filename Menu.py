from Main_PR1 import *


# On définit une fonction qui a pour rôle de présenter un menu, servant de lien entre différentes fonctions.
def menu():
    clear_terminal()
    print("-"*80)
    # On propose à l'utilisateur de choisir l'option qu'il souhaite exécuter.
    print("Que souhaitez-vous faire ?\n"
          "- Tapez 1 : Obtenir les mots moins importants des fichiers.\n")
    choice = input("Choix : ")


    clear_terminal()
    print("-"*80)

    # Selon le choix de l'utilisateur, on appelle la fonction appropriée.
    if choice == "1":
        n = int(input("indiquez le nombre de valeurs que vous voulez du nombre de mot non importants dans le repertoire: "))
        print(n_mot_moins_important(n))
    elif choice.upper() == "\x1b":
        print("Au revoir")
        return
    
 

    # Si l'utilisateur entre une option incorrecte, on lui propose de réessayer.
    else:
        re = input("Option invalide. Voulez-vous réessayer ?\n"
                      "- Tapez 1 pour Oui\n"
                      "- Tapez 2 pour Non\n")
        if re == "1":
            menu()
        else:
            print("Au revoir.")
            return

    # On propose à l'utilisateur d'essayer une autre option.
    re1 = input("Voulez-vous essayer une autre option ?\n"
                   "- Tapez 1 pour Oui\n"
                   "- Tapez 2 pour Non\n")
    if re1 == "1":
        menu()
    else:
        print("Au revoir.")

# On appelle la fonction menu pour démarrer le programme.
menu()
