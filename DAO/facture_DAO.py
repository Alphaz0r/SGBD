import mysql.connector
import interface_console
import facture_controller
from beautifultable import BeautifulTable
from datetime import datetime


class Facture_DAO():
    def __init__(self, cnx): #Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor() 
        self.cnx=cnx


    def Select_Rows(self, condition=False):   
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
                

    