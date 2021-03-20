import mysql.connector
import interface_console
import facture_controller
from beautifultable import BeautifulTable
from datetime import datetime


class Facture_modele():
    def __init__(self, cnx): #Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor() 
        self.cnx=cnx


    def Select_Rows(self, condition=False):   
        try:
            cursor=self.cnx.cursor()    #Initialisation du curseur qui va exécuter la requête SQL
            sql="SELECT facture.PK_facture_id, facture.FK_client_id, clients.name, clients.first_name, clients.email, clients.rue, clients.house_number, clients.postcode, facture.total_price, CAST(facture.date_creation AS CHAR) FROM facture JOIN clients ON facture.FK_client_id=clients.PK_client_id"
            if condition!=False:
                sql+=" WHERE PK_facture_id in("+condition+")"
            #On exécute la query
            cursor.execute(sql)               
            #On retourne le curseur pour le controller
            return cursor
        except:
            return None

    def Delete_Row(self, id):
        try:    
            cursor=self.cnx.cursor()
            sql="DELETE FROM facture"
            sql+=" WHERE facture.PK_facture_id="+id
            cursor.execute(sql)
            self.cnx.commit()         
        except:
            return False
        finally:
            cursor.close()

    def Update_Row(self, row, id):
        try:
            cursor=self.cnx.cursor()
            sql_update="UPDATE facture SET "    
            sql_update+="date_creation='"+row[1]+"'"
            sql_update+=" WHERE PK_facture_id="+id
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
            sql="INSERT INTO pharmacie.facture (PK_facture_id, total_price, FK_client_id, date_creation) VALUES "
            sql+="("+row[0]+", "+row[3]+",'"+row[1]+"','"+row[2]+"')"
            cursor.execute(sql)
            self.cnx.commit()
            return True
        except:
            return False
        finally:
            cursor.close()
                

    