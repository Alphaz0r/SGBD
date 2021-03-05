import mysql.connector, interface_console, dicoType 
import client, concentration, drugs, facture # DAO



class Database:
    __instance=None
    def __init__(self, user="root", passw="", host="127.0.0.1", db="pharmacie"):
        if Database.__instance != None:
            raise Exception("+++Cette classe est un singleton!+++")
        else:
            self.__instance = self
            print(self.__instance)
            self.user=user
            self.passw=passw
            self.host=host
            self.db=db
            self.Se_Connecter()
            self.Show_Tables()
            self.QueFaire()

    #Fonction  menu principal
    def QueFaire(self):
        dc=False
        while(dc==False):
            try:
                interface_console.aff_menu_principal(self.db)   #Affichage menu principal
                choix=input("\nVotre choix : ") 

                if choix=="1" or choix == "2" or choix=="3" or choix=="4" or choix=="5":
                    if choix!="5":
                        interface_console.aff_acces_table() #Affichage menu accès aux tables
                        if choix=="1":
                            clientDAO=client.Client()
                        elif choix=="2":
                            factureDAO=facture.Facture()
                        elif choix=="3":
                            drugDAO=drugs.Drugs()
                        elif choix=="4":
                            concentrationDAO=concentration.Concentration()
                    else:
                        dc = True  #Sortie de la boucle
                        self.Se_Deconnecter()
                else:
                    print("### Veuillez choisir l'un des choix proposés")
            except:
                print("+++Erreur rencontrée+++")
                raise


    #Méthode qui va afficher toutes les tables présentes dans la base de données
    def Show_Tables(self):
        sql="SHOW TABLES"
        print("\n***Tables présentes dans la base de données " + self.db + " ***")
        try:
            cursor=self.cnx.cursor()
            cursor.execute(sql)
            for i in cursor:
                print(i)
            print("*******************************************************")
        except:
            print("+++Une erreur est survenue lors de l'affichage des tables+++")

    #Méthode pour se connecter à la base de données ( 3 essais permis )
    def Se_Connecter(self):
        attempt=4
        while(attempt>=0):
            try:
                username=input("~Nom d'utilisateur : ")
                password=input("~Mot de passe : ")
                self.cnx = mysql.connector.connect(username=username, password=password, host=self.host, database=self.db)
                print("Connexion avec la base de données réalisée avec succès")
                attempt=4
                break   #Sortie de la boucle
            except:
                print("+++Une erreur est survenue lors de la connexion+++\n+++Identifiants incorrects+++")
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
   
        

