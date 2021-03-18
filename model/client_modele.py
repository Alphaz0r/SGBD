import mysql.connector
import interface_console
import database
import client_controller
import sys
sys.path.append("..\\model\\")
sys.path.append("..\\view\\")
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
            print("+++ Erreur dans la suppression de données +++")
        finally:
            cursor.close()

    def Alter_Row(self):
        try:
            cursor=self.cnx.cursor()
            sql_update="UPDATE clients SET "    

        
            new_info=self.Build_Row()
            print(new_info)
            if new_info==None:
                return None
            else:           #["PK_client_id", "name", "first_name", "birth_date", "age", "rue", "house_number", "postcode", "email", "phone_number"]
                sql_update+="name='"+new_info[1]+"', first_name='"+new_info[2]+"', birth_date='"+new_info[3]+"', age='"+new_info[4]+"', rue='"+new_info[5]+"', house_number='"+new_info[6]+"', postcode='"+new_info[7]+"', email='"+new_info[8]+"', phone_number='"+new_info[9]+"'"
                sql_update+=" WHERE PK_client_id="+id
                print(sql_update)
                cursor.execute(sql_update)
                self.cnx.commit()
                return None

            """elif reponse=="N":
                print("Retour au menu...")
                return None
"""
        except:
            pass
                

    