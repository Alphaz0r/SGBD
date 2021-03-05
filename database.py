import mysql.connector
import dicoType


class Database:
    __instance=None
    def __init__(self, user="root", passw="", host="127.0.0.1", db="pharmacie"):
        if Database.__instance != None:
            raise Exception("Cette classe est un singleton!")
        else:
            self.__instance = self
            print(self.__instance)
            self.user=user
            self.passw=passw
            self.host=host
            self.db=db
            self.dc=False
            self.Se_Connecter()
            while self.dc==False:
                self.QueFaire()


    def QueFaire(self):
        try:
            print("\n**********************************   Que souhaitez-vous faire dans la base de données " + self.db + "?     **********************************")
            print("**********************************   Choix 1 : Lister toutes les tables de la base de données        **********************************")
            print("********************************** Choix 2 : Accéder à l'une des tables de la base de données        **********************************")
            print("**********************************   Choix 3 : Se déconnecter                                        **********************************")
            choix=input("\nVotre choix : ")

            if choix=="1" or choix == "2" or choix=="3" or choix=="4" or choix=="5":
                if choix=="1":
                    self.Show_Tables()
                elif choix=="2":
                    print("Faut coder le choix numero 2 gaillard")
                elif choix=="3":
                    self.dc = True
                    self.Se_Deconnecter()
            else:
                print("Veuillez choisir l'un des choix proposés")
        except:
            print("Erreur rencontrée")



    #Méthode pour se connecter à la base de données
    def Se_Connecter(self):
        try:
            username=input("Nom d'utilisateur : ")
            password=input("Mot de passe : ")
        except:
            print("Identifiants incorrects")
        try:
            self.cnx = mysql.connector.connect(username=username, password=password, host=self.host, database=self.db)
            print("Connexion avec la base de données réalisée avec succès")
        except:
            print("Une erreur est survenue lors de la connexion")
        
    #Méthode pour se déconnecter de la base de données avec vérification
    def Se_Deconnecter(self):
        try:
            reponse=input("Êtes vous sûr de vouloir vous déconnecter ? Y/N\n")
            if reponse=="Y" or reponse == "N":
                if reponse == "Y":
                    try:
                        self.cnx.close()
                        print("Connexion fermée avec succès")
                    except:
                        print("Erreur survenue lors de la déconnexion")
                else:
                    return "Aucune action n'a été entreprise"
            else:
                print("Erreur dans le choix de reponse")
                self.Se_Deconnecter()
        except:
            print("Erreur dans la déconnexion")

    
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
            print("Une erreur est survenue lors de l'affichage des tables")

    
    """
    def Create_Table(self, name, pk, col):
        try:
            sql="CREATE TABLE "
            cursor=self.cnx.cursor()
            sql+=name + " (" + pk + " INT" + " AUTO_INCREMENT " + "PRIMARY KEY"
            for i in range(col):
                try:
                    sql+=", "
                    colname = input("Nom de la colonne " + str(i) + " : ")     #TODO Vérifier exceptions ici
                    coltype = input("Type de la colonne " + str(i) +  " ,veuillez choisir parmis les options suivantes\n\n" + "dico" + "\n\n" + "Votre choix : ")
                    sql+= " " + colname + " " + coltype
                except:
                    print("Erreur dans l'entrée du type ou du nom de la colonne")
            sql+=")"
            cursor.execute(sql)
        except:
            print("Une erreur est survenue lors de la création de la table")
        finally:
            print("Table dans la database " + self.db + " :")
            self.Show_Tables()
        """

        """
    def Drop_Table(self, nomTable):
        try:
            sql="DROP TABLE "
            sql+=nomTable
            cursor=self.cnx.cursor()
            cursor.execute(sql)
            print("Suppression de la table " + nomTable + " réussie")
        except:
            print("Une erreur est survenue lors de la suppression de la table")
        finally:
            print("Table dans la database : " + self.db + ": \n")
            self.Show_Tables()

    def Alter_Table(self, table, query):
        try:
            cursor=self.cnx.cursor()
            cursor.execute(query)
        except:
            print("Une erreur est survenue lors de la modification de la table")
        """

   
        

