import mysql.connector
import interface_console
import sys
sys.path.append("..\\model\\")
sys.path.append("..\\view\\")
from view.drugs_vue import *
from model.drugs_modele import *
from model.concentration_modele import *
from beautifultable import BeautifulTable
from datetime import datetime



class Drugs_controller():
    def __init__(self, cnx): #Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor() 
        self.cnx=cnx
        self.aff_col=["ID Médicament", "Nom", "Description", "Date de péremption", "Prix en €€€", "Concentration en mg", "Stock"]      #Pour affichage
        self.aff_col_concentration=["ID Concentration","Concentration en mg"]
        self.vue_drugs=Drugs_vue() #TODO: MODIFIE CA
        self.modele_drugs=Drugs_modele(self.cnx) #TODO: MODIFIE CA
        self.modele_concentration=Concentration_modele(self.cnx)
        
    def Menu(self):
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
        try:
            table_before=BeautifulTable(maxwidth=300)                   
            table_before.columns.header=self.aff_col
            table_concentration=BeautifulTable(maxwidth=300)
            table_concentration.columns.header=self.aff_col_concentration
            concentration_list=self.modele_concentration.Select_Rows()
            for row in concentration_list:
                table_concentration.rows.append(row)
            confirmation=self.vue_drugs.getConfirmation(id,2)  
            if confirmation==True:        
                row=self.vue_drugs.getRow(self.aff_col, table_concentration)
                if row!=None:
                    creation_reussie=self.modele_drugs.Insert_Row(row)
                    if creation_reussie==True:
                        self.vue_drugs.Display_BackToMenu()
                        return None
            self.vue_drugs.Display_Create_Error()

        except:
            return None

    def Display_Rows(self):   
        try:
            cursor=self.modele_drugs.Select_Rows()
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
        try:
            id=self.vue_drugs.Row_getId()
            confirmation=self.vue_drugs.getConfirmation(id,1)
            if  confirmation == True and id!=False:
                delete_confirmation=self.modele_drugs.Delete_Row(id)
                if delete_confirmation==True:
                    self.vue_drugs.Display_BackToMenu()
                    return None
            self.vue_drugs.Display_Delete_Error()
        except:
            self.vue_drugs.Display_Delete_Error()

    def Update_Row(self):
        try:
            table_before=BeautifulTable(maxwidth=300)                   
            table_before.columns.header=self.aff_col   
            table_concentration=BeautifulTable(maxwidth=300)
            table_concentration.columns.header=self.aff_col_concentration
            concentration_list=self.modele_concentration.Select_Rows()
            for row in concentration_list:
                table_concentration.rows.append(row)
            id=self.vue_drugs.Row_getId()
            if id !=False:
                cursor=self.modele_drugs.Select_Rows(id)
                for row in cursor:
                    table_before.rows.append(row)  
                self.vue_drugs.Display_Rows(table_before)

                confirmation=self.vue_drugs.getConfirmation(id,0)  
                if confirmation==True:  
                    row=self.vue_drugs.getRow(self.aff_col, table_concentration)
                    if row!=None:
                        modification_reussie=self.modele_drugs.Update_Row(row, id)
                        if modification_reussie==True:
                            self.vue_drugs.Display_BackToMenu()
                            return None
                    self.vue_drugs.Display_Alter_Error()
                else:
                    self.vue_drugs.AucuneActionEntreprise()
        except:
            self.vue_drugs.Display_Alter_Error()
