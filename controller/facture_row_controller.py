import mysql.connector
import sys
sys.path.append("..\\model\\")
sys.path.append("..\\view\\")
sys.path.append("..\\DAO\\")
from model.facture_row_model import *
from view.facture_row_vue import *
from DAO.facture_row_DAO import *
from DAO.drugs_DAO import *
from beautifultable import BeautifulTable
from datetime import datetime


class FactureRow_controller():
    """
    FactureRow class for table ``facture_row`` in db
    """
    def __init__(self, cnx, id_facture): #Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor() 
        self.cnx=cnx
        self.id_facture=id_facture
        self.aff_col= ["ID facture", "Ligne facture", "ID Médicament", "Nom médicament", "Nombre", "Concentration en mg", "Nom client", "Prénom client", "ID Client"] #Colonnes d'affichage pour BeautifulTables
        self.aff_col_drugs=["ID Médicament", "Nom", "Description", "Date de péremption", "Prix en €€€", "Concentration en mg", "Stock"]
        self.table_drugs=self.Get_Row_Drugs()
        self.vue_factureRow=FactureRow_vue(self.id_facture) #Création de la vue

        
    def Menu(self):
        """
        Main menu
        """
        while(True):
            choix_utilisateur=self.vue_factureRow.Menu()
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
            DAO_factureRow=FactureRow_DAO(self.cnx)
            table_before=BeautifulTable(maxwidth=300)                   
            table_before.columns.header=self.aff_col
        
            cursor=DAO_factureRow.Select_Rows(self.id_facture)
            for row in cursor:
                table_before.rows.append(row)  
            self.vue_factureRow.Display_Rows(table_before)
            confirmation=self.vue_factureRow.getConfirmation(id,2)  
            if confirmation==True:        
                row=self.vue_factureRow.getRow(self.aff_col, self.table_drugs)
                
                modele_facture_row.PK_fd_id=self.id_facture
                modele_facture_row=Facture_row_modele()
                modele_facture_row.item_count=row[0]
                modele_facture_row.FK_drug_id=row[1]
                modele_facture_row.FK_drug_id=[2]

                if row!=None:
                    creation_reussie=DAO_factureRow.Insert_Row()
                    if creation_reussie==True:
                        self.vue_factureRow.Display_BackToMenu()
                        return None
                self.vue_factureRow.Display_Create_Error()
            else:
                self.vue_factureRow.AucuneActionEntreprise()
        except:
            self.vue_factureRow.Display_Create_Error()

    def Display_Rows(self):   #OK
        """
        launch display row sequence
        """
        try:
            DAO_factureRow=FactureRow_DAO(self.cnx)
            cursor=DAO_factureRow.Select_Rows(self.id_facture)
            table=BeautifulTable(maxwidth=300) #Préparation de l'affichage des lignes de façon organisée

            #On exécute la query et on y place tous ses éléments dans un module qui va gérer l'affichage
            table.columns.header=self.aff_col
                    
            for row in cursor:
                table.rows.append(row)  
                
            #Affichage de la table
            self.vue_factureRow.Display_Rows(table)
            self.Menu()
        except:
            return None    
        finally:
            cursor.close()

    def Delete_Row(self):
        """
        launch delete row sequence 
        """
        try:
            DAO_factureRow=FactureRow_DAO(self.cnx)
            id=self.vue_factureRow.Row_getId()
            confirmation=self.vue_factureRow.getConfirmation(id,1)
            if  confirmation == True and id!=False:
                DAO_factureRow.Delete_Row(id, self.id_facture)
                self.vue_factureRow.Display_BackToMenu()
            else:
                self.vue_factureRow.AucuneActionEntreprise()
        except:
            self.vue_factureRow.Display_Delete_Error()

    def Update_Row(self):
        """
        launch update row sequence
        """ 
        try:
            modele_facture_row=Facture_row_modele()
            DAO_factureRow=FactureRow_DAO(self.cnx)
            table_before=BeautifulTable(maxwidth=300)                   
            table_before.columns.header=self.aff_col   
            modele_facture_row.PK_fd_id=self.vue_factureRow.Row_getId()
            if id !=False:
                cursor=DAO_factureRow.Select_Rows(self.id_facture,id)
                for row in cursor:
                    table_before.rows.append(row)  
                self.vue_factureRow.Display_Rows(table_before)

                confirmation=self.vue_factureRow.getConfirmation(modele_facture_row.PK_fd_id,0)  
                if confirmation==True:  
                    row=self.vue_factureRow.getRow(self.aff_col, self.table_drugs)
                    if row!=None:
                        modification_reussie=DAO_factureRow.Update_Row(modele_facture_row, self.id_facture)
                        if modification_reussie==True:
                            self.vue_factureRow.Display_BackToMenu()
                            return None
                    self.vue_factureRow.Display_Alter_Error()
                else :
                    self.vue_factureRow.AucuneActionEntreprise()
        except:
            self.vue_factureRow.Display_Alter_Error()

    def Get_Row_Drugs(self):
        """
        launch sequence to display the ``drugs`` table
        """ 
        try:
            DAO_drugs=Drugs_DAO(self.cnx)
            table_drugs=BeautifulTable(maxwidth=300)
            table_drugs.columns.header=self.aff_col_drugs
            drugs_list=DAO_drugs.Select_Rows_facture()
            for row in drugs_list:
                table_drugs.rows.append(row)
            return table_drugs
        except:
            return None
        finally:
            if drugs_list!=None:
                drugs_list.close()


    def getFactureRowId(self, id):
        """
        launch sequence to get the facture row id
        """ 
        try:
            cursor=self.DAO_factureRow.Select_factureRowId(id)
            if cursor==None:
                print("Erreur")
            else:
                return cursor
        except:
            self.vue_factureRow.Display_Select_Error()
        finally:
            cursor.close()

           


       