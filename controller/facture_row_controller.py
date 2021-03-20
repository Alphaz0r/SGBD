import mysql.connector
import sys
sys.path.append("..\\model\\")
sys.path.append("..\\view\\")
from view.facture_row_vue import *
from model.facture_row_modele import *
from model.drugs_modele import *
from beautifultable import BeautifulTable
from datetime import datetime


class FactureRow_controller():
    def __init__(self, cnx, id_facture): #Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor() 
        self.cnx=cnx
        self.id_facture=id_facture
        self.aff_col= ["ID facture", "Ligne facture", "ID Médicament", "Nom médicament", "Nombre", "Concentration en mg", "Nom client", "Prénom client", "ID Client"] #Colonnes d'affichage pour BeautifulTables
        self.aff_col_drugs=["ID Médicament", "Nom", "Description", "Date de péremption", "Prix en €€€", "Concentration en mg", "Stock"]
        self.table_drugs=self.Get_Row_Drugs()
        self.vue_factureRow=FactureRow_vue(self.id_facture) #Création de la vue

        
    def Menu(self):
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
        try:
            modele_factureRow=FactureRow_modele(self.cnx)
            table_before=BeautifulTable(maxwidth=300)                   
            table_before.columns.header=self.aff_col
        
            cursor=modele_factureRow.Select_Rows(self.id_facture)
            for row in cursor:
                table_before.rows.append(row)  
            self.vue_factureRow.Display_Rows(table_before)
            confirmation=self.vue_factureRow.getConfirmation(id,2)  
            if confirmation==True:        
                row=self.vue_factureRow.getRow(self.aff_col, self.table_drugs)
                row.append(self.id_facture)
                if row!=None:
                    creation_reussie=modele_factureRow.Insert_Row(row)
                    if creation_reussie==True:
                        self.vue_factureRow.Display_BackToMenu()
                        return None
            self.vue_factureRow.Display_Alter_Error()
        except:
            return None

    def Display_Rows(self):   #OK
        try:
            modele_factureRow=FactureRow_modele(self.cnx)
            cursor=modele_factureRow.Select_Rows(self.id_facture)
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
        try:
            modele_factureRow=FactureRow_modele(self.cnx)
            id=self.vue_factureRow.Row_getId()
            confirmation=self.vue_factureRow.getConfirmation(id,1)
            if  confirmation == True and id!=False:
                modele_factureRow.Delete_Row(id, self.id_facture)
                self.vue_factureRow.Display_BackToMenu()
            else:
                self.vue_factureRow.Display_Delete_Error()
        except:
            self.vue_factureRow.Display_Delete_Error()

    def Update_Row(self):
        try:
            modele_factureRow=FactureRow_modele(self.cnx)
            table_before=BeautifulTable(maxwidth=300)                   
            table_before.columns.header=self.aff_col   
            id=self.vue_factureRow.Row_getId()
            if id !=False:
                cursor=modele_factureRow.Select_Rows(self.id_facture,id)
                for row in cursor:
                    table_before.rows.append(row)  
                self.vue_factureRow.Display_Rows(table_before)

                confirmation=self.vue_factureRow.getConfirmation(id,0)  
                if confirmation==True:  
                    row=self.vue_factureRow.getRow(self.aff_col, self.table_drugs)
                    if row!=None:
                        modification_reussie=modele_factureRow.Update_Row(row,id, self.id_facture)
                        if modification_reussie==True:
                            self.vue_factureRow.Display_BackToMenu()
                            return None
                self.vue_factureRow.Display_Alter_Error()

        except:
            return None

    def Get_Row_Drugs(self):
        try:
            modele_drugs=Drugs_modele(self.cnx)
            table_drugs=BeautifulTable(maxwidth=300)
            table_drugs.columns.header=self.aff_col_drugs
            drugs_list=modele_drugs.Select_Rows_facture()
            for row in drugs_list:
                table_drugs.rows.append(row)
            return table_drugs
        except:
            return None
        finally:
            if drugs_list!=None:
                drugs_list.close()


    def getFactureRowId(self, id):
        try:
            cursor=self.modele_factureRow.Select_factureRowId(id)
            if cursor==None:
                print("Erreur")
            else:
                return cursor
        except:
            self.vue_factureRow.Display_Select_Error()
        finally:
            cursor.close()

           


       