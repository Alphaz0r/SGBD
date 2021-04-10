import mysql.connector
import interface_console
import sys
sys.path.append("..\\model\\")
sys.path.append("..\\view\\")
sys.path.append("..\\DAO\\")
from model.drugs_model import *
from view.drugs_vue import *
from DAO.drugs_DAO import *
from DAO.concentration_DAO import *
from beautifultable import BeautifulTable
from datetime import datetime



class Drugs_controller():
    """
        Drugs controller class for table ``drugs`` in db

        ``cnx`` is the connection object from ``mysql-connector`` needed to send sql commands to the database
    """ 
    def __init__(self, cnx): #Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor()
        
        self.cnx=cnx
        self.aff_col=["ID Médicament", "Nom", "Description", "Date de péremption", "Prix en €€€", "Concentration en mg", "Stock"]      #Pour affichage
        self.aff_col_concentration=["ID Concentration","Concentration en mg"]
        self.vue_drugs=Drugs_vue() #TODO: MODIFIE CA
        self.DAO_drugs=Drugs_DAO(self.cnx) #TODO: MODIFIE CA
        self.DAO_concentration=Concentration_DAO(self.cnx)
        
    def Menu(self):
        """Call client_vue to display menu then use its return to launch a chosen by user sequence
        """
        while(True):
            choix_utilisateur=self.vue_drugs.Menu()
            if choix_utilisateur=="1":
                self.Display_Rows()
            elif choix_utilisateur=="2":
                self.Update_Row()
            elif choix_utilisateur=="3":
                self.Delete_Row()
            elif choix_utilisateur=="4":
                self.Create_Row()
            elif choix_utilisateur=="5":
                break

    def Create_Row(self):
        """Launch a sequence to create a row in the table

        Returns:
            [None]: If all went well it will return None, however it will display an error
        """
        try:

            table_before=BeautifulTable(maxwidth=300)                   
            table_before.columns.header=self.aff_col
            table_concentration=BeautifulTable(maxwidth=300)
            table_concentration.columns.header=self.aff_col_concentration
            concentration_list=self.DAO_concentration.Select_Rows()
            for row in concentration_list:
                table_concentration.rows.append(row)
            confirmation=self.vue_drugs.getConfirmation(id,2)  
            if confirmation==True:        
                row=self.vue_drugs.getRow(self.aff_col, table_concentration)

                modele_drugs=Drugs_modele()
                modele_drugs.PK_drug_id=row[0]
                modele_drugs.name=row[1]
                modele_drugs.description=row[2]
                modele_drugs.peremption_date=row[3]
                modele_drugs.price=row[4]
                modele_drugs.FK_concentration_id=row[5]
                modele_drugs.stock=row[6]


                if row!=None:
                    creation_reussie=self.DAO_drugs.Insert_Row(modele_drugs)
                    if creation_reussie==True:
                        self.vue_drugs.Display_BackToMenu()
                        return None
            self.vue_drugs.Display_Create_Error()

        except:
            return None

    def Display_Rows(self):   
        """Launch a sequence to display the table to the user
        """
        try:
            cursor=self.DAO_drugs.Select_Rows()
            table=BeautifulTable(maxwidth=300) #Préparation de l'affichage des lignes de façon organisée

            #On exécute la query et on y place tous ses éléments dans un module qui va gérer l'affichage
            table.columns.header=self.aff_col
                    
            for row in cursor:
                table.rows.append(row)  

            #Affichage de la table
            self.vue_drugs.Display_Rows(table)
        except:
            self.vue_drugs.Display_Select_Error()    
        finally:
            cursor.close()

    def Delete_Row(self):
        """Launch a sequence to delete a row chosen by the user
        """
        try:
            id=self.vue_drugs.Row_getId()
            confirmation=self.vue_drugs.getConfirmation(id,1)
            if  confirmation == True and id!=False:
                delete_confirmation=self.DAO_drugs.Delete_Row(id)
                if delete_confirmation==True:
                    self.vue_drugs.Display_BackToMenu()
                    return None
            self.vue_drugs.Display_Delete_Error()
        except:
            self.vue_drugs.Display_Delete_Error()

    def Update_Row(self):
        """Launch a sequence to update a row chosen by the user

        Returns:
            [None]: If all went well it will return None, however it will display an error
        """
        try:
            modele_drugs=Drugs_modele()
            table_before=BeautifulTable(maxwidth=300)                   
            table_before.columns.header=self.aff_col   
            table_concentration=BeautifulTable(maxwidth=300)
            table_concentration.columns.header=self.aff_col_concentration
            concentration_list=self.DAO_concentration.Select_Rows()
            for row in concentration_list:
                table_concentration.rows.append(row)
            modele_drugs.PK_drug_id=self.vue_drugs.Row_getId()
            if modele_drugs.PK_drug_id !=False:
                cursor=self.DAO_drugs.Select_Rows(modele_drugs.PK_drug_id)
                for row in cursor:
                    table_before.rows.append(row)  
                self.vue_drugs.Display_Rows(table_before)

                confirmation=self.vue_drugs.getConfirmation(modele_drugs.PK_drug_id,0)  
                if confirmation==True:  
                    row=self.vue_drugs.getRow(self.aff_col, table_concentration)
                    
                    modele_drugs.name=row[1]
                    modele_drugs.description=row[2]
                    modele_drugs.peremption_date=row[3]
                    modele_drugs.price=row[4]
                    modele_drugs.FK_concentration_id=row[5]
                    modele_drugs.stock=row[6]

                    if row!=None:
                        modification_reussie=self.DAO_drugs.Update_Row(modele_drugs)
                        if modification_reussie==True:
                            self.vue_drugs.Display_BackToMenu()
                            return None
                    self.vue_drugs.Display_Alter_Error()
                else:
                    self.vue_drugs.AucuneActionEntreprise()
        except:
            self.vue_drugs.Display_Alter_Error()
