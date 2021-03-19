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
            if choix_utilisateur=="2":
                self.Update_Row()
            elif choix_utilisateur=="3":
                self.Delete_Row()
            elif choix_utilisateur=="4":
                self.Create_Row()
            elif choix_utilisateur=="5":
                break

    def Create_Row(self):
        try:
            table_before=BeautifulTable(maxwidth=300)                   
            table_before.columns.header=self.aff_col
            confirmation=self.vue_client.getConfirmation(id,0)  
            if confirmation==True:        
                row=self.vue_client.getRow(self.aff_col)
                if row!=None:
                    creation_reussie=self.modele_client.Insert_Row(row)
                    if creation_reussie==True:
                        self.vue_client.Display_BackToMenu()
                        return None
            self.vue_client.Display_Alter_Error()

        except:
            return None

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
            confirmation=self.vue_client.getConfirmation(id,1)
            if  confirmation == True and id!=False:
                self.modele_client.Delete_Row(id)
                self.vue_client.Display_BackToMenu()
            else:
                self.vue_client.Display_Delete_Error()
        except:
            self.vue_client.Display_Delete_Error()

    def Update_Row(self):
        try:
            table_before=BeautifulTable(maxwidth=300)                   
            table_before.columns.header=self.aff_col   

            id=self.vue_client.Row_getId()
            if id !=False:
                cursor=self.modele_client.Select_Rows(id)
                for row in cursor:
                    table_before.rows.append(row)  
                self.vue_client.Display_Rows(table_before)

                confirmation=self.vue_client.getConfirmation(id,0)  
                if confirmation==True:  
                    row=self.vue_client.getRow(self.aff_col)
                    if row!=None:
                        modification_reussie=self.modele_client.Update_Row(row, id)
                        if modification_reussie==True:
                            self.vue_client.Display_BackToMenu()
                            return None
                self.vue_client.Display_Alter_Error()

        except:
            return None

           


       