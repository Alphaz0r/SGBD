import mysql.connector
import interface_console
import database
import client_controller
import sys
sys.path.append("..\\model\\")
sys.path.append("..\\view\\")
from beautifultable import BeautifulTable
from datetime import datetime
from view.vue_mere import *

class Facture_vue(Vue_mere):
    def __init__(self):  # Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor()
        self.nomTable="facture"

    def Menu(self):
        try:    
            quit = False
            while(quit == False):
                interface_console.aff_menu_facture()  # Affichage menu table
                choix = input("\nVotre choix : ")
                if choix == "1" or choix == "2" or choix == "3" or choix == "4"or choix=="5" or choix=="6": return choix
        except:
            print("+++ Erreur dans le menu "+self.nomTable+" +++")

    def getConfirmation(self, id, position):
        crud=["modifiée", "supprimée","créée"]
        try:    
            while(True):
                if crud[position]=="modifiée" or crud[position]=="supprimée":
                    reponse = input("La ligne avec l'ID "+id+" va être "+crud[position]+". Confirmer ? Y/N\nVotre réponse : ")
                    if position==1:
                        print("/!\ Cela inclus toutes les informations de la factures. /!\\")
                        reponse=input("Confirmer quand même ? Y/N\nVotre réponse")
                else:
                    reponse = input("Lancement du processus de création. Confirmer ? Y/N\nVotre réponse : ")
                if reponse == "Y":
                    return True
                elif reponse == "N":
                    return False
                else:
                    print("### Veuillez choisir une des réponses proposées. ###")
        except:
            return False

    def getClient(self): #TODO: A FAIRE
        try:    
            reponse = input("Indiquez l'id du client à qui la facture sera adressée : ")
            return reponse
        except:
            return False


    def Row_getId(self):
        try:
            chiffre=False
            while(chiffre == False):
                # TODO: Vérifier que l'id se trouve dans la bdd pour notifier l'utilisateur
                id = input("Veuillez choisir l'ID de la facture \nVotre choix : ")
                chiffre = self.Intable(id)
            return id
        except:
            return False


    


   





