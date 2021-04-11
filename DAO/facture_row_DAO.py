import mysql.connector
from beautifultable import BeautifulTable
from datetime import datetime


class FactureRow_DAO():
    """
    Facture Row DAO class for table ``facture_row`` in db

    ``cnx`` is the connection object from ``mysql-connector`` needed to send sql commands to the database
    """
    def __init__(self, cnx): #Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor() 
        self.cnx=cnx


    def Select_Rows(self, id_facture="0", condition=False):   #OK
        """Execute a simple SELECT query

        Args:
            condition ([bool/str]): If condition is false, there's no WHERE statement. If condition is true, add a WHERE statement at the end of the query

        Returns:
            [MySQLCursor]: MySQLCursor object with the query content inside of it
        """
        try:
            cursor=self.cnx.cursor()    #Initialisation du curseur qui va exécuter la requête SQL
            sql="SELECT facture.PK_facture_id, facture_row.PK_fd_id, facture_row.FK_drug_id, drugs.name, facture_row.item_count, concentration.concentration_mg, clients.name, clients.first_name, clients.PK_client_id "
            sql+="FROM clients " 
            sql+="JOIN facture " 
            sql+="ON clients.PK_client_id=facture.FK_client_id " 
            sql+="JOIN facture_row " 
            sql+="ON facture.PK_facture_id=facture_row.FK_facture_id " 
            sql+="JOIN drugs " 
            sql+="ON facture_row.FK_drug_id=drugs.PK_drug_id " 
            sql+="JOIN concentration " 
            sql+="ON drugs.FK_concentration_id=concentration.PK_concentration_id WHERE "
            sql+="PK_facture_id in ("+id_facture+")"
            if condition!=False:
                sql+=" and PK_fd_id in("+condition+")" #TODO: MODIFIE CA
            #On exécute la query
            cursor.execute(sql)               
            #On retourne le curseur pour le controller
            return cursor
        except:
            return None

    def Delete_Row(self, id_row, id_facture):
        """Execute a simple DELETE statement

        Args:
            id ([String]): We need an id given by the user to delete the desired query.

        Returns:
            [Bool]: If the delete query didn't work, it returns a boolean (False)
        """
        try:    
            cursor=self.cnx.cursor()
            sql="DELETE FROM facture_row"
            sql+=" WHERE facture_row.PK_fd_id=("+id_row+") and FK_facture_id in ("+id_facture+")"
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

    def Update_Row(self, modele_facture_row, id_facture):
        """Execute a simple UPDATE statement

        Args:
            modele_facture_row ([modele_facture_row obj]): We need an modele_facture_row object to update a row in the table

        Returns:
            [Bool]: If the update query didn't work, it returns a boolean (False)
        """
        try:
            cursor=self.cnx.cursor()
            sql_update="UPDATE facture_row SET "    
            sql_update+="item_count='"+modele_facture_row.item_count+"', FK_drug_id='"+modele_facture_row.FK_drug_id+"'"
            sql_update+=" WHERE facture_row.PK_fd_id=("+modele_facture_row.PK_fd_id+") and FK_facture_id in ("+id_facture+")"
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

    def Insert_Row(self, modele_facture_row): 
        """Execute a simple INSERT statement

        Args:
            modele_facture_row ([modele_facture_row obj]): We need an modele_facture_row object to insert a new row in the table

        Returns:
            [Bool]: If the update query didn't work, it returns a boolean (False)
        """                         
        try:
            cursor=self.cnx.cursor()    
            sql="INSERT INTO pharmacie.facture_row (item_count, FK_drug_id,  FK_facture_id) VALUES "
            sql+="("+modele_facture_row.item_count+",'"+modele_facture_row.FK_drug_id+"','"+modele_facture_row.FK_facture_id+"')"
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
                

    