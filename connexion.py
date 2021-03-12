import mysql.connector
import sys

class Connexion:
    def __init__(self, user="root", passw="", host="127.0.0.1", port="3306", db="pharmacie"):
        self.user=user
        self.passw=passw
        self.host=host
        self.db=db
        self.Se_Connecter()

    #Méthode pour se connecter à la base de données ( 3 essais permis )
    def Se_Connecter(self):
        attempt=4
        while(attempt>=0):
            try:
                #username=input("~ Nom d'utilisateur : ")
                #password=input("~~~~~~ Mot de passe : ")
                username="root"
                password=""
                self.cnx = mysql.connector.connect(username=username, password=password, host=self.host, database=self.db) #TODO : Implémenter un ping test vers la base de données pour raise des erreurs plus claires
                print("\n       ### Test de connexion avec la base de données réalisée avec succès")
                attempt=4
                break   #Sortie de la boucle
            except:
                print("+++Une erreur est survenue lors de la connexion+++\n+++Identifiants incorrects ou la base de données n'a pas été atteinte+++")
                attempt-=1
                print("\nNombre d'essais restants : " + str(attempt) + "\n")
        if attempt==0:
            print("+++Nombre d'essais dépassés, au revoir+++")
            exit()
        
        
    #Méthode pour se déconnecter de la base de données avec vérification
    def Se_Deconnecter(self):
        try:
            reponse=input("~ Êtes vous sûr de vouloir vous déconnecter ? Y/N reponse : ")
            if reponse=="Y" or reponse == "N":
                if reponse == "Y":
                    try:
                        self.cnx.close()
                        print("Connexion fermée avec succès !")
                    except:
                        print("+++Erreur survenue lors de la déconnexion+++")
                else:
                    print ("### Aucune action n'a été entreprise")
            else:
                print("+++Erreur dans le choix de reponse+++")
        except:
            print("+++Erreur dans la déconnexion+++")



