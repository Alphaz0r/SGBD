
import mysql.connector
import interface_console
import database
from beautifultable import BeautifulTable
from datetime import datetime


class Table():
    def __init__(self, cnx, table_name, col): #Il faut récupérer la connexion cnx à la base de données pour l'utiliser avec les pointeurs cursor()
        self.table_name=table_name
        self.cnx=cnx
        self.col=col
        self.QueFaire()
        
    def QueFaire(self):
        quit=False
        while(quit==False):
            interface_console.aff_menu_table(self.table_name[0])  #Affichage menu table
            choix=input("\nVotre choix : ") 

            if choix=="1" or choix == "2" or choix=="3" or choix=="4":
                if choix!="5":
                    if choix=="1":
                        self.Afficher_Table()
                    elif choix=="2":
                        self.Modifier_Client()
                    elif choix=="3":
                        pass
                    elif choix=="4":
                        quit=True

    
    def Afficher_Table(self):
        #Construction de la query de base NB: Impossible de sélectionner autre chose que TOUTE la table
        sql="SELECT "  
        for col in self.col:
            sql+=""+col+", "
        sql=sql[:-2]
        sql+=" FROM " + self.table_name[0]
        table=BeautifulTable(maxwidth=300)      #Préparation de l'affichage des lignes de façon organisée

        #Proposition de choix au client, soit on affiche toute la table, soit on crée une query personnalisée selon les ID qu'il souhaite afficher
        try: 
            choix=input("~Souhaitez-vous afficher \n 1) Tous les clients \n 2) Je choisis quel(s) client(s) afficher\n~Votre choix : ")
            if choix=="1" or choix=="2":
                if choix=="1":
                    pass    #TODO : Delete ce truc
                elif choix=="2":
                    sql+=" WHERE "+self.table_name[0]+"."+self.col[0]+"= " # SELECT * FROM clients WHERE clients.PK_client_id=
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
            print("\nAffichage de votre requête : ")
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
        