import mysql.connector
import sys
sys.path.append("..\\model\\")
sys.path.append("..\\controller\\")
sys.path.append("..\\view\\")
sys.path.append("..\\DAO\\")
from model.facture_model import *
from view.facture_vue import *
from DAO.facture_DAO import *
from controller.client_controller import *
from controller.facture_row_controller import *
from beautifultable import BeautifulTable
from datetime import datetime


class Facture_controller():
    def __init__(self, cnx): #Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor() 
        self.cnx=cnx
        self.aff_col=["ID Facture","ID Client", "Nom","Prénom","email","Rue","Numéro de maison","Code postal","Prix Total Facture €€€","Date de facturation"]
        self.aff_col_client= ["ID", "Nom", "Prénom", "Date de naissance", "Age", "Rue", "Numéro de maison", "Code postal", "Email", "Numéro de téléphone"]
        self.table_client=self.Get_Row_Client()
        self.vue_facture=Facture_vue() #Création de la vue
        

    def WhereWeGoing(self):
        while(True):
            choix_utilisateur=self.vue_facture.Menu()
            if choix_utilisateur=="1":
                self.Display_Rows()
            if choix_utilisateur=="2":
                self.Display_FactureRow()
            elif choix_utilisateur=="3":
                self.Update_FactureRow()
            elif choix_utilisateur=="4":
                self.Delete_Row()
            elif choix_utilisateur=="5":
                self.Create_Row()
            elif choix_utilisateur=="6":break
                

    def Display_Rows(self):   
        try:
            DAO_facture=Facture_DAO(self.cnx) #Création du modèle
            vue_facture=Facture_vue()
            cursor=DAO_facture.Select_Rows()
            table=BeautifulTable(maxwidth=300) #Préparation de l'affichage des lignes de façon organisée

            #On exécute la query et on y place tous ses éléments dans un module qui va gérer l'affichage
            table.columns.header=self.aff_col
                    
            for row in cursor:
                table.rows.append(row)  
                
            #Affichage de la table
            vue_facture.Display_Rows(table)
        except:
            vue_facture.Display_Select_Error()    
        finally:
            cursor.close()

    def Delete_Row(self):
        try:
            DAO_facture=Facture_DAO(self.cnx) #Création du modèle
            vue_facture=Facture_vue()
            id=vue_facture.Row_getId()
            confirmation=vue_facture.getConfirmation(id, 1)
            if  confirmation == True and id!=False:
                DAO_facture.Delete_Row(id)
                vue_facture.Display_BackToMenu()
            else:
                vue_facture.Display_Delete_Error()
        except:
            vue_facture.Display_Delete_Error()

    def Create_Row(self):
        try:
            DAO_facture=Facture_DAO(self.cnx)
            table_before=BeautifulTable(maxwidth=300)                   
            table_before.columns.header=self.aff_col
            confirmation=self.vue_facture.getConfirmation(id,2)  
            if confirmation==True:        
                row=self.vue_facture.getRow(self.aff_col, self.table_client)

                modele_facture=Facture_modele()
                modele_facture.PK_facture_id=row[0]
                modele_facture.FK_client_id=row[1]
                modele_facture.date_creation=row[2]
                
                if row!=None:
                    creation_reussie=DAO_facture.Insert_Row(modele_facture)
                    if creation_reussie==True:
                        self.vue_facture.Display_BackToMenu()
                        return None
                self.vue_facture.Display_Create_Error()
            else :
                self.vue_facture.AucuneActionEntreprise()
        except:
            return None


    def Update_Row(self):   
        try:
            DAO_facture=Facture_DAO(self.cnx)
            table_before=BeautifulTable(maxwidth=300)                   
            table_before.columns.header=self.aff_col
            confirmation=self.vue_facture.getConfirmation(id,2)  
            if confirmation==True:        
                row=self.vue_facture.getRow(self.aff_col, self.table_client)

                modele_facture=Facture_modele()
                modele_facture.PK_facture_id=row[0]
                modele_facture.FK_client_id=row[1]
                modele_facture.date_creation=row[2]
                
                if row!=None:
                    creation_reussie=DAO_facture.Insert_Row(modele_facture)
                    if creation_reussie==True:
                        self.vue_facture.Display_BackToMenu()
                        return None
                self.vue_facture.Display_Create_Error()
            else :
                self.vue_facture.AucuneActionEntreprise()
        except:
            return None

    def Display_FactureRow(self):
        try:    
            vue_facture=Facture_vue()
            id_facture=vue_facture.Row_getId()
            if id_facture!=False:
                controller_factureRow=FactureRow_controller(self.cnx, id_facture)
                controller_factureRow.Display_Rows()
        except:
            self.vue_facture.Display_Select_Error()

    def Get_Row_Client(self):
        try:
            DAO_client=Client_DAO(self.cnx)
            client_list=DAO_client.Select_Rows()
            table_client=BeautifulTable(maxwidth=300)
            table_client.columns.header=self.aff_col_client
            for row in client_list:
                table_client.rows.append(row)
            return table_client
        except:
            return None
        finally:
            client_list.close()

   

           


       