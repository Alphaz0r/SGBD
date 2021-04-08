import mysql.connector
import sys
sys.path.append("..\\model\\")
sys.path.append("..\\view\\")
sys.path.append("..\\DAO\\")
from model.users_model import *
from view.users_vue import *
from DAO.users_DAO import *
from beautifultable import BeautifulTable
from datetime import datetime
import hashlib, binascii, os


class Users_controller():
    """
    Users controller class for table ``users`` in db

    ``cnx`` is the connection object from ``mysql-connector`` needed to send sql commands to the database
    """
    def __init__(self, cnx): #Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor() 
        self.cnx=cnx
        self.aff_col= ["ID Utilisateur","Nom","Pseudonyme","Password"]
        self.vue_users=Users_vue() #Création de la vue
        self.DAO_users=Users_DAO(self.cnx) #Création du modèle
        


    def Menu(self):
        """
        Main menu
        """
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
        """
        Launch create row sequence
        """
        try:
            table_before=BeautifulTable(maxwidth=300)                   
            table_before.columns.header=self.aff_col
            confirmation=self.vue_users.getConfirmation(id,2)  
            if confirmation==True:        
                row=self.vue_users.getRow(self.aff_col)
                row[3]=self.hash_password(row[3])

                modele_user=Users_modele()
                modele_user.PK_user_id=row[0]
                modele_user.name=row[1]
                modele_user.pseudonyme=row[2]
                modele_user.password=row[3]

                if row!=None:
                    creation_reussie=self.DAO_users.Insert_Row(modele_user)
                    if creation_reussie==True:
                        self.vue_users.Display_BackToMenu()
                        return None
                self.vue_users.Display_Alter_Error()
            else :
                self.vue_users.AucuneActionEntreprise()

        except:
            self.vue_users.Display_Create_Error()

    def Display_Rows(self):  
        """
        launch display row sequence
        """ 
        try:
            cursor=self.DAO_users.Select_Rows()
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
        """
        launch delete row sequence 
        """
        try:
            modele_user=Users_modele()
            modele_user.PK_user_id=self.vue_users.Row_getId()
            confirmation=self.vue_users.getConfirmation(modele_user.PK_user_id,1)
            if  confirmation == True and modele_user.PK_user_id!=False:
                self.DAO_users.Delete_Row(modele_user.PK_user_id)
                self.vue_users.Display_BackToMenu()
            else:
                self.vue_users.Display_Delete_Error()
        except:
            self.vue_users.Display_Delete_Error()

    def Update_Row(self):
        """
        launch update row sequence
        """
        try:
            modele_user=Users_modele()
            table_before=BeautifulTable(maxwidth=300)                   
            table_before.columns.header=self.aff_col   

            modele_user.PK_user_id=self.vue_users.Row_getId()
            if modele_user.PK_user_id !=False:
                cursor=self.DAO_users.Select_Rows(modele_user.PK_user_id)
                for row in cursor:
                    table_before.rows.append(row)  
                self.vue_users.Display_Rows(table_before)

                confirmation=self.vue_users.getConfirmation(modele_user.PK_user_id,0)  
                if confirmation==True:  
                    row=self.vue_users.getRow(self.aff_col)
                    row[3]=self.hash_password(row[3])           #hash du mdp
                    
                    modele_user=Users_modele()
                    modele_user.name=row[1]
                    modele_user.pseudonyme=row[2]
                    modele_user.password=row[3]

                    if row!=None:
                        modification_reussie=self.DAO_users.Update_Row(modele_user)
                        if modification_reussie==True:
                            self.vue_users.Display_BackToMenu()
                            return None
                    self.vue_users.Display_Alter_Error()
                else:
                    self.vue_users.AucuneActionEntreprise()
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


    def Get_and_Check_Creds(self):
        """
        Launch sequence to get password and hash it
        """
        try:
            liste=self.vue_users.getUser_Pass()
            liste[3]=self.hash_password(liste[3])       #Hashage du mdp
            confirmation=self.vue_users.getConfirmation(id,2)  
            if confirmation==True:
                creation_reussie=self.DAO_users.Insert_Row(liste)
                if creation_reussie==True:
                    self.vue_users.Display_BackToMenu()
                    return None
            self.vue_users.Display_Create_Error()
        except:
            self.vue_users.Display_Create_Error()

    def Check_User_Passw(self, user, passw):
        """
        Check password given by user on login form
        """
        try:
            cursor=self.DAO_users.Select_Rows()
            liste=[]
            for row in cursor:
                for element in row:
                    liste.append(element)
                check_pass=self.verify_password(liste[3], passw)
                if liste[2]==user and check_pass==True :
                    return True
                liste=[]
            return False
        except:
            print("ERROR")
            if cursor!=None:cursor.close()


       