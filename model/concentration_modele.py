import mysql.connector
import interface_console
import client_controller
from beautifultable import BeautifulTable
from datetime import datetime


class Concentration_modele():
    def __init__(self, cnx): #Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor() 
        self.cnx=cnx


    def Select_Rows(self, condition=False):   
        try:
            cursor=self.cnx.cursor()    #Initialisation du curseur qui va exécuter la requête SQL
            sql="SELECT * FROM concentration" #TODO: MODIFIE CA
            if condition!=False:
                sql+=" WHERE PK_concentration_id in("+condition+")" #TODO: MODIFIE CA
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
            sql="DELETE FROM concentration" #TODO: MODIFIE CA
            sql+=" WHERE concentration.PK_concentration_id="+id #TODO: MODIFIE CA
            cursor.execute(sql)
            self.cnx.commit()
            return True         
        except:
            return False
        finally:
            cursor.close()

    def Update_Row(self, row, id):
        try:
            cursor=self.cnx.cursor()
            sql_update="UPDATE concentration SET "  #TODO: MODIFIE CA   
            sql_update+="concentration_mg='"+row[1]+"'" #TODO: MODIFIE CA
            sql_update+=" WHERE PK_concentration_id="+id #TODO: MODIFIE CA
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
            sql="INSERT INTO pharmacie.concentration (PK_concentration_id, concentration_mg) VALUES " #TODO: MODIFIE CA
            sql+="("+row[0]+", '"+row[1]+"');" #TODO: MODIFIE CA
            print(sql)
            cursor.execute(sql)
            self.cnx.commit()
            return True
        except:
            return False
        finally:
            cursor.close()
                

    