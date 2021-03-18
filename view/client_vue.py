import mysql.connector
import interface_console
import database
import client_controller
import sys
sys.path.append("..\\model\\")
sys.path.append("..\\view\\")
from beautifultable import BeautifulTable
from datetime import datetime


class Client_vue():
    def __init__(self):  # Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor()
        pass

    def Menu(self):
        try:    
            quit = False
            while(quit == False):
                interface_console.aff_menu_table("clients")  # Affichage menu table
                choix = input("\nVotre choix : ")
                if choix == "1" or choix == "2" or choix == "3" or choix == "4":
                    return choix
                elif choix == "5":
                    quit = True
        except:
            print("+++ Erreur dans le menu clients +++")

    def Display_Rows(self, table):
        try:
            if table == None:
                vue_client.Display_Error()
            else:
                print("### Affichage de votre requête : ###\n")
                print(table)
        except:
            self.Display_Error()

    def Row_getId(self):
        try:
            chiffre=False
            while(chiffre == False):
                # TODO: Vérifier que l'id se trouve dans la bdd pour notifier l'utilisateur
                id = input("Veuillez choisir l'ID de la ligne à effacer\nVotre choix : ")
                chiffre = self.Intable(id)
            return id
        except:
            return False

    def Delete_Row_getConfirmation(self, id):
        try:    
            while(True):
                reponse = input("La ligne avec l'ID "+id+" va être supprimée. Confirmer ? Y/N\nVotre réponse : ")
                if reponse == "Y":
                    return True
                elif reponse == "N":
                    return False
                else:
                    print("### Veuillez choisir une des réponses proposées. ###")
        except:
            self.Display_Delete_Error()

    def Alter_Row_getConfirmation(self, id):
        try:    
            while(True):
                reponse = input("La ligne avec l'ID "+id+" va être modifiée. Confirmer ? Y/N\nVotre réponse : ")
                if reponse == "Y":
                    return True
                elif reponse == "N":
                    return False
                else:
                    print("### Veuillez choisir une des réponses proposées. ###")
        except:
            self.Display_Delete_Error()

    def Build_Row(self):
        #Initialisation de la liste qui va récupérer les variables pour la query
        query_list=["NULL"]
        #Préparation de la table magique
        table_vide=BeautifulTable(maxwidth=300)
        result_table=BeautifulTable(maxwidth=300)
        result_table.columns.header=self.aff_col
        table_vide.columns.header=self.aff_col
        table_vide.rows.append(["","","","","","","","","",""])  #Ajout de valeur "invisible" dans la table magique pour pouvoir afficher à l'utilisateur la row qu'il souhaite remplir de valeurs
        print(table_vide)
        try:
            for value in self.aff_col:
                if value!="ID":
                    print("Indiquez une valeur pour \""+value+"\"")     #TODO: Gérer erreur ici insertion
                    rep=input("Valeur : ")      #TODO : Gérer la date et l'âge et rien
                    if rep=="":    
                        while rep=="":
                            rep=input("### Veuillez entrer une valeur ###")
                    elif value=="Age":
                        test_int=self.Intable(rep)
                        while(test_int==False):
                            rep=input("### Veuillez entrer un NOMBRE  ###")
                            test_int=self.Intable(rep)
                    elif value=="Date de naissance":
                        test_date=self.Dateable(rep)
                        while(test_date==False):
                            rep=input("### Veuillez entrer une date selon ce format : YYYY-MM-DD  ###")
                            test_date=self.Dateable(rep)
                        rep+=' 00:00:00'
                        print(rep)
                    
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
                    print("### Redémarrage de l'insertion de données ###")
                    self.Build_Row()
                elif reponse=="Q":
                    print("### Retour au menu... ###")
                    return None
            except:
                print("+++ Erreur dans la validation des données +++")



    def Display_Select_Error(self):
        print("+++ Une erreur est survenue dans l'affichage des clients +++")

    def Display_Delete_Error(self):
        print("+++ Une erreur est survenue dans la suppression du client +++")

    def Display_BackToMenu(self):
        input("~~~ Action réussie. Retour au menu. Appuyer sur une touche pour continuer... ~~~")


    #
    # Méthodes de tests
    #
    def Intable(self, nombre):
        try:
            int_nombre=int(nombre)
            return True
        except:
            return False

    def Dateable(self, date):
        try:
            date=datetime.strptime(date, '%Y-%m-%d')
            return True
        except:
            return False
    #
    #
    #





