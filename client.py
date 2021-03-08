import mysql.connector
import interface_console
import database
from beautifultable import BeautifulTable
from datetime import datetime


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
                        pass
                    elif choix=="4":
                        quit=True

    
    def Afficher_Client(self):
        sql="SELECT PK_client_id, name, first_name, CAST(birth_date AS CHAR), age, rue, house_number, postcode, email, phone_number FROM " + self.name        # SELECT * FROM clients
        cursor=self.cnx.cursor(dictionary=True) #Initialisation du curseur mysql, celui-ci retourne chaque ligne sous la forme clef:valeur 
        table=BeautifulTable(maxwidth=300)      #Préparation de l'affichage des lignes
        try: 
            choix=input("~Souhaitez-vous afficher \n 1) Tous les clients \n 2) Je choisis quel(s) client(s) afficher\n~Votre choix : ")
            if choix=="1" or choix=="2":
                if choix=="1":
                    pass    #TODO : Delete ce truc
                elif choix=="2":
                    sql+=" WHERE clients.PK_client_id= " # SELECT * FROM clients WHERE clients.PK_client_id=
                    try:
                        nbrClient=input("~Veuillez indiquer le nombre exact de clients que vous souhaitez afficher : ")
                        for i in nbrClient:
                            idClient=input("~~Veuillez indiquer l'ID' du client n°" + i + " : ")
                            sql+=idClient + ", "   #SELECT * FROM clients WHERE clients.PK_client_id=2,4,8, <<< On note bien la virgule+espace à la fin qu'on doit enlever
                            sql=sql[:-2]            #SELECT * FROM clients WHERE clients.PK_client_id=2,4,8
                    except:
                        print("\n+++Une erreur est survenue, un nombre est attendu+++")
            else:
                return "Veuillez choisir parmis les choix proposés"
            cursor=self.cnx.cursor()
            cursor.execute(sql)
            print("Affichage de votre requête : ")
            table.columns.header=["ID", "Nom", "Prénom", "Date de naissance", "Age", "Rue", "Numéro de maison", "Code postal", "Email", "Numéro de téléphone"]
            
            for row in cursor:
                table.rows.append(row)
            print(table)
        except:
            print("\n+++Une erreur est survenue lors de l'affichage de valeurs dans la table+++")
        finally:
            cursor.close()

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
        