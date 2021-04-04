import mysql.connector
import interface_console
import client_controller
from beautifultable import BeautifulTable
from datetime import datetime


class Users_DAO():
    def __init__(self, cnx): #Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor() 
        self.cnx=cnx


    def Select_Rows(self, condition=False):   
        try:
            cursor=self.cnx.cursor()    #Initialisation du curseur qui va exécuter la requête SQL
            sql="SELECT PK_user_id, name, pseudonyme, password"
            sql+=" FROM users"
            if condition!=False:
                sql+=" WHERE PK_user_id in("+condition+")"
            #On exécute la query
            cursor.execute(sql)               
            #On retourne le curseur pour le controller
            return cursor
        except:
            return None

    def Delete_Row(self, id):
        try:    
            cursor=self.cnx.cursor()
            sql="DELETE FROM users"
            sql+=" WHERE users.PK_user_id="+id
            try:
                cursor.execute(sql)
                self.cnx.commit()
                return True
            except:
                self.cnx.rollback()
                return False
        except:
            return False
        finally:
            cursor.close()

    def Update_Row(self, modele_users):
        try:
            cursor=self.cnx.cursor()
            sql_update="UPDATE users SET "    
            sql_update+="name='"+modele_users.name+"', pseudonyme='"+modele_users.pseudonyme+"', password='"+modele_users.password+"'"
            sql_update+=" WHERE PK_user_id="+modele_users.PK_user_id
            try:    
                cursor.execute(sql_update)
                self.cnx.commit()
                return True
            except:
                self.cnx.rollback()
                return False
        except:
            return False
        finally:
            cursor.close()

    def Insert_Row(self, modele_users):                           
        try:
            cursor=self.cnx.cursor()    
            sql="INSERT INTO pharmacie.users (PK_user_id, name, pseudonyme, password) VALUES "
            sql+="("+modele_users.PK_user_id+", '"+modele_users.name+"','"+modele_users.pseudonyme+"','"+modele_users.password+"')"
            try:    
                cursor.execute(sql)
                self.cnx.commit()
                return True
            except:
                self.cnx.rollback()
                return False
        except:
            return False
        finally:
            cursor.close()
                

    