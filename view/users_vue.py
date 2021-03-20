import mysql.connector
import interface_console
import database
import client_controller
import sys
sys.path.append("..\\model\\")
sys.path.append("..\\view\\")
from beautifultable import BeautifulTable
from datetime import datetime
from view.vue_mere import *
from getpass import getpass

class Users_vue(Vue_mere):
    def __init__(self):  # Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor()
        self.nomTable="users"

    def Menu(self):
        try:    
            quit = False
            while(quit == False):
                interface_console.aff_menu_users()  # Affichage menu table
                choix = input("\nVotre choix : ")
                if choix == "1" or choix == "2" or choix == "3" or choix == "4":
                    return choix
                elif choix == "5":
                    quit = True
        except:
            print("+++ Erreur dans le menu "+self.nomTable+" +++")

    def getRow(self, header):
        #Initialisation de la liste qui va récupérer les variables pour la query
        query_list=["NULL"]
        #Préparation de la table magique
        table_vide=BeautifulTable(maxwidth=300)
        result_table=BeautifulTable(maxwidth=600)
        result_table.columns.header=header
        table_vide.columns.header=header
        table_vide.rows.append(["","","",""])  #Ajout de valeur "invisible" dans la table magique pour pouvoir afficher à l'utilisateur la row qu'il souhaite remplir de valeurs
        print(table_vide)
        try:
            for value in header:
                if value!="ID Utilisateur":
                    if value=="Password":
                        rep=getpass("Password : ")
                    else:
                        rep=input("### Veuillez entrer une valeur ###\n"+value+" : ")     #Gestion des erreurs et mauvais input      
                    if rep=="":    
                        while rep=="":
                            rep=input("### Veuillez entrer une valeur ###\n"+value+" : ")
                    elif value=="Nom" or value=="Pseudonyme":
                        if len(rep)>20:
                            reponse=input("Attention, cette valeur est trop longue. Elle risque d'être tronquée dans la base de données.\nEntrer une nouvelle valeur ? Y/N : ")
                            if reponse=="Y":
                                rep=input("### Veuillez entrer une valeur ###\n"+value+" : ")
                    elif value=="Password":
                        check_password=self.strongPasswordChecker(rep)
                        while(check_password>0):
                            print("Veuillez indiquer un mot de passe contenant une majuscule, une minuscule et un chiffre. 3 même lettres à la suite sont interdites. min : 6 max : 20")
                            rep=getpass("Password : ")
                            check_password=self.strongPasswordChecker(rep)
                    query_list.append(rep)
        except:
            print("+++ Erreur dans l'insertion de données, veuillez recommencer +++")

        result_table.rows.append(query_list)
        print(result_table)
        while(True):
            try:
                print("\n\nVeuillez vérifier ces valeurs, sont-elles correctes ? Y/N \nou annuler et revenir au menu ? Q")
                reponse=input("Votre réponse : ")
                if reponse=="Y":
                    return query_list
                elif reponse=="N":
                    while(True):
                        reponse=input("Indiquez le nom exact de la colonne dont la valeur n'est pas correcte. \nSi vous souhaitez ré-afficher les valeurs, entrez \"P\"\nSi vous souhaitez valider, entrez \"V\"\nSi vous souhaitez annuler et retour au menu, entrez \"A\".\n Votre réponse : ")
                        if reponse=="A":
                            input("Retour au menu... Appuyer sur une touche pour continuer")
                            return None
                        elif reponse=="V":
                            return query_list
                        elif reponse=="P":
                            print(result_table)         #TODO: Implémenter une méthode de récupération de mot de passe similaire à celle du dessus || découper ce bloc en plusieurs fonctions
                        elif reponse in header:
                            new_value=input("Entrez la valeur pour "+reponse+": ")
                            header[header.index(reponse)]=new_value
                            result_table.rows.append(query_list)

                elif reponse=="Q":
                    print("### Retour au menu... ###")
                    return None
            except:
                print("+++ Erreur dans la validation des données +++")


    def strongPasswordChecker(self, s): #Trouvée sur internet
        missing_type = 3
        if any('a' <= c <= 'z' for c in s): missing_type -= 1
        if any('A' <= c <= 'Z' for c in s): missing_type -= 1
        if any(c.isdigit() for c in s): missing_type -= 1
        change = 0
        one = two = 0
        p = 2
        while p < len(s):
            if s[p] == s[p-1] == s[p-2]:
                length = 2
                while p < len(s) and s[p] == s[p-1]:
                    length += 1
                    p += 1
                change += length / 3
                if length % 3 == 0: one += 1
                elif length % 3 == 1: two += 1
                else:
                    p += 1
            if len(s) < 6:
                return max(missing_type, 6 - len(s))
            elif len(s) <= 20:
                return max(missing_type, change)
            else:
                delete = len(s) - 20
                change -= min(delete, one)
                change -= min(max(delete - one, 0), two * 2) / 2
                change -= max(delete - one - 2 * two, 0) / 3
                return delete + max(missing_type, change)


    


   





