import mysql.connector
import interface_console
import client_controller
from beautifultable import BeautifulTable
from datetime import datetime


class Drugs_modele():
    def __init__(self, cnx): #Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor() 
        self.cnx=cnx


    def Select_Rows(self, condition=False):   
        try:
            cursor=self.cnx.cursor()    #Initialisation du curseur qui va exécuter la requête SQL
            sql="SELECT * FROM drugs" #TODO: MODIFIE CA
            if condition!=False:
                sql+=" WHERE PK_drug_id in("+condition+")" #TODO: MODIFIE CA
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
            sql="DELETE FROM drugs" 
            sql+=" WHERE drugs.PK_drug_id="+id #TODO: MODIFIE CA
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
            sql_update="UPDATE drugs SET "  #TODO: MODIFIE CA   
            sql_update+="name='"+new_info[1]+"', description='"+new_info[2]+"', peremption_date='"+new_info[3]+"', price='"+new_info[4]+"', FK_concentration_id='"+new_info[5]+"', stock='"+new_info[6]+"'"
            sql_update+=" WHERE PK_drug_id="+id #TODO: MODIFIE CA
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
            sql="INSERT INTO pharmacie.drugs (PK_drug_id, name, description, peremption_date, price, FK_concentration_id, stock) VALUES " #TODO: MODIFIE CA
            sql+="("+row[0]+", '"+row[1]+"', '"+row[2]+"', '"+row[3]+"', '"+row[4]+"', '"+row[5]+"', '"+row[6]+"');" #TODO: MODIFIE CA
            print(sql)
            cursor.execute(sql)
            self.cnx.commit()
            return True
        except:
            return False
        finally:
            cursor.close()

    
                

    def Select_Rows_facture(self):   
        try:
            cursor=self.cnx.cursor()    #Initialisation du curseur qui va exécuter la requête SQL
            sql="SELECT drugs.PK_drug_id, drugs.name, drugs.description, drugs.peremption_date, drugs.price, concentration.concentration_mg, drugs.stock FROM drugs JOIN concentration ON concentration.PK_concentration_id=drugs.FK_concentration_id" #TODO: MODIFIE CA
            #On exécute la query
            cursor.execute(sql)               
            #On retourne le curseur pour le controller
            print(cursor)
            return cursor
        except:
            return None