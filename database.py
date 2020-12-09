import mysql.connector
import dicoType


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
            sql="SHOW TABLES"
            cursor=self.cnx.cursor()
            cursor.execute(sql)
            for i in cursor:
                print(i)
        except:
            print("Une erreur est survenue lors de l'affichage des tables")

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
                    return "Veuillez recommencer"
            sql+=")"
            cursor.execute(sql)
        except:
            print("Une erreur est survenue lors de la création de la table")
        finally:
            print("Table dans la database : " + self.db + " :")
            self.Show_Tables()

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


   
        

