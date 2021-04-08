import mysql.connector
import interface_console
import facture_controller
from beautifultable import BeautifulTable
from datetime import datetime


class Facture_DAO():
    """
    Facture DAO class for table ``facture`` in db

    ``cnx`` is the connection object from ``mysql-connector`` needed to send sql commands to the database
    """ 
    def __init__(self, cnx): #Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor() 
        self.cnx=cnx


    def Select_Rows(self, condition=False):   
        """Execute a simple SELECT query

        Args:
            condition ([bool/str]): If condition is false, there's no WHERE statement. If condition is true, add a WHERE statement at the end of the query

        Returns:
            [MySQLCursor]: MySQLCursor object with the SELECT content inside of it
        """
        try:
            cursor=self.cnx.cursor()    #Initialisation du curseur qui va exécuter la requête SQL
            sql="SELECT facture.PK_facture_id, facture.FK_client_id, clients.name, clients.first_name, clients.email, clients.rue, clients.house_number, clients.postcode, (SELECT SUM(drugs.price*facture_row.item_count) FROM drugs, facture_row WHERE facture_row.FK_drug_id=drugs.PK_drug_id) as prix_facture, CAST(facture.date_creation AS CHAR) FROM facture JOIN clients ON facture.FK_client_id=clients.PK_client_id"
            if condition!=False:
                sql+=" WHERE PK_facture_id in("+condition+")"
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
            sql="DELETE FROM facture"
            sql+=" WHERE facture.PK_facture_id="+id
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

    def Update_Row(self, modele_facture):
        """Execute a simple UPDATE statement

        Args:
            modele_facture ([modele_facture obj]): We need an modele_facture object to update a row in the table

        Returns:
            [Bool]: If the update query didn't work, it returns a boolean (False)
        """
        try:
            cursor=self.cnx.cursor()
            sql_update="UPDATE facture SET "    
            sql_update+="date_creation='"+modele_facture.date_creation+"'"
            sql_update+=" WHERE PK_facture_id="+modele_facture.PK_facture_id
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

    def Insert_Row(self, modele_facture):    
        """Execute a simple INSERT statement

        Args:
            modele_facture ([modele_facture obj]): We need an modele_facture object to insert a new row in the table

        Returns:
            [Bool]: If the update query didn't work, it returns a boolean (False)
        """                         
        try:
            cursor=self.cnx.cursor()    
            sql="INSERT INTO pharmacie.facture (FK_client_id, date_creation) VALUES "
            sql+="("+modele_facture.FK_client_id+", \""+modele_facture.date_creation+"\")"
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
                

    