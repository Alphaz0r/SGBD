import mysql.connector
import interface_console
import database
import sys
sys.path.append("..\\model\\")
sys.path.append("..\\view\\")
from view.users_vue import *
from model.users_modele import *
from beautifultable import BeautifulTable
from datetime import datetime
import hashlib, binascii, os


class Users_controller():
    def __init__(self, cnx): #Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor() 
        self.cnx=cnx
        self.aff_col= ["ID Utilisateur","Nom","Prénom","Password"]
        self.vue_users=Users_vue() #Création de la vue
        self.modele_users=Users_modele(self.cnx) #Création du modèle
        while(True):
            choix_utilisateur=self.vue_users.Menu()
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
            confirmation=self.vue_users.getConfirmation(id,2)  
            if confirmation==True:        
                row=self.vue_users.getRow(self.aff_col)
                row[3]=self.hash_password(row[3])
                print(row[3])
                if row!=None:
                    creation_reussie=self.modele_users.Insert_Row(row)
                    if creation_reussie==True:
                        self.vue_users.Display_BackToMenu()
                        return None
            self.vue_users.Display_Alter_Error()

        except:
            self.vue_users.Display_Create_Error()

    def Display_Rows(self):   
        try:
            cursor=self.modele_users.Select_Rows()
            table=BeautifulTable(maxwidth=300) #Préparation de l'affichage des lignes de façon organisée

            #On exécute la query et on y place tous ses éléments dans un module qui va gérer l'affichage
            table.columns.header=self.aff_col
                    
            for row in cursor:
                table.rows.append(row)  
                
            #Affichage de la table
            self.vue_users.Display_Rows(table)
        except:
            self.vue_users.Display_Select_Error()    
        finally:
            cursor.close()

    def Delete_Row(self):
        try:
            id=self.vue_users.Row_getId()
            confirmation=self.vue_users.getConfirmation(id,1)
            if  confirmation == True and id!=False:
                self.modele_users.Delete_Row(id)
                self.vue_users.Display_BackToMenu()
            else:
                self.vue_users.Display_Delete_Error()
        except:
            self.vue_users.Display_Delete_Error()

    def Update_Row(self):
        try:
            table_before=BeautifulTable(maxwidth=300)                   
            table_before.columns.header=self.aff_col   

            id=self.vue_users.Row_getId()
            if id !=False:
                cursor=self.modele_users.Select_Rows(id)
                for row in cursor:
                    table_before.rows.append(row)  
                self.vue_users.Display_Rows(table_before)

                confirmation=self.vue_users.getConfirmation(id,0)  
                if confirmation==True:  
                    row=self.vue_users.getRow(self.aff_col)
                    row[3]=self.hash_password(row[3])           #hash du mdp
                    print(row[3])
                    if row!=None:
                        modification_reussie=self.modele_users.Update_Row(row, id)
                        if modification_reussie==True:
                            self.vue_users.Display_BackToMenu()
                            return None
            self.vue_users.Display_Alter_Error()
        except:
            self.vue_users.Display_Alter_Error()

    def hash_password(self, password):  #Trouvée sur internet
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                    salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    def verify_password(self, stored_password, provided_password): #Trouvée sur internet
        """Verify a stored password against one provided by user"""
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                    provided_password.encode('utf-8'), 
                                    salt.encode('ascii'), 
                                    100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password

       