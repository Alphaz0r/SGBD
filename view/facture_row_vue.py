import mysql.connector
import interface_console
import client_controller
import sys
sys.path.append("..\\model\\")
sys.path.append("..\\view\\")
from beautifultable import BeautifulTable
from datetime import datetime
from view.vue_mere import *

class FactureRow_vue(Vue_mere):
    """
    FactureRow_vue class for table ``facture_row`` in db
    """
    def __init__(self, id_facture):  # Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor()
        self.nomTable="facture"
        self.id_facture=id_facture

    def Menu(self):
        """Main menu

        Returns:
            choix [String]: User option choice when navigating to the menu
        """
        try:    
            quit = False
            while(quit == False):
                interface_console.aff_menu_facturerow(self.id_facture)  # Affichage menu table
                choix = input("\nVotre choix : ")
                if choix == "1" or choix == "2" or choix == "3" or choix == "4" or choix=="5":return choix  
        except:
            print("+++ Erreur dans le menu "+self.nomTable+" +++")

    def getConfirmation(self, id, position):
        crud=["modifiée", "supprimée","créée"]
        try:    
            while(True):
                if crud[position]=="modifiée" or crud[position]=="supprimée":
                    reponse = input("La ligne avec l'ID "+id+" va être "+crud[position]+". Confirmer ? Y/N\nVotre réponse : ")
                    if position==1:
                        print("/!\ Cela inclus toutes les informations de la factures. /!\\")
                        reponse=input("Confirmer quand même ? Y/N\nVotre réponse : ")
                else:
                    reponse = input("Lancement du processus de création. Confirmer ? Y/N\nVotre réponse : ")
                if reponse == "Y":
                    return True
                elif reponse == "N":
                    return False
                else:
                    print("### Veuillez choisir une des réponses proposées. ###")
        except:
            return False

    def getClient(self): #TODO: A FAIRE
        try:    
            reponse = input("Indiquez l'id du client à qui la facture sera adressée : ")
            return reponse
        except:
            return False

    def Row_getId(self):
        try:
            chiffre=False
            while(chiffre == False):
                # TODO: Vérifier que l'id se trouve dans la bdd pour notifier l'utilisateur
                id = input("Veuillez choisir la LIGNE FACTURE \nVotre choix : ")
                chiffre = self.Intable(id)
            return id
        except:
            return False

    def getRow(self, header, table_drugs):
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
        result_table.columns.header=["Ligne facture","ID Médicament","Nombre"]
        table_vide.columns.header=header
        table_vide.rows.append(["","","","","","","","",""])  #Ajout de valeur "invisible" dans la table magique pour pouvoir afficher à l'utilisateur la row qu'il souhaite remplir de valeurs
        print(table_vide)
        try:
            for value in header:
                if value=="ID Médicament":
                    print(table_drugs)
                    rep=input("### Veuillez entrer un ID Médicament  ###\n ID Médicament : ")
                    query_list.append(rep)
                elif value!="ID facture" and value!="Ligne facture" and value!="Nom médicament" and value!="Concentration en mg" and value!="Nom client" and value!="Prénom client" and value!="ID Client" :
                    rep=input("### Veuillez entrer une valeur ###\n"+value+" : ")     #Gestion des erreurs et mauvais input      
                    if rep=="":    
                        while rep=="":
                            rep=input("### Veuillez entrer une valeur ###\n"+value+" : ")
                    test_int=self.Intable(rep)
                    while(test_int==False):
                        rep=input("### Veuillez entrer un NOMBRE  ###\n Nombre : ")
                        test_int=self.Intable(rep)
                    query_list.append(rep)
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
                                print(result_table)         #TODO:5découper ce bloc en plusieurs fonctions
                            elif reponse in header:
                                new_value=input("Entrez la valeur pour "+reponse+": ")
                                header[header.index(reponse)]=new_value     #TODO:Vérification ???? ATTENTION ATTENTION
                                result_table.rows.append(query_list)        #Régler cette ligne, affichage double ATTENTION ATTENTION
 
                    elif reponse=="Q":
                        print("### Retour au menu... ###")
                        return None
                except:
                    print("+++ Erreur dans la validation des données +++")
        except:
            print("+++ Erreur dans l'insertion de données, veuillez recommencer +++")


    


   





