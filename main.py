import mysql.connector
import interface_console
import sys
sys.path.append("./controller/")
from facture_controller import *
from users_controller import *
from drugs_controller import *
from concentration_controller import *
from client_controller import *

# Méthode pour se connecter à la base de données ( 3 essais permis )


def Test_Connection_DB():
    attempt = 4
    while(attempt >= 0):
        try:
            username = "root"
            password = ""
            host = "127.0.0.1"
            db = "pharmacie"
            # TODO : Implémenter un ping test vers la base de données pour raise des erreurs plus claires
            cnx = mysql.connector.connect(
                username=username, password=password, host=host, database=db)
            print(
                "\n       ### Test de connexion avec la base de données réalisée avec succès ###")
            attempt = 4
            return cnx
        except:
            print("+++Une erreur est survenue lors de la connexion+++\n+++Identifiants incorrects ou la base de données n'a pas été atteinte+++")
            attempt -= 1
            print("\nNombre d'essais restants : " + str(attempt) + "\n")
            if attempt == 0:
                print("+++ Nombre d'essais dépassés, au revoir +++")
                exit()


def Connexion_utilisateur(cnx):
    while(True):
        try:
            reponse = input(
                "\nConnexion ou enregistrement ou quitter le programme ? C/E/Q\nVotre réponse : ")
            if reponse == "C":
                user = input("Entrez votre username : ")
                passw = input("Entrez votre mot de passe : ")
                controller_users = Users_controller(cnx)
                creds_ok = controller_users.Check_User_Passw(user, passw)
                if creds_ok == True:
                    break
            elif reponse == "E":
                controller_users = Users_controller(cnx)
                controller_users.Get_and_Check_Creds()
            elif reponse == "Q":
                exit()
        except:
            if reponse == "Q":
                raise SystemExit()
            else:
                print("+++ Erreur dans le menu de connexion +++")


def Menu(db):
    dc = False
    try:
        while(dc == False):
            interface_console.aff_menu_principal(db)  # Affichage menu principal
            choix = input("\nVotre choix : ")
            if choix == "1" or choix == "2" or choix == "3" or choix == "4" or choix == "5":
                interface_console.aff_acces_table()  # Affichage menu accès aux tables
                return choix
            elif choix == "6":
                return choix
            else:
                print("### Veuillez choisir l'un des choix proposés ###")
    except:
        print("+++ Erreur rencontrée dans le menu principal +++")


# Méthode pour se déconnecter de la base de données avec vérification
def Se_Deconnecter(cnx):
    try:
        reponse = input("~ Êtes vous sûr de vouloir vous déconnecter ? Y/N reponse : ")
        if reponse == "Y":
            try:
                cnx.close()
                input("Connexion fermée avec succès ! Appuyez sur une touche pour quitter le programme.")
                return True
            except:
                print("+++ Erreur survenue lors de la déconnexion +++\n+++ Tentative de fermeture du programme +++")
                return True
        elif reponse == "N":
            print("### Aucune action n'a été entreprise ###")
            return False
        else:
            print("+++ Erreur dans le choix de reponse +++")
            return False
    except:
        print("+++ Erreur dans la déconnexion +++")
        return False


if __name__ == "__main__":
    cnx = Test_Connection_DB()
    Connexion_utilisateur(cnx)
    dc = False
    while(dc == False):
        choix = Menu("pharmacie")
        if choix == "1":
            controller_client = Client_controller(cnx)
            controller_client.Menu()
        elif choix == "2":
            controller_facture = Facture_controller(cnx)
            controller_facture.WhereWeGoing()
        elif choix == "3":
            controller_drugs = Drugs_controller(cnx)
        elif choix == "4":
            controller_concentration = Concentration_controller(cnx)
        elif choix == "5":
            controller_users = Users_controller(cnx)
        elif choix == "6":
            dc = Se_Deconnecter(cnx)
