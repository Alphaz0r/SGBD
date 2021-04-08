import mysql.connector
import interface_console
import client_controller
import sys
sys.path.append("..\\model\\")
sys.path.append("..\\view\\")
from beautifultable import BeautifulTable
from datetime import datetime
from view.vue_mere import *

class Client_vue(Vue_mere):
    """
    Client_vue class for table ``client`` in db
    """ 
    def __init__(self):  # Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor()
        self.nomTable="clients"

    def Menu(self):
        """Main menu

        Returns:
            choix [String]: User option choice when navigating to the menu
        """
        try:    
            quit = False
            while(quit == False):
                interface_console.aff_menu_clients()  # Affichage menu table
                choix = input("\nVotre choix : ")
                if choix == "1" or choix == "2" or choix == "3" or choix == "4" or choix=="5":return choix  
        except:
            print("+++ Erreur dans le menu "+self.nomTable+" +++")

    def getRow(self, header):
        """Ask the user to fill a row and check if every user input is correct. Then ask the user is everything is okay or if he wants to modify something
           Note : - The checks are made after every input but not when asking to modify something >> critical
                  - There could be more checks 

        Args:
            header ([list]): header list of String for "header" row for BeautifulTables

        Returns:
            [list]: Returns a list with every user input in it
        """
        #Initialisation de la liste qui va récupérer les variables pour la query
        query_list=["NULL"]
        #Préparation de la table magique
        table_vide=BeautifulTable(maxwidth=300)
        result_table=BeautifulTable(maxwidth=300)
        result_table.columns.header=header
        table_vide.columns.header=header
        table_vide.rows.append(["","","","","","","","","",""])  #Ajout de valeur "invisible" dans la table magique pour pouvoir afficher à l'utilisateur la row qu'il souhaite remplir de valeurs
        print(table_vide)
        try:
            for value in header:
                if value!="ID":
                    rep=input("### Veuillez entrer une valeur ###\n"+value+" : ")     #Gestion des erreurs et mauvais input      
                    if rep=="":    
                        while rep=="":
                            rep=input("### Veuillez entrer une valeur ###\n"+value+" : ")
                    elif value=="Age" or value=="Code postal":
                        test_int=self.Intable(rep)
                        while(test_int==False):
                            rep=input("### Veuillez entrer un NOMBRE  ###\n Nombre : ")
                            test_int=self.Intable(rep)
                    elif value=="Date de naissance":
                        test_date=self.Dateable(rep)
                        while(test_date==False):
                            rep=input("### Veuillez entrer une date selon ce format : YYYY-MM-DD  ###\n Date sous bon format : ")
                            test_date=self.Dateable(rep)
                        rep+=' 00:00:00'
                    elif value=="Rue" or value=="Email":
                        if len(rep)>30:
                            reponse=input("Attention, cette valeur est trop longue. Elle risque d'être tronquée dans la base de données.\nEntrer une nouvelle valeur ? Y/N : ")
                            if reponse=="Y":
                                rep=input("### Veuillez entrer une valeur ###\n"+value+" : ")
                    elif value=="Nom" or value=="Prenom" or value=="Numéro de téléphone":
                        if len(rep)>20:
                            reponse=input("Attention, cette valeur est trop longue. Elle risque d'être tronquée dans la base de données.\nEntrer une nouvelle valeur ? Y/N : ")
                            if reponse=="Y":
                                rep=input("### Veuillez entrer une valeur ###\n"+value+" : ")
                    elif value=="Numéro de maison":
                        if len(rep)>5:
                            reponse=input("Attention, cette valeur est trop longue. Elle risque d'être tronquée dans la base de données.\nEntrer une nouvelle valeur ? Y/N : ")
                            if reponse=="Y":
                                rep=input("### Veuillez entrer une valeur ###\n"+value+" : ")
                    elif value=="Code postal":
                        if len(rep)>6:
                            reponse=input("Attention, cette valeur est trop longue. Elle risque d'être tronquée dans la base de données.\nEntrer une nouvelle valeur ? Y/N : ")
                            if reponse=="Y":
                                rep=input("### Veuillez entrer une valeur ###\n"+value+" : ")
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
                            print(result_table)
                        elif reponse in header:
                            new_value=input("Entrez la valeur pour "+reponse+": ")
                            header[header.index(reponse)]=new_value
                            result_table.rows.append(query_list)

                elif reponse=="Q":
                    print("### Retour au menu... ###")
                    return None
            except:
                print("+++ Erreur dans la validation des données +++")


    


   





