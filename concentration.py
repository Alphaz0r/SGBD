import mysql.connector
import interface_console
import database
from beautifultable import BeautifulTable
from datetime import datetime

class Concentration():
    def __init__(self, cnx):
        self.table_name="concentration"
        self.aff_col=["ID Concentration", "Concentration en mg"]
        self.cnx=cnx
        self.Menu()


    def Menu(self):
        quit=False
        while(quit==False):
            interface_console.aff_menu_table(self.table_name)  #Affichage menu table
            choix=input("\nVotre choix : ") 
            if choix=="1":
                self.Afficher_Table()
            elif choix=="2":
                pass
            elif choix=="3":
                pass
            elif choix=="4":
                pass
            elif choix=="5":
                quit=True

    def Afficher_Table(self):   
        try:    
            cursor=self.cnx.cursor()    #Initialisation du curseur qui va exécuter la requête SQL
            sql="SELECT * FROM concentration"
            table=BeautifulTable(maxwidth=300)      #Préparation de l'affichage des lignes de façon organisée
            #On exécute la query et on y place tous ses éléments dans un module qui va gérer l'affichage
            cursor.execute(sql)
            print("\nAffichage de votre requête : ")
            table.columns.header=self.aff_col
            for row in cursor:
                table.rows.append(row)  
            print(table)

        except:
            print("\n+++Une erreur est survenue lors de l'affichage de valeurs dans la table+++")
        finally:
            cursor.close()  #Dans tous les cas on ferme le curseur