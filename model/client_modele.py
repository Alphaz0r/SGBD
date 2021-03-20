import mysql.connector
from beautifultable import BeautifulTable
from datetime import datetime


class Client_modele():
    def __init__(self, cnx): #Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor() 
        self.cnx=cnx


    def Select_Rows(self, condition=False):   
        try:
            cursor=self.cnx.cursor()    #Initialisation du curseur qui va exécuter la requête SQL
            sql="SELECT PK_client_id, name, first_name, CAST(birth_date AS CHAR),age, rue, house_number, postcode, email, phone_number"
            sql+=" FROM clients"
            if condition!=False:
                sql+=" WHERE PK_client_id in("+condition+")"
            #On exécute la query
            cursor.execute(sql)               
            #On retourne le curseur pour le controller
            print(cursor)
            return cursor
        except:
            return None

    def Delete_Row(self, id):
        try:    
            cursor=self.cnx.cursor()
            sql="DELETE FROM clients"
            sql+=" WHERE clients.PK_client_id="+id
            cursor.execute(sql)
            self.cnx.commit()         
        except:
            return False
        finally:
            cursor.close()

    def Update_Row(self, row, id):
        try:
            cursor=self.cnx.cursor()
            sql_update="UPDATE clients SET "    
            sql_update+="name='"+row[1]+"', first_name='"+row[2]+"', birth_date='"+row[3]+"', age='"+row[4]+"', rue='"+row[5]+"', house_number='"+row[6]+"', postcode='"+row[7]+"', email='"+row[8]+"', phone_number='"+row[9]+"'"
            sql_update+=" WHERE PK_client_id="+id
            print(sql_update)
            cursor.execute(sql_update)
            self.cnx.commit()
            return True
        except:
            return False
        finally:
            cursor.close()

    def Insert_Row(self, row):                           
        try:
            cursor=self.cnx.cursor()    
            sql="INSERT INTO pharmacie.clients (PK_client_id, name, first_name, birth_date, age, rue, house_number, postcode, email, phone_number) VALUES "
            sql+="("+row[0]+", '"+row[1]+"','"+row[2]+"','"+row[3]+"',"+row[4]+",'"+row[5]+"','"+row[6]+"','"+row[7]+"','"+row[8]+"','"+row[9]+"');"
            cursor.execute(sql)
            self.cnx.commit()
            return True
        except:
            return False
        finally:
            cursor.close()

    
    def Select_clientId(self):   
        try:
            cursor=self.cnx.cursor()    #Initialisation du curseur qui va exécuter la requête SQL
            sql="SELECT PK_client_id"
            sql+=" FROM clients"
            #On exécute la query
            cursor.execute(sql)               
            #On retourne le curseur pour le controller
            print(cursor)
            return cursor
        except:
            return None
            

    