import mysql.connector
import interface_console
import database
import client_controller
from client_vue import *
from beautifultable import BeautifulTable
from datetime import datetime



class Client_vue():
    def __init__(self): #Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor() 
        pass
    def Menu(self):
        quit=False
        while(quit==False):
            interface_console.aff_menu_table("clients")  #Affichage menu table
            choix=input("\nVotre choix : ") 
            if choix=="1" or choix=="2" or choix=="3" or choix=="4":
                return choix
            elif choix=="5":
                quit=True

    def Display_Rows(self, table):
        try:
            if table==None:
                vue_client.Display_Error("CLIENT_MODEL")
            else:
                print("### Affichage de votre requête : ###\n")
                print(table)
        except:
            self.Display_Error("CLIENT_VIEW")

    def Display_Error(self, where):
        print("\+\+\+ Une erreur est survenue dans l'affichage des clients("+where+") \+\+\+")





