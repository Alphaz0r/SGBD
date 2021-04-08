import mysql.connector
import interface_console
import client_controller
from beautifultable import BeautifulTable
from datetime import datetime


class Drugs_DAO():
    """
    Drugs DAO class for table ``drugs`` in db

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
            sql="SELECT drugs.PK_drug_id, drugs.name, drugs.description, CAST(drugs.peremption_date AS CHAR), drugs.price, concentration.concentration_mg, drugs.stock FROM drugs JOIN concentration ON concentration.PK_concentration_id=drugs.FK_concentration_id"
            if condition!=False:
                sql+=" WHERE PK_drug_id in("+condition+")" #Si il existe une condition on la place ici
            #On exécute la query
            cursor.execute(sql)               
            #On retourne le curseur pour le controller
            return cursor
        except:
            if cursor!=None:
                cursor.close()
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
            sql="DELETE FROM drugs" 
            sql+=" WHERE drugs.PK_drug_id="+id 
            try:
                cursor.execute(sql)
                self.cnx.commit()
                return True
            except:
                cursor.rollback()
                return False         
        except:
            return False
        finally:
            cursor.close()

    def Update_Row(self, modele_drugs):
        """Execute a simple UPDATE statement

        Args:
            modele_client ([modele_client obj]): We need an modele_client object to update a row in the table

        Returns:
            [Bool]: If the update query didn't work, it returns a boolean (False)
        """
        try:
            cursor=self.cnx.cursor()
            sql_update="UPDATE drugs SET "  #TODO: MODIFIE CA   
            sql_update+="name='"+modele_drugs.name+"', description='"+modele_drugs.description+"', peremption_date='"+modele_drugs.peremption_date+"', price='"+modele_drugs.price+"', FK_concentration_id='"+modele_drugs.FK_concentration_id+"', stock='"+modele_drugs.stock+"'"
            sql_update+=" WHERE PK_drug_id="+id #TODO: MODIFIE CA
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

    def Insert_Row(self, modele_drugs):  
        """Execute a simple INSERT statement

        Args:
            modele_client ([modele_client obj]): We need an modele_client object to insert a new row in the table

        Returns:
            [Bool]: If the update query didn't work, it returns a boolean (False)
        """                            
        try:
            cursor=self.cnx.cursor()   
            sql="INSERT INTO pharmacie.drugs (PK_drug_id, name, description, peremption_date, price, FK_concentration_id, stock) VALUES " 
            sql+="("+modele_drugs.PK_drug_id+", '"+modele_drugs.name+"', '"+modele_drugs.description+"', '"+modele_drugs.peremption_date+"', '"+modele_drugs.price+"', '"+modele_drugs.FK_concentration_id+"', '"+modele_drugs.stock+"');" 
            print(sql)
            cursor.execute(sql)
            self.cnx.commit()
            return True
        except:
            return False
        finally:
            cursor.close()

    def Select_Rows_facture(self):   
        """Execute a simple SELECT statement

        Returns:
            [MySQLCursor]: Returns a MySQLCursor object with every client id in the table
        """ 
        try:
            cursor=self.cnx.cursor()    #Initialisation du curseur qui va exécuter la requête SQL
            sql="SELECT drugs.PK_drug_id, drugs.name, drugs.description, drugs.peremption_date, drugs.price, concentration.concentration_mg, drugs.stock FROM drugs JOIN concentration ON concentration.PK_concentration_id=drugs.FK_concentration_id" 
            #On exécute la query
            cursor.execute(sql)               
            #On retourne le curseur pour le controller
            return cursor
        except:
            return None