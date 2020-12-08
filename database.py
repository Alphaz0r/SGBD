import mysql.connector

class Database:
    def __init__(self, user="root", passw="", host="127.0.0.1", db="ecole"):
        self.user=user
        self.passw=passw
        self.host=host
        self.db=db
        self.Se_Connecter()

    def Se_Connecter(self):
        try:
            self.cnx = mysql.connector.connect(user=self.user, password=self.passw, host=self.host, database=self.db)
            print("Connexion avec la base de données réalisée avec succès")
        except:
            print("Une erreur est survenue lors de la connexion")
        

    def Se_Deconnecter(self):
        try:
            self.cnx.close()
            print("Connexion fermée avec succès")
        except:
            print("Erreur survenue lors de la déconnexion")

    
    def Show_Tables(self):
        try:
            cursor=self.cnx.cursor()
            cursor.execute("SHOW TABLES")
            for i in cursor:
                print(i)
        except:
            print("Une erreur est survenue lors de l'affichage des tables")

    def Create_Table(self, query):
        try:
            cursor=self.cnx.cursor()
            cursor.execute(query)
        except:
            print("Une erreur est survenue lors de la création de la table")
        finally:
            print("Table dans la database : " + self.db)
            self.Show_Tables()

    def Drop_Table(self, table, query):
        try:
            cursor=self.cnx.cursor()
            cursor.execute(query)
        except:
            print("Une erreur est survenue lors de la suppression de la table")
        finally:
            print("Table dans la database : " + self.db)
            self.Show_Tables()

    def Alter_Table(self, table, query):
        try:
            cursor=self.cnx.cursor()
            cursor.execute(query)
        except:
            print("Une erreur est survenue lors de la modification de la table")


   
        

