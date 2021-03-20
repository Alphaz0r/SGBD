import mysql.connector
import interface_console
import client_controller
import sys
sys.path.append("..\\model\\")
sys.path.append("..\\view\\")
from beautifultable import BeautifulTable
from datetime import datetime
from view.vue_mere import *

class Facture_vue(Vue_mere):
    def __init__(self):  # Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor()
        self.nomTable="facture"

    def Menu(self):
        try:    
            quit = False
            while(quit == False):
                interface_console.aff_menu_facture()  # Affichage menu table
                choix = input("\nVotre choix : ")
                if choix == "1" or choix == "2" or choix == "3" or choix == "4"or choix=="5" or choix=="6": return choix
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
                        reponse=input("Confirmer quand même ? Y/N\nVotre réponse")
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
                id = input("Veuillez choisir l'ID de la facture \nVotre choix : ")
                chiffre = self.Intable(id)
            return id
        except:
            return False

    def getRow(self, header, table_client):
        #Initialisation de la liste qui va récupérer les variables pour la query
        query_list=["NULL"]
        #Préparation de la table magique
        table_vide=BeautifulTable(maxwidth=300)
        result_table=BeautifulTable(maxwidth=300)
        result_table.columns.header=["ID Facture","FK_client_id","Date de création"]
        table_vide.columns.header=header
        table_vide.rows.append(["","","","","","","","","",""])  #Ajout de valeur "invisible" dans la table magique pour pouvoir afficher à l'utilisateur la row qu'il souhaite remplir de valeurs
        print(table_vide)
        try:
            for value in header:
                if value!="ID Facture" and value!="Nom" and value!="Prénom" and value!="email" and value!="Rue" and value!="Numéro de maison" and value!="Code postal" and value!="Prix Total Facture €€€" and value!="Code postal":
                    if value=="ID Client":print(table_client)
                    elif value=="Date de facturation":print("Utilisez le mot-clef 'now' pour appliquer la date et heure actuelle.")
                    rep=input("### Veuillez entrer une valeur ###\n"+value+" : ")     #Gestion des erreurs et mauvais input      
                    if rep=="":    
                        while rep=="":
                            rep=input("### Veuillez entrer une valeur ###\n"+value+" : ")
                    elif rep=="ID Client":
                        test_int=self.Intable(rep)
                        while(test_int==False):
                            rep=input("### Veuillez entrer un NOMBRE  ###\n Nombre : ")
                            test_int=self.Intable(rep)
                    elif value=="Date de facturation":
                        test_date=self.Dateable(rep)
                        while(test_date==False) and rep!="now":
                            rep=input("### Veuillez entrer une date selon ce format : YYYY-MM-DD HH:MM:SS ###\n Date sous bon format : ")
                            test_date=self.Dateable(rep)
                        if rep=="now":
                            now=datetime.now()
                            rep=now.strftime("%Y-%m-%d %H:%M:%S")
                        
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
                    query_list.append("Null")
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


    


    def Dateable(self, date):
        try:
            date=datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            return True
        except:
            return False


    


   





