import mysql.connector
import interface_console
import database

class Client():
    def __init__(self, cnx): #Il faut récupérer la connexion à la base de données pour l'utiliser avec les pointeurs
        self.name="clients"
        self.cnx = cnx
        self.QueFaire()
        

    
    def QueFaire(self):
        quit=False
        while(quit==False):
            interface_console.aff_menu_table(self.name)  #Affichage menu table
            choix=input("\nVotre choix : ") 

            if choix=="1" or choix == "2" or choix=="3" or choix=="4":
                if choix!="5":
                    if choix=="1":
                        self.Afficher_Client()
                    elif choix=="2":
                        self.Modifier_Client()
                    elif choix=="3":
                        drugDAO=drugs.Drugs()
                    elif choix=="4":
                        quit=True

    

    
    def Afficher_Client(self):
        sql="SELECT * FROM " + self.name        # SELECT * FROM clients
        try: 
            choix=input("~Souhaitez-vous afficher \n 1) Tous les clients \n 2) 1 ou plusieurs clients\n~Votre choix : ")
            if choix=="1" or choix=="2":
                if choix=="1":
                    pass
                elif choix=="2":
                    sql+="WHERE clients.name= " # SELECT * FROM clients WHERE clients.name=
                    try:
                        nbrClient=input("~Veuillez indiquer le nombre exact de clients que vous souhaitez afficher : ")
                        for i in nbrClient:
                            nomClient=input("~~Veuillez indiquer le nom du client n°" + i + " : ")
                            sql+=nomClient + ", "   #SELECT * FROM clients WHERE clients.name=roger,alain,jean-pierre, <<< On note bien la virgule+espace à la fin qu'on doit enlever
                            sql=sql[:-2]            #SELECT * FROM clients WHERE clients.name=roger,alain,jean-pierre
                    except:
                        print("\n+++Une erreur est survenue, un nombre est attendu+++")
            else:
                print("Veuillez choisir parmis les choix proposés")
            cursor=self.cnx.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            for i in result:
                print(i)
        except:
            print("\n+++Une erreur est survenue lors de l'affichage de valeurs dans la table+++")

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
        