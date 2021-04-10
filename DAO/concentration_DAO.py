import mysql.connector
import interface_console
import client_controller
from beautifultable import BeautifulTable
from datetime import datetime


class Concentration_DAO():
    """
    Concentration DAO class for table ``concentration`` in db

    ``cnx`` is the connection object from ``mysql-connector`` needed to send sql commands to the database
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
            sql="SELECT * FROM concentration" 
            if condition!=False:
                sql+=" WHERE PK_concentration_id in("+condition+")" 
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
            sql="DELETE FROM concentration" 
            sql+=" WHERE concentration.PK_concentration_id="+id 
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

    def Update_Row(self, concentration_modele):
        """Execute a simple UPDATE statement

        Args:
            concentration_modele ([concentration_modele obj]): We need an concentration_modele object to update a row in the table

        Returns:
            [Bool]: If the update query didn't work, it returns a boolean (False)
        """
        try:
            cursor=self.cnx.cursor()
            sql_update="UPDATE concentration SET "     
            sql_update+="concentration_mg='"+concentration_modele.concentration_mg+"'" 
            sql_update+=" WHERE PK_concentration_id="+concentration_modele.PK_concentration_id 
            try:
                cursor.execute(sql_update)
                self.cnx.commit()
            except:
                self.cnx.rollback()
                return False
            return True
        except:
            return False
        finally:
            cursor.close()

    def Insert_Row(self, concentration_modele):  
        """Execute a simple INSERT statement

        Args:
            concentration_modele ([concentration_modele obj]): We need an concentration_modele object to insert a new row in the table

        Returns:
            [Bool]: If the update query didn't work, it returns a boolean (False)
        """                              
        try:
            cursor=self.cnx.cursor()   
            sql="INSERT INTO pharmacie.concentration (PK_concentration_id, concentration_mg) VALUES " 
            sql+="('"+concentration_modele.PK_concentration_id+"', '"+concentration_modele.concentration_mg+"');" 
            try:
                cursor.execute(sql)
                self.cnx.commit()
                return True
            except:
                self.cnx.rollback()
        except:
            return False
        finally:
            cursor.close()
                

    