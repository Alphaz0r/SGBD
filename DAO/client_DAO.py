import mysql.connector
from beautifultable import BeautifulTable
from datetime import datetime


class Client_DAO():
    """
    Client DAO class for table ``client`` in db

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
            sql="SELECT PK_client_id, name, first_name, CAST(birth_date AS CHAR),age, rue, house_number, postcode, email, phone_number"
            sql+=" FROM clients"
            if condition!=False:
                sql+=" WHERE PK_client_id in("+condition+")"
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
            sql="DELETE FROM clients"
            sql+=" WHERE clients.PK_client_id="+id
            try:
                cursor.execute(sql)
                self.cnx.commit()
            except:
                self.cnx.rollback()
                return False        
        except:
            return False
        finally:
            cursor.close()

    def Update_Row(self, modele_client):
        """Execute a simple UPDATE statement

        Args:
            modele_client ([modele_client obj]): We need an modele_client object to update a row in the table

        Returns:
            [Bool]: If the update query didn't work, it returns a boolean (False)
        """
        try:
            cursor=self.cnx.cursor()
            sql_update="UPDATE clients SET "    
            sql_update+="name='"+modele_client.name+"', first_name='"+modele_client.first_name+"', birth_date='"+modele_client.birth_date+"', age='"+modele_client.age+"', rue='"+modele_client.rue+"', house_number='"+modele_client.house_number+"', postcode='"+modele_client.postcode+"', email='"+modele_client.email+"', phone_number='"+modele_client.phone_number+"'"
            sql_update+=" WHERE PK_client_id="+modele_client.PK_client_id
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

    def Insert_Row(self, modele_client):       
        """Execute a simple INSERT statement

        Args:
            modele_client ([modele_client obj]): We need an modele_client object to insert a new row in the table

        Returns:
            [Bool]: If the update query didn't work, it returns a boolean (False)
        """                    
        try:
            cursor=self.cnx.cursor()    
            sql="INSERT INTO pharmacie.clients (name, first_name, birth_date, age, rue, house_number, postcode, email, phone_number) VALUES "
            sql+="('"+modele_client.name+"','"+modele_client.first_name+"','"+modele_client.birth_date+"','"+modele_client.age+"','"+modele_client.rue+"','"+modele_client.house_number+"','"+modele_client.postcode+"','"+modele_client.email+"','"+modele_client.phone_number+"');"
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

    
    def Select_clientId(self):   
        """Execute a simple SELECT statement

        Returns:
            [MySQLCursor]: Returns a MySQLCursor object with every client id in the table
        """     
        try:
            cursor=self.cnx.cursor()    #Initialisation du curseur qui va exécuter la requête SQL
            sql="SELECT PK_client_id"
            sql+=" FROM clients"
            #On exécute la query
            cursor.execute(sql)               
            #On retourne le curseur pour le controller
            return cursor
        except:
            return None
            

    