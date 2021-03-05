import mysql.connector

class Client:
    def __init__(self): 
        self.QueFaire()

    
    def QueFaire(self):
        quit=False
        while(quit==False):
            print("Bienvenue dans la gestion des clients !")
    

    
    def Select_all(self):
        try:   
            cursor=self.db.cursor()
            cursor.execute("SELECT * FROM " + self.nom)
            result = cursor.fetchall()
            for i in result:
                print(i)
        except:
            print("+++Une erreur est survenue lors de l'affichage de valeurs dans la table+++")


    def Select(self, query):
        try:   
            cursor=self.db.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            for i in result:
                print(i)
        except:
            print("+++Une erreur est survenue lors de l'affichage de valeurs dans la table+++")        


    def Delete(self, query):
        try:
            cursor=self.db.cursor()
            cursor.execute(query)
            self.db.commit()
            print("Suppression des records réussie")
        except:
            print("+++Une erreur est survenue lors de la suppression des données dans la table+++")


    def Insert_Into_Table(self, query):
        try:   
            cursor=self.db.cursor()
            cursor.execute(query)
            self.db.commit()
            print(cursor.rowcount, "Insertion de valeur dans la table réussie")
        except:
            print("+++Une erreur est survenue lors de l'ajout de valeur dans la table+++")
        