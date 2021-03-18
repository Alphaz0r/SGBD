import mysql.connector
import interface_console
import database
import sys
sys.path.append("..\\model\\")
sys.path.append("..\\view\\")
from view.client_vue import *
from model.client_modele import *
from beautifultable import BeautifulTable
from datetime import datetime


class Client_controller():
    def __init__(self, cnx): #Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor() 
        self.cnx=cnx
        self.aff_col= ["ID", "Nom", "Prénom", "Date de naissance", "Age", "Rue", "Numéro de maison", "Code postal", "Email", "Numéro de téléphone"] #Colonnes d'affichage pour BeautifulTables
        self.vue_client=Client_vue() #Création de la vue
        self.modele_client=Client_modele(self.cnx) #Création du modèle
        while(True):
            choix_utilisateur=self.vue_client.Menu()
            if choix_utilisateur=="1":
                self.Display_Rows()
            elif choix_utilisateur=="3":
                self.Delete_Row()
            elif choix_utilisateur=="5":
                break

    def Display_Rows(self):   
        try:
            cursor=self.modele_client.Select_Rows()
            table=BeautifulTable(maxwidth=300) #Préparation de l'affichage des lignes de façon organisée

            #On exécute la query et on y place tous ses éléments dans un module qui va gérer l'affichage
            table.columns.header=self.aff_col
                    
            for row in cursor:
                table.rows.append(row)  
                
            #Affichage de la table
            self.vue_client.Display_Rows(table)
        except:
            self.vue_client.Display_Select_Error()    
        finally:
            cursor.close()

    def Delete_Row(self):
        try:
            id=self.vue_client.Row_getId()
            confirmation=self.vue_client.Delete_Row_getConfirmation(id)
            if  confirmation == True and id!=False:
                self.modele_client.Delete_Row(id)
                self.vue_client.Display_BackToMenu()
            else:
                self.vue_client.Display_Delete_Error()
        except:
            self.vue_client.Display_Delete_Error()

    def Alter_Row(self):
        try:
            table_before=BeautifulTable(maxwidth=300)                   
            table_before.columns.header=self.aff_col   

            id=self.vue_client.Row_getId()
            if id !=False:
                cursor=self.modele_client.Select_Rows(id)
                for row in cursor:
                    table_before.rows.append(row)  

                confirmation=self.vue_client.Alter_Row_getConfirmation(id)
                if confirmation==True:
                    pass
        except:
            return None

           


       