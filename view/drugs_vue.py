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



class Drugs_vue(Vue_mere):
    def __init__(self):  # Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor()
        self.nomTable="drugs"

    def Menu(self):
        try:    
            quit = False
            while(quit == False):
                interface_console.aff_menu_drugs()  # Affichage menu table
                choix = input("\nVotre choix : ")
                if choix == "1" or choix == "2" or choix == "3" or choix == "4":
                    return choix
                elif choix == "5":
                    quit = True
        except:
            print("+++ Erreur dans le menu "+self.nomTable+" +++")

    def getRow(self, header, table_concentration):
        #Initialisation de la liste qui va récupérer les variables pour la query
        query_list=["NULL"]
        #Préparation de la table magique
        table_vide=BeautifulTable(maxwidth=300)
        result_table=BeautifulTable(maxwidth=300)
        result_table.columns.header=header
        table_vide.columns.header=header
        table_vide.rows.append(["","","","","","",""])  #TODO: MODIFIE CA OK
        print(table_vide)
        try:
            for value in header:
                if value!="ID Médicament": #TODO: MODIFIE CA OK
                    if value=="ID Concentration en mg":
                        print(table_concentration)
                    rep=input("### Veuillez entrer une valeur ###\n"+value+" : ")     #Gestion des erreurs et mauvais input      
                    if rep=="":
                        while (rep==""):
                            rep=input("### Veuillez entrer une valeur ###\n"+value+" : ")
                    if value=="Date de péremption":
                        test_date=self.Dateable(rep)
                        while(test_date==False):
                            rep=input("### Veuillez entrer une date selon ce format : YYYY-MM-DD  ###\n Date sous bon format : ")
                            test_date=self.Dateable(rep)
                        rep+=' 00:00:00'
                    elif value=="Nom":
                        if len(rep)>20:
                            reponse=input("Attention, cette valeur est trop longue. Elle risque d'être tronquée dans la base de données.\nEntrer une nouvelle valeur ? Y/N : ")
                            if reponse=="Y":
                                rep=input("### Veuillez entrer une valeur ###\n"+value+" : ")
                    elif value=="Description":
                        if len(rep)>60:
                            reponse=input("Attention, cette valeur est trop longue. Elle risque d'être tronquée dans la base de données.\nEntrer une nouvelle valeur ? Y/N : ")
                            if reponse=="Y":
                                rep=input("### Veuillez entrer une valeur ###\n"+value+" : ")
                    elif value=="Stock" or value=="Prix en €€€" or value=="ID Concentration en mg":
                        test_int=self.Intable(rep)
                        while(test_int==False):
                            rep=input("### Veuillez entrer un NOMBRE  ###\n Nombre : ")
                            test_int=self.Intable(rep)
                    query_list.append(rep)
        except:
            return None

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
                        reponse=input("Indiquez le nom -exact- de la colonne dont la valeur n'est pas correcte. \nSi vous souhaitez ré-afficher les valeurs, entrez \"P\"\nSi vous souhaitez valider, entrez \"V\"\nSi vous souhaitez annuler et retour au menu, entrez \"A\".\n Votre réponse : ")
                        if reponse=="A":
                            input("Retour au menu... Appuyer sur une touche pour continuer")
                            return None
                        elif reponse=="V":
                            return query_list
                        elif reponse=="P":
                            print(result_table)
                        elif reponse in header:
                            if value=="ID concentration en mg":
                                print(table_concentration)
                            new_value=input("Entrez la valeur pour "+reponse+": ")
                            header[header.index(reponse)]=new_value
                            result_table.rows.append(query_list)

                elif reponse=="Q":
                    print("### Retour au menu... ###")
                    return None
            except:
                return None
                



    


   





