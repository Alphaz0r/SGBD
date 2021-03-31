import mysql.connector
import interface_console
import client_controller
from beautifultable import BeautifulTable
from datetime import datetime


class Concentration_DAO():
    def __init__(self, cnx): #Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor() 
        self.cnx=cnx


    def Select_Rows(self, condition=False):   
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

    def Update_Row(self, concentration_DAO):
        try:
            cursor=self.cnx.cursor()
            sql_update="UPDATE concentration SET "     
            sql_update+="concentration_mg='"+concentration_DAO.concentration_mg+"'" 
            sql_update+=" WHERE PK_concentration_id="+concentration_DAO.PK_concentration_id 
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

    def Insert_Row(self, concentration_DAO):                           
        try:
            cursor=self.cnx.cursor()   
            sql="INSERT INTO pharmacie.concentration (PK_concentration_id, concentration_mg) VALUES " 
            sql+="('"+concentration_DAO.PK_concentration_id+"', '"+concentration_DAO.concentration_mg+"');" 
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
                

    