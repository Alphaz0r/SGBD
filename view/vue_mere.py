import mysql.connector
import interface_console
import client_controller
import sys
sys.path.append("..\\model\\")
sys.path.append("..\\view\\")
from beautifultable import BeautifulTable
from datetime import datetime


class Vue_mere():
    def __init__(self):
        pass


    def Display_Rows(self, table):
        try:
            if table == None:
                vue_client.Display_Error()
            else:
                print("### Affichage de votre requête : ###\n")
                print(table)
        except:
            self.Display_Error()

    def Row_getId(self):
        try:
            chiffre=False
            while(chiffre == False):
                # TODO: Vérifier que l'id se trouve dans la bdd pour notifier l'utilisateur
                id = input("Veuillez choisir l'ID de la ligne \nVotre choix : ")
                chiffre = self.Intable(id)
            return id
        except:
            return False

    def getConfirmation(self, id, position):
        crud=["modifiée", "supprimée","créée"]
        try:    
            while(True):
                if crud[position]=="modifiée" or crud[position]=="supprimée":
                    reponse = input("La ligne avec l'ID "+id+" va être "+crud[position]+". Confirmer ? Y/N\nVotre réponse : ")
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
    #
    # Méthodes d'affichage erreur ou réussite
    #
    def Display_Select_Error(self):
        print("+++ Une erreur est survenue dans le processus d'affichage +++")

    def Display_Delete_Error(self):
        print("+++ Une erreur est survenue dans le processus de suppression +++")

    def Display_Alter_Error(self):
        print("+++ Une erreur est survenue dans le processus de modification +++")
    
    def Display_Create_Error(self):
        print("+++ Une erreur est survenue dans le processus de création +++")

    def Display_BackToMenu(self):
        input("~~~ Action réussie. Retour au menu. Appuyer sur une touche pour continuer... ~~~")
    #
    #
    #
    #
    # Méthodes de tests et validation
    #
    def Intable(self, nombre):
        try:
            int_nombre=int(nombre)
            return True
        except:
            return False

    def Dateable(self, date):
        try:
            date=datetime.strptime(date, '%Y-%m-%d')
            return True
        except:
            return False
    #
    #
    #