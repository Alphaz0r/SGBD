import mysql.connector
import interface_console
import sys
sys.path.append("./controller/")
from client_controller import *
from concentration_controller import *
from drugs_controller import *
from users_controller import *
from facture_controller import *

def Menu(db):
        dc=False
        try:
            while(dc==False):
                interface_console.aff_menu_principal(db)   #Affichage menu principal
                choix=input("\nVotre choix : ")
                if choix=="1" or choix == "2" or choix=="3" or choix=="4" or choix=="5":
                        interface_console.aff_acces_table() #Affichage menu accès aux tables
                        return choix
                elif choix=="6":
                    return choix                  
                else:
                    print("### Veuillez choisir l'un des choix proposés ###")
        except:
            print("+++ Erreur rencontrée dans le menu principal +++")


#Méthode pour se déconnecter de la base de données avec vérification
def Se_Deconnecter(cnx):
    try:
        reponse=input("~ Êtes vous sûr de vouloir vous déconnecter ? Y/N reponse : ")
        if reponse == "Y":
            try:
                cnx.close()
                input("Connexion fermée avec succès ! Appuyez sur une touche pour quitter le programme.")
                return True
            except:
                print("+++ Erreur survenue lors de la déconnexion +++\n+++ Tentative de fermeture du programme +++")
                return True
        elif reponse=="N":
            print ("### Aucune action n'a été entreprise ###")
            return False
        else:
            print("+++ Erreur dans le choix de reponse +++")
            return False
    except:
        print("+++ Erreur dans la déconnexion +++")
        return False


if __name__=="__main__":
    launcher=database.Database()
    dc=False
    while(dc==False):
        choix=Menu(launcher.db)
        if choix=="1":
            controller_client=Client_controller(launcher.cnx)
            controller_client.Menu()
        elif choix=="2":
            controller_facture=Facture_controller(launcher.cnx)
            controller_facture.WhereWeGoing()
        elif choix=="3":
            controller_drugs=Drugs_controller(launcher.cnx)
        elif choix=="4":
            controller_concentration=Concentration_controller(launcher.cnx)
        elif choix=="5":
            controller_users=Users_controller(launcher.cnx)
        elif choix=="6":
            dc=Se_Deconnecter(launcher.cnx)