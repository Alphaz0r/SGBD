import mysql.connector
import interface_console
import database
import client_modele, client_vue

from beautifultable import BeautifulTable
from datetime import datetime


class Client_controller():
    def __init__(self, cnx): #Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor() 
        self.cnx=cnx
        self.aff_col= ["ID", "Nom", "Prénom", "Date de naissance", "Age", "Rue", "Numéro de maison", "Code postal", "Email", "Numéro de téléphone"] #Colonnes d'affichage pour BeautifulTables
        self.vue_client=client_vue.Client_vue()
        choix_utilisateur=self.vue_client.Menu()

        if choix_utilisateur=="1":
            self.Display_Rows()

    def Display_Rows(self):   
        try:
            modele_client=client_modele.Client_modele(self.cnx)
            cursor=modele_client.Display_Rows()
            table=BeautifulTable(maxwidth=300)      #Préparation de l'affichage des lignes de façon organisée

            #On exécute la query et on y place tous ses éléments dans un module qui va gérer l'affichage
            table.columns.header=self.aff_col
                    
            for row in cursor:
                table.rows.append(row)  
                
            #Affichage de la table
            self.vue_client.Display_Rows(table)
        except:
            self.vue_client.Display_Error("CLIENT_CONTROLLER")    
        finally:
            cursor.close()        


       