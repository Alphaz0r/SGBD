import mysql.connector
import interface_console
import client_controller
from beautifultable import BeautifulTable
from datetime import datetime


class Users_DAO():
    """
    Users DAO class for table ``users`` in db

    
    """
    
    def __init__(self, cnx): #Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor() 
        self.cnx=cnx


    def Select_Rows(self, condition=False): 
        """Execute a simple SELECT query

        Args:
            condition ([bool/str]): If condition is false, there's no WHERE statement. If condition is true, add a WHERE statement at the end of the query

        Returns:
            [MySQLCursor]: MySQLCursor object with the query content inside of it
        """  
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
        """Execute a simple DELETE statement

        Args:
            id ([String]): We need an id given by the user to delete the desired query.

        Returns:
            [Bool]: If the delete query didn't work, it returns a boolean (False)
        """
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

    def Update_Row(self, modele_user):
        """Execute a simple UPDATE statement

        Args:
            modele_facture_row ([modele_facture_row obj]): We need an modele_facture_row object to update a row in the table

        Returns:
            [Bool]: If the update query didn't work, it returns a boolean (False)
        """
        try:
            cursor=self.cnx.cursor()
            sql_update="UPDATE users SET "    
            sql_update+="name='"+modele_user.name+"', pseudonyme='"+modele_user.pseudonyme+"', password='"+modele_user.password+"'"
            sql_update+=" WHERE PK_user_id="+modele_user.PK_user_id
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

    def Insert_Row(self, modele_user): 
        """Execute a simple INSERT statement

        Args:
            modele_facture_row ([modele_facture_row obj]): We need an modele_facture_row object to insert a new row in the table

        Returns:
            [Bool]: If the update query didn't work, it returns a boolean (False)
        """                             
        try:
            cursor=self.cnx.cursor()    
            sql="INSERT INTO pharmacie.users (PK_user_id, name, pseudonyme, password) VALUES "
            sql+="("+modele_user.PK_user_id+", '"+modele_user.name+"','"+modele_user.pseudonyme+"','"+modele_user.password+"')"
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
                

    