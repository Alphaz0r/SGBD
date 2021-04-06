import mysql.connector
import interface_console
import sys
sys.path.append("..\\model\\")
sys.path.append("..\\view\\")
sys.path.append("..\\DAO\\")
from model.concentration_model import *
from view.concentration_vue import *
from DAO.concentration_DAO import *
from beautifultable import BeautifulTable
from datetime import datetime



class Concentration_controller():
    """
    Concentration class for table ``concentration`` in db

    ``cnx`` is the connection object from ``mysql-connector`` needed to send sql commands to the database
    """
    def __init__(self, cnx): #Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor() 
        self.cnx=cnx
        self.aff_col=["ID Concentration","Concentration en mg"] 
        self.vue_concentration=Concentration_vue() 
        self.DAO_concentration=Concentration_DAO(self.cnx) 
        


    def Menu(self):
        """
        Main menu
        """
        while(True):
            choix_utilisateur=self.vue_concentration.Menu()
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
        """
        Launch create row sequence
        """
        try:
            modele_concentration=Concentration_modele()
            table_before=BeautifulTable(maxwidth=300)                   
            table_before.columns.header=self.aff_col
            confirmation=self.vue_concentration.getConfirmation(id,2)  
            if confirmation==True:        
                row=self.vue_concentration.getRow(self.aff_col)

                
                modele_concentration.concentration_mg=row[1]

                if modele_concentration.concentration_mg!=None:
                    creation_reussie=self.DAO_concentration.Insert_Row(modele_concentration)
                    if creation_reussie==True:
                        self.vue_concentration.Display_BackToMenu()
                        return None
            self.vue_concentration.Display_Create_Error()
        except:
            return None

    def Display_Rows(self):   
        """
        launch display row sequence
        """
        try:
            #Préparation de l'affichage des lignes de façon organisée
            cursor=self.DAO_concentration.Select_Rows()
            table=BeautifulTable(maxwidth=300) 

            #On exécute la query et on y place tous ses éléments dans un module qui va gérer l'affichage
            table.columns.header=self.aff_col
                    
            for row in cursor:
                table.rows.append(row)  

            #Affichage de la table
            self.vue_concentration.Display_Rows(table)
        except:
            self.vue_concentration.Display_Select_Error()    
        finally:
            cursor.close()

    def Delete_Row(self):
        """
        launch delete row sequence 
        """
        try:
            id=self.vue_concentration.Row_getId()
            confirmation=self.vue_concentration.getConfirmation(id,1)
            if  confirmation == True and id!=False:
                delete_confirmation=self.DAO_concentration.Delete_Row(id)
                if delete_confirmation==True:
                    self.vue_concentration.Display_BackToMenu()
                    return None
                self.vue_concentration.Display_Delete_Error()
            else :
                print("\n### Aucune action n'a été entreprise, retour au menu ###")
        except:
            self.vue_concentration.Display_Delete_Error()

    def Update_Row(self):
        """
        launch update row sequence
        """
        try:
            modele_concentration=Concentration_modele()
            table_before=BeautifulTable(maxwidth=300)                   
            table_before.columns.header=self.aff_col   

            modele_concentration.PK_concentration_id=self.vue_concentration.Row_getId()
            if modele_concentration.PK_concentration_id !=False:
                cursor=self.DAO_concentration.Select_Rows(modele_concentration.PK_concentration_id)
                for row in cursor:
                    table_before.rows.append(row)  
                self.vue_concentration.Display_Rows(table_before)

                confirmation=self.vue_concentration.getConfirmation(modele_concentration.PK_concentration_id,0)  
                if confirmation==True:  
                    row=self.vue_concentration.getRow(self.aff_col)

                    modele_concentration.concentration_mg=row[1]

                    if modele_concentration.concentration_mg!=None:
                        modification_reussie=self.DAO_concentration.Update_Row(modele_concentration)
                        if modification_reussie==True:
                            self.vue_concentration.Display_BackToMenu()
                            return None
                    self.vue_concentration.Display_Alter_Error()
                else :
                    print("\n### Aucune action n'a été entreprise, retour au menu ###")

        except:
            self.vue_concentration.Display_Alter_Error()
